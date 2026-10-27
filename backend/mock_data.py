from models import (
    Application, DocumentItem, EVCEvidenceItem, Finding, RuleDefinition,
    AuditEvent, ValidationStatus, VerificationStatus, ReviewPriority,
    ExtractedField, BoundingBox, VideoKeyframe, DocumentMappingHistory
)

SAMPLE_APPLICATIONS = [
    Application(
        id="app-001",
        application_number="AICTE-2025-ENG-0891",
        academic_year="2025-26",
        institution_name="Vishwa Bharati Institute of Technology & Science",
        institution_id="1-44981023",
        institution_address="Survey No. 42/1, Electronic City Phase 2, Bengaluru, Karnataka - 560100",
        category="Extension of Approval (EoA)",
        status="UNDER_SCRUTINY",
        priority=ReviewPriority.AMBER,
        assigned_reviewer="Prof. S. R. Sharma (Senior Scrutiny Officer)",
        created_at="2025-03-12 10:14:00",
        declared_lat=12.9716,
        declared_lon=77.5946,
        trust_name="Vishwa Bharati Educational Foundation",
        total_intake_applied=420,
        total_carpet_area_sqm=5820.0,
        documents_count=7,
        findings_count=4,
        evc_items_count=4,
        deficiency_count=1,
        compliance_score=82
    ),
    Application(
        id="app-002",
        application_number="AICTE-2025-ENG-0422",
        academic_year="2025-26",
        institution_name="Apex Institute of Technology & Research",
        institution_id="1-88910245",
        institution_address="Sector 14, BVB Campus, Hubballi-Dharwad, Karnataka - 580031",
        category="Intake Increase",
        status="DEFICIENCY_FLAGGED",
        priority=ReviewPriority.RED,
        assigned_reviewer="Dr. M. K. Ananth (EVC Committee Member)",
        created_at="2025-03-14 14:32:00",
        declared_lat=15.3647,
        declared_lon=75.1240,
        trust_name="Apex Shaikshanik Sanstha",
        total_intake_applied=600,
        total_carpet_area_sqm=3780.0,
        documents_count=8,
        findings_count=3,
        evc_items_count=4,
        deficiency_count=3,
        compliance_score=58
    ),
    Application(
        id="app-003",
        application_number="AICTE-2025-ENG-1104",
        academic_year="2025-26",
        institution_name="Sree Rama Engineering College",
        institution_id="1-99238471",
        institution_address="Rami Reddy Nagar, Karakambadi Road, Venkatapuram, Renigunta (M), Tirupati District, Andhra Pradesh - 517507",
        category="Extension of Approval (EoA)",
        status="UNDER_SCRUTINY",
        priority=ReviewPriority.GREEN,
        assigned_reviewer="Dr. Neha Verma (Joint Director, Scrutiny)",
        created_at="2025-03-15 09:20:00",
        declared_lat=13.6586,
        declared_lon=79.4900,
        trust_name="Sri Rama Educational Society",
        total_intake_applied=540,
        total_carpet_area_sqm=13490.0,
        documents_count=8,
        findings_count=3,
        evc_items_count=4,
        deficiency_count=0,
        compliance_score=98
    ),
    Application(
        id="app-004",
        application_number="AICTE-2025-PHARM-0199",
        academic_year="2025-26",
        institution_name="Saraswati College of Pharmaceutical Sciences",
        institution_id="1-77123901",
        institution_address="NH-48, Gandhinagar Highway, Ahmedabad, Gujarat - 382421",
        category="Extension of Approval (EoA)",
        status="UNDER_SCRUTINY",
        priority=ReviewPriority.AMBER,
        assigned_reviewer="Prof. S. R. Sharma (Senior Scrutiny Officer)",
        created_at="2025-03-16 16:45:00",
        declared_lat=23.2156,
        declared_lon=72.6369,
        trust_name="Saraswati Education Trust",
        total_intake_applied=100,
        total_carpet_area_sqm=3450.0,
        documents_count=7,
        findings_count=2,
        evc_items_count=4,
        deficiency_count=1,
        compliance_score=78
    )
]

