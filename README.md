# AICTE AI-Powered Application Scrutiny & EVC Review Assistant

> **Internal Regulatory Review Platform for Authorized Scrutiny Reviewers and EVC Inspectors**  
> *Academic Cycle: AY 2025–26 Approval Process Handbook (APH) Alignment*

---

## 1. Statutory Scope & Non-Negotiable Boundaries
- **Existing Applications Only**: This platform is **NOT** an application registration, creation, submission, or fee-payment portal.
- **Decision Support**: All automated findings, optical character recognition (OCR) extractions, and perceptual duplicate signals are **advisory review aids**.
- **Statutory Authority**: The authorized human reviewer and the Competent Authority under the AICTE Act, 1987 retain all statutory approval and rejection decisions.

---

## 2. Core Capabilities & Architecture

### A. Explainability-First Decision Model ("Why Was This Flagged?")
For **every** decision and classification made by the model, the reviewer can click **"Inspect Evidence & Why"** to view:
- **Model Rationale**: Plain-language breakdown of what discrepancy was found.
- **Evidence Provenance**: Document name, page number, OCR confidence percentage, and bounding box coordinates.
- **Authoritative Rule Reference**: Exact AICTE Approval Process Handbook (APH) clause and section.
- **Comparative Diff**: Extracted value vs Expected portal benchmark value.
- **Reviewer Disposition**: Reviewers can record decisions (`ACCEPTED`, `DEFICIENCY_UPHELD`, `NEED_CLARIFICATION`, `DISMISSED`) with notes saved to an immutable audit trail.

### B. Three-Stage Document Auto-Mapping Pipeline
1. **Filename & Alias Stage**: Regex normalization and alias dictionary matching (e.g., `Affidavit_2.pdf`, `TER_Receipt.pdf`, `Fire_Safety_Certificate.pdf`).
2. **Content Confirmation (OCR)**: Keyword density and structural checks (extracting issuing authorities, seals, dates).
3. **Confidence Workflow**:
   - High Confidence (>= 90%): Suggest/auto-map with reversibility.
   - Medium Confidence (70–89%): Proposed candidate requiring reviewer confirmation.
   - Low Confidence (< 70%): Classified as "Unmapped / Manual review".
   - Reviewer can manually remap with mandatory rationale logged to the audit history.

### C. EVC Physical Evidence Room & Perceptual Hashing (pHash)
- **Duplicate & Reused Image Detection**: Computes perceptual hashes (`pHash`/`dHash`) to detect photos reused across institutions (e.g. computer lab photo matching another college with 98.4% visual similarity).
- **Geolocation & EXIF Verification**: Compares declared campus coordinates against photo EXIF GPS using the Haversine formula.
- **Video Walkthrough Scene Keyframes**: Extracts scene timestamps for libraries, labs, and workshops.
- **Statutory Precaution**: The system explicitly warns reviewers that visual similarity is an **investigative signal**, not proof of fraud, and provides a toggle to **Flag for On-Site Physical Inspection**.

### D. Multi-Dimensional Findings Model
Outcomes are never collapsed into a single status. Separate dimensions are tracked:
- **Validation Status**: `PASS`, `DEFICIENCY`, `INSUFFICIENT EVIDENCE`, `NOT APPLICABLE`, `NOT EVALUATED`.
- **Verification Status**: `VERIFIED`, `MISMATCH`, `PENDING`, `SOURCE UNAVAILABLE`, `MANUAL REVIEW`.
- **Review Priority**: `GREEN`, `AMBER`, `RED` (for workflow triage only).

### E. Evidence-Linked Scrutiny Report Export
- Generates official PDF summary reports (using ReportLab) and structured JSON summaries.
- Carries an explicit legal disclaimer stating that the report is an AI-assisted synthesis and that the statutory decision remains exclusively with the Competent Authority.

---

## 3. Project Structure

```
sih/
├── backend/
│   ├── main.py                  # FastAPI application with REST endpoints
│   ├── models.py                # Pydantic schemas (Applications, Docs, Findings, EVC, Rules, Audit)
│   ├── mock_data.py             # Realistic AICTE AY 2025-26 seed applications
│   └── services/
│       ├── mapping_engine.py    # 3-stage filename & OCR content auto-mapping
│       ├── evc_analyzer.py      # Perceptual hash & geolocation verifier
│       └── report_exporter.py   # ReportLab PDF generator with statutory disclaimer
└── frontend/
    ├── src/
    │   ├── App.tsx              # Main application shell with tab & modal state
    │   ├── types.ts             # TypeScript interfaces
    │   ├── components/
    │   │   ├── Navbar.tsx                # AICTE branding & RBAC role switcher
    │   │   ├── ScrutinyQueue.tsx         # Triage cards, metrics, and application list
    │   │   ├── ApplicationDetailView.tsx # Deep scrutiny workspace (Docs, Findings, EVC)
    │   │   ├── ExplainabilityModal.tsx   # "Why was this flagged?" evidence inspector
    │   │   ├── DocumentViewerModal.tsx   # OCR bounding box viewer & remap tool
    │   │   ├── EvcDuplicateModal.tsx     # Side-by-side perceptual hash comparison
    │   │   ├── EvcRoomGlobal.tsx         # Cross-application EVC evidence gallery
    │   │   ├── RulesManager.tsx          # Versioned APH rule administration
    │   │   ├── IngestionView.tsx         # CSV metadata & ZIP package importer
    │   │   └── AuditTrailView.tsx        # Immutable forensic audit log
    └── vite.config.ts           # Vite + Tailwind v4 + Proxy to backend
```

---

## 4. Running the Application Locally

### Backend (FastAPI)
```bash
cd backend
python -m uvicorn main:app --host 127.0.0.1 --port 8000
```
- API Docs: `http://127.0.0.1:8000/docs`

### Frontend (Vite + React + TypeScript + Tailwind)
```bash
cd frontend
npm run dev
```
- Web Application: `http://127.0.0.1:5173/`

---

## 5. Role-Based Access Control (RBAC)
Reviewers can quickly switch roles from the top-right role selector to test all permissions:
1. **Scrutiny Reviewer** (Prof. S. R. Sharma): Reviews applications, examines OCR evidence, updates finding dispositions.
2. **EVC Reviewer / Inspector** (Dr. M. K. Ananth): Inspects physical evidence, compares duplicate pHash signals, flags on-site physical visits.
3. **System Administrator** (S. K. Bansal): Manages versioned rules, activates/retires APH clauses, controls ingestion.
4. **Read-only Auditor** (CMA Rajesh Singhania): Inspects findings and immutable audit events.
