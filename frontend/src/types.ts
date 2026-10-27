export type UserRole = 
  | 'System Administrator'
  | 'Scrutiny Reviewer'
  | 'EVC Reviewer/Inspector'
  | 'Read-only Auditor';

export type ValidationStatus = 
  | 'PASS'
  | 'DEFICIENCY'
  | 'INSUFFICIENT EVIDENCE'
  | 'NOT APPLICABLE'
  | 'NOT EVALUATED';

export type VerificationStatus = 
  | 'VERIFIED'
  | 'MISMATCH'
  | 'PENDING'
  | 'SOURCE UNAVAILABLE'
  | 'MANUAL REVIEW';

export type ReviewPriority = 'GREEN' | 'AMBER' | 'RED';

export type WorkflowStage = 
  | 'checklist'
  | 'document_verification'
  | 'evc_evidence'
  | 'final_summary';

export type StepProgressStatus = 
  | 'Not Started'
  | 'In Progress'
  | 'Completed'
  | 'Action Required';

export interface BoundingBox {
  page: number;
  x: number;
  y: number;
  width: number;
  height: number;
  label: string;
}

export interface ExtractedField {
  key: string;
  label: string;
  value: string;
  confidence: number;
  page: number;
  provenance: string;
  bbox?: BoundingBox;
}

export interface DocumentMappingHistory {
  timestamp: string;
  actor: string;
  action: string;
  from_type?: string;
  to_type: string;
  reason: string;
}

export interface DocumentItem {
  id: string;
  application_id: string;
  original_filename: string;
  mapped_type: string;
  mapping_confidence: number;
  mapping_stage: string;
  candidate_types: Array<{ type: string; score: number }>;
  ocr_status: string;
  page_count: number;
  extracted_fields: ExtractedField[];
  bounding_boxes: BoundingBox[];
  preview_url?: string;
  audit_history: DocumentMappingHistory[];
  is_mandatory?: boolean;
  upload_status?: 'Uploaded' | 'Not Uploaded';
  document_status?: 'Pending Verification' | 'Reviewed' | 'Needs Attention';
  remarks?: string;
  document_body_text?: string;
}

export interface VideoKeyframe {
  timestamp: string;
  frame_url: string;
  label: string;
  notes: string;
}

export interface EVCEvidenceItem {
  id: string;
  application_id: string;
  category: string;
  filename: string;
  file_type: 'image' | 'video';
  preview_url: string;
  phash: string;
  duplicate_flag: boolean;
  duplicate_match_app?: string;
  duplicate_match_institution?: string;
  duplicate_similarity?: number;
  duplicate_explanation?: string;
  exif_gps?: { lat: number; lon: number };
  declared_gps?: { lat: number; lon: number };
  gps_distance_km?: number;
  gps_match_status?: 'MATCHED' | 'DISCREPANCY' | 'NO_EXIF';
  video_keyframes: VideoKeyframe[];
  inspection_needed: boolean;
  inspection_reason?: string;
  reviewer_notes?: string;
  review_decision?: string;
}

export interface Finding {
  id: string;
  application_id: string;
  rule_id: string;
  rule_clause: string;
  title: string;
  explanation: string;
  why_evidence: string;
  validation_status: ValidationStatus;
  verification_status: VerificationStatus;
  priority: ReviewPriority;
  document_id?: string;
  document_name?: string;
  page_number?: number;
  bounding_box?: BoundingBox;
  extracted_value?: string;
  expected_value?: string;
  confidence: number;
  suggested_action: string;
  reviewer_notes?: string;
  disposition?: string;
  updated_at: string;
}

export interface Application {
  id: string;
  application_number: string;
  academic_year: string;
  institution_name: string;
  institution_id: string;
  institution_address: string;
  location_city: string;
  location_state: string;
  category: string;
  status: string;
  priority: ReviewPriority;
  assigned_reviewer: string;
  created_at: string;
  declared_lat: number;
  declared_lon: number;
  trust_name: string;
  total_intake_applied: number;
  total_carpet_area_sqm: number;
  documents_count: number;
  expected_documents_count: number;
  missing_documents_count: number;
  findings_count: number;
  evc_items_count: number;
  deficiency_count: number;
  compliance_score: number;
  workflow_stage: WorkflowStage;
  stage_progress: {
    checklist: StepProgressStatus;
    document_verification: StepProgressStatus;
    evc_evidence: StepProgressStatus;
    final_summary: StepProgressStatus;
  };
  review_cycle: number;
}

export interface CategorySummary {
  category: string;
  total: number;
  pending: number;
  in_review: number;
  action_required: number;
}

export interface DeficiencyLetterDraft {
  id: string;
  application_id: string;
  institution_name: string;
  academic_year: string;
  ref_number: string;
  date: string;
  missing_documents: string[];
  confirmed_deficiencies: Array<{
    rule_id: string;
    clause: string;
    description: string;
    evidence: string;
  }>;
  officer_remarks: string;
  signatory: string;
  is_final: boolean;
}

export interface ApplicationHistoryEvent {
  id: string;
  application_id: string;
  institution_name: string;
  timestamp: string;
  event_type: string;
  previous_status: string;
  new_status: string;
  performed_by: string;
  review_cycle: number;
  remarks: string;
}

export interface RuleDefinition {
  id: string;
  title: string;
  category: string;
  academic_year: string;
  clause: string;
  source_title: string;
  validation_logic: string;
  severity: string;
  outcome_guidance: string;
  is_active: boolean;
  version: string;
  effective_from: string;
  effective_to: string;
  author: string;
  last_reviewed: string;
}

export interface AuditEvent {
  id: string;
  timestamp: string;
  user_name: string;
  user_role: string;
  action: string;
  target_type: string;
  target_id: string;
  details: string;
}
