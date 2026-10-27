import os
import json
from database import (
    engine, Base, SessionLocal,
    ApplicationModel, DocumentModel, FindingModel, EVCEvidenceModel, RuleModel, AuditEventModel,
    safe_json_dumps
)
from rich_app_generator import get_rich_documents_for_all_apps

def build_seed_dataset():
    apps = [
        # =========================================================================
        # CATEGORY 1: New Technical Institution (4 Applications)
        # =========================================================================
        {
            "id": "app-nti-01",
            "application_number": "AICTE-2025-NEW-0101",
            "academic_year": "2025-26",
            "institution_name": "St. Xavier Institute of Technology & Engineering",
            "institution_id": "1-11029384",
            "institution_address": "Plot No. 12, Sector 24, Kharghar, Navi Mumbai, Maharashtra - 410210",
            "category": "New Technical Institution",
            "status": "UNDER_SCRUTINY",
            "priority": "AMBER",
            "assigned_reviewer": "Prof. S. R. Sharma (Senior Scrutiny Officer)",
            "created_at": "2025-03-10 11:30:00",
            "declared_lat": 19.0434,
            "declared_lon": 73.0645,
            "trust_name": "St. Xavier Educational Trust Bombay",
            "total_intake_applied": 360,
            "total_carpet_area_sqm": 8500.0,
            "documents_count": 7,
            "findings_count": 2,
            "evc_items_count": 4,
            "deficiency_count": 1,
            "compliance_score": 84,
            "expected_documents_count": 7,
            "workflow_stage": "document_verification",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "Action Required", "evc_evidence": "In Progress", "final_summary": "Not Started"}),
            "review_cycle": 1
        },
        {
            "id": "app-nti-02",
            "application_number": "AICTE-2025-NEW-0102",
            "academic_year": "2025-26",
            "institution_name": "Kalinga Institute of Engineering & Emerging Technologies",
            "institution_id": "1-11029385",
            "institution_address": "Plot No. 441, Infocity Avenue, Patia, Bhubaneswar, Odisha - 751024",
            "category": "New Technical Institution",
            "status": "UNDER_SCRUTINY",
            "priority": "GREEN",
            "assigned_reviewer": "Dr. Neha Verma (Joint Director, Scrutiny)",
            "created_at": "2025-03-11 09:15:00",
            "declared_lat": 20.3556,
            "declared_lon": 85.8189,
            "trust_name": "Kalinga Foundation & Education Society",
            "total_intake_applied": 300,
            "total_carpet_area_sqm": 9200.0,
            "documents_count": 7,
            "findings_count": 1,
            "evc_items_count": 4,
            "deficiency_count": 0,
            "compliance_score": 96,
            "expected_documents_count": 7,
            "workflow_stage": "checklist",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "In Progress", "evc_evidence": "In Progress", "final_summary": "Not Started"}),
            "review_cycle": 1
        },
        {
            "id": "app-nti-03",
            "application_number": "AICTE-2025-NEW-0103",
            "academic_year": "2025-26",
            "institution_name": "Heritage Institute of Technology & Research",
            "institution_id": "1-11029386",
            "institution_address": "RIICO Industrial Area, Phase IV, Sitapura, Jaipur, Rajasthan - 302022",
            "category": "New Technical Institution",
            "status": "UNDER_SCRUTINY",
            "priority": "GREEN",
            "assigned_reviewer": "Dr. M. K. Ananth (EVC Committee Member)",
            "created_at": "2025-03-12 14:00:00",
            "declared_lat": 26.7725,
            "declared_lon": 75.8456,
            "trust_name": "Heritage Vidya Niketan Society",
            "total_intake_applied": 240,
            "total_carpet_area_sqm": 6800.0,
            "documents_count": 7,
            "findings_count": 1,
            "evc_items_count": 4,
            "deficiency_count": 0,
            "compliance_score": 92,
            "expected_documents_count": 7,
            "workflow_stage": "checklist",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "In Progress", "evc_evidence": "In Progress", "final_summary": "Not Started"}),
            "review_cycle": 1
        },
        {
            "id": "app-nti-04",
            "application_number": "AICTE-2025-NEW-0104",
            "academic_year": "2025-26",
            "institution_name": "Dr. A.P.J. Abdul Kalam Technical Campus",
            "institution_id": "1-11029387",
            "institution_address": "Sector 11, Jankipuram Extension, Kursi Road, Lucknow, Uttar Pradesh - 226031",
            "category": "New Technical Institution",
            "status": "DEFICIENCY_FLAGGED",
            "priority": "RED",
            "assigned_reviewer": "Prof. S. R. Sharma (Senior Scrutiny Officer)",
            "created_at": "2025-03-13 16:30:00",
            "declared_lat": 26.9214,
            "declared_lon": 80.9521,
            "trust_name": "Kalam Memorial Education Foundation",
            "total_intake_applied": 300,
            "total_carpet_area_sqm": 7900.0,
            "documents_count": 7,
            "findings_count": 3,
            "evc_items_count": 4,
            "deficiency_count": 2,
            "compliance_score": 62,
            "expected_documents_count": 7,
            "workflow_stage": "document_verification",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "Action Required", "evc_evidence": "In Progress", "final_summary": "Not Started"}),
            "review_cycle": 1
        },

        # =========================================================================
        # CATEGORY 2: Extension of Approval (EoA) (4 Applications)
        # =========================================================================
        {
            "id": "app-001",
            "application_number": "AICTE-2025-ENG-0891",
            "academic_year": "2025-26",
            "institution_name": "Vishwa Bharati Institute of Technology & Science",
            "institution_id": "1-44981023",
            "institution_address": "Survey No. 42/1, Electronic City Phase 2, Bengaluru, Karnataka - 560100",
            "category": "Extension of Approval (EoA)",
            "status": "UNDER_SCRUTINY",
            "priority": "AMBER",
            "assigned_reviewer": "Prof. S. R. Sharma (Senior Scrutiny Officer)",
            "created_at": "2025-03-12 10:14:00",
            "declared_lat": 12.9716,
            "declared_lon": 77.5946,
            "trust_name": "Vishwa Bharati Educational Foundation",
            "total_intake_applied": 420,
            "total_carpet_area_sqm": 5820.0,
            "documents_count": 7,
            "findings_count": 4,
            "evc_items_count": 4,
            "deficiency_count": 1,
            "compliance_score": 82,
            "expected_documents_count": 7,
            "workflow_stage": "document_verification",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "Action Required", "evc_evidence": "In Progress", "final_summary": "Not Started"}),
            "review_cycle": 1
        },
        {
            "id": "app-003",
            "application_number": "AICTE-2025-ENG-1104",
            "academic_year": "2025-26",
            "institution_name": "Sree Rama Engineering College",
            "institution_id": "1-99238471",
            "institution_address": "Rami Reddy Nagar, Karakambadi Road, Venkatapuram, Renigunta (M), Tirupati District, Andhra Pradesh - 517507",
            "category": "Extension of Approval (EoA)",
            "status": "UNDER_SCRUTINY",
            "priority": "GREEN",
            "assigned_reviewer": "Dr. Neha Verma (Joint Director, Scrutiny)",
            "created_at": "2025-03-15 09:20:00",
            "declared_lat": 13.6586,
            "declared_lon": 79.4900,
            "trust_name": "Sri Rama Educational Society",
            "total_intake_applied": 540,
            "total_carpet_area_sqm": 13490.0,
            "documents_count": 8,
            "findings_count": 3,
            "evc_items_count": 4,
            "deficiency_count": 0,
            "compliance_score": 98,
            "expected_documents_count": 8,
            "workflow_stage": "checklist",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "In Progress", "evc_evidence": "In Progress", "final_summary": "Not Started"}),
            "review_cycle": 1
        },
        {
            "id": "app-eoa-03",
            "application_number": "AICTE-2025-ENG-1105",
            "academic_year": "2025-26",
            "institution_name": "PSG College of Technology & Applied Research",
            "institution_id": "1-99238472",
            "institution_address": "Avinashi Road, Peelamedu, Coimbatore, Tamil Nadu - 641004",
            "category": "Extension of Approval (EoA)",
            "status": "APPROVED_SCRUTINY",
            "priority": "GREEN",
            "assigned_reviewer": "Dr. M. K. Ananth (EVC Committee Member)",
            "created_at": "2025-03-16 11:10:00",
            "declared_lat": 11.0242,
            "declared_lon": 76.9945,
            "trust_name": "PSG & Sons' Charities",
            "total_intake_applied": 780,
            "total_carpet_area_sqm": 16400.0,
            "documents_count": 8,
            "findings_count": 1,
            "evc_items_count": 4,
            "deficiency_count": 0,
            "compliance_score": 100,
            "expected_documents_count": 8,
            "workflow_stage": "final_summary",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "Completed", "evc_evidence": "Completed", "final_summary": "Completed"}),
            "review_cycle": 1
        },
        {
            "id": "app-004",
            "application_number": "AICTE-2025-PHARM-0199",
            "academic_year": "2025-26",
            "institution_name": "Saraswati College of Pharmaceutical Sciences",
            "institution_id": "1-77123901",
            "institution_address": "NH-48, Gandhinagar Highway, Ahmedabad, Gujarat - 382421",
            "category": "Extension of Approval (EoA)",
            "status": "UNDER_SCRUTINY",
            "priority": "AMBER",
            "assigned_reviewer": "Prof. S. R. Sharma (Senior Scrutiny Officer)",
            "created_at": "2025-03-16 16:45:00",
            "declared_lat": 23.2156,
            "declared_lon": 72.6369,
            "trust_name": "Saraswati Education Trust",
            "total_intake_applied": 100,
            "total_carpet_area_sqm": 3450.0,
            "documents_count": 7,
            "findings_count": 2,
            "evc_items_count": 4,
            "deficiency_count": 1,
            "compliance_score": 78,
            "expected_documents_count": 7,
            "workflow_stage": "document_verification",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "Action Required", "evc_evidence": "In Progress", "final_summary": "Not Started"}),
            "review_cycle": 1
        },

        # =========================================================================
        # CATEGORY 3: New Programme / Level (4 Applications)
        # =========================================================================
        {
            "id": "app-npl-01",
            "application_number": "AICTE-2025-PG-0301",
            "academic_year": "2025-26",
            "institution_name": "BMS Institute of Technology & Management",
            "institution_id": "1-55829104",
            "institution_address": "Doddaballapur Main Road, Avalahalli, Yelahanka, Bengaluru, Karnataka - 560064",
            "category": "New Programme / Level",
            "status": "UNDER_SCRUTINY",
            "priority": "GREEN",
            "assigned_reviewer": "Dr. Neha Verma (Joint Director, Scrutiny)",
            "created_at": "2025-03-13 11:20:00",
            "declared_lat": 13.1362,
            "declared_lon": 77.5684,
            "trust_name": "B.M.S. Educational Trust",
            "total_intake_applied": 60,
            "total_carpet_area_sqm": 6200.0,
            "documents_count": 7,
            "findings_count": 1,
            "evc_items_count": 4,
            "deficiency_count": 0,
            "compliance_score": 94,
            "expected_documents_count": 7,
            "workflow_stage": "checklist",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "In Progress", "evc_evidence": "In Progress", "final_summary": "Not Started"}),
            "review_cycle": 1
        },
        {
            "id": "app-npl-02",
            "application_number": "AICTE-2025-PG-0302",
            "academic_year": "2025-26",
            "institution_name": "Vellore Institute of Technology & Advanced Studies",
            "institution_id": "1-55829105",
            "institution_address": "Vandalur-Kelambakkam Road, Chennai, Tamil Nadu - 600127",
            "category": "New Programme / Level",
            "status": "UNDER_SCRUTINY",
            "priority": "AMBER",
            "assigned_reviewer": "Prof. S. R. Sharma (Senior Scrutiny Officer)",
            "created_at": "2025-03-14 10:45:00",
            "declared_lat": 12.8406,
            "declared_lon": 80.1534,
            "trust_name": "North Arcot Educational Charitable Trust",
            "total_intake_applied": 120,
            "total_carpet_area_sqm": 8400.0,
            "documents_count": 7,
            "findings_count": 2,
            "evc_items_count": 4,
            "deficiency_count": 1,
            "compliance_score": 80,
            "expected_documents_count": 7,
            "workflow_stage": "document_verification",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "Action Required", "evc_evidence": "In Progress", "final_summary": "Not Started"}),
            "review_cycle": 1
        },
        {
            "id": "app-npl-03",
            "application_number": "AICTE-2025-PG-0303",
            "academic_year": "2025-26",
            "institution_name": "G.H. Raisoni College of Engineering & Management",
            "institution_id": "1-55829106",
            "institution_address": "Gat No. 1200, Domkhel Road, Wagholi, Pune, Maharashtra - 412207",
            "category": "New Programme / Level",
            "status": "UNDER_SCRUTINY",
            "priority": "GREEN",
            "assigned_reviewer": "Dr. M. K. Ananth (EVC Committee Member)",
            "created_at": "2025-03-15 15:10:00",
            "declared_lat": 18.5793,
            "declared_lon": 73.9827,
            "trust_name": "Raisoni Shikshan Prasarak Mandal",
            "total_intake_applied": 60,
            "total_carpet_area_sqm": 7100.0,
            "documents_count": 7,
            "findings_count": 1,
            "evc_items_count": 4,
            "deficiency_count": 0,
            "compliance_score": 95,
            "expected_documents_count": 7,
            "workflow_stage": "checklist",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "In Progress", "evc_evidence": "In Progress", "final_summary": "Not Started"}),
            "review_cycle": 1
        },
        {
            "id": "app-npl-04",
            "application_number": "AICTE-2025-PG-0304",
            "academic_year": "2025-26",
            "institution_name": "Chaitanya Bharathi Institute of Technology",
            "institution_id": "1-55829107",
            "institution_address": "Gandipet, Kokapet (V), Hyderabad, Telangana - 500075",
            "category": "New Programme / Level",
            "status": "APPROVED_SCRUTINY",
            "priority": "GREEN",
            "assigned_reviewer": "Dr. Neha Verma (Joint Director, Scrutiny)",
            "created_at": "2025-03-16 12:00:00",
            "declared_lat": 17.3916,
            "declared_lon": 78.3188,
            "trust_name": "Chaitanya Bharathi Educational Society",
            "total_intake_applied": 60,
            "total_carpet_area_sqm": 9400.0,
            "documents_count": 7,
            "findings_count": 1,
            "evc_items_count": 4,
            "deficiency_count": 0,
            "compliance_score": 98,
            "expected_documents_count": 7,
            "workflow_stage": "final_summary",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "Completed", "evc_evidence": "Completed", "final_summary": "Completed"}),
            "review_cycle": 1
        },

        # =========================================================================
        # CATEGORY 4: Intake Increase (4 Applications)
        # =========================================================================
        {
            "id": "app-002",
            "application_number": "AICTE-2025-ENG-0422",
            "academic_year": "2025-26",
            "institution_name": "Apex Institute of Technology & Research",
            "institution_id": "1-88910245",
            "institution_address": "Sector 14, BVB Campus, Hubballi-Dharwad, Karnataka - 580031",
            "category": "Intake Increase",
            "status": "DEFICIENCY_FLAGGED",
            "priority": "RED",
            "assigned_reviewer": "Dr. M. K. Ananth (EVC Committee Member)",
            "created_at": "2025-03-14 14:32:00",
            "declared_lat": 15.3647,
            "declared_lon": 75.1240,
            "trust_name": "Apex Shaikshanik Sanstha",
            "total_intake_applied": 600,
            "total_carpet_area_sqm": 3780.0,
            "documents_count": 8,
            "findings_count": 3,
            "evc_items_count": 4,
            "deficiency_count": 3,
            "compliance_score": 58,
            "expected_documents_count": 8,
            "workflow_stage": "document_verification",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "Action Required", "evc_evidence": "Action Required", "final_summary": "Not Started"}),
            "review_cycle": 1
        },
        {
            "id": "app-ii-02",
            "application_number": "AICTE-2025-ENG-0423",
            "academic_year": "2025-26",
            "institution_name": "Kumaraguru College of Technology",
            "institution_id": "1-88910246",
            "institution_address": "Athipalayam Road, Chinnavedampatti, Coimbatore, Tamil Nadu - 641049",
            "category": "Intake Increase",
            "status": "UNDER_SCRUTINY",
            "priority": "GREEN",
            "assigned_reviewer": "Prof. S. R. Sharma (Senior Scrutiny Officer)",
            "created_at": "2025-03-14 16:15:00",
            "declared_lat": 11.0827,
            "declared_lon": 76.9934,
            "trust_name": "Ramanadha Adigalar Educational Trust",
            "total_intake_applied": 540,
            "total_carpet_area_sqm": 12800.0,
            "documents_count": 8,
            "findings_count": 2,
            "evc_items_count": 4,
            "deficiency_count": 0,
            "compliance_score": 95,
            "expected_documents_count": 8,
            "workflow_stage": "checklist",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "In Progress", "evc_evidence": "In Progress", "final_summary": "Not Started"}),
            "review_cycle": 1
        },
        {
            "id": "app-ii-03",
            "application_number": "AICTE-2025-ENG-0424",
            "academic_year": "2025-26",
            "institution_name": "Thakur College of Engineering & Technology",
            "institution_id": "1-88910247",
            "institution_address": "A-Block, Thakur Educational Campus, Shyamnarayan Thakur Marg, Kandivali (E), Mumbai - 400101",
            "category": "Intake Increase",
            "status": "UNDER_SCRUTINY",
            "priority": "GREEN",
            "assigned_reviewer": "Dr. Neha Verma (Joint Director, Scrutiny)",
            "created_at": "2025-03-15 11:40:00",
            "declared_lat": 19.2064,
            "declared_lon": 72.8732,
            "trust_name": "Zagdu Singh Charitable Trust",
            "total_intake_applied": 240,
            "total_carpet_area_sqm": 8900.0,
            "documents_count": 8,
            "findings_count": 1,
            "evc_items_count": 4,
            "deficiency_count": 0,
            "compliance_score": 93,
            "expected_documents_count": 8,
            "workflow_stage": "checklist",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "In Progress", "evc_evidence": "In Progress", "final_summary": "Not Started"}),
            "review_cycle": 1
        },
        {
            "id": "app-ii-04",
            "application_number": "AICTE-2025-ENG-0425",
            "academic_year": "2025-26",
            "institution_name": "Vasavi College of Engineering",
            "institution_id": "1-88910248",
            "institution_address": "9-5-81, Ibrahimbagh, Hyderabad, Telangana - 500031",
            "category": "Intake Increase",
            "status": "UNDER_SCRUTINY",
            "priority": "AMBER",
            "assigned_reviewer": "Dr. M. K. Ananth (EVC Committee Member)",
            "created_at": "2025-03-16 14:00:00",
            "declared_lat": 17.3804,
            "declared_lon": 78.3826,
            "trust_name": "Vasavi Academy of Education",
            "total_intake_applied": 180,
            "total_carpet_area_sqm": 7600.0,
            "documents_count": 8,
            "findings_count": 2,
            "evc_items_count": 4,
            "deficiency_count": 1,
            "compliance_score": 81,
            "expected_documents_count": 8,
            "workflow_stage": "document_verification",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "Action Required", "evc_evidence": "In Progress", "final_summary": "Not Started"}),
            "review_cycle": 1
        },

        # =========================================================================
        # CATEGORY 5: Other Application Types (4 Applications)
        # =========================================================================
        {
            "id": "app-oth-01",
            "application_number": "AICTE-2025-OTH-0501",
            "academic_year": "2025-26",
            "institution_name": "Priyadarshini College of Engineering & Architecture",
            "institution_id": "1-66778891",
            "institution_address": "Near CRPF Campus, Hingna Road, Digdoh Hills, Nagpur, Maharashtra - 440019",
            "category": "Other Application Types",
            "status": "DEFICIENCY_FLAGGED",
            "priority": "AMBER",
            "assigned_reviewer": "Prof. S. R. Sharma (Senior Scrutiny Officer)",
            "created_at": "2025-03-11 15:45:00",
            "declared_lat": 21.1075,
            "declared_lon": 79.0028,
            "trust_name": "Lokmanya Tilak Jankalyan Shikshan Sanstha",
            "total_intake_applied": 0,
            "total_carpet_area_sqm": 5400.0,
            "documents_count": 6,
            "findings_count": 2,
            "evc_items_count": 4,
            "deficiency_count": 1,
            "compliance_score": 75,
            "expected_documents_count": 6,
            "workflow_stage": "document_verification",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "Action Required", "evc_evidence": "In Progress", "final_summary": "Not Started"}),
            "review_cycle": 1
        },
        {
            "id": "app-oth-02",
            "application_number": "AICTE-2025-OTH-0502",
            "academic_year": "2025-26",
            "institution_name": "Symbiosis Institute of Applied International Studies",
            "institution_id": "1-66778892",
            "institution_address": "Gram Lavale, Taluka Mulshi, Pune, Maharashtra - 412115",
            "category": "Other Application Types",
            "status": "UNDER_SCRUTINY",
            "priority": "GREEN",
            "assigned_reviewer": "Dr. Neha Verma (Joint Director, Scrutiny)",
            "created_at": "2025-03-12 16:20:00",
            "declared_lat": 18.5308,
            "declared_lon": 73.7297,
            "trust_name": "Symbiosis Society Pune",
            "total_intake_applied": 60,
            "total_carpet_area_sqm": 8200.0,
            "documents_count": 7,
            "findings_count": 1,
            "evc_items_count": 4,
            "deficiency_count": 0,
            "compliance_score": 94,
            "expected_documents_count": 7,
            "workflow_stage": "checklist",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "In Progress", "evc_evidence": "In Progress", "final_summary": "Not Started"}),
            "review_cycle": 1
        },
        {
            "id": "app-oth-03",
            "application_number": "AICTE-2025-OTH-0503",
            "academic_year": "2025-26",
            "institution_name": "Aditya Institute of Technology & Management",
            "institution_id": "1-66778893",
            "institution_address": "K.Kotturu, Tekkali, Srikakulam District, Andhra Pradesh - 532201",
            "category": "Other Application Types",
            "status": "APPROVED_SCRUTINY",
            "priority": "GREEN",
            "assigned_reviewer": "Dr. M. K. Ananth (EVC Committee Member)",
            "created_at": "2025-03-13 13:10:00",
            "declared_lat": 18.6186,
            "declared_lon": 84.2341,
            "trust_name": "Sri Aditya Educational Society",
            "total_intake_applied": 480,
            "total_carpet_area_sqm": 11200.0,
            "documents_count": 6,
            "findings_count": 1,
            "evc_items_count": 4,
            "deficiency_count": 0,
            "compliance_score": 97,
            "expected_documents_count": 6,
            "workflow_stage": "final_summary",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "Completed", "evc_evidence": "Completed", "final_summary": "Completed"}),
            "review_cycle": 1
        },
        {
            "id": "app-oth-04",
            "application_number": "AICTE-2025-OTH-0504",
            "academic_year": "2025-26",
            "institution_name": "Dr. D.Y. Patil Institute of Engineering & Technology",
            "institution_id": "1-66778894",
            "institution_address": "Sant Tukaram Nagar, Pimpri, Pune, Maharashtra - 411018",
            "category": "Other Application Types",
            "status": "UNDER_SCRUTINY",
            "priority": "GREEN",
            "assigned_reviewer": "Prof. S. R. Sharma (Senior Scrutiny Officer)",
            "created_at": "2025-03-14 17:30:00",
            "declared_lat": 18.6256,
            "declared_lon": 73.8184,
            "trust_name": "Dr. D.Y. Patil Educational Pratishthan",
            "total_intake_applied": 600,
            "total_carpet_area_sqm": 14500.0,
            "documents_count": 7,
            "findings_count": 1,
            "evc_items_count": 4,
            "deficiency_count": 0,
            "compliance_score": 96,
            "expected_documents_count": 7,
            "workflow_stage": "checklist",
            "stage_progress": json.dumps({"checklist": "Completed", "document_verification": "In Progress", "evc_evidence": "In Progress", "final_summary": "Not Started"}),
            "review_cycle": 1
        }
    ]

    return apps