SAMPLE_DOCUMENTS = {
    # -------------------------------------------------------------
    # APP-001: Vishwa Bharati Institute of Technology & Science
    # -------------------------------------------------------------
    "app-001": [
        DocumentItem(
            id="doc-001-1",
            application_id="app-001",
            original_filename="Affidavit_Format_2_Signed.pdf",
            mapped_type="Affidavit 2 (Self-Disclosure)",
            mapping_confidence=0.96,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[
                {"type": "Affidavit 2 (Self-Disclosure)", "score": 0.96},
                {"type": "Affidavit 1 (Land)", "score": 0.42}
            ],
            ocr_status="COMPLETED",
            page_count=4,
            preview_url="/sample_docs/affidavit2_sample.pdf",
            document_body_text="""Approval Process Handbook 2024-2027 (Page 186-188)
AFFIDAVIT-2
(For the applications submitted under Chapter I/II/IV except Closure of the Institution)

I/we, Dr. K. S. Rajendra, Secretary, Vishwa Bharati Education & Charitable Trust, son of Late S. N. Rao, aged 54, resident of 14/B, 5th Main, Indiranagar, Bengaluru - 560038, do hereby solemnly affirm and declare as under:

1. That I/we have applied for Extension of Approval (EoA) vide application AICTE-2025-ENG-0891 dated 10-03-2025.
2. That I/we will abide by all terms and conditions as laid down in the Approval Process Handbook 2024-27.
3. That the information given by Dr. K. S. Rajendra in the application made to AICTE is true and complete. Nothing is false and no information/ material has been concealed;
4. That the Institution is functioning in the location as approved by the Council;
5. That I/we have uploaded the Occupancy/Completion Certificate/Building License/Form D issued by the Competent Authority and the Structural Stability Certificate by the Competent Authority;
6. That the Trust/Society/Company runs the following other Institutions in the same Campus: Vishwa Bharati Polytechnic (Built-Up Area: 2,400 Sq.M., Approved by AICTE).
7. That I/we have uploaded valid Fire Safety Certificate issued by the Competent Authority;
8. That Principal of the Institution is regular and qualified as per AICTE norms;
9. That the Faculty norms as well as Faculty : Student ratio is maintained as per Approval Process Handbook and the Faculty data uploaded is true and complete;
12. That the declaration, information and documents submitted/uploaded as per Annexure-1/2 of the Approval Process Handbook with regard to Land, Built-up area (Instructional area, Administrative area and Amenities area) and other Infrastructure therein where the letter of approval/ Extension of Approval is sought for Vishwa Bharati Institute of Technology & Science is true, complete and nothing is false;
13. That the Land is contiguous, there is no dispute pertaining to the said Land;
15. That the Land/Built-up area details: Land Area: 7.5 Acres at Survey No. 42/1, Electronic City Phase 2. Total Built-up: 5,820 Sq.M. Completed in all respects.
20. That the financial transactions have been done only by digital payment;
26. That Audited statement of accounts of the Trust/Society for the previous year has been uploaded;
31. That the Anti-Ragging Committee, Grievance Redressal Committee, Internal Committee (IC), and Committee for SC/ST are duly constituted.

VERIFICATION
Verified at Bengaluru on this the 10th day of March, 2025 that the contents of this affidavit are true to my knowledge.
DEPONENT: Dr. K. S. Rajendra (Secretary)
Solemnly affirmed and signed before me by the deponent on this 10th day of March 2025 at my office.
Notary Public: V. Narayanan, Advocate & Notary, Govt. of Karnataka (Reg. No. BLR/992/2012). Printed on Non-Judicial Stamp Paper Rs. 100/-.""",
            extracted_fields=[
                ExtractedField(
                    key="app_number",
                    label="Application ID in Header",
                    value="AICTE-2025-ENG-0891",
                    confidence=0.98,
                    page=1,
                    provenance="Page 1, Header Clause 1 (PaddleOCR 0.98)",
                    bbox=BoundingBox(page=1, x=65, y=5, width=28, height=4, label="Application Ref")
                ),
                ExtractedField(
                    key="trust_name",
                    label="Trust Name Mentioned in Preamble",
                    value="Vishwa Bharati Education & Charitable Trust",
                    confidence=0.94,
                    page=1,
                    provenance="Page 1, Paragraph 1 (PaddleOCR 0.94)",
                    bbox=BoundingBox(page=1, x=15, y=28, width=70, height=5, label="Trust Mention Discrepancy")
                ),
                ExtractedField(
                    key="deponent_name",
                    label="Deponent / Signatory Name",
                    value="Dr. K. S. Rajendra (Secretary)",
                    confidence=0.91,
                    page=4,
                    provenance="Page 4, Verification Block (PaddleOCR 0.91)",
                    bbox=BoundingBox(page=4, x=55, y=78, width=38, height=8, label="Signatory Seal")
                ),
                ExtractedField(
                    key="notary_attestation",
                    label="Notary Public Registration",
                    value="Advocate V. Narayanan (Reg. No. BLR/992/2012), Valid till Dec 2027",
                    confidence=0.89,
                    page=4,
                    provenance="Page 4, Notary Stamp (PaddleOCR 0.89)",
                    bbox=BoundingBox(page=4, x=12, y=82, width=32, height=12, label="Notary Stamp")
                )
            ],
            bounding_boxes=[
                BoundingBox(page=1, x=15, y=28, width=70, height=5, label="Trust Name Discrepancy"),
                BoundingBox(page=4, x=55, y=78, width=38, height=8, label="Deponent Signature"),
                BoundingBox(page=4, x=12, y=82, width=32, height=12, label="Notary Seal")
            ],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-001-2",
            application_id="app-001",
            original_filename="Karnataka_Fire_Safety_Renewal_Cert.pdf",
            mapped_type="Fire Safety Certificate",
            mapping_confidence=0.94,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Fire Safety Certificate", "score": 0.94}],
            ocr_status="COMPLETED",
            page_count=2,
            preview_url="/sample_docs/fire_safety_sample.pdf",
            document_body_text="""GOVERNMENT OF KARNATAKA
KARNATAKA STATE FIRE AND EMERGENCY SERVICES DEPARTMENT
Office of the Chief Fire Officer, Bengaluru East Division

Rc.No. 441/CFO/BNG-E/CC/2023, Dated: 16-01-2023
To: The AICTE / The Principal, Vishwa Bharati Institute of Technology & Science, Survey No. 42/1, Electronic City Phase 2, Bengaluru.

SUBJECT: Issuance of Fire Safety Certificate for Educational Occupancy - Regarding.
PARTICULARS OF BUILDING:
1. Name & Address: Vishwa Bharati Institute of Technology & Science, Electronic City Phase 2, Bengaluru - 560100
2. Total Plot Area: 7.50 Acres | Height: 14.50 Mtrs | Ground + 3 Upper Floors
3. Total Built-up Area: 5,820.00 Sq.Mtrs | Occupancy: Educational (Group B)
4. Means of Escape: Internal Staircases (02 Nos, width 2.00m each), External Emergency Fire Escape (01 No, width 1.50m).

FIRE FIGHTING INSTALLATIONS:
- Fire Extinguishers (ABC & CO2 type): 85 Nos (Installed and inspected)
- Hose Reel System: 06 Nos connected to Overhead Tank
- Terrace Water Tank: 10,000 Litres exclusively for fire fighting
- Booster Pump: 450 LPM capacity with auto-starter

VALIDITY CLAUSE:
This Certificate is valid for a period of two (02) years only from 16-01-2023 to 15-01-2025. The management shall apply for renewal two months prior to expiry.
Signed: Chief Fire Officer, Bengaluru East Division (Official Seal)""",
            extracted_fields=[
                ExtractedField(
                    key="cert_no",
                    label="Certificate Reference Number",
                    value="Rc.No. 441/CFO/BNG-E/CC/2023",
                    confidence=0.97,
                    page=1,
                    provenance="Page 1, Top Header (PaddleOCR 0.97)",
                    bbox=BoundingBox(page=1, x=10, y=12, width=35, height=4, label="Cert No")
                ),
                ExtractedField(
                    key="validity_period",
                    label="Validity Expired On",
                    value="15-01-2025",
                    confidence=0.96,
                    page=1,
                    provenance="Page 1, Clause 'valid from 16-01-2023 to 15-01-2025' (PaddleOCR 0.96)",
                    bbox=BoundingBox(page=1, x=15, y=45, width=72, height=6, label="Expired Validity Date")
                )
            ],
            bounding_boxes=[
                BoundingBox(page=1, x=15, y=45, width=72, height=6, label="Expired Validity Date")
            ],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-001-3",
            application_id="app-001",
            original_filename="TER_Receipt_2025_26_AICTE.pdf",
            mapped_type="TER / Payment Receipt",
            mapping_confidence=0.98,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "TER / Payment Receipt", "score": 0.98}],
            ocr_status="COMPLETED",
            page_count=1,
            document_body_text="""ALL INDIA COUNCIL FOR TECHNICAL EDUCATION
OFFICIAL PAYMENT RECEIPT (TER CHARGES 2025-26)

Application ID: AICTE-2025-ENG-0891
Institution: Vishwa Bharati Institute of Technology & Science
Payment Reference / UTR Number: AICTE-2025-TXN-998124
Payment Date & Time: 11-03-2025 14:22:18 IST
Category: Extension of Approval (EoA) - Existing Technical Institution
Total Amount Paid: Rs. 1,50,000.00 (One Lakh Fifty Thousand Rupees Only)
Payment Gateway Status: SUCCESS / SETTLED (Transaction Verified by Central Payment Gateway)""",
            extracted_fields=[
                ExtractedField(
                    key="transaction_id",
                    label="Payment Reference / UTR Number",
                    value="AICTE-2025-TXN-998124",
                    confidence=0.99,
                    page=1,
                    provenance="Page 1, Transaction Row (PaddleOCR 0.99)",
                    bbox=BoundingBox(page=1, x=20, y=30, width=35, height=4, label="Txn Ref")
                ),
                ExtractedField(
                    key="amount_paid",
                    label="Amount Paid",
                    value="Rs. 1,50,000.00",
                    confidence=0.99,
                    page=1,
                    provenance="Page 1, Amount Field (PaddleOCR 0.99)",
                    bbox=BoundingBox(page=1, x=65, y=55, width=25, height=5, label="Amount Paid")
                )
            ],
            bounding_boxes=[
                BoundingBox(page=1, x=20, y=30, width=35, height=4, label="Txn Ref"),
                BoundingBox(page=1, x=65, y=55, width=25, height=5, label="Amount Paid")
            ],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-001-4",
            application_id="app-001",
            original_filename="BBMP_Occupancy_Certificate_Appendix_I.pdf",
            mapped_type="Occupancy Certificate",
            mapping_confidence=0.92,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Occupancy Certificate", "score": 0.92}],
            ocr_status="COMPLETED",
            page_count=2,
            document_body_text="""APPENDIX 'I' - FORM FOR OCCUPANCY CERTIFICATE
BRUHAT BENGALURU MAHANAGARA PALIKE (BBMP)
Office of the Additional Director of Town Planning (South)

Occupancy Certificate No: BBMP/Addl.Dir/JD/OC/812/2019-20, Date: 24-10-2020
To: Dr. K. S. Rajendra, Secretary, Vishwa Bharati Educational Foundation

Sir,
The construction / erection of Educational Building at Survey No. 42/1, Electronic City Phase 2, completed under the supervision of Registered Architect (COA Reg: CA/2004/31892) and Structural Engineer, may be occupied on the conditions mentioned herein.
Built-Up Area Sanctioned: 6,150.00 Sq.Mtrs. Ground + 3 Upper Floors.
OCCUPATION GRANTED subject to adherence to building by-laws.
Signed: The Chief Officer / Joint Director Town Planning, BBMP.""",
            extracted_fields=[
                ExtractedField(
                    key="occupancy_no",
                    label="Occupancy Certificate No",
                    value="BBMP/Addl.Dir/JD/OC/812/2019-20",
                    confidence=0.95,
                    page=1,
                    provenance="Page 1, Order Header (PaddleOCR 0.95)",
                    bbox=BoundingBox(page=1, x=12, y=18, width=42, height=4, label="OC Number")
                ),
                ExtractedField(
                    key="built_up_area",
                    label="Sanctioned Built-up Area",
                    value="6,150.00 Sq. Meters",
                    confidence=0.92,
                    page=1,
                    provenance="Page 1, Property Schedule (PaddleOCR 0.92)",
                    bbox=BoundingBox(page=1, x=50, y=42, width=35, height=5, label="Total Area")
                )
            ],
            bounding_boxes=[
                BoundingBox(page=1, x=12, y=18, width=42, height=4, label="OC Number")
            ],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-001-5",
            application_id="app-001",
            original_filename="Structural_Engineer_Stability_Cert_2024.pdf",
            mapped_type="Structural Stability Certificate",
            mapping_confidence=0.91,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Structural Stability Certificate", "score": 0.91}],
            ocr_status="COMPLETED",
            page_count=2,
            document_body_text="""STRUCTURAL STABILITY CERTIFICATE
Issued by Chartered Structural Engineer (Letterhead of Engineer)

I hereby certify that the building of Vishwa Bharati Institute of Technology & Science, situated at Survey No. 42/1, Electronic City Phase 2, Bengaluru, has been inspected.
The RCC Framed Structure comprising Ground + 3 Upper Floors was designed and constructed complying with IS 456-2000 and IS 1893 (Seismic Zone II norms).
The building is structurally sound, stable, and safe for Educational Institution Occupancy.
Engineer Name: Er. S. Mohan Kumar, FIE, Chartered Engineer (Reg. No. M-145829-8 / Karnataka State Centre). Valid License.""",
            extracted_fields=[
                ExtractedField(
                    key="engineer_reg",
                    label="Chartered Engineer Reg. No.",
                    value="AMIE / M-145829-8 / Karnataka State Centre",
                    confidence=0.94,
                    page=2,
                    provenance="Page 2, Seal Block (PaddleOCR 0.94)",
                    bbox=BoundingBox(page=2, x=55, y=75, width=38, height=8, label="Eng Reg")
                )
            ],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-001-6",
            application_id="app-001",
            original_filename="Satellite_Map_GPS_Coordinates_Survey.pdf",
            mapped_type="Satellite / Geolocation Map",
            mapping_confidence=0.88,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Satellite / Geolocation Map", "score": 0.88}],
            ocr_status="COMPLETED",
            page_count=1,
            document_body_text="""GEOLOCATION AND SATELLITE SURVEY MAP
Institution: Vishwa Bharati Institute of Technology & Science
Declared Campus Entrance: 12°58'17.8"N 77°35'40.5"E (12.9716, 77.5946)
Land Parcel: Survey No. 42/1, Electronic City Phase 2, Bengaluru. Earmarked boundary verified via cadastral overlay.""",
            extracted_fields=[
                ExtractedField(
                    key="map_coords",
                    label="Coordinates on Survey Map",
                    value="12°58'17.8\"N 77°35'40.5\"E (12.9716, 77.5946)",
                    confidence=0.91,
                    page=1,
                    provenance="Page 1, Legend (PaddleOCR 0.91)",
                    bbox=BoundingBox(page=1, x=20, y=75, width=45, height=5, label="GPS Coordinates")
                )
            ],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-001-7",
            application_id="app-001",
            original_filename="Audited_Balance_Sheet_FY_2023_24.pdf",
            mapped_type="Audited Financial Statement",
            mapping_confidence=0.93,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Audited Financial Statement", "score": 0.93}],
            ocr_status="COMPLETED",
            page_count=4,
            document_body_text="""CHARTERED ACCOUNTANTS AUDIT REPORT
To the Trustees, Vishwa Bharati Educational Foundation
We have audited the Balance Sheet of Vishwa Bharati Institute of Technology & Science as at 31st March 2024.
Total Assets: Rs. 24,18,92,400.00 | Total Corpus Fund: Rs. 18,50,00,000.00
In our opinion, the financial statements give a true and fair view of the state of affairs.
Auditor: R. Sundaram & Associates, Chartered Accountants (FRN: 004812S). ICAI UDIN: 24098144AAAAAA1029.""",
            extracted_fields=[
                ExtractedField(
                    key="auditor_udin",
                    label="ICAI UDIN Number",
                    value="24098144AAAAAA1029",
                    confidence=0.96,
                    page=4,
                    provenance="Page 4, Auditor Block (PaddleOCR 0.96)",
                    bbox=BoundingBox(page=4, x=52, y=82, width=40, height=5, label="ICAI UDIN")
                )
            ],
            bounding_boxes=[],
            audit_history=[]
        )
    ],

    # -------------------------------------------------------------
    # APP-002: Apex Institute of Technology & Research (Intake Increase)
    # -------------------------------------------------------------
    "app-002": [
        DocumentItem(
            id="doc-002-1",
            application_id="app-002",
            original_filename="Affidavit_8_Intake_Increase.pdf",
            mapped_type="Affidavit 8 (Additional Course/Increase in Intake)",
            mapping_confidence=0.97,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Affidavit 8 (Additional Course/Increase in Intake)", "score": 0.97}],
            ocr_status="COMPLETED",
            page_count=2,
            document_body_text="""Approval Process Handbook 2024-2027 (Page 194)
AFFIDAVIT-8
(For Additional Course/ Increase in Intake)

I/we, Ramesh Patil, Chairman, Apex Shaikshanik Sanstha, son of Late V. B. Patil, aged 58, resident of BVB Campus Road, Hubballi - 580031, do hereby solemnly affirm and declare as under:

1. That I/we have applied for additional Course/ increase in intake of our Institution Apex Institute of Technology & Research vide application AICTE-2025-ENG-0422 dated 14-03-2025 (Applying for +180 intake in Computer Science & AI, total intake 600).
2. That above named Trust/Society vide a resolution dated 12-01-2025 resolved to apply for additional Course/ increase in intake in above named Institution in the Web-Portal and had paid the requisite TER Charges as per AICTE norms;
3. That we have created all the additional facilities such as Infrastructure, hostel (wherever applicable), Faculty, etc. for meeting the requirements of additional Course/increase in the Intake.
4. That liabilities, if any, arise out of additional Course/ increase in the Intake in the above named institutions shall be solely of the above named Trust/ Society; and
5. That the facts stated in this Affidavit are true to my/ our knowledge. No part of the same is false and no material has been concealed therefrom.

VERIFICATION
Verified at Hubballi on this 14th day of March 2025 that the facts stated above are true and correct.
DEPONENT: Ramesh Patil (Chairman)
Notary Public: S. G. Kulkarni, Hubballi, Karnataka. Non-Judicial Stamp Paper Rs. 100/-.""",
            extracted_fields=[
                ExtractedField(
                    key="applied_intake",
                    label="Applied Total Intake",
                    value="600 Seats (+180 Additional)",
                    confidence=0.98,
                    page=1,
                    provenance="Page 1, Clause 1 (PaddleOCR 0.98)",
                    bbox=BoundingBox(page=1, x=20, y=25, width=60, height=5, label="Intake Clause")
                )
            ],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-002-2",
            application_id="app-002",
            original_filename="Certificate_2_Architect_Carpet_Area.pdf",
            mapped_type="Certificate of an Architect (Certificate-2)",
            mapping_confidence=0.95,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Certificate of an Architect (Certificate-2)", "score": 0.95}],
            ocr_status="COMPLETED",
            page_count=3,
            document_body_text="""Approval Process Handbook 2024-2027 (Page 212)
CERTIFICATE-2
Certificate of an Architect Registered with Council of Architecture
(To be produced in the Letterhead of Architect)

The copies of the approved Site Plan and Building Plans in respect of application submitted by Apex Shaikshanik Sanstha for Apex Institute of Technology & Research at Sector 14, BVB Campus, Hubballi were provided to me for verification.

ROOM SCHEDULE & CARPET AREA DETAILS:
Sl. No. | Room No | Room Type | Carpet Area (in m2) | Completion of Flooring | Completion of Walls | Electrification
1. | CR-101 to 108 | Class Rooms (8 Nos) | 528.00 | Completed | Completed | Completed
2. | LB-201 to 206 | Laboratories (6 Nos) | 396.00 | Completed | Completed | Completed
3. | CC-301 | Central Computer Center | 150.00 | Completed | Completed | Completed
4. | WS-101 | Workshop Area | 200.00 | Completed | Completed | Completed
5. | LIB-01 | Central Library | 400.00 | Completed | Completed | Completed
6. | ADM-01 | Admin & Faculty Rooms | 450.00 | Completed | Completed | Completed
TOTAL INSTRUCTIONAL & ADM AREA AVAILABLE: 3,780.00 Sq.Mtrs.

I hereby certify that the above mentioned site plan and construction details are authentic.
Architect Name: Ar. Vinod Desai (Council of Architecture Reg. No. CA/2011/52819).""",
            extracted_fields=[
                ExtractedField(
                    key="total_carpet_area",
                    label="Certified Total Carpet Area",
                    value="3,780.00 Sq. Meters",
                    confidence=0.96,
                    page=2,
                    provenance="Page 2, Room Schedule Table Total (PaddleOCR 0.96)",
                    bbox=BoundingBox(page=2, x=25, y=65, width=50, height=5, label="Carpet Area Shortfall")
                )
            ],
            bounding_boxes=[
                BoundingBox(page=2, x=25, y=65, width=50, height=5, label="Carpet Area Shortfall")
            ],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-002-3",
            application_id="app-002",
            original_filename="Format_2_University_NOC_VTU.pdf",
            mapped_type="NOC from Affiliating University (Format-2)",
            mapping_confidence=0.94,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "NOC from Affiliating University (Format-2)", "score": 0.94}],
            ocr_status="COMPLETED",
            page_count=2,
            document_body_text="""Approval Process Handbook 2024-2027 (Page 202-204)
FORMAT-2
No Objection Certificate from the Affiliating University / Board
VISVESVARAYA TECHNOLOGICAL UNIVERSITY (VTU), BELAGAVI

Ref No: VTU/ACA/NOC/2025/1182, Date: 18-02-2025
This is to confirm that the Visvesvaraya Technological University has no objection for the Institution applied for:
v. Starting of new Programme / Level / Increase in Intake:
   - B.Tech Computer Science & Engineering (Intake from 180 to 240)
   - B.Tech Artificial Intelligence & Machine Learning (New Intake: 120)
Total Sanctioned Intake approved by University: 600 Students for AY 2025-26.
Signed: Registrar, VTU Belagavi (Official Seal).""",
            extracted_fields=[
                ExtractedField(
                    key="vtu_noc",
                    label="University NOC Reference",
                    value="VTU/ACA/NOC/2025/1182",
                    confidence=0.97,
                    page=1,
                    provenance="Page 1, Ref Header (PaddleOCR 0.97)"
                )
            ],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-002-4",
            application_id="app-002",
            original_filename="Format_3_Trust_Resolution.pdf",
            mapped_type="Resolution of the Trust (Format-3)",
            mapping_confidence=0.92,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Resolution of the Trust (Format-3)", "score": 0.92}],
            ocr_status="COMPLETED",
            page_count=2,
            document_body_text="""Approval Process Handbook 2024-2027 (Page 205-206)
FORMAT-3
Resolution of the Trust / Society / Company
APEX SHAIKSHANIK SANSTHA, HUBBALLI

Resolution passed at the Executive Committee meeting held on 12-01-2025 at Hubballi:
Resolved that the Society shall apply to AICTE for Increase in Intake in Engineering & Technology from 420 to 600 at Apex Institute of Technology & Research.
Resolved further that required funds of Rs. 85,00,000/- are allocated for equipment and additional instructional carpet area.
Signed: Ramesh Patil (Chairman) & Trustees.""",
            extracted_fields=[],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-002-5",
            application_id="app-002",
            original_filename="Municipal_Occupancy_Appendix_I.pdf",
            mapped_type="Occupancy Certificate",
            mapping_confidence=0.91,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Occupancy Certificate", "score": 0.91}],
            ocr_status="COMPLETED",
            page_count=2,
            document_body_text="""APPENDIX 'I' - FORM FOR OCCUPANCY CERTIFICATE
HUBBALLI-DHARWAD MUNICIPAL CORPORATION
Occupancy Certificate No: HDMC/TPO/OC/2021/419, Date: 15-06-2021
Occupation granted for Educational Building Block A & B admeasuring 3,780.00 Sq.M. at Sector 14, BVB Campus.
Signed: The Chief Officer / Town Planning Officer, HDMC.""",
            extracted_fields=[],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-002-6",
            application_id="app-002",
            original_filename="Fire_Safety_NOC_Hubballi.pdf",
            mapped_type="Fire Safety Certificate",
            mapping_confidence=0.96,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Fire Safety Certificate", "score": 0.96}],
            ocr_status="COMPLETED",
            page_count=2,
            document_body_text="""KARNATAKA STATE FIRE & EMERGENCY SERVICES
Office of the Regional Fire Officer, Hubballi-Dharwad Region
No. RFO/FES/HD/NOC/2023-559, Date: 12-11-2023
No Objection Certificate for Educational Occupancy. Valid for 3 years up to 11-11-2026.
Signed: Regional Fire Officer.""",
            extracted_fields=[],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-002-7",
            application_id="app-002",
            original_filename="AICTE_TER_Receipt_2025.pdf",
            mapped_type="TER / Payment Receipt",
            mapping_confidence=0.99,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "TER / Payment Receipt", "score": 0.99}],
            ocr_status="COMPLETED",
            page_count=1,
            document_body_text="""AICTE FEE PAYMENT RECEIPT
Application ID: AICTE-2025-ENG-0422
Category: Increase in Intake
Txn Ref: AICTE-2025-TXN-881249 | Amount Paid: Rs. 2,00,000.00 | Status: SUCCESS""",
            extracted_fields=[],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-002-8",
            application_id="app-002",
            original_filename="Structural_Stability_Certificate_Unattested.pdf",
            mapped_type="Structural Stability Certificate",
            mapping_confidence=0.82,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Structural Stability Certificate", "score": 0.82}],
            ocr_status="COMPLETED",
            page_count=1,
            document_body_text="""STRUCTURAL FITNESS REPORT
Building of Apex Institute of Technology & Research, Sector 14, Hubballi.
The structure is inspected and observed sound.
(Missing Engineer License Number and Official Council of Architecture / Institution of Engineers Seal)
Signed: Er. P. K. Rao (Consultant). [Unsealed / Unattested]""",
            extracted_fields=[
                ExtractedField(
                    key="missing_seal",
                    label="Structural Engineer License / Seal",
                    value="NOT DETECTED (Unsealed Consultant Slip)",
                    confidence=0.88,
                    page=1,
                    provenance="Page 1, Signature Footer (PaddleOCR 0.88)"
                )
            ],
            bounding_boxes=[],
            audit_history=[]
        )
    ],

    # -------------------------------------------------------------
    # APP-003: Sree Rama Engineering College (Tirupati, Andhra Pradesh)
    # -------------------------------------------------------------
    "app-003": [
        DocumentItem(
            id="doc-003-1",
            application_id="app-003",
            original_filename="AP_Fire_Services_NOC_Occupancy_Rc502.pdf",
            mapped_type="Fire Safety Certificate",
            mapping_confidence=0.98,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Fire Safety Certificate", "score": 0.98}],
            ocr_status="COMPLETED",
            page_count=4,
            document_body_text="""GOVERNMENT OF ANDHRA PRADESH
A.P. STATE DISASTER RESPONSE AND FIRE SERVICES DEPARTMENT
From: The Director General, State Disaster Response & Fire Services, Andhra Pradesh, Vijayawada.
To: The AICTE, New Delhi.

Rc.No.502/MSB/SR/TPT/2023, Dated: 17-02-2023.

Sub: A.P State Disaster Response & Fire Services Department - MSB Section - Southern Region - Issuance of No Objection Certificate for Occupancy to the Existing Building of M/s Sri Rama Engineering College, located at Sy.No.224/2, 3, 4, 5, 6A, 7, 8, 9A & B, 10, 225/2A & B, 226/1A & B, Karakambadi Road, Venkatapuram, Renigunta (M), Tirupati District - Regarding.

PARTICULARS OF THE BUILDING:
a) Name & Address: M/s Sri Rama Engineering College, located at Sy.No.224/2, 3, 4, 5, 6A, 7, 8, 9A & B, 10, 225/2A & B, 226/1A & B, Karakambadi Road, Venkatapuram, Renigunta (M), Tirupati District.
b) Total Plot/Site Area: 10.01 Acres
c) Height of Building: 12.00 Mtrs
d) No. of Floors: Ground + (02) Upper Floors
e) Total Built-up Area: 13,490.00 Sq.Mtrs
f) Type of Occupancy: Educational Occupancy

NBC 2016 COMPLIANCE & MEANS OF ESCAPE:
- Ground Floor Built-up Area: 4,645.00 Sq.Mtrs (Educational)
- First Floor Built-up Area: 4,381.00 Sq.Mtrs (Educational)
- Second Floor Built-up Area: 4,464.00 Sq.Mtrs (Educational)
Total: 13,490.00 Sq.Mtrs.
- Internal Staircase: 01 No., Width: 04.60 Mtrs (Middle of Building)
- External Staircases / Ramp: 02 Nos., Width: 02.00 Mtrs each (South-West & South-East)

FIRE FIGHTING INSTALLATIONS (Table-07 NBC 2016):
1. Fire Extinguishers: 135 No.'s (Installed & Tested)
2. Hose Reel Hose: 09 No.'s (Provided)
3. Terrace Water Tank: 10,000 Ltrs. (Provided)
4. Booster Pump: 450 LPM - 01 No. (Tested & Working)
5. Electrical Safety: MCB provided for each floor; Emergency lighting at corridors with UPS backup.

VALIDITY:
15) This No Objection Certificate for Occupancy is valid for a period of Five (05) years only from the date of issue of this letter (Valid from 17-02-2023 to 16-02-2028).
Signed: Additional Director General of Police, C.I.D. / Director General, State Disaster Response and Fire Services, Andhra Pradesh, Vijayawada.""",
            extracted_fields=[
                ExtractedField(
                    key="fire_rc_no",
                    label="NOC Reference Number",
                    value="Rc.No.502/MSB/SR/TPT/2023",
                    confidence=0.99,
                    page=1,
                    provenance="Page 1, Reference Header (PaddleOCR 0.99)",
                    bbox=BoundingBox(page=1, x=25, y=14, width=50, height=4, label="NOC Ref")
                ),
                ExtractedField(
                    key="validity_period",
                    label="Validity Period (5 Years)",
                    value="17-02-2023 to 16-02-2028",
                    confidence=0.98,
                    page=4,
                    provenance="Page 4, Clause 15 (PaddleOCR 0.98)",
                    bbox=BoundingBox(page=4, x=15, y=12, width=70, height=6, label="5-Year Validity")
                ),
                ExtractedField(
                    key="total_builtup_area",
                    label="Certified Total Built-up Area",
                    value="13,490.00 Sq.Mtrs",
                    confidence=0.97,
                    page=1,
                    provenance="Page 1, Particulars Section (PaddleOCR 0.97)",
                    bbox=BoundingBox(page=1, x=45, y=82, width=30, height=4, label="Built-up Area")
                )
            ],
            bounding_boxes=[
                BoundingBox(page=1, x=25, y=14, width=50, height=4, label="NOC Ref"),
                BoundingBox(page=4, x=15, y=12, width=70, height=6, label="5-Year Validity")
            ],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-003-2",
            application_id="app-003",
            original_filename="Certificate_1_Advocate_Land_Title.pdf",
            mapped_type="Certificate of an Advocate (Certificate-1)",
            mapping_confidence=0.96,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Certificate of an Advocate (Certificate-1)", "score": 0.96}],
            ocr_status="COMPLETED",
            page_count=2,
            document_body_text="""Approval Process Handbook 2024-2027 (Page 210-211)
CERTIFICATE-1
Certificate of an Advocate
(To be produced in the Letterhead of Advocate)

The copies of Sri Rama Educational Society registration documents, Land documents, Land use Certificate, Land Conversion Certificate in respect of application submitted by Sri Rama Educational Society for Sree Rama Engineering College, Karakambadi Road, Renigunta (M), Tirupati were provided to me for verification.

A. Trust / Society Registration Documents:
Registration Certificate No: 418/2007, Date of Registration: 14-06-2007, Registered at: Sub-Registrar Office, Tirupati. Registered under Andhra Pradesh Societies Registration Act, 2001. Authentic.

B. Land Documents:
Deed Holder: Sri Rama Educational Society
Survey Numbers: Sy.No.224/2, 3, 4, 5, 6A, 7, 8, 9A & B, 10, 225/2A & B, 226/1A & B
Location: Karakambadi Road, Venkatapuram, Renigunta (M), Tirupati District.
Total Land Area: 10.01 Acres (Registered sale deeds No. 1824/2007, 1825/2007).
I hereby certify that the land is in lawful possession of the applicant, contiguous, and has clear, unencumbered marketable title.
Signed: Advocate T. Chandrasekhar Reddy, B.Sc., B.L., Advocate & Notary, Tirupati Bar Association.""",
            extracted_fields=[
                ExtractedField(
                    key="land_area_acre",
                    label="Verified Land Area",
                    value="10.01 Acres (Contiguous)",
                    confidence=0.98,
                    page=1,
                    provenance="Page 1, Land Table (PaddleOCR 0.98)"
                )
            ],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-003-3",
            application_id="app-003",
            original_filename="Certificate_2_Architect_Building_Plans.pdf",
            mapped_type="Certificate of an Architect (Certificate-2)",
            mapping_confidence=0.95,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Certificate of an Architect (Certificate-2)", "score": 0.95}],
            ocr_status="COMPLETED",
            page_count=3,
            document_body_text="""Approval Process Handbook 2024-2027 (Page 212)
CERTIFICATE-2
Certificate of an Architect Registered with Council of Architecture
(To be produced in the Letterhead of Architect)

Approved Site Plan and Building Plans of Sree Rama Engineering College at Karakambadi Road, Tirupati.
Plans approved by: Tirupati Urban Development Authority (TUDA)
Approval Number: TUDA/BP/819/2012, Date: 11-04-2012.
Building admeasuring Ground + 2 Floors, Total Built-up Area: 13,490.00 Sq.Mtrs.
Construction is completed in all respects as per approved building plan.
Architect: Ar. K. Murali Krishna, Council of Architecture Reg. No: CA/98/22814.""",
            extracted_fields=[],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-003-4",
            application_id="app-003",
            original_filename="Affidavit_Format_2_Sree_Rama.pdf",
            mapped_type="Affidavit 2 (Self-Disclosure)",
            mapping_confidence=0.97,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Affidavit 2 (Self-Disclosure)", "score": 0.97}],
            ocr_status="COMPLETED",
            page_count=4,
            document_body_text="""Approval Process Handbook 2024-2027 (Page 186-188)
AFFIDAVIT-2
(For the applications submitted under Chapter I/II/IV except Closure of the Institution)

I/we, K. Rami Reddy, Chairman, Sri Rama Educational Society, son of Late K. Subba Reddy, aged 62, resident of Tirupati, do hereby solemnly affirm and declare under 33 clauses of APH:
1. Applied for Extension of Approval for Sree Rama Engineering College (AICTE-2025-ENG-1104).
2. Abiding by all terms of APH 2024-27.
3. Information submitted is true and complete.
4. Functioning at approved permanent site at Karakambadi Road, Tirupati (10.01 Acres, 13,490 sqm built-up).
7. Uploaded valid Fire Safety NOC Rc.No.502/MSB/SR/TPT/2023.
8. Qualified regular Principal in place.
9. Faculty:Student ratio maintained at 1:15.
Deponent: K. Rami Reddy. Sworn before Notary Public at Tirupati. Non-Judicial Stamp Paper Rs. 100/-.""",
            extracted_fields=[],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-003-5",
            application_id="app-003",
            original_filename="Certificate_3_Bank_Manager_Funds.pdf",
            mapped_type="Certificate of the Bank Manager (Certificate-3)",
            mapping_confidence=0.96,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Certificate of the Bank Manager (Certificate-3)", "score": 0.96}],
            ocr_status="COMPLETED",
            page_count=2,
            document_body_text="""Approval Process Handbook 2024-2027 (Page 213)
CERTIFICATE-3
Certificate of the Bank Manager where the Applicant has a Bank Account
(To be produced in the Letterhead of Bank duly signed by the Bank Manager)
STATE BANK OF INDIA, TIRUPATI MAIN BRANCH

A. Bank Statement:
Name of Account Holder: Sri Rama Educational Society
Account Number: 30819482914 | IFSC: SBIN0000938
Balance as on 28-02-2025: Rs. 1,45,28,490.00 (One Crore Forty Five Lakhs Twenty Eight Thousand Four Hundred Ninety Only).

B. Fixed Deposits:
FDR No: 38192849102 | Deposit Date: 14-06-2020 | Maturity Date: 14-06-2030 | Amount: Rs. 35,00,000.00
FDR is unencumbered and held in joint name with AICTE.
Signed: Chief Manager, State Bank of India, Tirupati Branch (Seal).""",
            extracted_fields=[
                ExtractedField(
                    key="operational_balance",
                    label="Bank Operational Balance",
                    value="Rs. 1,45,28,490.00",
                    confidence=0.99,
                    page=1,
                    provenance="Page 1, Account Row (PaddleOCR 0.99)"
                )
            ],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-003-6",
            application_id="app-003",
            original_filename="Occupancy_Certificate_Appendix_I_Tirupati.pdf",
            mapped_type="Occupancy Certificate",
            mapping_confidence=0.93,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Occupancy Certificate", "score": 0.93}],
            ocr_status="COMPLETED",
            page_count=2,
            document_body_text="""APPENDIX 'I' - FORM FOR OCCUPANCY CERTIFICATE
MUNICIPAL CORPORATION OF TIRUPATI
Occupancy Certificate No: MCT/TP/OC/2014/198, Date: 20-08-2014
To: Sri Rama Educational Society
Building at Sy.No.224/2, 3, 4, 5, Karakambadi Road, Renigunta (M), Tirupati.
OCCUPATION GRANTED for 13,490.00 Sq.Mtrs.
Signed: Commissioner / Town Planning Officer, Municipal Corporation Tirupati.""",
            extracted_fields=[],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-003-7",
            application_id="app-003",
            original_filename="AICTE_TER_Receipt_EoA_2025.pdf",
            mapped_type="TER / Payment Receipt",
            mapping_confidence=0.99,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "TER / Payment Receipt", "score": 0.99}],
            ocr_status="COMPLETED",
            page_count=1,
            document_body_text="""AICTE FEE PAYMENT RECEIPT
Application ID: AICTE-2025-ENG-1104
Institution: Sree Rama Engineering College, Tirupati
Transaction ID: AICTE-2025-TXN-559102 | Date: 12-03-2025 | Amount: Rs. 1,50,000.00 | Status: SUCCESS""",
            extracted_fields=[],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-003-8",
            application_id="app-003",
            original_filename="JNTUA_Affiliation_NOC_Format_2.pdf",
            mapped_type="NOC from Affiliating University (Format-2)",
            mapping_confidence=0.95,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "NOC from Affiliating University (Format-2)", "score": 0.95}],
            ocr_status="COMPLETED",
            page_count=2,
            document_body_text="""APPROVAL PROCESS HANDBOOK (FORMAT-2)
JAWAHARLAL NEHRU TECHNOLOGICAL UNIVERSITY ANANTAPUR (JNTUA)
Affiliation grant for Sree Rama Engineering College, Tirupati for B.Tech & M.Tech courses for AY 2025-26.
Signed: Registrar, JNTUA Ananthapuramu.""",
            extracted_fields=[],
            bounding_boxes=[],
            audit_history=[]
        )
    ],

    # -------------------------------------------------------------
    # APP-004: Saraswati College of Pharmaceutical Sciences
    # -------------------------------------------------------------
    "app-004": [
        DocumentItem(
            id="doc-004-1",
            application_id="app-004",
            original_filename="Affidavit_2_Pharmacy_Signed.pdf",
            mapped_type="Affidavit 2 (Self-Disclosure)",
            mapping_confidence=0.95,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Affidavit 2 (Self-Disclosure)", "score": 0.95}],
            ocr_status="COMPLETED",
            page_count=3,
            document_body_text="""Approval Process Handbook 2024-2027 (Page 186-188)
AFFIDAVIT-2 (Self-Disclosure)
I/we, Dr. Mahendra Patel, Secretary, Saraswati Education Trust, resident of Ahmedabad, Gujarat.
Application for Extension of Approval for Saraswati College of Pharmaceutical Sciences (AICTE-2025-PHARM-0199).
Land area: 3.2 Acres, Total Built-up: 3,450.00 Sq.M.
Sworn before Notary Public at Ahmedabad. Non-Judicial Stamp Paper Rs. 100/-.""",
            extracted_fields=[],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-004-2",
            application_id="app-004",
            original_filename="Gujarat_Fire_Safety_NOC.pdf",
            mapped_type="Fire Safety Certificate",
            mapping_confidence=0.94,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Fire Safety Certificate", "score": 0.94}],
            ocr_status="COMPLETED",
            page_count=2,
            document_body_text="""GUJARAT STATE FIRE PREVENTION SERVICES
Ahmedabad Municipal Corporation Fire Emergency Services
No. CFO/FES/AHM/NOC/2024-811, Date: 19-04-2024
No Objection Certificate for Educational Occupancy. Valid till 18-04-2027.""",
            extracted_fields=[],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-004-3",
            application_id="app-004",
            original_filename="TER_Fee_Receipt_2025.pdf",
            mapped_type="TER / Payment Receipt",
            mapping_confidence=0.98,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "TER / Payment Receipt", "score": 0.98}],
            ocr_status="COMPLETED",
            page_count=1,
            document_body_text="""AICTE FEE PAYMENT RECEIPT
Application ID: AICTE-2025-PHARM-0199 | Amount: Rs. 1,50,000.00 | Status: SUCCESS / SETTLED""",
            extracted_fields=[],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-004-4",
            application_id="app-004",
            original_filename="AMC_Occupancy_Certificate_Appendix_I.pdf",
            mapped_type="Occupancy Certificate",
            mapping_confidence=0.91,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Occupancy Certificate", "score": 0.91}],
            ocr_status="COMPLETED",
            page_count=2,
            document_body_text="""APPENDIX 'I' - FORM FOR OCCUPANCY CERTIFICATE
AHMEDABAD MUNICIPAL CORPORATION
Occupancy Certificate for Pharmacy College Building Block, 3,450 sqm. Occupation Granted.""",
            extracted_fields=[],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-004-5",
            application_id="app-004",
            original_filename="GTU_Affiliation_NOC_Format_2.pdf",
            mapped_type="NOC from Affiliating University (Format-2)",
            mapping_confidence=0.93,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "NOC from Affiliating University (Format-2)", "score": 0.93}],
            ocr_status="COMPLETED",
            page_count=2,
            document_body_text="""GUJARAT TECHNOLOGICAL UNIVERSITY (GTU)
NOC for B.Pharm and M.Pharm courses at Saraswati College of Pharmaceutical Sciences.""",
            extracted_fields=[],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-004-6",
            application_id="app-004",
            original_filename="Bank_Manager_Certificate_3.pdf",
            mapped_type="Certificate of the Bank Manager (Certificate-3)",
            mapping_confidence=0.94,
            mapping_stage="Content Confirmation (OCR)",
            candidate_types=[{"type": "Certificate of the Bank Manager (Certificate-3)", "score": 0.94}],
            ocr_status="COMPLETED",
            page_count=1,
            document_body_text="""BANK OF BARODA - CERTIFICATE OF BANK MANAGER
Operational account balance: Rs. 84,20,000.00 in name of Saraswati Education Trust.""",
            extracted_fields=[],
            bounding_boxes=[],
            audit_history=[]
        ),
        DocumentItem(
            id="doc-004-7",
            application_id="app-004",
            original_filename="Scan_Doc_2025_0049.pdf",
            mapped_type="Unmapped / Manual review",
            mapping_confidence=0.32,
            mapping_stage="Low Confidence / Needs Review",
            candidate_types=[
                {"type": "Structural Stability Certificate", "score": 0.32},
                {"type": "Satellite / Geolocation Map", "score": 0.28}
            ],
            ocr_status="COMPLETED",
            page_count=1,
            document_body_text="""[SCANNED DOCUMENT WITHOUT OFFICIAL HEADER]
Handwritten field measurement notes. Title not legible. Requires manual inspection by scrutiny officer.""",
            extracted_fields=[],
            bounding_boxes=[],
            audit_history=[]
        )
    ]
}

