from enum import Enum
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field
import datetime

class UserRole(str, Enum):
    ADMIN = "System Administrator"
    SCRUTINY_REVIEWER = "Scrutiny Reviewer"
    EVC_REVIEWER = "EVC Reviewer/Inspector"
    AUDITOR = "Read-only Auditor"

class ValidationStatus(str, Enum):
    PASS = "PASS"
    DEFICIENCY = "DEFICIENCY"
    INSUFFICIENT_EVIDENCE = "INSUFFICIENT EVIDENCE"
    NOT_APPLICABLE = "NOT APPLICABLE"
    NOT_EVALUATED = "NOT EVALUATED"

class VerificationStatus(str, Enum):
    VERIFIED = "VERIFIED"
    MISMATCH = "MISMATCH"
    PENDING = "PENDING"
    SOURCE_UNAVAILABLE = "SOURCE UNAVAILABLE"
    MANUAL_REVIEW = "MANUAL REVIEW"

class ReviewPriority(str, Enum):
    GREEN = "GREEN"
    AMBER = "AMBER"
    RED = "RED"

class BoundingBox(BaseModel):
    page: int
    x: float # percentage 0-100
    y: float # percentage 0-100
    width: float # percentage 0-100
    height: float # percentage 0-100
    label: str

class ExtractedField(BaseModel):
    key: str
    label: str
    value: str
    confidence: float # 0.0 - 1.0
    page: int
    provenance: str # e.g. "Page 1, Paragraph 2 (OCR PaddleOCR 0.96)"
    bbox: Optional[BoundingBox] = None

class DocumentMappingHistory(BaseModel):
    timestamp: str
    actor: str
    action: str
    from_type: Optional[str]
    to_type: str
    reason: str

class DocumentItem(BaseModel):
    id: str
    application_id: str
    original_filename: str
    mapped_type: str # e.g., "Affidavit 2", "Fire Safety Certificate", etc.
    mapping_confidence: float # 0.0 - 1.0
    mapping_stage: str # "Filename & Alias", "Content Confirmation (OCR)", "Manual Remap"
    candidate_types: List[Dict[str, Any]] = []
    ocr_status: str # "COMPLETED", "PROCESSING", "FAILED"
    page_count: int = 1
    extracted_fields: List[ExtractedField] = []
    bounding_boxes: List[BoundingBox] = []
    preview_url: Optional[str] = None
    document_body_text: Optional[str] = None
    audit_history: List[DocumentMappingHistory] = []

class VideoKeyframe(BaseModel):
    timestamp: str # "00:04", "00:18"
    frame_url: str
    label: str
    notes: str

class EVCEvidenceItem(BaseModel):
    id: str
    application_id: str
    category: str # "Computer Center", "Fire Safety", "Campus Infrastructure", "Central Library", "Language Lab"
    filename: str
    file_type: str # "image" or "video"
    preview_url: str
    phash: str
    duplicate_flag: bool = False
    duplicate_match_app: Optional[str] = None
    duplicate_match_institution: Optional[str] = None
    duplicate_similarity: Optional[float] = None
    duplicate_explanation: Optional[str] = None
    exif_gps: Optional[Dict[str, float]] = None # {"lat": 12.9716, "lon": 77.5946}
    declared_gps: Optional[Dict[str, float]] = None
    gps_distance_km: Optional[float] = None
    gps_match_status: Optional[str] = None # "MATCHED", "DISCREPANCY", "NO_EXIF"
    video_keyframes: List[VideoKeyframe] = []
    inspection_needed: bool = False
    inspection_reason: Optional[str] = None
    reviewer_notes: Optional[str] = None

class Finding(BaseModel):
    id: str
    application_id: str
    rule_id: str
    rule_clause: str # e.g. "APH 2025-26 Clause 2.4.1"
    title: str
    explanation: str
    why_evidence: str # Explicit explanation of why model/rule triggered this
    validation_status: ValidationStatus
    verification_status: VerificationStatus
    priority: ReviewPriority
    document_id: Optional[str] = None
    document_name: Optional[str] = None
    page_number: Optional[int] = None
    bounding_box: Optional[Any] = None
    extracted_value: Optional[str] = None
    expected_value: Optional[str] = None
    confidence: float = 0.95
    suggested_action: str
    reviewer_notes: Optional[str] = None
    disposition: Optional[str] = None # "ACCEPTED", "DEFICIENCY_UPHELD", "DISMISSED", "NEED_CLARIFICATION"
    updated_at: str

class Application(BaseModel):
    id: str
    application_number: str
    academic_year: str
    institution_name: str
    institution_id: str
    institution_address: str
    category: str # "Extension of Approval (EoA)", "New Technical Institution", "Intake Increase", "New Programme"
    status: str # "UNDER_SCRUTINY", "DEFICIENCY_FLAGGED", "SCRUTINY_COMPLETED"
    priority: ReviewPriority
    assigned_reviewer: str
    created_at: str
    declared_lat: float
    declared_lon: float
    trust_name: str
    total_intake_applied: int
    total_carpet_area_sqm: float
    documents_count: int
    findings_count: int
    evc_items_count: int
    deficiency_count: int
    compliance_score: int # 0 to 100

class RuleDefinition(BaseModel):
    id: str
    title: str
    category: str
    academic_year: str
    clause: str
    source_title: str
    validation_logic: str
    severity: str
    outcome_guidance: str
    is_active: bool
    version: str
    effective_from: str
    effective_to: str
    author: str
    last_reviewed: str

class AuditEvent(BaseModel):
    id: str
    timestamp: str
    user_name: str
    user_role: str
    action: str
    target_type: str
    target_id: str
    details: str
