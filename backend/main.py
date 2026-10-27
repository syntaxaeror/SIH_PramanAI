import os
import datetime
import json
from typing import List, Optional, Dict, Any
from fastapi import FastAPI, HTTPException, Query, UploadFile, File, Form, Response, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm import Session
from sqlalchemy import func

from database import (
    engine, Base, SessionLocal, get_db, init_db,
    ApplicationModel, DocumentModel, FindingModel, EVCEvidenceModel, RuleModel, AuditEventModel,
    safe_json_loads, safe_json_dumps
)
from models import (
    Application, DocumentItem, EVCEvidenceItem, Finding, RuleDefinition,
    AuditEvent, UserRole, ValidationStatus, VerificationStatus, ReviewPriority,
    DocumentMappingHistory
)
from services.mapping_engine import map_document_filename, confirm_with_content
from services.report_exporter import generate_scrutiny_pdf
from services.rule_engine import run_application_verification

app = FastAPI(
    title="AICTE AI-Powered Application Scrutiny & EVC Review Assistant",
    description="Internal, access-controlled platform for scrutiny reviewers and EVC inspectors backed by SQLAlchemy.",
    version="2.0.0"
)

# CORS middleware for local frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Session user mock
current_user = {
    "id": "usr-101",
    "name": "Prof. S. R. Sharma",
    "role": UserRole.SCRUTINY_REVIEWER,
    "email": "sr.sharma@aicte-india.org",
    "division": "Approvals & Scrutiny Bureau (South-Western Region)"
}

@app.on_event("startup")
def startup_event():
    init_db()
    db = SessionLocal()
    try:
        count = db.query(ApplicationModel).count()
        if count == 0:
            print("Database empty. Seeding with 20 applications across 5 categories...")
            import seed_data
            seed_data.seed_database()
        else:
            print(f"Database ready: {count} applications loaded.")
    finally:
        db.close()

def log_audit(db: Session, action: str, target_type: str, target_id: str, details: str):
    role_str = current_user["role"].value if isinstance(current_user["role"], UserRole) else str(current_user["role"])
    new_event = AuditEventModel(
        id=f"aud-{datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')[:17]}",
        timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        user_name=current_user["name"],
        user_role=role_str,
        action=action,
        target_type=target_type,
        target_id=target_id,
        details=details
    )
    db.add(new_event)
    db.commit()

@app.get("/api/auth/me")
def get_current_user():
    return current_user

@app.post("/api/auth/switch-role")
def switch_user_role(role: UserRole, db: Session = Depends(get_db)):
    current_user["role"] = role
    role_names = {
        UserRole.ADMIN: "S. K. Bansal (Chief System Administrator)",
        UserRole.SCRUTINY_REVIEWER: "Prof. S. R. Sharma (Senior Scrutiny Officer)",
        UserRole.EVC_REVIEWER: "Dr. M. K. Ananth (EVC Committee Member)",
        UserRole.AUDITOR: "CMA Rajesh Singhania (Independent Quality Auditor)"
    }
    current_user["name"] = role_names.get(role, "Authorized Reviewer")
    log_audit(db, "SWITCH_ROLE", "USER_SESSION", current_user["id"], f"Switched session role to {role.value}")
    return current_user

@app.get("/api/stats")
def get_overview_stats(db: Session = Depends(get_db)):
    apps = db.query(ApplicationModel).all()
    total_apps = len(apps)
    under_scrutiny = sum(1 for a in apps if a.status == "UNDER_SCRUTINY")
    deficiency_flagged = sum(1 for a in apps if a.status == "DEFICIENCY_FLAGGED" or a.deficiency_count > 0)
    in_review = sum(1 for a in apps if a.status in ["IN_REVIEW", "SCRUTINY_IN_PROGRESS", "UNDER_SCRUTINY"])
    
    total_evc_duplicates = db.query(EVCEvidenceModel).filter(EVCEvidenceModel.duplicate_flag == True).count()

    return {
        "total_applications": total_apps,
        "under_scrutiny": under_scrutiny,
        "in_review": in_review,
        "deficiencies_count": deficiency_flagged,
        "duplicate_evc_flags": total_evc_duplicates,
        "priority_red": sum(1 for a in apps if a.priority == "RED"),
        "priority_amber": sum(1 for a in apps if a.priority == "AMBER"),
        "priority_green": sum(1 for a in apps if a.priority == "GREEN"),
    }