SAMPLE_FINDINGS = {
    "app-001": [
        Finding(
            id="fnd-001",
            application_id="app-001",
            rule_id="RULE-FIRE-01",
            rule_clause="AICTE APH 2024-2027 Appendix 16 Clause 3.2 & National Building Code Part 4",
            title="Fire Safety Certificate Expired Prior to Academic Year 2025-26",
            explanation="The submitted Fire Safety Certificate was valid for 2 years from 16-01-2023 and expired on 15-01-2025. An active, valid Fire Safety Certificate or proof of timely renewal submission is required for Extension of Approval (EoA).",
            why_evidence="OCR extracted 'valid from 16-01-2023 to 15-01-2025' from Page 1 (bbox [15, 45, 72, 6], OCR confidence 96%). Scrutiny date is March 2025 for AY 2025-26, meaning validity has elapsed by 56 days without renewal acknowledgment attached.",
            validation_status=ValidationStatus.DEFICIENCY,
            verification_status=VerificationStatus.MISMATCH,
            priority=ReviewPriority.RED,
            document_id="doc-001-2",
            document_name="Karnataka_Fire_Safety_Renewal_Cert.pdf",
            page_number=1,
            bounding_box=BoundingBox(page=1, x=15, y=45, width=72, height=6, label="Expired Date"),
            extracted_value="Expired: 15-01-2025",
            expected_value="Valid through at least 31-05-2025 or official renewal receipt",
            confidence=0.96,
            suggested_action="Issue scrutiny deficiency letter asking applicant to upload latest Fire Safety Certificate renewal endorsement from Chief Fire Officer.",
            reviewer_notes="Deficiency confirmed by reviewer. Expiry date verified against official CFO format.",
            disposition="DEFICIENCY_UPHELD",
            updated_at="2025-03-12 11:20:00"
        ),
        Finding(
            id="fnd-002",
            application_id="app-001",
            rule_id="RULE-AFF2-02",
            rule_clause="AICTE APH 2024-2027 Chapter II Clause 2.4.1 (Identity of Sponsoring Body)",
            title="Sponsoring Trust Legal Name Discrepancy",
            explanation="The Trust name recorded in the official application portal is 'Vishwa Bharati Educational Foundation', whereas Affidavit 2 (Paragraph 1) states 'Vishwa Bharati Education & Charitable Trust'.",
            why_evidence="Cross-document entity comparison between Application Metadata (trust_name='Vishwa Bharati Educational Foundation') and OCR text on Affidavit 2, Page 1: 'Vishwa Bharati Education & Charitable Trust' (Fuzzy similarity: 81%, below 95% threshold).",
            validation_status=ValidationStatus.DEFICIENCY,
            verification_status=VerificationStatus.MANUAL_REVIEW,
            priority=ReviewPriority.AMBER,
            document_id="doc-001-1",
            document_name="Affidavit_Format_2_Signed.pdf",
            page_number=1,
            bounding_box=BoundingBox(page=1, x=15, y=28, width=70, height=5, label="Trust Mention"),
            extracted_value="Vishwa Bharati Education & Charitable Trust",
            expected_value="Vishwa Bharati Educational Foundation",
            confidence=0.94,
            suggested_action="Reviewer to verify if this is an amended Trust Deed or clerical typo in the portal.",
            reviewer_notes="Under review. Calling for Trust Deed copy.",
            disposition="NEED_CLARIFICATION",
            updated_at="2025-03-12 11:35:00"
        ),
        Finding(
            id="fnd-003",
            application_id="app-001",
            rule_id="RULE-EVC-DUP-01",
            rule_clause="AICTE EVC Guidelines Section 4 (Infrastructure Authenticity)",
            title="Suspected Reused/Duplicate Computer Lab Image Across Applications",
            explanation="The photo submitted for 'Central Computer Center - Lab 3' produces a perceptual hash (pHash: 9f8a3c2b1e4d5a6b) matching another institute's submission (Apex Institute of Technology, Hubli, APP-2025-ENG-0422) with 98.4% visual similarity.",
            why_evidence="pHash Hamming distance is 1 (similarity 98.4%). Both photos exhibit identical monitor layout, asset tags, whiteboard markings ('Lab 04 - AI Lab'), and wall poster.",
            validation_status=ValidationStatus.DEFICIENCY,
            verification_status=VerificationStatus.MANUAL_REVIEW,
            priority=ReviewPriority.RED,
            document_id=None,
            document_name="EVC_Computer_Lab_03.jpg",
            page_number=1,
            bounding_box=None,
            extracted_value="pHash: 9f8a3c2b1e4d5a6b (Similarity: 98.4%)",
            expected_value="Unique geo-tagged institute photograph",
            confidence=0.98,
            suggested_action="Flag for mandatory physical On-Site EVC Inspection. Do not make fraud conclusion automatically.",
            reviewer_notes="Flagged for on-site inspection team with GPS camera verification.",
            disposition="ACCEPTED",
            updated_at="2025-03-12 11:45:00"
        ),
        Finding(
            id="fnd-004",
            application_id="app-001",
            rule_id="RULE-TER-01",
            rule_clause="AICTE APH 2024-2027 Chapter I Clause 1.6 (TER Fee Reconciliation)",
            title="TER Processing Fee Reconciled Successfully",
            explanation="Prescribed TER fee of Rs. 1,50,000 for EoA matches the uploaded banking receipt and gateway transaction record.",
            why_evidence="Receipt transaction ID 'AICTE-2025-TXN-998124' matches application fee reference. OCR extracted amount 'Rs. 1,50,000.00' matches prescribed table for EoA (Technical). Status verified SETTLED.",
            validation_status=ValidationStatus.PASS,
            verification_status=VerificationStatus.VERIFIED,
            priority=ReviewPriority.GREEN,
            document_id="doc-001-3",
            document_name="TER_Receipt_2025_26_AICTE.pdf",
            page_number=1,
            extracted_value="Rs. 1,50,000.00 (Settled)",
            expected_value="Rs. 1,50,000.00",
            confidence=0.99,
            suggested_action="No reviewer action required.",
            reviewer_notes="Fee reconciled.",
            disposition="ACCEPTED",
            updated_at="2025-03-12 11:05:00"
        )
    ],

    "app-002": [
        Finding(
            id="fnd-002-1",
            application_id="app-002",
            rule_id="RULE-CARPET-01",
            rule_clause="AICTE APH 2024-2027 Appendix 4 Table 4.1 (Norms for Intake Increase)",
            title="Instructional Carpet Area Shortfall for 600 Intake",
            explanation="Applied for intake increase to 600 seats. Prescribed minimum instructional and administrative carpet area is 4,500.00 Sq.Mtrs, but Architect Certificate-2 certifies only 3,780.00 Sq.Mtrs (Shortfall of 720 Sq.Mtrs).",
            why_evidence="Architect Certificate-2 Room Schedule table sums to 3,780.00 Sq.M. Under APH Table 4.1, an institution with 600 approved intake requires a minimum of 4,500 Sq.M. Built-up shortfall is 16.0%.",
            validation_status=ValidationStatus.DEFICIENCY,
            verification_status=VerificationStatus.MISMATCH,
            priority=ReviewPriority.RED,
            document_id="doc-002-2",
            document_name="Certificate_2_Architect_Carpet_Area.pdf",
            page_number=2,
            extracted_value="3,780.00 Sq.Mtrs",
            expected_value="Minimum 4,500.00 Sq.Mtrs",
            confidence=0.97,
            suggested_action="Deficiency upheld. Issue deficiency letter regarding infrastructure shortfall.",
            reviewer_notes="Shortfall confirmed by scrutiny team.",
            disposition="DEFICIENCY_UPHELD",
            updated_at="2025-03-14 15:10:00"
        ),
        Finding(
            id="fnd-002-2",
            application_id="app-002",
            rule_id="RULE-STRUCT-01",
            rule_clause="AICTE APH 2024-2027 Chapter II Clause 2.14 & NBC Part 6",
            title="Structural Stability Certificate Missing Engineer Seal & Registration",
            explanation="The submitted structural stability slip does not bear the registration number or official seal of a Chartered Engineer or Council of Architecture member.",
            why_evidence="OCR scan of Structural_Stability_Certificate_Unattested.pdf detected signature but no AMIE / municipal license number or official seal.",
            validation_status=ValidationStatus.DEFICIENCY,
            verification_status=VerificationStatus.MANUAL_REVIEW,
            priority=ReviewPriority.RED,
            document_id="doc-002-8",
            document_name="Structural_Stability_Certificate_Unattested.pdf",
            page_number=1,
            extracted_value="Unsealed / Unattested Document",
            expected_value="Chartered Structural Engineer with valid registration number and seal",
            confidence=0.88,
            suggested_action="Direct applicant to upload attested certificate from registered structural engineer.",
            disposition="DEFICIENCY_UPHELD",
            updated_at="2025-03-14 15:25:00"
        ),
        Finding(
            id="fnd-002-3",
            application_id="app-002",
            rule_id="RULE-EVC-DUP-01",
            rule_clause="AICTE EVC Guidelines Section 4 (Infrastructure Authenticity)",
            title="Shared Photographic Evidence with Vishwa Bharati Institute",
            explanation="Central Computer Lab photo matches submission from Vishwa Bharati Institute (AICTE-2025-ENG-0891) with 98.4% perceptual similarity.",
            why_evidence="Hamming distance 1 between pHash hashes. Same whiteboard notes, desktop model, and seating arrangement.",
            validation_status=ValidationStatus.DEFICIENCY,
            verification_status=VerificationStatus.MANUAL_REVIEW,
            priority=ReviewPriority.RED,
            extracted_value="pHash: 9f8a3c2b1e4d5a6b",
            expected_value="Distinct verified campus infrastructure",
            confidence=0.98,
            suggested_action="Flag for mandatory physical inspection by EVC.",
            disposition="ACCEPTED",
            updated_at="2025-03-14 15:30:00"
        )
    ],

    "app-003": [
        Finding(
            id="fnd-003-1",
            application_id="app-003",
            rule_id="RULE-FIRE-01",
            rule_clause="AICTE APH 2024-2027 Appendix 16 Clause 3.2 & AP Fire Services Act",
            title="Fire Safety Certificate Fully Compliant (5-Year Validity)",
            explanation="Andhra Pradesh State Disaster Response and Fire Services Department NOC (Rc.No.502/MSB/SR/TPT/2023) is verified for 13,490.00 Sq.M. with validity till 16-02-2028.",
            why_evidence="OCR verified Director General AP Fire Services seal, reference number Rc.No.502/MSB/SR/TPT/2023, 135 extinguishers, 9 hose reels, 10,000L tank, 450 LPM booster pump. Validity active till 16-02-2028.",
            validation_status=ValidationStatus.PASS,
            verification_status=VerificationStatus.VERIFIED,
            priority=ReviewPriority.GREEN,
            document_id="doc-003-1",
            document_name="AP_Fire_Services_NOC_Occupancy_Rc502.pdf",
            page_number=4,
            extracted_value="Valid till 16-02-2028 (13,490 sqm)",
            expected_value="Valid through at least 31-05-2025",
            confidence=0.99,
            suggested_action="Verified compliant. No action required.",
            disposition="ACCEPTED",
            updated_at="2025-03-15 10:00:00"
        ),
        Finding(
            id="fnd-003-2",
            application_id="app-003",
            rule_id="RULE-LAND-01",
            rule_clause="AICTE APH 2024-2027 Appendix 1 (Land Requirements for Technical Institution)",
            title="Advocate Title Certificate-1 Verifies 10.01 Acres Contiguous Land",
            explanation="Advocate Certificate-1 verifies clear marketable title for 10.01 Acres at Karakambadi Road, Renigunta (M), Tirupati in Sy.Nos 224/2, 3, 4, 5, etc.",
            why_evidence="Certificate-1 from practicing advocate confirms registered sale deeds 1824/2007 & 1825/2007. Land exceeds minimum 7.5 Acre norm for rural/semi-urban technical campus.",
            validation_status=ValidationStatus.PASS,
            verification_status=VerificationStatus.VERIFIED,
            priority=ReviewPriority.GREEN,
            document_id="doc-003-2",
            document_name="Certificate_1_Advocate_Land_Title.pdf",
            page_number=1,
            extracted_value="10.01 Acres clear title",
            expected_value="Minimum 7.50 Acres",
            confidence=0.98,
            suggested_action="Verified compliant.",
            disposition="ACCEPTED",
            updated_at="2025-03-15 10:15:00"
        ),
        Finding(
            id="fnd-003-3",
            application_id="app-003",
            rule_id="RULE-FUNDS-01",
            rule_clause="AICTE APH 2024-2027 Chapter I Clause 1.7 (Financial Solvency & FDR)",
            title="Bank Manager Certificate-3 Reconciles Operational Solvency",
            explanation="SBI Tirupati Branch confirms operational fund balance of Rs. 1.45 Crores and joint FDR of Rs. 35.00 Lakhs for 10 years maturity.",
            why_evidence="Bank Manager Certificate-3 verifies Account 30819482914 with Rs. 1,45,28,490 balance. FDR No. 38192849102 is unencumbered in joint name with AICTE.",
            validation_status=ValidationStatus.PASS,
            verification_status=VerificationStatus.VERIFIED,
            priority=ReviewPriority.GREEN,
            document_id="doc-003-5",
            document_name="Certificate_3_Bank_Manager_Funds.pdf",
            page_number=1,
            extracted_value="Rs. 1,45,28,490 balance + Rs. 35L FDR",
            expected_value="Operational funds >= Rs. 1.00 Crore",
            confidence=0.99,
            suggested_action="Verified compliant.",
            disposition="ACCEPTED",
            updated_at="2025-03-15 10:30:00"
        )
    ],

    "app-004": [
        Finding(
            id="fnd-004-1",
            application_id="app-004",
            rule_id="RULE-DOC-MAP-01",
            rule_clause="AICTE APH 2024-2027 Chapter II Document Ingestion Guidelines",
            title="Unmapped / Low Confidence Uploaded File Detected",
            explanation="File 'Scan_Doc_2025_0049.pdf' could not be automatically mapped to a canonical document type (Confidence: 32%).",
            why_evidence="Filename and content analysis did not match any alias in dictionary. Optical scan contains handwritten notes without official seal.",
            validation_status=ValidationStatus.INSUFFICIENT_EVIDENCE,
            verification_status=VerificationStatus.MANUAL_REVIEW,
            priority=ReviewPriority.AMBER,
            document_id="doc-004-7",
            document_name="Scan_Doc_2025_0049.pdf",
            page_number=1,
            extracted_value="Unmapped Scan (32% Confidence)",
            expected_value="Canonical APH Document Type",
            confidence=0.32,
            suggested_action="Reviewer to manually inspect file and reassign or request clear upload.",
            disposition="NEED_CLARIFICATION",
            updated_at="2025-03-16 17:00:00"
        ),
        Finding(
            id="fnd-004-2",
            application_id="app-004",
            rule_id="RULE-TER-01",
            rule_clause="AICTE APH 2024-2027 Chapter I Clause 1.6",
            title="TER Processing Fee Reconciled",
            explanation="Prescribed TER fee of Rs. 1,50,000 for Pharmacy EoA matches gateway logs.",
            why_evidence="Payment slip shows settled status.",
            validation_status=ValidationStatus.PASS,
            verification_status=VerificationStatus.VERIFIED,
            priority=ReviewPriority.GREEN,
            document_id="doc-004-3",
            document_name="TER_Fee_Receipt_2025.pdf",
            page_number=1,
            extracted_value="Rs. 1,50,000.00 (Settled)",
            expected_value="Rs. 1,50,000.00",
            confidence=0.98,
            suggested_action="No reviewer action required.",
            disposition="ACCEPTED",
            updated_at="2025-03-16 17:15:00"
        )
    ]
}