def build_all_documents():
    from mock_data import SAMPLE_DOCUMENTS
    docs_dict = dict(SAMPLE_DOCUMENTS)
    rich_docs = get_rich_documents_for_all_apps()
    docs_dict.update(rich_docs)

    # For any remaining app, synthesize genuine handbook documents tailored to that institution
    remaining_apps = ["app-npl-02", "app-npl-03", "app-npl-04", "app-ii-03", "app-ii-04"]
    apps_meta = {a["id"]: a for a in build_seed_dataset()}

    for app_id in remaining_apps:
        if app_id in apps_meta:
            meta = apps_meta[app_id]
            is_intake = "Intake" in meta["category"]
            affidavit_type = "Affidavit 8 (Additional Course/Increase in Intake)" if is_intake else "Affidavit 2 (Self-Disclosure)"
            affidavit_no = "AFFIDAVIT-8" if is_intake else "AFFIDAVIT-2"
            docs_dict[app_id] = [
                {
                    "id": f"doc-{app_id[4:]}-1",
                    "application_id": app_id,
                    "original_filename": f"{affidavit_no}_{meta['institution_name'].split()[0]}.pdf",
                    "mapped_type": affidavit_type,
                    "mapping_confidence": 0.98,
                    "mapping_stage": "Content Confirmation (OCR)",
                    "candidate_types": json.dumps([{"type": affidavit_type, "score": 0.98}]),
                    "ocr_status": "COMPLETED",
                    "page_count": 3,
                    "document_body_text": f"""Approval Process Handbook 2024-2027
{affidavit_no}
I/we, Authorised Signatory, {meta['trust_name']} do hereby affirm and declare:
1. Applied for {meta['category']} for {meta['institution_name']}, {meta['institution_address']} vide {meta['application_number']}.
2. Abiding by all rules and regulations of the AICTE Approval Process Handbook.
3. Total Built-Up Area: {meta['total_carpet_area_sqm']:,.2f} Sq.M. ready in all respects.
4. Total Applied Intake: {meta['total_intake_applied']} seats.
DEPONENT: Authorized Trustee. Sworn before Notary Public.""",
                    "extracted_fields": json.dumps([
                        {"key": "app_num", "label": "Application Ref", "value": meta["application_number"], "confidence": 0.99, "page": 1, "provenance": "Clause 1"},
                        {"key": "intake", "label": "Intake", "value": str(meta["total_intake_applied"]), "confidence": 0.98, "page": 1, "provenance": "Clause 4"}
                    ]),
                    "bounding_boxes": json.dumps([{"x": 10, "y": 30, "width": 80, "height": 8, "label": meta["application_number"], "page": 1}]),
                    "remarks": f"Verified {affidavit_no} conforming to APH norms.",
                    "is_mandatory": True,
                    "upload_status": "Uploaded",
                    "document_status": "Reviewed"
                },
                {
                    "id": f"doc-{app_id[4:]}-2",
                    "application_id": app_id,
                    "original_filename": f"Architect_Certificate_2_{app_id[4:]}.pdf",
                    "mapped_type": "Certificate of an Architect (Certificate-2)",
                    "mapping_confidence": 0.97,
                    "mapping_stage": "Content Confirmation (OCR)",
                    "candidate_types": json.dumps([{"type": "Certificate of an Architect (Certificate-2)", "score": 0.97}]),
                    "ocr_status": "COMPLETED",
                    "page_count": 2,
                    "document_body_text": f"""Approval Process Handbook 2024-2027 (Page 212)
CERTIFICATE-2 (Certificate of an Architect)
Registered Architect (Council of Architecture).
Certified that site plan and building plans for {meta['institution_name']} have been approved.
Total Completed Carpet / Built-Up Area: {meta['total_carpet_area_sqm']:,.2f} Sq.M.
Flooring, painting, electrification, and safety exits complete as per approved plans.""",
                    "extracted_fields": json.dumps([{"key": "area", "label": "Carpet Area", "value": f"{meta['total_carpet_area_sqm']:,.2f} Sq.M.", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
                    "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": f"{meta['total_carpet_area_sqm']:,.2f} Sq.M.", "page": 1}]),
                    "remarks": f"Architect certified {meta['total_carpet_area_sqm']:,.2f} sqm.",
                    "is_mandatory": True,
                    "upload_status": "Uploaded",
                    "document_status": "Reviewed"
                },
                {
                    "id": f"doc-{app_id[4:]}-3",
                    "application_id": app_id,
                    "original_filename": f"Format2_University_NOC_{app_id[4:]}.pdf",
                    "mapped_type": "NOC from Affiliating University (Format-2)",
                    "mapping_confidence": 0.98,
                    "mapping_stage": "Content Confirmation (OCR)",
                    "candidate_types": json.dumps([{"type": "NOC from Affiliating University (Format-2)", "score": 0.98}]),
                    "ocr_status": "COMPLETED",
                    "page_count": 2,
                    "document_body_text": f"""Approval Process Handbook 2024-2027 (Page 202)
FORMAT-2 (Affiliating University NOC)
The Affiliating University has No Objection for {meta['category']} of {meta['institution_name']} for {meta['total_intake_applied']} seats.
Registrar.""",
                    "extracted_fields": json.dumps([{"key": "univ", "label": "University NOC", "value": "NO OBJECTION", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
                    "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "University NOC Granted", "page": 1}]),
                    "remarks": "University NOC verified.",
                    "is_mandatory": True,
                    "upload_status": "Uploaded",
                    "document_status": "Reviewed"
                },
                {
                    "id": f"doc-{app_id[4:]}-4",
                    "application_id": app_id,
                    "original_filename": f"Format3_Trust_Resolution_{app_id[4:]}.pdf",
                    "mapped_type": "Resolution of the Trust (Format-3)",
                    "mapping_confidence": 0.96,
                    "mapping_stage": "Content Confirmation (OCR)",
                    "candidate_types": json.dumps([{"type": "Resolution of the Trust (Format-3)", "score": 0.96}]),
                    "ocr_status": "COMPLETED",
                    "page_count": 1,
                    "document_body_text": f"""Approval Process Handbook 2024-2027 (Page 205)
FORMAT-3 (Resolution of Trust)
{meta['trust_name']} Governing Body resolved to apply for {meta['category']} for {meta['institution_name']} and allocate required operational budget.""",
                    "extracted_fields": json.dumps([{"key": "res", "label": "Trust Resolution", "value": "ADOPTED", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
                    "bounding_boxes": json.dumps([{"x": 10, "y": 40, "width": 80, "height": 8, "label": "Trust Resolution Passed", "page": 1}]),
                    "remarks": "Trust resolution verified.",
                    "is_mandatory": True,
                    "upload_status": "Uploaded",
                    "document_status": "Reviewed"
                },
                {
                    "id": f"doc-{app_id[4:]}-5",
                    "application_id": app_id,
                    "original_filename": f"Fire_Safety_NOC_{app_id[4:]}.pdf",
                    "mapped_type": "Fire Safety Certificate",
                    "mapping_confidence": 0.96,
                    "mapping_stage": "Content Confirmation (OCR)",
                    "candidate_types": json.dumps([{"type": "Fire Safety Certificate", "score": 0.96}]),
                    "ocr_status": "COMPLETED",
                    "page_count": 2,
                    "document_body_text": f"""STATE DISASTER RESPONSE & FIRE SERVICES DEPARTMENT
Fire Safety Clearance Certificate issued to {meta['institution_name']}.
Valid for 3 years up to 31-12-2027. Fire prevention measures conform to NBC 2016 Table-07.""",
                    "extracted_fields": json.dumps([{"key": "valid", "label": "Valid Till", "value": "31-12-2027", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
                    "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Valid till 31-12-2027", "page": 1}]),
                    "remarks": "Fire safety certificate valid.",
                    "is_mandatory": True,
                    "upload_status": "Uploaded",
                    "document_status": "Reviewed"
                },
                {
                    "id": f"doc-{app_id[4:]}-6",
                    "application_id": app_id,
                    "original_filename": f"Municipal_Occupancy_{app_id[4:]}.pdf",
                    "mapped_type": "Occupancy Certificate",
                    "mapping_confidence": 0.97,
                    "mapping_stage": "Content Confirmation (OCR)",
                    "candidate_types": json.dumps([{"type": "Occupancy Certificate", "score": 0.97}]),
                    "ocr_status": "COMPLETED",
                    "page_count": 1,
                    "document_body_text": f"""APPENDIX 'I' - FORM FOR OCCUPANCY CERTIFICATE
Municipal Corporation / Local Planning Authority.
Full Occupation Granted for {meta['institution_name']}, {meta['total_carpet_area_sqm']:,.2f} Sq.M.
Chief Officer / Municipal Town Planner.""",
                    "extracted_fields": json.dumps([{"key": "occ", "label": "Occupancy", "value": "FULL OCCUPANCY GRANTED", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
                    "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "FULL OCCUPATION GRANTED", "page": 1}]),
                    "remarks": "Occupancy verified.",
                    "is_mandatory": True,
                    "upload_status": "Uploaded",
                    "document_status": "Reviewed"
                },
                {
                    "id": f"doc-{app_id[4:]}-7",
                    "application_id": app_id,
                    "original_filename": f"TER_Fee_Receipt_{app_id[4:]}.pdf",
                    "mapped_type": "TER / Payment Receipt",
                    "mapping_confidence": 0.99,
                    "mapping_stage": "Content Confirmation (OCR)",
                    "candidate_types": json.dumps([{"type": "TER / Payment Receipt", "score": 0.99}]),
                    "ocr_status": "COMPLETED",
                    "page_count": 1,
                    "document_body_text": f"""AICTE PAYMENT RECEIPT
Transaction Ref: AICTE2025FEE{app_id[4:].upper()}99
Payment Status: SUCCESSFUL. Amount: Rs. 2,00,000/-.
Purpose: TER Charges for {meta['category']}.""",
                    "extracted_fields": json.dumps([{"key": "fee", "label": "Fee", "value": "Rs. 2,00,000/-", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
                    "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Rs. 2,00,000/- SUCCESS", "page": 1}]),
                    "remarks": "TER receipt verified.",
                    "is_mandatory": True,
                    "upload_status": "Uploaded",
                    "document_status": "Reviewed"
                }
            ]

    return docs_dict

def build_all_evc_items(apps_data):
    """
    Generates rich EVC evidence items covering the 11 mandatory categories required by AICTE:
    1. Institution's front and rear exterior
    2. Classrooms and tutorial rooms
    3. Laboratories and workshops
    4. Computer centre
    5. Library and reading room
    6. Drawing hall and seminar hall, where applicable
    7. Administrative offices
    8. Faculty seating
    9. Toilets, common rooms and cafeteria
    10. Entrance, passages, staircases and circulation areas
    11. Other required instructional and amenity areas
    """
    evc_items = []
    
    cat_templates = [
        {
            "category": "Institution's front and rear exterior",
            "filename": "EVC_Front_Rear_Exterior_Elevation.jpg",
            "file_type": "image",
            "preview_url": "https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=1200&auto=format&fit=crop&q=80",
            "phash": "a1f8e3d2c1b09876",
            "keyframes": []
        },
        {
            "category": "Classrooms and tutorial rooms",
            "filename": "EVC_Classrooms_BlockA_Inspection.jpg",
            "file_type": "image",
            "preview_url": "https://images.unsplash.com/photo-1580582932707-520aed937b7b?w=1200&auto=format&fit=crop&q=80",
            "phash": "b2e7d4c3f5a18765",
            "keyframes": []
        },
        {
            "category": "Laboratories and workshops",
            "filename": "EVC_Engineering_Workshops_Labs.jpg",
            "file_type": "image",
            "preview_url": "https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=1200&auto=format&fit=crop&q=80",
            "phash": "c3d6e5f4a2b37654",
            "keyframes": []
        },
        {
            "category": "Computer centre",
            "filename": "EVC_Central_Computer_Centre.jpg",
            "file_type": "image",
            "preview_url": "https://images.unsplash.com/photo-1562774053-701939374585?w=1200&auto=format&fit=crop&q=80",
            "phash": "9f8a3c2b1e4d5a6b",
            "keyframes": []
        },
        {
            "category": "Library and reading room",
            "filename": "EVC_Central_Library_Stack_Reading.jpg",
            "file_type": "image",
            "preview_url": "https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=1200&auto=format&fit=crop&q=80",
            "phash": "d4c5b6a7f8e96543",
            "keyframes": []
        },
        {
            "category": "Drawing hall and seminar hall, where applicable",
            "filename": "EVC_Seminar_Hall_AudioVisual.jpg",
            "file_type": "image",
            "preview_url": "https://images.unsplash.com/photo-1517457373958-b7bdd4587205?w=1200&auto=format&fit=crop&q=80",
            "phash": "e5b4a3f2d1c05432",
            "keyframes": []
        },
        {
            "category": "Administrative offices",
            "filename": "EVC_Principal_Admin_Offices.jpg",
            "file_type": "image",
            "preview_url": "https://images.unsplash.com/photo-1497366216548-37526070297c?w=1200&auto=format&fit=crop&q=80",
            "phash": "f6a5b4c3d2e14321",
            "keyframes": []
        },
        {
            "category": "Faculty seating",
            "filename": "EVC_Faculty_Cabins_BlockB.jpg",
            "file_type": "image",
            "preview_url": "https://images.unsplash.com/photo-1527192491265-7e15c55b1ed2?w=1200&auto=format&fit=crop&q=80",
            "phash": "a7b6c5d4e3f23210",
            "keyframes": []
        },
        {
            "category": "Toilets, common rooms and cafeteria",
            "filename": "EVC_Toilets_CommonRooms_Cafeteria.jpg",
            "file_type": "image",
            "preview_url": "https://images.unsplash.com/photo-1555396273-367ea4eb4db5?w=1200&auto=format&fit=crop&q=80",
            "phash": "b8c7d6e5f4a32109",
            "keyframes": []
        },
        {
            "category": "Entrance, passages, staircases and circulation areas",
            "filename": "EVC_Circulation_Staircases_Corridors.jpg",
            "file_type": "image",
            "preview_url": "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=1200&auto=format&fit=crop&q=80",
            "phash": "c9d8e7f6a5b41098",
            "keyframes": []
        },
        {
            "category": "Other required instructional and amenity areas",
            "filename": "EVC_Medical_FirstAid_Station.jpg",
            "file_type": "image",
            "preview_url": "https://images.unsplash.com/photo-1519494026892-80bbd2d6fd0d?w=1200&auto=format&fit=crop&q=80",
            "phash": "dae9f8a7b6c50987",
            "keyframes": []
        }
    ]

    for app in apps_data:
        app_id = app["id"]
        lat = app.get("declared_lat", 12.9716)
        lon = app.get("declared_lon", 77.5946)

        for idx, t in enumerate(cat_templates, 1):
            is_dup = False
            dup_match_app = None
            dup_match_inst = None
            dup_sim = 0.12
            dup_expl = None
            dist_km = 0.018 # 18m inside campus
            gps_status = "MATCHED (18m)"
            insp_needed = False
            insp_reason = None

            # Specifically flag duplicate for certain applications to demonstrate cross-institute matching
            if app_id in ["app-002", "app-nti-04"] and t["category"] == "Computer centre":
                is_dup = True
                dup_match_app = "AICTE-2025-ENG-0891 (Vishwa Bharati Institute)"
                dup_match_inst = "Vishwa Bharati Institute of Technology & Science, Bengaluru"
                dup_sim = 0.984
                dup_expl = "Visual pHash collision (Hamming distance 1). Whiteboard diagram, desktop monitor layout, and blue chair fabric match exactly with photo submitted by Vishwa Bharati Institute."
                insp_needed = True
                insp_reason = "Suspected duplicate visual evidence across institutions. Mandatory surprise on-site verification."

            if app_id in ["app-002"] and t["category"] == "Laboratories and workshops":
                is_dup = True
                dup_match_app = "AICTE-2025-NEW-0103 (Heritage Institute of Technology)"
                dup_match_inst = "Heritage Institute of Technology & Research, Jaipur"
                dup_sim = 0.962
                dup_expl = "Workshop lathe layout and safety instructional posters match footage filed by Heritage Institute."
                insp_needed = True
                insp_reason = "Reused workshop video footage detected. Physical inspection required."

            # Geotag discrepancy for app-002 on exterior
            if app_id == "app-002" and t["category"] == "Institution's front and rear exterior":
                dist_km = 14.2
                gps_status = "DISCREPANCY (14.2km)"
                insp_needed = True
                insp_reason = "EXIF coordinates diverge 14.2 km from approved campus boundary."

            evc_items.append({
                "id": f"evc-{app_id[4:]}-{idx:02d}",
                "application_id": app_id,
                "category": t["category"],
                "filename": t["filename"],
                "file_type": t["file_type"],
                "preview_url": t["preview_url"],
                "phash": t["phash"],
                "duplicate_flag": is_dup,
                "duplicate_match_app": dup_match_app,
                "duplicate_match_institution": dup_match_inst,
                "duplicate_similarity": dup_sim,
                "duplicate_explanation": dup_expl,
                "exif_gps": json.dumps({"lat": round(lat + (0.0001 if dist_km < 1 else 0.12), 4), "lon": round(lon + (0.0001 if dist_km < 1 else 0.09), 4)}),
                "declared_gps": json.dumps({"lat": lat, "lon": lon}),
                "gps_distance_km": dist_km,
                "gps_match_status": gps_status,
                "video_keyframes": json.dumps(t["keyframes"]),
                "inspection_needed": insp_needed,
                "inspection_reason": insp_reason,
                "reviewer_notes": "Reviewed in EVC room." if not insp_needed else "Flagged for on-site verification"
            })

    return evc_items

def seed_database():
    print("Initializing SQLite database tables via SQLAlchemy...")
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    try:
        # Wipe clean
        db.query(DocumentModel).delete()
        db.query(FindingModel).delete()
        db.query(EVCEvidenceModel).delete()
        db.query(ApplicationModel).delete()
        db.query(RuleModel).delete()
        db.query(AuditEventModel).delete()
        db.commit()

        apps_data = build_seed_dataset()
        for a in apps_data:
            a["evc_items_count"] = 11

        docs_dict = build_all_documents()
        all_evc_items = build_all_evc_items(apps_data)
        from mock_data import SAMPLE_RULES, SAMPLE_AUDIT_LOGS

        print(f"Seeding {len(apps_data)} applications...")
        for a_data in apps_data:
            app_obj = ApplicationModel(**a_data)
            db.add(app_obj)
        db.commit()

        print("Seeding documents...")
        for app_id, doc_list in docs_dict.items():
            for d in doc_list:
                doc_kwargs = d if isinstance(d, dict) else d.model_dump()
                clean_kwargs = {
                    "id": doc_kwargs["id"],
                    "application_id": doc_kwargs["application_id"],
                    "original_filename": doc_kwargs["original_filename"],
                    "mapped_type": doc_kwargs["mapped_type"],
                    "mapping_confidence": doc_kwargs.get("mapping_confidence", 0.9),
                    "mapping_stage": doc_kwargs.get("mapping_stage", "Content Confirmation (OCR)"),
                    "candidate_types": safe_json_dumps(doc_kwargs.get("candidate_types"), "[]"),
                    "ocr_status": doc_kwargs.get("ocr_status", "COMPLETED"),
                    "page_count": doc_kwargs.get("page_count", 1),
                    "extracted_fields": safe_json_dumps(doc_kwargs.get("extracted_fields"), "[]"),
                    "bounding_boxes": safe_json_dumps(doc_kwargs.get("bounding_boxes"), "[]"),
                    "preview_url": doc_kwargs.get("preview_url", ""),
                    "document_body_text": doc_kwargs.get("document_body_text", ""),
                    "audit_history": safe_json_dumps(doc_kwargs.get("audit_history"), "[]"),
                    "remarks": doc_kwargs.get("remarks", ""),
                    "is_mandatory": doc_kwargs.get("is_mandatory", True),
                    "upload_status": doc_kwargs.get("upload_status", "Uploaded"),
                    "document_status": doc_kwargs.get("document_status", "Reviewed")
                }
                db.add(DocumentModel(**clean_kwargs))
        db.commit()

        print(f"Seeding {len(all_evc_items)} EVC evidence items covering 11 categories...")
        for e in all_evc_items:
            db.add(EVCEvidenceModel(**e))
        db.commit()

        print("Executing Live Rule Verification Engine across all seeded applications...")
        from services.rule_engine import run_application_verification
        for a in apps_data:
            run_application_verification(a["id"], db)
        print("Live Rule Verification completed for all 20 applications!")

        print("Seeding rules...")
        for r in SAMPLE_RULES:
            r_kwargs = r if isinstance(r, dict) else r.model_dump()
            db.add(RuleModel(
                id=r_kwargs["id"],
                title=r_kwargs["title"],
                category=r_kwargs["category"],
                academic_year=r_kwargs.get("academic_year", "2025-26"),
                clause=r_kwargs["clause"],
                source_title=r_kwargs["source_title"],
                validation_logic=r_kwargs["validation_logic"],
                severity=r_kwargs["severity"],
                outcome_guidance=r_kwargs["outcome_guidance"],
                is_active=r_kwargs["is_active"],
                version=r_kwargs.get("version", "1.0"),
                effective_from=r_kwargs["effective_from"],
                effective_to=r_kwargs["effective_to"],
                author=r_kwargs["author"],
                last_reviewed=r_kwargs["last_reviewed"]
            ))
        db.commit()

        print("Seeding audit logs...")
        for a in SAMPLE_AUDIT_LOGS:
            a_kwargs = a if isinstance(a, dict) else a.model_dump()
            db.add(AuditEventModel(**a_kwargs))
        db.commit()

        total_apps = db.query(ApplicationModel).count()
        total_docs = db.query(DocumentModel).count()
        print(f"DATABASE SEED COMPLETE! Total Applications: {total_apps}, Total Documents: {total_docs}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()