@app.get("/api/categories")
def get_categories_stats(db: Session = Depends(get_db)):
    categories = [
        "New Technical Institution",
        "Extension of Approval (EoA)",
        "New Programme / Level",
        "Intake Increase",
        "Other Application Types"
    ]
    result = []
    for cat in categories:
        cat_apps = db.query(ApplicationModel).filter(ApplicationModel.category == cat).all()
        total = len(cat_apps)
        pending = sum(1 for a in cat_apps if a.status == "UNDER_SCRUTINY")
        in_review = sum(1 for a in cat_apps if a.status in ["IN_REVIEW", "SCRUTINY_IN_PROGRESS"])
        action_required = sum(1 for a in cat_apps if a.status == "DEFICIENCY_FLAGGED" or a.deficiency_count > 0)
        result.append({
            "category": cat,
            "total": total,
            "pending": pending,
            "in_review": in_review,
            "action_required": action_required
        })
    return result

@app.get("/api/applications", response_model=List[Application])
def list_applications(
    category: Optional[str] = None,
    academic_year: Optional[str] = None,
    priority: Optional[ReviewPriority] = None,
    search: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(ApplicationModel)
    if category and category != "ALL":
        query = query.filter(ApplicationModel.category == category)
    if academic_year and academic_year != "ALL":
        query = query.filter(ApplicationModel.academic_year == academic_year)
    if priority:
        priority_val = priority.value if hasattr(priority, "value") else str(priority)
        query = query.filter(ApplicationModel.priority == priority_val)
    if search:
        s = f"%{search.lower()}%"
        query = query.filter(
            func.lower(ApplicationModel.application_number).like(s) |
            func.lower(ApplicationModel.institution_name).like(s) |
            func.lower(ApplicationModel.trust_name).like(s)
        )
    rows = query.all()
    return [r.to_dict() for r in rows]

@app.get("/api/applications/{app_id}", response_model=Application)
def get_application(app_id: str, db: Session = Depends(get_db)):
    row = db.query(ApplicationModel).filter(ApplicationModel.id == app_id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Application not found")
    return row.to_dict()

@app.put("/api/applications/{app_id}")
def update_application(app_id: str, payload: Dict[str, Any], db: Session = Depends(get_db)):
    row = db.query(ApplicationModel).filter(ApplicationModel.id == app_id).first()
    if not row:
        raise HTTPException(status_code=404, detail="Application not found")
    
    for key, val in payload.items():
        if hasattr(row, key):
            if key == "stage_progress" and isinstance(val, dict):
                setattr(row, key, json.dumps(val))
            else:
                setattr(row, key, val)
    db.commit()
    log_audit(db, "APPLICATION_UPDATE", "APPLICATION", app_id, f"Updated application fields: {list(payload.keys())}")
    return row.to_dict()

@app.get("/api/applications/{app_id}/documents", response_model=List[DocumentItem])
def get_application_documents(app_id: str, db: Session = Depends(get_db)):
    rows = db.query(DocumentModel).filter(DocumentModel.application_id == app_id).all()
    return [r.to_dict() for r in rows]

@app.put("/api/documents/{doc_id}")
def update_document(doc_id: str, payload: Dict[str, Any], db: Session = Depends(get_db)):
    doc = db.query(DocumentModel).filter(DocumentModel.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    
    for key, val in payload.items():
        if hasattr(doc, key):
            if key in ["candidate_types", "extracted_fields", "bounding_boxes", "audit_history"] and isinstance(val, (dict, list)):
                setattr(doc, key, json.dumps(val))
            else:
                setattr(doc, key, val)
    db.commit()
    log_audit(db, "DOCUMENT_UPDATE", "DOCUMENT", doc_id, f"Updated document fields: {list(payload.keys())}")
    return doc.to_dict()

@app.post("/api/documents/{doc_id}/remap")
def remap_document(doc_id: str, payload: Dict[str, str], db: Session = Depends(get_db)):
    target_type = payload.get("new_type")
    reason = payload.get("reason", "Manual reviewer reassignment")
    
    if not target_type:
        raise HTTPException(status_code=400, detail="Missing new_type")

    doc = db.query(DocumentModel).filter(DocumentModel.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")

    old_type = doc.mapped_type
    doc.mapped_type = target_type
    doc.mapping_stage = "Manual Remap"
    doc.mapping_confidence = 1.0

    history = safe_json_loads(doc.audit_history, [])
    history.insert(0, {
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "actor": current_user["name"],
        "action": "Manual Remap",
        "from_type": old_type,
        "to_type": target_type,
        "reason": reason
    })
    doc.audit_history = json.dumps(history)
    db.commit()

    log_audit(db, "DOCUMENT_REMAP", "DOCUMENT", doc_id, f"Remapped '{doc.original_filename}' from '{old_type}' to '{target_type}'. Reason: {reason}")
    return doc.to_dict()

@app.post("/api/documents/{doc_id}/mark-reviewed")
def mark_document_reviewed(doc_id: str, db: Session = Depends(get_db)):
    doc = db.query(DocumentModel).filter(DocumentModel.id == doc_id).first()
    if not doc:
        raise HTTPException(status_code=404, detail="Document not found")
    doc.document_status = "Reviewed"
    db.commit()
    log_audit(db, "DOCUMENT_REVIEWED", "DOCUMENT", doc_id, f"Document '{doc.mapped_type}' marked as reviewed.")
    return doc.to_dict()

@app.post("/api/applications/{app_id}/run-verification")
def trigger_application_verification(app_id: str, db: Session = Depends(get_db)):
    try:
        result = run_application_verification(app_id, db)
        log_audit(
            db, 
            "RUN_VERIFICATION_ENGINE", 
            "APPLICATION", 
            app_id, 
            f"Executed live statutory rule engine. Deficiencies: {result['deficiency_count']}, Score: {result['compliance_score']}%"
        )
        return result
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Rule verification failed: {str(e)}")

@app.get("/api/applications/{app_id}/findings", response_model=List[Finding])
def get_application_findings(app_id: str, db: Session = Depends(get_db)):
    rows = db.query(FindingModel).filter(FindingModel.application_id == app_id).all()
    return [r.to_dict() for r in rows]

@app.post("/api/findings/{finding_id}/disposition")
def update_finding_disposition(finding_id: str, payload: Dict[str, str], db: Session = Depends(get_db)):
    disposition = payload.get("disposition")
    reviewer_notes = payload.get("reviewer_notes", "")

    f = db.query(FindingModel).filter(FindingModel.id == finding_id).first()
    if not f:
        raise HTTPException(status_code=404, detail="Finding not found")

    f.disposition = disposition
    if reviewer_notes:
        f.reviewer_notes = reviewer_notes
    f.updated_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    db.commit()

    log_audit(db, "RECORD_DISPOSITION", "FINDING", finding_id, f"Set disposition to '{disposition}'. Note: '{reviewer_notes}'")
    return f.to_dict()

@app.get("/api/applications/{app_id}/evc", response_model=List[EVCEvidenceItem])
def get_application_evc_items(app_id: str, db: Session = Depends(get_db)):
    rows = db.query(EVCEvidenceModel).filter(EVCEvidenceModel.application_id == app_id).all()
    return [r.to_dict() for r in rows]

@app.post("/api/evc/{evc_id}/flag-inspection")
def flag_evc_item_inspection(evc_id: str, payload: Dict[str, Any], db: Session = Depends(get_db)):
    needed = payload.get("inspection_needed", True)
    reason = payload.get("inspection_reason", "Reviewer requested on-site verification")
    notes = payload.get("reviewer_notes", "")

    item = db.query(EVCEvidenceModel).filter(EVCEvidenceModel.id == evc_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="EVC item not found")

    item.inspection_needed = needed
    item.inspection_reason = reason if needed else None
    if notes:
        item.reviewer_notes = notes
    db.commit()

    action_text = "FLAGGED_FOR_ON_SITE" if needed else "UNFLAGGED_ON_SITE"
    log_audit(db, action_text, "EVC_ITEM", evc_id, f"Reason: {reason}")
    return item.to_dict()

@app.get("/api/rules", response_model=List[RuleDefinition])
def get_rules(db: Session = Depends(get_db)):
    rows = db.query(RuleModel).all()
    return [r.to_dict() for r in rows]

@app.post("/api/rules/{rule_id}/toggle")
def toggle_rule_active(rule_id: str, db: Session = Depends(get_db)):
    if current_user["role"] != UserRole.ADMIN:
        raise HTTPException(status_code=403, detail="Only System Administrators can activate or retire rules.")
    rule = db.query(RuleModel).filter(RuleModel.id == rule_id).first()
    if not rule:
        raise HTTPException(status_code=404, detail="Rule not found")
    
    rule.is_active = not rule.is_active
    db.commit()
    status_str = "ACTIVATED" if rule.is_active else "RETIRED"
    log_audit(db, "RULE_TOGGLE", "RULE", rule_id, f"Rule {rule.title} {status_str}")
    return rule.to_dict()

@app.get("/api/audit", response_model=List[AuditEvent])
def get_audit_trail(db: Session = Depends(get_db)):
    rows = db.query(AuditEventModel).order_by(AuditEventModel.timestamp.desc()).all()
    return [r.to_dict() for r in rows]

# PDF Report Generation
@app.get("/api/applications/{app_id}/report/pdf")
def download_pdf_report(app_id: str, db: Session = Depends(get_db)):
    app_obj = db.query(ApplicationModel).filter(ApplicationModel.id == app_id).first()
    if not app_obj:
        raise HTTPException(status_code=404, detail="Application not found")
    
    docs = [d.to_dict() for d in db.query(DocumentModel).filter(DocumentModel.application_id == app_id).all()]
    findings = [f.to_dict() for f in db.query(FindingModel).filter(FindingModel.application_id == app_id).all()]
    evc_items = [e.to_dict() for e in db.query(EVCEvidenceModel).filter(EVCEvidenceModel.application_id == app_id).all()]

    pdf_bytes = generate_scrutiny_pdf(app_obj.to_dict(), docs, findings, evc_items)
    
    log_audit(db, "REPORT_EXPORT_PDF", "APPLICATION", app_id, f"Exported AI Scrutiny PDF report for {app_obj.application_number}")

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f"attachment; filename=AICTE_Scrutiny_Summary_{app_obj.application_number}.pdf"
        }
    )

@app.get("/api/applications/{app_id}/report/json")
def get_json_report(app_id: str, db: Session = Depends(get_db)):
    app_obj = db.query(ApplicationModel).filter(ApplicationModel.id == app_id).first()
    if not app_obj:
        raise HTTPException(status_code=404, detail="Application not found")

    docs = [d.to_dict() for d in db.query(DocumentModel).filter(DocumentModel.application_id == app_id).all()]
    findings = [f.to_dict() for f in db.query(FindingModel).filter(FindingModel.application_id == app_id).all()]
    evc_items = [e.to_dict() for e in db.query(EVCEvidenceModel).filter(EVCEvidenceModel.application_id == app_id).all()]

    log_audit(db, "REPORT_EXPORT_JSON", "APPLICATION", app_id, f"Exported AI Scrutiny JSON report for {app_obj.application_number}")

    return {
        "metadata": {
            "title": "AICTE Application Scrutiny & EVC Review Summary",
            "academic_year": app_obj.academic_year,
            "generated_at": datetime.datetime.now().isoformat(),
            "export_user": current_user["name"],
            "disclaimer": "This document is an AI-assisted evidence synthesis report for authorized human reviewers. It does NOT make statutory approval decisions."
        },
        "application": app_obj.to_dict(),
        "documents": docs,
        "findings": findings,
        "evc_items": evc_items
    }