SAMPLE_EVC_ITEMS = {
    # APP-001
    "app-001": [
        EVCEvidenceItem(
            id="evc-001-1",
            application_id="app-001",
            category="Computer Center",
            filename="EVC_Computer_Lab_03.jpg",
            file_type="image",
            preview_url="https://images.unsplash.com/photo-1562774053-701939374585?w=800&auto=format&fit=crop&q=80",
            phash="9f8a3c2b1e4d5a6b",
            duplicate_flag=True,
            duplicate_match_app="AICTE-2025-ENG-0422 (Apex Institute of Technology)",
            duplicate_match_institution="Apex Institute of Technology & Research, Hubballi",
            duplicate_similarity=0.984,
            duplicate_explanation="Visual pHash Hamming distance is 1 (98.4% match). Whiteboard diagram, desktop monitor layout, and blue chair fabric match exactly with photo submitted by Apex Institute.",
            exif_gps={"lat": 12.9715, "lon": 77.5948},
            declared_gps={"lat": 12.9716, "lon": 77.5946},
            gps_distance_km=0.024,
            gps_match_status="MATCHED",
            inspection_needed=True,
            inspection_reason="Suspected shared/reused photo between two different institutions. Requires surprise physical inspection.",
            reviewer_notes="Reviewer added on-site verification request."
        ),
        EVCEvidenceItem(
            id="evc-001-2",
            application_id="app-001",
            category="Fire Safety",
            filename="EVC_Fire_Hydrant_Block_A.jpg",
            file_type="image",
            preview_url="https://images.unsplash.com/photo-1582139329536-e7284fece509?w=800&auto=format&fit=crop&q=80",
            phash="a1b2c3d4e5f67890",
            duplicate_flag=False,
            exif_gps={"lat": 12.9718, "lon": 77.5945},
            declared_gps={"lat": 12.9716, "lon": 77.5946},
            gps_distance_km=0.022,
            gps_match_status="MATCHED",
            inspection_needed=False,
            reviewer_notes="Fire safety equipment visible with pressure gauge."
        ),
        EVCEvidenceItem(
            id="evc-001-3",
            application_id="app-001",
            category="Campus Infrastructure",
            filename="EVC_Main_Entrance_GeoTag.jpg",
            file_type="image",
            preview_url="https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=800&auto=format&fit=crop&q=80",
            phash="b5c4d3e2f1a09876",
            duplicate_flag=False,
            exif_gps={"lat": 12.9716, "lon": 77.5946},
            declared_gps={"lat": 12.9716, "lon": 77.5946},
            gps_distance_km=0.002,
            gps_match_status="MATCHED",
            inspection_needed=False,
            reviewer_notes="Name board clearly legible matching portal institution name."
        ),
        EVCEvidenceItem(
            id="evc-001-4",
            application_id="app-001",
            category="Central Library",
            filename="EVC_Central_Library_Walkthrough.mp4",
            file_type="video",
            preview_url="https://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4",
            phash="c3d2e1f0a9b87654",
            duplicate_flag=False,
            video_keyframes=[
                VideoKeyframe(timestamp="00:04", frame_url="https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=600&auto=format&fit=crop&q=80", label="Stack Area", notes="Bookshelves with AICTE subject classification evident"),
                VideoKeyframe(timestamp="00:14", frame_url="https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=600&auto=format&fit=crop&q=80", label="Reading Hall", notes="Adequate seating for 150+ students observed")
            ],
            inspection_needed=False,
            reviewer_notes="Keyframes confirm reading hall."
        )
    ],

    # APP-002
    "app-002": [
        EVCEvidenceItem(
            id="evc-002-1",
            application_id="app-002",
            category="Computer Center",
            filename="EVC_Apex_Lab_04_AI.jpg",
            file_type="image",
            preview_url="https://images.unsplash.com/photo-1562774053-701939374585?w=800&auto=format&fit=crop&q=80",
            phash="9f8a3c2b1e4d5a6b",
            duplicate_flag=True,
            duplicate_match_app="AICTE-2025-ENG-0891 (Vishwa Bharati Institute)",
            duplicate_match_institution="Vishwa Bharati Institute of Technology & Science, Bengaluru",
            duplicate_similarity=0.984,
            duplicate_explanation="Perceptual hash match with Vishwa Bharati Institute. Whiteboard notes, workstation placement, and background signage match identically.",
            exif_gps={"lat": 15.3648, "lon": 75.1241},
            declared_gps={"lat": 15.3647, "lon": 75.1240},
            gps_distance_km=0.015,
            gps_match_status="MATCHED",
            inspection_needed=True,
            inspection_reason="Suspected duplicate computer center photo. Mandatory on-site verification required.",
            reviewer_notes="Reviewer flagged for EVC on-site visit."
        ),
        EVCEvidenceItem(
            id="evc-002-2",
            application_id="app-002",
            category="Campus Infrastructure",
            filename="EVC_Apex_Main_Building.jpg",
            file_type="image",
            preview_url="https://images.unsplash.com/photo-1592280771190-3e2e4d571952?w=800&auto=format&fit=crop&q=80",
            phash="8e7d6c5b4a3f2e1d",
            duplicate_flag=False,
            exif_gps={"lat": 15.3647, "lon": 75.1240},
            declared_gps={"lat": 15.3647, "lon": 75.1240},
            gps_distance_km=0.001,
            gps_match_status="MATCHED",
            inspection_needed=False
        ),
        EVCEvidenceItem(
            id="evc-002-3",
            application_id="app-002",
            category="Classrooms",
            filename="EVC_Smart_Classroom_101.jpg",
            file_type="image",
            preview_url="https://images.unsplash.com/photo-1580582932707-520aed937b7b?w=800&auto=format&fit=crop&q=80",
            phash="7a6b5c4d3e2f1a09",
            duplicate_flag=False,
            exif_gps={"lat": 15.3649, "lon": 75.1242},
            declared_gps={"lat": 15.3647, "lon": 75.1240},
            gps_distance_km=0.028,
            gps_match_status="MATCHED",
            inspection_needed=False
        ),
        EVCEvidenceItem(
            id="evc-002-4",
            application_id="app-002",
            category="Central Library",
            filename="EVC_Apex_Central_Library.jpg",
            file_type="image",
            preview_url="https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?w=800&auto=format&fit=crop&q=80",
            phash="6f5e4d3c2b1a0987",
            duplicate_flag=False,
            exif_gps={"lat": 15.3646, "lon": 75.1239},
            declared_gps={"lat": 15.3647, "lon": 75.1240},
            gps_distance_km=0.018,
            gps_match_status="MATCHED",
            inspection_needed=False
        )
    ],

    # APP-003: Sree Rama Engineering College (Tirupati, AP)
    "app-003": [
        EVCEvidenceItem(
            id="evc-003-1",
            application_id="app-003",
            category="Fire Safety",
            filename="EVC_Sree_Rama_Fire_Extinguisher_Sand_Buckets.jpg",
            file_type="image",
            preview_url="https://images.unsplash.com/photo-1582139329536-e7284fece509?w=800&auto=format&fit=crop&q=80",
            phash="5a4b3c2d1e0f9876",
            duplicate_flag=False,
            exif_gps={"lat": 13.658607, "lon": 79.490022},
            declared_gps={"lat": 13.6586, "lon": 79.4900},
            gps_distance_km=0.003,
            gps_match_status="MATCHED",
            inspection_needed=False,
            reviewer_notes="Fire Extinguisher & Sand Buckets stand at Rami Reddy Nagar, Karakambadi Road, Tirupati. Geotag verified."
        ),
        EVCEvidenceItem(
            id="evc-003-2",
            application_id="app-003",
            category="Campus Infrastructure",
            filename="EVC_Sree_Rama_Campus_Entrance.jpg",
            file_type="image",
            preview_url="https://images.unsplash.com/photo-1541339907198-e08756dedf3f?w=800&auto=format&fit=crop&q=80",
            phash="4e3d2c1b0a9f8765",
            duplicate_flag=False,
            exif_gps={"lat": 13.658747, "lon": 79.490011},
            declared_gps={"lat": 13.6586, "lon": 79.4900},
            gps_distance_km=0.016,
            gps_match_status="MATCHED",
            inspection_needed=False,
            reviewer_notes="Main entrance board clearly states 'SREE RAMA ENGINEERING COLLEGE (Approved by AICTE, Affiliated to JNTUA)'."
        ),
        EVCEvidenceItem(
            id="evc-003-3",
            application_id="app-003",
            category="Computer Center",
            filename="EVC_Sree_Rama_Computer_Center.jpg",
            file_type="image",
            preview_url="https://images.unsplash.com/photo-1517694712202-14dd9538aa97?w=800&auto=format&fit=crop&q=80",
            phash="3d2c1b0a9f8e7654",
            duplicate_flag=False,
            exif_gps={"lat": 13.658618, "lon": 79.490164},
            declared_gps={"lat": 13.6586, "lon": 79.4900},
            gps_distance_km=0.018,
            gps_match_status="MATCHED",
            inspection_needed=False,
            reviewer_notes="120 i5 systems with networking racks and UPS backup."
        ),
        EVCEvidenceItem(
            id="evc-003-4",
            application_id="app-003",
            category="Central Library",
            filename="EVC_Sree_Rama_Library.jpg",
            file_type="image",
            preview_url="https://images.unsplash.com/photo-1497633762265-9d179a990aa6?w=600&auto=format&fit=crop&q=80",
            phash="2c1b0a9f8e7d6543",
            duplicate_flag=False,
            exif_gps={"lat": 13.658590, "lon": 79.490050},
            declared_gps={"lat": 13.6586, "lon": 79.4900},
            gps_distance_km=0.006,
            gps_match_status="MATCHED",
            inspection_needed=False,
            reviewer_notes="Reading hall with seating capacity for 200+ students."
        )
    ],

    # APP-004: Saraswati College of Pharmacy (Ahmedabad)
    "app-004": [
        EVCEvidenceItem(
            id="evc-004-1",
            application_id="app-004",
            category="Laboratories",
            filename="EVC_Pharmaceutics_Lab_1.jpg",
            file_type="image",
            preview_url="https://images.unsplash.com/photo-1582719478250-c89cae4dc85b?w=800&auto=format&fit=crop&q=80",
            phash="1b0a9f8e7d6c5432",
            duplicate_flag=False,
            exif_gps={"lat": 23.2158, "lon": 72.6370},
            declared_gps={"lat": 23.2156, "lon": 72.6369},
            gps_distance_km=0.024,
            gps_match_status="MATCHED",
            inspection_needed=False
        ),
        EVCEvidenceItem(
            id="evc-004-2",
            application_id="app-004",
            category="Laboratories",
            filename="EVC_Pharmaceutical_Chemistry_Lab.jpg",
            file_type="image",
            preview_url="https://images.unsplash.com/photo-1532094349884-543bc11b234d?w=800&auto=format&fit=crop&q=80",
            phash="0a9f8e7d6c5b4321",
            duplicate_flag=False,
            exif_gps={"lat": 23.2157, "lon": 72.6368},
            declared_gps={"lat": 23.2156, "lon": 72.6369},
            gps_distance_km=0.015,
            gps_match_status="MATCHED",
            inspection_needed=False
        ),
        EVCEvidenceItem(
            id="evc-004-3",
            application_id="app-004",
            category="Campus Infrastructure",
            filename="EVC_Medicinal_Herbal_Garden.jpg",
            file_type="image",
            preview_url="https://images.unsplash.com/photo-1585320806297-9794b3e4eeae?w=800&auto=format&fit=crop&q=80",
            phash="9f8e7d6c5b4a3210",
            duplicate_flag=False,
            exif_gps={"lat": 23.2155, "lon": 72.6367},
            declared_gps={"lat": 23.2156, "lon": 72.6369},
            gps_distance_km=0.022,
            gps_match_status="MATCHED",
            inspection_needed=False
        ),
        EVCEvidenceItem(
            id="evc-004-4",
            application_id="app-004",
            category="Central Library",
            filename="EVC_Pharmacy_Library.jpg",
            file_type="image",
            preview_url="https://images.unsplash.com/photo-1521587760476-6c12a4b040da?w=600&auto=format&fit=crop&q=80",
            phash="8e7d6c5b4a3f2109",
            duplicate_flag=False,
            exif_gps={"lat": 23.2156, "lon": 72.6369},
            declared_gps={"lat": 23.2156, "lon": 72.6369},
            gps_distance_km=0.001,
            gps_match_status="MATCHED",
            inspection_needed=False
        )
    ]
}

