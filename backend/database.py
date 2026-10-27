import os
import json
from typing import List, Dict, Any, Optional
from sqlalchemy import (
    create_engine, Column, Integer, String, Float, Boolean, Text, ForeignKey
)
from sqlalchemy.orm import declarative_base, sessionmaker, relationship, Session

DB_PATH = os.path.join(os.path.dirname(__file__), "aicte_scrutiny.db")
DATABASE_URL = f"sqlite:///{DB_PATH}"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def safe_json_loads(val, default):
    if not val:
        return default
    if isinstance(val, (dict, list)):
        return val
    try:
        return json.loads(val)
    except Exception:
        return default

def safe_json_dumps(val, default="[]"):
    if val is None:
        return default
    if isinstance(val, str):
        return val
    try:
        return json.dumps(val)
    except Exception:
        return default

class ApplicationModel(Base):
    __tablename__ = "applications"

    id = Column(String, primary_key=True, index=True)
    application_number = Column(String, unique=True, index=True)
    academic_year = Column(String, default="2025-26")
    institution_name = Column(String, index=True)
    institution_id = Column(String)
    institution_address = Column(Text)
    category = Column(String, index=True)
    status = Column(String, default="UNDER_SCRUTINY")
    priority = Column(String, default="GREEN")
    assigned_reviewer = Column(String)
    created_at = Column(String)
    declared_lat = Column(Float)
    declared_lon = Column(Float)
    trust_name = Column(String)
    total_intake_applied = Column(Integer)
    total_carpet_area_sqm = Column(Float)
    documents_count = Column(Integer, default=0)
    findings_count = Column(Integer, default=0)
    evc_items_count = Column(Integer, default=0)
    deficiency_count = Column(Integer, default=0)
    compliance_score = Column(Integer, default=100)
    expected_documents_count = Column(Integer, default=7)
    workflow_stage = Column(String, default="checklist")
    stage_progress = Column(Text, default="{}")
    review_cycle = Column(Integer, default=1)

    documents = relationship("DocumentModel", back_populates="application", cascade="all, delete-orphan")
    findings = relationship("FindingModel", back_populates="application", cascade="all, delete-orphan")
    evc_items = relationship("EVCEvidenceModel", back_populates="application", cascade="all, delete-orphan")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "application_number": self.application_number,
            "academic_year": self.academic_year,
            "institution_name": self.institution_name,
            "institution_id": self.institution_id,
            "institution_address": self.institution_address,
            "category": self.category,
            "status": self.status,
            "priority": self.priority,
            "assigned_reviewer": self.assigned_reviewer,
            "created_at": self.created_at,
            "declared_lat": self.declared_lat,
            "declared_lon": self.declared_lon,
            "trust_name": self.trust_name,
            "total_intake_applied": self.total_intake_applied,
            "total_carpet_area_sqm": self.total_carpet_area_sqm,
            "documents_count": self.documents_count,
            "findings_count": self.findings_count,
            "evc_items_count": self.evc_items_count,
            "deficiency_count": self.deficiency_count,
            "compliance_score": self.compliance_score,
            "expected_documents_count": self.expected_documents_count,
            "workflow_stage": self.workflow_stage,
            "stage_progress": safe_json_loads(self.stage_progress, {
                "checklist": "Completed",
                "document_verification": "Action Required" if self.deficiency_count > 0 else "In Progress",
                "evc_evidence": "In Progress",
                "final_summary": "Not Started"
            }),
            "review_cycle": self.review_cycle
        }

class DocumentModel(Base):
    __tablename__ = "documents"

    id = Column(String, primary_key=True, index=True)
    application_id = Column(String, ForeignKey("applications.id"), index=True)
    original_filename = Column(String)
    mapped_type = Column(String)
    mapping_confidence = Column(Float, default=0.90)
    mapping_stage = Column(String, default="Content Confirmation (OCR)")
    candidate_types = Column(Text, default="[]")
    ocr_status = Column(String, default="COMPLETED")
    page_count = Column(Integer, default=1)
    extracted_fields = Column(Text, default="[]")
    bounding_boxes = Column(Text, default="[]")
    preview_url = Column(String, nullable=True)
    document_body_text = Column(Text, nullable=True)
    audit_history = Column(Text, default="[]")
    remarks = Column(Text, nullable=True)
    is_mandatory = Column(Boolean, default=True)
    upload_status = Column(String, default="Uploaded")
    document_status = Column(String, default="Reviewed")

    application = relationship("ApplicationModel", back_populates="documents")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "application_id": self.application_id,
            "original_filename": self.original_filename,
            "mapped_type": self.mapped_type,
            "mapping_confidence": self.mapping_confidence,
            "mapping_stage": self.mapping_stage,
            "candidate_types": safe_json_loads(self.candidate_types, []),
            "ocr_status": self.ocr_status,
            "page_count": self.page_count,
            "extracted_fields": safe_json_loads(self.extracted_fields, []),
            "bounding_boxes": safe_json_loads(self.bounding_boxes, []),
            "preview_url": self.preview_url,
            "document_body_text": self.document_body_text or "",
            "audit_history": safe_json_loads(self.audit_history, []),
            "remarks": self.remarks or "",
            "is_mandatory": self.is_mandatory,
            "upload_status": self.upload_status or "Uploaded",
            "document_status": self.document_status or "Reviewed"
        }

class FindingModel(Base):
    __tablename__ = "findings"

    id = Column(String, primary_key=True, index=True)
    application_id = Column(String, ForeignKey("applications.id"), index=True)
    rule_id = Column(String)
    rule_clause = Column(String)
    title = Column(String)
    explanation = Column(Text)
    why_evidence = Column(Text)
    validation_status = Column(String, default="DEFICIENT")
    verification_status = Column(String, default="PENDING_REVIEW")
    priority = Column(String, default="AMBER")
    document_id = Column(String, nullable=True)
    document_name = Column(String, nullable=True)
    page_number = Column(Integer, nullable=True)
    bounding_box = Column(Text, nullable=True)
    extracted_value = Column(String, nullable=True)
    expected_value = Column(String, nullable=True)
    confidence = Column(Float, default=0.95)
    suggested_action = Column(Text)
    reviewer_notes = Column(Text, nullable=True)
    disposition = Column(String, nullable=True)
    updated_at = Column(String)

    application = relationship("ApplicationModel", back_populates="findings")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "application_id": self.application_id,
            "rule_id": self.rule_id,
            "rule_clause": self.rule_clause,
            "title": self.title,
            "explanation": self.explanation,
            "why_evidence": self.why_evidence,
            "validation_status": self.validation_status if self.validation_status in ["PASS", "DEFICIENCY", "INSUFFICIENT EVIDENCE", "NOT APPLICABLE", "NOT EVALUATED"] else ("DEFICIENCY" if "DEFIC" in str(self.validation_status).upper() else "PASS"),
            "verification_status": "MANUAL REVIEW" if str(self.verification_status) in ["PENDING_REVIEW", "MANUAL_REVIEW", "MANUAL REVIEW"] else ("VERIFIED" if str(self.verification_status) == "VERIFIED" else "PENDING"),
            "priority": self.priority if self.priority in ["RED", "AMBER", "GREEN"] else "AMBER",
            "document_id": self.document_id,
            "document_name": self.document_name,
            "page_number": self.page_number,
            "bounding_box": safe_json_loads(self.bounding_box, None) if safe_json_loads(self.bounding_box, None) and isinstance(safe_json_loads(self.bounding_box, None), dict) and safe_json_loads(self.bounding_box, None).get("label") else None,
            "extracted_value": self.extracted_value,
            "expected_value": self.expected_value,
            "confidence": self.confidence,
            "suggested_action": self.suggested_action,
            "reviewer_notes": self.reviewer_notes,
            "disposition": self.disposition,
            "updated_at": self.updated_at
        }

class EVCEvidenceModel(Base):
    __tablename__ = "evc_evidence"

    id = Column(String, primary_key=True, index=True)
    application_id = Column(String, ForeignKey("applications.id"), index=True)
    category = Column(String)
    filename = Column(String)
    file_type = Column(String, default="image")
    preview_url = Column(String)
    phash = Column(String)
    duplicate_flag = Column(Boolean, default=False)
    duplicate_match_app = Column(String, nullable=True)
    duplicate_match_institution = Column(String, nullable=True)
    duplicate_similarity = Column(Float, nullable=True)
    duplicate_explanation = Column(Text, nullable=True)
    exif_gps = Column(Text, nullable=True)
    declared_gps = Column(Text, nullable=True)
    gps_distance_km = Column(Float, nullable=True)
    gps_match_status = Column(String, nullable=True)
    video_keyframes = Column(Text, default="[]")
    inspection_needed = Column(Boolean, default=False)
    inspection_reason = Column(Text, nullable=True)
    reviewer_notes = Column(Text, nullable=True)

    application = relationship("ApplicationModel", back_populates="evc_items")

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "application_id": self.application_id,
            "category": self.category,
            "filename": self.filename,
            "file_type": self.file_type,
            "preview_url": self.preview_url,
            "phash": self.phash,
            "duplicate_flag": self.duplicate_flag,
            "duplicate_match_app": self.duplicate_match_app,
            "duplicate_match_institution": self.duplicate_match_institution,
            "duplicate_similarity": self.duplicate_similarity,
            "duplicate_explanation": self.duplicate_explanation,
            "exif_gps": safe_json_loads(self.exif_gps, None),
            "declared_gps": safe_json_loads(self.declared_gps, None),
            "gps_distance_km": self.gps_distance_km,
            "gps_match_status": self.gps_match_status,
            "video_keyframes": safe_json_loads(self.video_keyframes, []),
            "inspection_needed": self.inspection_needed,
            "inspection_reason": self.inspection_reason,
            "reviewer_notes": self.reviewer_notes
        }

class RuleModel(Base):
    __tablename__ = "rules"

    id = Column(String, primary_key=True, index=True)
    title = Column(String)
    category = Column(String)
    academic_year = Column(String, default="2025-26")
    clause = Column(String)
    source_title = Column(String)
    validation_logic = Column(Text)
    severity = Column(String)
    outcome_guidance = Column(Text)
    is_active = Column(Boolean, default=True)
    version = Column(String, default="1.0")
    effective_from = Column(String)
    effective_to = Column(String)
    author = Column(String)
    last_reviewed = Column(String)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title": self.title,
            "category": self.category,
            "academic_year": self.academic_year,
            "clause": self.clause,
            "source_title": self.source_title,
            "validation_logic": self.validation_logic,
            "severity": self.severity,
            "outcome_guidance": self.outcome_guidance,
            "is_active": self.is_active,
            "version": self.version,
            "effective_from": self.effective_from,
            "effective_to": self.effective_to,
            "author": self.author,
            "last_reviewed": self.last_reviewed
        }

class AuditEventModel(Base):
    __tablename__ = "audit_events"

    id = Column(String, primary_key=True, index=True)
    timestamp = Column(String)
    user_name = Column(String)
    user_role = Column(String)
    action = Column(String)
    target_type = Column(String)
    target_id = Column(String)
    details = Column(Text)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "timestamp": self.timestamp,
            "user_name": self.user_name,
            "user_role": self.user_role,
            "action": self.action,
            "target_type": self.target_type,
            "target_id": self.target_id,
            "details": self.details
        }

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    Base.metadata.create_all(bind=engine)