SAMPLE_RULES = [
    RuleDefinition(
        id="RULE-AFF2-01",
        title="Affidavit 2 Completeness & Notarization (APH 2024-2027)",
        category="Extension of Approval (EoA)",
        academic_year="2025-26",
        clause="APH 2024-2027 Appendix 16 Clause 2.1 (p. 186-188)",
        source_title="AICTE Approval Process Handbook 2024-2027",
        validation_logic="Verify 33 statutory clauses, deponent signature, valid notary stamp with expiry year >= current year, non-judicial stamp paper value >= Rs 100",
        severity="HIGH",
        outcome_guidance="Flag DEFICIENCY if notary stamp is expired or signature is missing.",
        is_active=True,
        version="v2.4",
        effective_from="2024-01-01",
        effective_to="2027-03-31",
        author="Legal Cell & Approvals Bureau",
        last_reviewed="2025-02-15"
    ),
    RuleDefinition(
        id="RULE-FIRE-01",
        title="Fire Safety Certificate Validity (State Disaster Management)",
        category="All Categories",
        academic_year="2025-26",
        clause="APH 2024-2027 Appendix 16 Clause 3.2 & National Building Code Part 4",
        source_title="AICTE Approval Process Handbook 2024-2027",
        validation_logic="Verify issuing authority is competent State Disaster Response & Fire Services. Check validity date >= 31st May of academic year.",
        severity="HIGH",
        outcome_guidance="Flag DEFICIENCY if certificate has expired before scrutiny window without official renewal submission slip.",
        is_active=True,
        version="v2.2",
        effective_from="2024-01-01",
        effective_to="2027-03-31",
        author="Infrastructure Scrutiny Cell",
        last_reviewed="2025-02-10"
    ),
    RuleDefinition(
        id="RULE-EVC-DUP-01",
        title="EVC Photographic Integrity & Duplicate Detection",
        category="All Categories",
        academic_year="2025-26",
        clause="AICTE EVC Operational Guidelines Section 4 (Infrastructure Authenticity)",
        source_title="Guidelines for Expert Visiting Committee (EVC)",
        validation_logic="Compute pHash and dHash across all submissions. Flag items with perceptual similarity >= 95% against other institutions.",
        severity="HIGH",
        outcome_guidance="Flag for mandatory On-Site Physical Inspection. Note: Do not make legal fraud finding automatically; treat as investigation signal.",
        is_active=True,
        version="v1.6",
        effective_from="2024-01-01",
        effective_to="2027-03-31",
        author="Digital Vigilance Unit",
        last_reviewed="2025-02-20"
    ),
    RuleDefinition(
        id="RULE-TER-01",
        title="TER Processing Fee Reconciliation",
        category="All Categories",
        academic_year="2025-26",
        clause="APH 2024-2027 Chapter I Clause 1.6 (TER Fee Schedule)",
        source_title="AICTE Approval Process Handbook 2024-2027",
        validation_logic="Compare fee paid against prescribed table based on intake and category. Reconcile transaction reference with gateway logs.",
        severity="MEDIUM",
        outcome_guidance="If shortfall or unverified status, mark DEFICIENCY.",
        is_active=True,
        version="v1.2",
        effective_from="2024-01-01",
        effective_to="2027-03-31",
        author="Finance Bureau",
        last_reviewed="2025-01-15"
    ),
    RuleDefinition(
        id="RULE-CARPET-01",
        title="Minimum Carpet Area for Intake Increase",
        category="Intake Increase",
        academic_year="2025-26",
        clause="APH 2024-2027 Appendix 4 Table 4.1",
        source_title="AICTE Approval Process Handbook 2024-2027",
        validation_logic="Verify total instructional, administrative, and amenities area meets minimum prescribed square meters per student enrolled.",
        severity="HIGH",
        outcome_guidance="Calculate shortfall percentage. Flag DEFICIENCY if total area < prescribed minimum.",
        is_active=True,
        version="v2.5",
        effective_from="2024-01-01",
        effective_to="2027-03-31",
        author="Technical Norms Bureau",
        last_reviewed="2025-02-05"
    )
]

SAMPLE_AUDIT_LOGS = [
    AuditEvent(
        id="aud-001",
        timestamp="2025-03-12 10:14:02",
        user_name="Ingestion Worker",
        user_role="System Administrator",
        action="DATA_IMPORT",
        target_type="BATCH",
        target_id="BATCH-2025-03-12-01",
        details="Imported 4 application records from AICTE_Applications_2025_Export.csv. 0 schema errors."
    ),
    AuditEvent(
        id="aud-002",
        timestamp="2025-03-12 10:15:20",
        user_name="OCR & Auto-Mapper",
        user_role="System Administrator",
        action="DOCUMENT_MAPPING",
        target_type="APPLICATION",
        target_id="AICTE-2025-ENG-0891",
        details="Auto-mapped 7/7 documents. 6 high confidence (>90%), 1 medium confidence (88%). OCR text indexed."
    ),
    AuditEvent(
        id="aud-003",
        timestamp="2025-03-12 11:20:15",
        user_name="Prof. S. R. Sharma",
        user_role="Scrutiny Reviewer",
        action="DEFICIENCY_UPHELD",
        target_type="FINDING",
        target_id="fnd-001",
        details="Upheld deficiency on Fire Safety Certificate expiry (expired 15-01-2025). Added guidance note."
    ),
    AuditEvent(
        id="aud-004",
        timestamp="2025-03-12 11:45:30",
        user_name="Prof. S. R. Sharma",
        user_role="Scrutiny Reviewer",
        action="EVC_FLAG_ASSIGNED",
        target_type="EVC_ITEM",
        target_id="evc-001-1",
        details="Flagged Computer Lab 3 photo for on-site verification due to 98.4% visual pHash match with Apex Institute."
    )
]
