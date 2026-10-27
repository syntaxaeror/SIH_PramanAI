import json

def get_rich_documents_for_all_apps():
    docs = {}

    # Template definitions using the official handbook
    # -------------------------------------------------------------
    # APP-NTI-02: Kalinga Institute of Engineering & Emerging Technologies
    # -------------------------------------------------------------
    docs["app-nti-02"] = [
        {
            "id": "doc-nti02-1",
            "application_id": "app-nti-02",
            "original_filename": "Affidavit_3_SecurityDeposit_Kalinga.pdf",
            "mapped_type": "Affidavit 3 (Security Deposit)",
            "mapping_confidence": 0.98,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Affidavit 3 (Security Deposit)", "score": 0.98}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 189)
AFFIDAVIT-3
(For submitting the Security Deposit Upon establishment of New Technical Institution)

I/we, Dr. Achyuta Samanta, Managing Trustee, Kalinga Foundation & Education Society, resident of Patia, Bhubaneswar, Odisha - 751024, do hereby solemnly affirm and declare:
1. That I/we have applied for the establishment of Kalinga Institute of Engineering & Emerging Technologies, Plot No. 441, Infocity Avenue, Patia, Bhubaneswar vide application AICTE-2025-NEW-0102 dated 11-03-2025.
2. That an amount of Rs. 25,00,000/- was deposited by Kalinga Foundation in AICTE's account for a period of 10 years;
3. That the interest accrued on the deposit shall be retained by AICTE;
4. That the Land measuring 10.20 Acres on which the proposed Institution is located was not mortgaged for any purpose.

VERIFICATION
Verified at Bhubaneswar on 11-03-2025.
DEPONENT: Dr. Achyuta Samanta (Managing Trustee). Executed on Rs. 100/- E-Stamp Paper.""",
            "extracted_fields": json.dumps([{"key": "deposit_amount", "label": "Security Deposit", "value": "Rs. 25,00,000/-", "confidence": 0.99, "page": 1, "provenance": "Clause 2"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 30, "width": 80, "height": 8, "label": "Deposit: Rs. 25,00,000/-", "page": 1}]),
            "remarks": "₹25 Lakhs Security deposit verified with AICTE treasury.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-nti02-2",
            "application_id": "app-nti-02",
            "original_filename": "Advocate_Certificate_Land_Patia.pdf",
            "mapped_type": "Certificate of an Advocate (Certificate-1)",
            "mapping_confidence": 0.97,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Certificate of an Advocate (Certificate-1)", "score": 0.97}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 210-211)
CERTIFICATE-1
Certificate of an Advocate (Letterhead of Advocate)

Advocate B. K. Mohanty, M.A., LL.M., High Court of Orissa, Cuttack.
The copies of Kalinga Foundation registration documents and Land documents for establishment of Kalinga Institute of Engineering & Emerging Technologies at Khata No. 441, Patia, Bhubaneswar were verified:
1. Trust Registration: Society Reg. No. 1822-104 of 1992, Office of Registrar of Societies, Odisha.
2. Land Documents: Khata No. 441, Plot Nos. 108/1, 108/2, measuring 10.20 Acres, Sub Registrar Office Bhubaneswar. Clear title and lawful possession.
3. Land Use & Conversion: Converted for Educational purpose vide Collector Khordha Order No. 4491/2021.

Advocate B. K. Mohanty, Odisha State Bar Council Reg. No. OR/491/1989.""",
            "extracted_fields": json.dumps([{"key": "land_area", "label": "Land Area", "value": "10.20 Acres", "confidence": 0.98, "page": 1, "provenance": "Clause 2"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 40, "width": 80, "height": 8, "label": "Khata 441 Area: 10.20 Acres", "page": 1}]),
            "remarks": "10.20 Acres clear title certified by High Court Advocate.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-nti02-3",
            "application_id": "app-nti-02",
            "original_filename": "Architect_Certificate_Bhubaneswar.pdf",
            "mapped_type": "Certificate of an Architect (Certificate-2)",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Certificate of an Architect (Certificate-2)", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 212)
CERTIFICATE-2
Certificate of Registered Architect

Architect Soumya Ranjan Dash (CA/2010/48190), Bhubaneswar.
Building Plans approved by: Bhubaneswar Development Authority (BDA), Approval No. BDA/BP/2023/4011.
Completed Built-Up Area:
- Instructional Area: 5,800.00 Sq.M.
- Administrative Area: 1,600.00 Sq.M.
- Amenities Area: 1,800.00 Sq.M.
Total Carpet / Built-Up Area: 9,200.00 Sq.M.
Construction completed in all respects. Flooring, electrification, and safety staircases 100% complete.""",
            "extracted_fields": json.dumps([{"key": "total_builtup", "label": "Built-up Area", "value": "9,200.00 Sq.M.", "confidence": 0.99, "page": 1, "provenance": "Summary"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Total: 9,200.00 Sq.M.", "page": 1}]),
            "remarks": "Architect certified 9,200 sqm built-up area conforming to BDA norms.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-nti02-4",
            "application_id": "app-nti-02",
            "original_filename": "Odisha_Fire_Safety_Certificate.pdf",
            "mapped_type": "Fire Safety Certificate",
            "mapping_confidence": 0.95,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Fire Safety Certificate", "score": 0.95}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """ODISHA FIRE AND EMERGENCY SERVICES
Directorate of Fire Services, Nuapatna, Cuttack - 753001.
Certificate No. OFS/FP/2024/1102. Date: 12-02-2024.
Fire Safety Certificate granted to Kalinga Institute of Engineering & Emerging Technologies, Patia, Bhubaneswar.
NBC 2016 educational fire installations verified in order: Fire hydrants, 110 Extinguishers, 25,000L Overhead tank, automatic smoke detectors.
Valid for 3 years up to 11-02-2027.
Director General of Fire Services, Odisha.""",
            "extracted_fields": json.dumps([{"key": "valid_upto", "label": "Valid Upto", "value": "11-02-2027", "confidence": 0.98, "page": 1, "provenance": "Clause 4"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 55, "width": 80, "height": 8, "label": "Valid up to 11-02-2027", "page": 1}]),
            "remarks": "Valid Fire Safety Certificate up to 2027.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-nti02-5",
            "application_id": "app-nti-02",
            "original_filename": "BDA_Occupancy_Certificate.pdf",
            "mapped_type": "Occupancy Certificate",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Occupancy Certificate", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """BHUBANESWAR DEVELOPMENT AUTHORITY (BDA)
Akash Shova Building, Pandit Jawaharlal Nehru Marg, Bhubaneswar.
Occupancy Certificate No. BDA/OCC/2023/9102. Date: 18-12-2023.
OCCUPATION PERMISSION GRANTED for Institutional Educational Building G+3 floors, 9,200.00 Sq.M. at Plot No. 441, Patia.
Vice Chairman / Planning Member, BDA.""",
            "extracted_fields": json.dumps([{"key": "occupancy", "label": "Status", "value": "PERMISSION GRANTED", "confidence": 0.99, "page": 1, "provenance": "Grant Block"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 50, "width": 80, "height": 8, "label": "OCCUPATION PERMISSION GRANTED", "page": 1}]),
            "remarks": "BDA full occupancy permission verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-nti02-6",
            "application_id": "app-nti-02",
            "original_filename": "SBI_Bank_Manager_Certificate.pdf",
            "mapped_type": "Certificate of the Bank Manager (Certificate-3)",
            "mapping_confidence": 0.95,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Certificate of the Bank Manager (Certificate-3)", "score": 0.95}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 213)
CERTIFICATE-3
State Bank of India, Infocity Branch, Bhubaneswar.
Certified that Kalinga Foundation maintains Account No. 38910248812 with operational balance of Rs. 1,22,40,000/- as on 08-03-2025.
Fixed Deposit Receipts: FDR No. 4019283 for Rs. 1,00,00,000/- deposited for 10 years without lien or mortgage.
Branch Manager, SBI Infocity Branch.""",
            "extracted_fields": json.dumps([{"key": "balance", "label": "Balance", "value": "Rs. 1,22,40,000/-", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "FDR: Rs. 1,00,00,000/-", "page": 1}]),
            "remarks": "SBI Manager Certificate verifies ₹1.0 Cr FDR and ₹1.22 Cr balance.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-nti02-7",
            "application_id": "app-nti-02",
            "original_filename": "Odisha_Skill_Dev_DTE_NOC.pdf",
            "mapped_type": "NOC from State Government (Format-1)",
            "mapping_confidence": 0.97,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "NOC from State Government (Format-1)", "score": 0.97}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """FORMAT-1
GOVERNMENT OF ODISHA
SKILL DEVELOPMENT & TECHNICAL EDUCATION DEPARTMENT, Kalinga, Bhubaneswar.
No. SDTE-HE-04/2025/2911. Date: 20-02-2025.
No Objection Certificate granted to Kalinga Foundation for establishment of Kalinga Institute of Engineering & Emerging Technologies with intake of 300 seats.
Joint Secretary to Government.""",
            "extracted_fields": json.dumps([{"key": "noc", "label": "State NOC", "value": "GRANTED (300 Seats)", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "NOC Granted for 300 Seats", "page": 1}]),
            "remarks": "Odisha State Government NOC granted.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        }
    ]

    # -------------------------------------------------------------
    # APP-NTI-03: Heritage Institute of Technology & Research (Jaipur)
    # -------------------------------------------------------------
    docs["app-nti-03"] = [
        {
            "id": "doc-nti03-1",
            "application_id": "app-nti-03",
            "original_filename": "Affidavit_3_Heritage_Jaipur.pdf",
            "mapped_type": "Affidavit 3 (Security Deposit)",
            "mapping_confidence": 0.98,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Affidavit 3 (Security Deposit)", "score": 0.98}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 189)
AFFIDAVIT-3
(Security Deposit for New Institution)
I/we, Shri Radhe Shyam Sharma, Secretary, Heritage Vidya Niketan Society, Jaipur, solemnly affirm:
1. Applied for establishment of Heritage Institute of Technology & Research, Sitapura, Jaipur vide AICTE-2025-NEW-0103.
2. Security deposit of Rs. 20,00,000/- deposited in AICTE account for 10 years.
3. Land measuring 6.50 Acres at Sitapura Industrial Area without encumbrance.
DEPONENT: Radhe Shyam Sharma. Notary Public Jaipur.""",
            "extracted_fields": json.dumps([{"key": "deposit", "label": "Deposit", "value": "Rs. 20,00,000/-", "confidence": 0.98, "page": 1, "provenance": "Clause 2"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 35, "width": 80, "height": 8, "label": "Rs. 20,00,000/- Security Deposit", "page": 1}]),
            "remarks": "Security deposit confirmed.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-nti03-2",
            "application_id": "app-nti-03",
            "original_filename": "Advocate_Certificate_Sitapura.pdf",
            "mapped_type": "Certificate of an Advocate (Certificate-1)",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Certificate of an Advocate (Certificate-1)", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 210)
CERTIFICATE-1 (Advocate Certificate)
Advocate M. L. Gupta, Rajasthan High Court Jaipur Bench.
Certified that Heritage Vidya Niketan Society possesses 6.50 Acres at RIICO Phase IV Sitapura, Plot SP-12, registered at Sub Registrar Sanganer. Title clear and unencumbered.""",
            "extracted_fields": json.dumps([{"key": "area", "label": "Land Area", "value": "6.50 Acres", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 40, "width": 80, "height": 8, "label": "Area: 6.50 Acres", "page": 1}]),
            "remarks": "Clear title verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-nti03-3",
            "application_id": "app-nti-03",
            "original_filename": "Architect_Certificate_Jaipur.pdf",
            "mapped_type": "Certificate of an Architect (Certificate-2)",
            "mapping_confidence": 0.95,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Certificate of an Architect (Certificate-2)", "score": 0.95}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 212)
CERTIFICATE-2 (Architect Certificate)
Architect Sanjay Mathur (CA/98/23940), Jaipur.
JDA approved building plans: Total completed built-up area: 6,800.00 Sq.M. Classrooms: 14 Nos, Labs: 18 Nos, Library: 450 Sq.M. Completed in all respects.""",
            "extracted_fields": json.dumps([{"key": "builtup", "label": "Built-up Area", "value": "6,800.00 Sq.M.", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Built-up: 6,800.00 Sq.M.", "page": 1}]),
            "remarks": "Architect certified 6,800 sqm area.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-nti03-4",
            "application_id": "app-nti-03",
            "original_filename": "Rajasthan_Fire_NOC.pdf",
            "mapped_type": "Fire Safety Certificate",
            "mapping_confidence": 0.94,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Fire Safety Certificate", "score": 0.94}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """RAJASTHAN FIRE SERVICES - JAIPUR NAGAR NIGAM
Fire Safety Clearance Certificate No. JMC/FIRE/2024/889. Valid till 15-01-2027.
Educational building meets NBC 2016 safety installations: 80 Extinguishers, Hose Reel, 15,000L Overhead tank.""",
            "extracted_fields": json.dumps([{"key": "validity", "label": "Valid Till", "value": "15-01-2027", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 50, "width": 80, "height": 8, "label": "Valid till 15-01-2027", "page": 1}]),
            "remarks": "Valid Fire Safety NOC.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-nti03-5",
            "application_id": "app-nti-03",
            "original_filename": "JDA_Occupancy_Certificate.pdf",
            "mapped_type": "Occupancy Certificate",
            "mapping_confidence": 0.97,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Occupancy Certificate", "score": 0.97}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """JAIPUR DEVELOPMENT AUTHORITY (JDA)
Occupancy Certificate No. JDA/BPC/2023/1209.
Occupation permission granted for Educational Institution at Sitapura Phase IV, 6,800.00 Sq.M.
Senior Town Planner, JDA.""",
            "extracted_fields": json.dumps([{"key": "occupancy", "label": "Status", "value": "OCCUPANCY GRANTED", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 50, "width": 80, "height": 8, "label": "OCCUPANCY GRANTED", "page": 1}]),
            "remarks": "JDA Occupancy Certificate verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-nti03-6",
            "application_id": "app-nti-03",
            "original_filename": "ICICI_Bank_Certificate.pdf",
            "mapped_type": "Certificate of the Bank Manager (Certificate-3)",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Certificate of the Bank Manager (Certificate-3)", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 213)
CERTIFICATE-3 (Bank Manager Certificate)
ICICI Bank Ltd., Tonk Road Branch, Jaipur.
Certified that Heritage Vidya Niketan Society holds Account No. 001405009121 with operational balance of Rs. 1,15,60,000/-.
Operational FDR No. 994012 of Rs. 80,00,000/- without lien.
Branch Manager, ICICI Bank.""",
            "extracted_fields": json.dumps([{"key": "balance", "label": "Balance", "value": "Rs. 1,15,60,000/-", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Balance: Rs. 1,15,60,000/-", "page": 1}]),
            "remarks": "Bank certificate verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-nti03-7",
            "application_id": "app-nti-03",
            "original_filename": "Rajasthan_Govt_DTE_NOC.pdf",
            "mapped_type": "NOC from State Government (Format-1)",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "NOC from State Government (Format-1)", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """FORMAT-1 (State Govt NOC)
GOVERNMENT OF RAJASTHAN, TECHNICAL EDUCATION DEPARTMENT, Jaipur.
No. F.12(4)TE/2025/1109. Date: 16-02-2025.
No Objection Certificate granted for establishment of Heritage Institute of Technology & Research with 240 intake.
Joint Secretary, Technical Education.""",
            "extracted_fields": json.dumps([{"key": "noc", "label": "NOC", "value": "GRANTED (240 Intake)", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "NOC Granted: 240 Intake", "page": 1}]),
            "remarks": "State Govt NOC verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        }
    ]

    # -------------------------------------------------------------
    # APP-NTI-04: Dr. A.P.J. Abdul Kalam Technical Campus (Lucknow)
    # -------------------------------------------------------------
    docs["app-nti-04"] = [
        {
            "id": "doc-nti04-1",
            "application_id": "app-nti-04",
            "original_filename": "Affidavit_3_Kalam_Campus.pdf",
            "mapped_type": "Affidavit 3 (Security Deposit)",
            "mapping_confidence": 0.98,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Affidavit 3 (Security Deposit)", "score": 0.98}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 189)
AFFIDAVIT-3
I/we, Mohd. Tariq Khan, Secretary, Kalam Memorial Education Foundation, Lucknow affirm:
1. Applied for Dr. A.P.J. Abdul Kalam Technical Campus at Kursi Road, Lucknow vide AICTE-2025-NEW-0104.
2. Deposited Rs. 30,00,000/- security deposit for 10 years in AICTE account.
3. Land measuring 8.00 Acres at Jankipuram Extension.
DEPONENT: Mohd. Tariq Khan. Notary Lucknow.""",
            "extracted_fields": json.dumps([{"key": "deposit", "label": "Deposit", "value": "Rs. 30,00,000/-", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 35, "width": 80, "height": 8, "label": "Deposit: Rs. 30,00,000/-", "page": 1}]),
            "remarks": "Security deposit verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-nti04-2",
            "application_id": "app-nti-04",
            "original_filename": "Advocate_Certificate_Lucknow.pdf",
            "mapped_type": "Certificate of an Advocate (Certificate-1)",
            "mapping_confidence": 0.97,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Certificate of an Advocate (Certificate-1)", "score": 0.97}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """CERTIFICATE-1 (Advocate Certificate)
Advocate R. P. Shukla, High Court Allahabad, Lucknow Bench.
Verified land documents for 8.00 Acres at Kursi Road, Jankipuram, Lucknow. Title clear and in lawful possession of Kalam Memorial Education Foundation.""",
            "extracted_fields": json.dumps([{"key": "area", "label": "Area", "value": "8.00 Acres", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 40, "width": 80, "height": 8, "label": "Land Area: 8.00 Acres", "page": 1}]),
            "remarks": "Advocate certificate clear.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-nti04-3",
            "application_id": "app-nti-04",
            "original_filename": "Architect_Certificate_Lucknow.pdf",
            "mapped_type": "Certificate of an Architect (Certificate-2)",
            "mapping_confidence": 0.95,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Certificate of an Architect (Certificate-2)", "score": 0.95}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """CERTIFICATE-2 (Architect Certificate)
Architect Amit Srivastava (CA/2008/42911), Lucknow.
LDA Approved Plan: Total Completed Built-Up Area: 7,900.00 Sq.M.
Construction completed in all respects.""",
            "extracted_fields": json.dumps([{"key": "builtup", "label": "Area", "value": "7,900.00 Sq.M.", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Area: 7,900.00 Sq.M.", "page": 1}]),
            "remarks": "Architect certificate verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-nti04-4",
            "application_id": "app-nti-04",
            "original_filename": "UP_Fire_Safety_Certificate_Expired.pdf",
            "mapped_type": "Fire Safety Certificate",
            "mapping_confidence": 0.92,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Fire Safety Certificate", "score": 0.92}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """UTTAR PRADESH FIRE SERVICE - LUCKNOW
Provisional Fire Safety NOC No. UPFS/LKO/2023/1109.
Dated: 10-01-2023. Valid for 1 year up to 09-01-2024.
WARNING: Certificate has expired on 09-01-2024. Final Fire NOC renewal has not been submitted.""",
            "extracted_fields": json.dumps([{"key": "expiry", "label": "Expiry Date", "value": "09-01-2024", "confidence": 0.99, "page": 1, "provenance": "Warning Block"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 50, "width": 80, "height": 8, "label": "EXPIRED: 09-01-2024", "page": 1}]),
            "remarks": "DEFICIENCY: Fire Safety Certificate expired on 09-01-2024.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Needs Attention"
        },
        {
            "id": "doc-nti04-5",
            "application_id": "app-nti-04",
            "original_filename": "LDA_Occupancy_Certificate.pdf",
            "mapped_type": "Occupancy Certificate",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Occupancy Certificate", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """LUCKNOW DEVELOPMENT AUTHORITY (LDA)
Part Occupancy Certificate No. LDA/BP/2023/8812.
Granted for Ground + 2 Floors, 7,900.00 Sq.M. at Kursi Road, Lucknow.""",
            "extracted_fields": json.dumps([{"key": "occupancy", "label": "Occupancy", "value": "PART OCCUPANCY GRANTED", "confidence": 0.97, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 50, "width": 80, "height": 8, "label": "PART OCCUPANCY GRANTED", "page": 1}]),
            "remarks": "Part occupancy verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-nti04-6",
            "application_id": "app-nti-04",
            "original_filename": "PNB_Bank_Certificate.pdf",
            "mapped_type": "Certificate of the Bank Manager (Certificate-3)",
            "mapping_confidence": 0.95,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Certificate of the Bank Manager (Certificate-3)", "score": 0.95}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """Punjab National Bank, Hazratganj Branch, Lucknow.
Certified that Kalam Memorial Foundation has operational balance of Rs. 1,30,50,000/- and FDRs of Rs. 1.0 Cr without mortgage.""",
            "extracted_fields": json.dumps([{"key": "balance", "label": "Balance", "value": "Rs. 1,30,50,000/-", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Balance: Rs. 1,30,50,000/-", "page": 1}]),
            "remarks": "PNB certificate verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-nti04-7",
            "application_id": "app-nti-04",
            "original_filename": "UP_Govt_Technical_Edu_NOC.pdf",
            "mapped_type": "NOC from State Government (Format-1)",
            "mapping_confidence": 0.97,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "NOC from State Government (Format-1)", "score": 0.97}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """GOVERNMENT OF UTTAR PRADESH, TECHNICAL EDUCATION SECTION-1, Lucknow.
No. 402/TE/2025. Date: 15-02-2025.
No Objection Certificate granted for establishment of Dr. A.P.J. Abdul Kalam Technical Campus with 300 seats.""",
            "extracted_fields": json.dumps([{"key": "noc", "label": "NOC", "value": "GRANTED (300 Seats)", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "NOC: 300 Seats", "page": 1}]),
            "remarks": "UP State Govt NOC verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        }
    ]

    # -------------------------------------------------------------
    # APP-EOA-03: PSG College of Technology & Applied Research (Coimbatore)
    # -------------------------------------------------------------
    docs["app-eoa-03"] = [
        {
            "id": "doc-eoa03-1",
            "application_id": "app-eoa-03",
            "original_filename": "Affidavit_2_PSG_Charities.pdf",
            "mapped_type": "Affidavit 2 (Self-Disclosure)",
            "mapping_confidence": 0.98,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Affidavit 2 (Self-Disclosure)", "score": 0.98}]),
            "ocr_status": "COMPLETED",
            "page_count": 4,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 186-188)
AFFIDAVIT-2 (33 Clauses Self-Disclosure)
I/we, L. Gopalakrishnan, Managing Trustee, PSG & Sons' Charities, Coimbatore, solemnly affirm:
1. Applied for Extension of Approval (EoA) for PSG College of Technology & Applied Research vide AICTE-2025-ENG-1105.
2. Abiding by all 33 clauses of Approval Process Handbook 2024-27.
3. Land measuring 15.5 Acres at Peelamedu, Coimbatore without dispute.
4. Total Built-Up Area: 16,400.00 Sq.M. completed in all respects.
5. All mandatory committees (Anti-Ragging, Grievance, IC, SC/ST) functional.
DEPONENT: L. Gopalakrishnan. Notary Public Coimbatore.""",
            "extracted_fields": json.dumps([{"key": "app", "label": "Application ID", "value": "AICTE-2025-ENG-1105", "confidence": 0.99, "page": 1, "provenance": "Clause 1"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 30, "width": 80, "height": 8, "label": "AICTE-2025-ENG-1105", "page": 1}]),
            "remarks": "PSG Affidavit-2 verified 100% compliant.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-eoa03-2",
            "application_id": "app-eoa-03",
            "original_filename": "TamilNadu_Fire_Services_NOC.pdf",
            "mapped_type": "Fire Safety Certificate",
            "mapping_confidence": 0.97,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Fire Safety Certificate", "score": 0.97}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """TAMIL NADU FIRE AND RESCUE SERVICES DEPARTMENT
Office of the Divisional Fire Officer, Coimbatore District.
R.Dis.No. 4921/CBE/2024. Date: 14-02-2024.
Fire Safety Certificate renewed for PSG College of Technology & Applied Research, Peelamedu, Coimbatore.
Valid for 3 years up to 13-02-2027.""",
            "extracted_fields": json.dumps([{"key": "validity", "label": "Validity", "value": "13-02-2027", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 50, "width": 80, "height": 8, "label": "Valid up to 13-02-2027", "page": 1}]),
            "remarks": "TN Fire Safety certificate valid till 2027.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-eoa03-3",
            "application_id": "app-eoa-03",
            "original_filename": "Anna_University_Format2_NOC.pdf",
            "mapped_type": "NOC from Affiliating University (Format-2)",
            "mapping_confidence": 0.98,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "NOC from Affiliating University (Format-2)", "score": 0.98}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 202)
FORMAT-2 (Affiliating University NOC)
ANNA UNIVERSITY, Sardar Patel Road, Chennai - 600025.
Ref: AU/AFF/2025/1102. Date: 22-02-2025.
This is to confirm that Anna University has no objection for the Extension of Approval (EoA) of PSG College of Technology & Applied Research for 780 intake across approved engineering branches.
Registrar, Anna University.""",
            "extracted_fields": json.dumps([{"key": "affiliation", "label": "University NOC", "value": "NO OBJECTION (780 Intake)", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Anna University NOC (780 Seats)", "page": 1}]),
            "remarks": "Anna University Format-2 NOC verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-eoa03-4",
            "application_id": "app-eoa-03",
            "original_filename": "Coimbatore_Corporation_Occupancy.pdf",
            "mapped_type": "Occupancy Certificate",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Occupancy Certificate", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """COIMBATORE CITY MUNICIPAL CORPORATION
Occupancy Certificate No. CCMC/TP/2022/881.
Occupation Granted for Educational Complex, 16,400.00 Sq.M. at Avinashi Road, Peelamedu.
Commissioner, Coimbatore Corporation.""",
            "extracted_fields": json.dumps([{"key": "occupancy", "label": "Occupancy", "value": "GRANTED", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "OCCUPANCY GRANTED", "page": 1}]),
            "remarks": "Corporation Occupancy verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-eoa03-5",
            "application_id": "app-eoa-03",
            "original_filename": "Canara_Bank_Manager_Certificate.pdf",
            "mapped_type": "Certificate of the Bank Manager (Certificate-3)",
            "mapping_confidence": 0.95,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Certificate of the Bank Manager (Certificate-3)", "score": 0.95}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """Canara Bank, Peelamedu Branch, Coimbatore.
Certified that PSG College has operational funds of Rs. 3,40,00,000/- and unencumbered FDR of Rs. 2.0 Cr.
Branch Manager, Canara Bank.""",
            "extracted_fields": json.dumps([{"key": "balance", "label": "Balance", "value": "Rs. 3,40,00,000/-", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Balance: Rs. 3,40,00,000/-", "page": 1}]),
            "remarks": "Bank funds verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-eoa03-6",
            "application_id": "app-eoa-03",
            "original_filename": "Structural_Stability_Certificate_PSG.pdf",
            "mapped_type": "Structural Stability Certificate",
            "mapping_confidence": 0.97,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Structural Stability Certificate", "score": 0.97}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """FORM 1A - STRUCTURAL SOUNDNESS CERTIFICATE
Chartered Structural Engineer Dr. K. Radhakrishnan (M.E., Ph.D., F.I.E.), Panel Engineer Class-1A.
Certified that buildings of PSG College of Technology & Applied Research are structurally sound for educational use under seismic zone III norms.
Valid for 5 years up to 2029.""",
            "extracted_fields": json.dumps([{"key": "stability", "label": "Stability", "value": "SOUND & CERTIFIED", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "STRUCTURAL SOUNDNESS VERIFIED", "page": 1}]),
            "remarks": "Structural stability verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-eoa03-7",
            "application_id": "app-eoa-03",
            "original_filename": "Audited_Balance_Sheet_PSG.pdf",
            "mapped_type": "Audited Financial Statement",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Audited Financial Statement", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 3,
            "document_body_text": """AUDITED FINANCIAL STATEMENTS FY 2023-24
M/s S. Lakshminarayanan & Co., Chartered Accountants, Coimbatore.
Audited balance sheet and income/expenditure statement for PSG College.
UDIN: 24029104AAAAAB9912. Net Surplus: Rs. 4.82 Crores. Depreciation and reserves fully funded.""",
            "extracted_fields": json.dumps([{"key": "udin", "label": "CA UDIN", "value": "24029104AAAAAB9912", "confidence": 0.99, "page": 1, "provenance": "Header"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 35, "width": 80, "height": 8, "label": "UDIN: 24029104AAAAAB9912", "page": 1}]),
            "remarks": "Audited accounts with valid UDIN.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-eoa03-8",
            "application_id": "app-eoa-03",
            "original_filename": "AICTE_TER_Fee_Payment_Receipt.pdf",
            "mapped_type": "TER / Payment Receipt",
            "mapping_confidence": 0.98,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "TER / Payment Receipt", "score": 0.98}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """AICTE WEB PORTAL - PAYMENT RECEIPT
Transaction ID: AICTE2025PAY889124
Payment Date: 12-03-2025. Amount: Rs. 2,00,000/-.
Purpose: TER Extension of Approval AY 2025-26. Payment Status: SUCCESSFUL.""",
            "extracted_fields": json.dumps([{"key": "amount", "label": "TER Fee", "value": "Rs. 2,00,000/-", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 40, "width": 80, "height": 8, "label": "Rs. 2,00,000/- SUCCESS", "page": 1}]),
            "remarks": "TER fee receipt verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        }
    ]

    # Additional applications generator (NPL, II, OTH)
    # -------------------------------------------------------------
    # BMS Institute (app-npl-01) - New M.Tech in AI & Data Science
    # -------------------------------------------------------------
    docs["app-npl-01"] = [
        {
            "id": "doc-npl01-1",
            "application_id": "app-npl-01",
            "original_filename": "Affidavit_2_BMSIT.pdf",
            "mapped_type": "Affidavit 2 (Self-Disclosure)",
            "mapping_confidence": 0.97,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Affidavit 2 (Self-Disclosure)", "score": 0.97}]),
            "ocr_status": "COMPLETED",
            "page_count": 3,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 186)
AFFIDAVIT-2 (New Programme / Level)
I/we, Aviram Sharma, Trustee, B.M.S. Educational Trust, Bengaluru affirm:
1. Applied for New Programme: M.Tech in Artificial Intelligence & Data Science (Intake: 60) vide AICTE-2025-PG-0301.
2. Verified all instructional labs and faculty for PG programme created as per APH norms.
DEPONENT: Aviram Sharma. Notary Bengaluru.""",
            "extracted_fields": json.dumps([{"key": "course", "label": "New Course", "value": "M.Tech in AI & Data Science (60 Seats)", "confidence": 0.98, "page": 1, "provenance": "Clause 1"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 35, "width": 80, "height": 8, "label": "M.Tech AI & Data Science (60 Seats)", "page": 1}]),
            "remarks": "Affidavit for new PG programme verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-npl01-2",
            "application_id": "app-npl-01",
            "original_filename": "VTU_Format2_NOC_NewPG.pdf",
            "mapped_type": "NOC from Affiliating University (Format-2)",
            "mapping_confidence": 0.98,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "NOC from Affiliating University (Format-2)", "score": 0.98}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 202)
FORMAT-2 (Affiliating University NOC)
VISVESVARAYA TECHNOLOGICAL UNIVERSITY (VTU), Belagavi, Karnataka.
Ref: VTU/ACA/2025/PG-0412. Date: 19-02-2025.
No objection granted to BMS Institute of Technology & Management for starting of new PG Programme: M.Tech in Artificial Intelligence & Data Science with intake of 60 students.
Registrar, VTU Belagavi.""",
            "extracted_fields": json.dumps([{"key": "vtu_noc", "label": "VTU NOC", "value": "GRANTED (60 Seats M.Tech AI)", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "VTU No Objection: 60 Seats", "page": 1}]),
            "remarks": "VTU Belagavi University NOC verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-npl01-3",
            "application_id": "app-npl-01",
            "original_filename": "Trust_Resolution_Format3_BMS.pdf",
            "mapped_type": "Resolution of the Trust (Format-3)",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Resolution of the Trust (Format-3)", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 205)
FORMAT-3 (Resolution of Trust)
B.M.S. Educational Trust Executive Committee Meeting held on 15-01-2025.
Resolved: Apply for starting of new M.Tech Programme in Artificial Intelligence & Data Science with 60 intake and allocate Rs. 1.5 Crores for high-performance GPU lab setup and faculty recruitment.
Chairman, B.M.S. Educational Trust.""",
            "extracted_fields": json.dumps([{"key": "allocation", "label": "Fund Allocation", "value": "Rs. 1.5 Crores", "confidence": 0.98, "page": 1, "provenance": "Resolution"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 40, "width": 80, "height": 8, "label": "Allocated Rs. 1.5 Cr for AI Labs", "page": 1}]),
            "remarks": "Format-3 Trust resolution verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-npl01-4",
            "application_id": "app-npl-01",
            "original_filename": "Architect_Certificate_PG_Area.pdf",
            "mapped_type": "Certificate of an Architect (Certificate-2)",
            "mapping_confidence": 0.95,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Certificate of an Architect (Certificate-2)", "score": 0.95}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """CERTIFICATE-2 (Architect Certificate)
Architect Ramesh K. Rao (CA/2001/29841), Bengaluru.
Certified that dedicated PG instructional space of 1,200.00 Sq.M. (2 PG Classrooms: 132 Sq.M., 2 Advanced Research Labs: 400 Sq.M., Seminar Hall: 150 Sq.M.) has been created on 3rd Floor of Academic Block-C for the new M.Tech Programme.""",
            "extracted_fields": json.dumps([{"key": "pg_area", "label": "PG Area", "value": "1,200.00 Sq.M.", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Dedicated PG Space: 1,200 Sq.M.", "page": 1}]),
            "remarks": "Architect certified 1,200 sqm dedicated PG floor.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-npl01-5",
            "application_id": "app-npl-01",
            "original_filename": "BBMP_Occupancy_BMSIT.pdf",
            "mapped_type": "Occupancy Certificate",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Occupancy Certificate", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """BRUHAT BENGALURU MAHANAGARA PALIKE (BBMP)
Occupancy Certificate for Academic Block-C, Yelahanka, Bengaluru.
Full Occupation Granted for Educational Occupancy.
Joint Commissioner (Yelahanka Zone), BBMP.""",
            "extracted_fields": json.dumps([{"key": "occupancy", "label": "Occupancy", "value": "GRANTED", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "BBMP Full Occupation Granted", "page": 1}]),
            "remarks": "BBMP Occupancy verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-npl01-6",
            "application_id": "app-npl-01",
            "original_filename": "Karnataka_Fire_NOC_BMSIT.pdf",
            "mapped_type": "Fire Safety Certificate",
            "mapping_confidence": 0.95,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Fire Safety Certificate", "score": 0.95}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """KARNATAKA STATE FIRE AND EMERGENCY SERVICES
Fire Safety Recommendation Certificate No. GBC(1)140/2024. Valid up to 28-02-2027.
Chief Fire Officer, Bengaluru East.""",
            "extracted_fields": json.dumps([{"key": "validity", "label": "Valid Upto", "value": "28-02-2027", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Valid up to 28-02-2027", "page": 1}]),
            "remarks": "Fire safety certificate valid.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-npl01-7",
            "application_id": "app-npl-01",
            "original_filename": "TER_Payment_Receipt_BMSIT.pdf",
            "mapped_type": "TER / Payment Receipt",
            "mapping_confidence": 0.99,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "TER / Payment Receipt", "score": 0.99}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """AICTE PAYMENT RECEIPT
Transaction ID: AICTE2025PG77819
Payment Date: 11-03-2025. Amount: Rs. 1,50,000/-.
Purpose: TER Charges for New Programme (M.Tech AI & Data Science). Status: SUCCESSFUL.""",
            "extracted_fields": json.dumps([{"key": "ter", "label": "TER Fee", "value": "Rs. 1,50,000/-", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Rs. 1,50,000/- SUCCESS", "page": 1}]),
            "remarks": "TER Fee verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        }
    ]

    # -------------------------------------------------------------
    # APP-OTH-01: Priyadarshini College (Nagpur) - Progressive Closure with Affidavit-4
    # -------------------------------------------------------------
    docs["app-oth-01"] = [
        {
            "id": "doc-oth01-1",
            "application_id": "app-oth-01",
            "original_filename": "Affidavit_Format_4_Closure.pdf",
            "mapped_type": "Affidavit 4 (Closure of Institution / Course)",
            "mapping_confidence": 0.98,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Affidavit 4 (Closure of Institution / Course)", "score": 0.98}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 190)
AFFIDAVIT-4
(For the Progressive/Complete Closure of the Institution)

I/we, Dr. Satish Chaturvedi, Chairman, Lokmanya Tilak Jankalyan Shikshan Sanstha, resident of Nagpur, Maharashtra, do hereby solemnly affirm and declare:
1. That I/we have applied for Progressive Closure of B.Arch Programme at Priyadarshini College of Engineering & Architecture vide application AICTE-2025-OTH-0501 dated 11-03-2025.
2. That our Trust vide resolution dated 05-01-2025 resolved for closing the B.Arch course and paid requisite TER fees;
3. That liabilities, if any, arise out of closure shall be solely of the Trust;
4. That the Trust undertakes that NO FURTHER ADMISSION OF STUDENTS shall be made in current and forthcoming years;
5. That the Trust undertakes to provide all facilities to existing students till they pass out;
6. Details of RPGF / Joint FDR: Joint FDR No. 492102 with AICTE for Rs. 50,00,000/- with State Bank of India, Nagpur. FDR was neither mortgaged nor encashed.
Student Re-arrangement schedule: 4th year: 28 students, 5th year: 34 students. Adequate faculty retained.

VERIFICATION
Verified at Nagpur on 11-03-2025 that facts stated are true and complete.
DEPONENT: Dr. Satish Chaturvedi. Sworn before Judicial Magistrate First Class, Nagpur.""",
            "extracted_fields": json.dumps([
                {"key": "closure_type", "label": "Closure Type", "value": "Progressive Closure of B.Arch", "confidence": 0.98, "page": 1, "provenance": "Clause 1"},
                {"key": "fdr_amount", "label": "AICTE Joint FDR", "value": "Rs. 50,00,000/-", "confidence": 0.97, "page": 1, "provenance": "Clause 6"},
                {"key": "trailing_students", "label": "Existing Students", "value": "62 Students (4th & 5th Yr)", "confidence": 0.98, "page": 1, "provenance": "Clause 6"}
            ]),
            "bounding_boxes": json.dumps([
                {"x": 10, "y": 30, "width": 80, "height": 8, "label": "Progressive Closure of B.Arch", "page": 1},
                {"x": 10, "y": 60, "width": 80, "height": 8, "label": "Joint FDR: Rs. 50,00,000/- with AICTE", "page": 1}
            ]),
            "remarks": "Affidavit-4 for progressive closure verified. Joint FDR of ₹50 Lakhs intact.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth01-2",
            "application_id": "app-oth-01",
            "original_filename": "University_Closure_NOC_RTMNU.pdf",
            "mapped_type": "NOC from Affiliating University (Format-2)",
            "mapping_confidence": 0.97,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "NOC from Affiliating University (Format-2)", "score": 0.97}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 203)
FORMAT-2 (Clause ix - Closure of Programme)
RASHTRASANT TUKADOJI MAHARAJ NAGPUR UNIVERSITY (RTMNU), Nagpur.
No. RTMNU/AFF/2025/CL-889. Date: 14-02-2025.
No Objection Certificate granted for Progressive Closure of B.Arch Programme at Priyadarshini College of Engineering & Architecture.
Re-arrangement of existing 62 enrolled students confirmed till completion of degrees.
Registrar, RTMNU Nagpur.""",
            "extracted_fields": json.dumps([{"key": "closure_noc", "label": "University NOC", "value": "NOC FOR CLOSURE GRANTED", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "RTMNU Closure NOC Granted", "page": 1}]),
            "remarks": "University NOC for closure verified with student re-arrangement schedule.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth01-3",
            "application_id": "app-oth-01",
            "original_filename": "Trust_Resolution_Closure_LTJSS.pdf",
            "mapped_type": "Resolution of the Trust (Format-3)",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Resolution of the Trust (Format-3)", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 205)
FORMAT-3 (Resolution of Trust)
Lokmanya Tilak Jankalyan Shikshan Sanstha Executive Meeting dated 05-01-2025.
Resolution No. 12: Resolved to apply for progressive closure of B.Arch course due to rationalization of programmes and ensure completion of all academic requirements for enrolled students.""",
            "extracted_fields": json.dumps([{"key": "resolution", "label": "Trust Resolution", "value": "ADOPTED (Progressive Closure)", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 40, "width": 80, "height": 8, "label": "Trust Resolution for Closure", "page": 1}]),
            "remarks": "Trust resolution for closure verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth01-4",
            "application_id": "app-oth-01",
            "original_filename": "SBI_Joint_FDR_Receipt.pdf",
            "mapped_type": "Certificate of the Bank Manager (Certificate-3)",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Certificate of the Bank Manager (Certificate-3)", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """State Bank of India, Hingna Road Branch, Nagpur.
Certified that Joint FDR No. 492102 of Rs. 50,00,000/- created in joint names of Regional Officer AICTE Western Region and Secretary LTJSS is active and safe in our vault without lien or encumbrance.
Branch Manager, SBI Nagpur.""",
            "extracted_fields": json.dumps([{"key": "fdr", "label": "Joint FDR", "value": "Rs. 50,00,000/- (AICTE Joint Name)", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "AICTE Joint FDR: Rs. 50,00,000/-", "page": 1}]),
            "remarks": "AICTE Joint FDR ₹50 Lakhs verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth01-5",
            "application_id": "app-oth-01",
            "original_filename": "Nagpur_Fire_Safety_Certificate.pdf",
            "mapped_type": "Fire Safety Certificate",
            "mapping_confidence": 0.94,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Fire Safety Certificate", "score": 0.94}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """NAGPUR MUNICIPAL CORPORATION - FIRE DEPARTMENT
Fire Safety Compliance Certificate No. NMC/FIRE/2024/712. Valid till 31-12-2025.""",
            "extracted_fields": json.dumps([{"key": "validity", "label": "Validity", "value": "31-12-2025", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Valid till 31-12-2025", "page": 1}]),
            "remarks": "Fire safety certificate valid.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth01-6",
            "application_id": "app-oth-01",
            "original_filename": "TER_Receipt_Closure.pdf",
            "mapped_type": "TER / Payment Receipt",
            "mapping_confidence": 0.98,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "TER / Payment Receipt", "score": 0.98}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """AICTE PAYMENT RECEIPT
Transaction ID: AICTE2025CL0012
Amount: Rs. 75,000/-. Purpose: TER Charges for Closure of Course. Status: SUCCESSFUL.""",
            "extracted_fields": json.dumps([{"key": "ter", "label": "TER Fee", "value": "Rs. 75,000/-", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Rs. 75,000/- SUCCESS", "page": 1}]),
            "remarks": "TER fee receipt verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        }
    ]

    # -------------------------------------------------------------
    # APP-OTH-02: Symbiosis (Pune) - Collaboration & Twinning with Affidavit-11
    # -------------------------------------------------------------
    docs["app-oth-02"] = [
        {
            "id": "doc-oth02-1",
            "application_id": "app-oth-02",
            "original_filename": "Affidavit_11_Twinning_Symbiosis.pdf",
            "mapped_type": "Affidavit 11 (Foreign Collaboration / Twinning)",
            "mapping_confidence": 0.98,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Affidavit 11 (Foreign Collaboration / Twinning)", "score": 0.98}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 197)
AFFIDAVIT-11
(For Collaboration and Twinning Programme Between Foreign University / Institution and AICTE Approved Institution)

I/we, Dr. Vidya Yeravdekar, Executive Director, Symbiosis Society Pune, resident of Senapati Bapat Road, Pune, solemnly affirm:
1. Applied for Collaboration and Twinning Programme between Melbourne Institute of Technology (Australia) and Symbiosis Institute of Applied International Studies, Lavale, Pune vide AICTE-2025-OTH-0502 dated 12-03-2025.
2. Degree awarded to students in India shall be recognized in Australia and treated equivalent;
3. Institution shall admit students as per approved intake of 60 seats;
4. Students admitted under Twinning will spend 2 Semesters at foreign campus in Melbourne, Australia;
5. MoU executed to accommodate students who fail to get VISA in local affiliating institution to continue education without loss of academic year.

VERIFICATION
Verified at Pune on 12-03-2025. DEPONENT: Dr. Vidya Yeravdekar.""",
            "extracted_fields": json.dumps([
                {"key": "partner", "label": "Foreign Partner", "value": "Melbourne Institute of Technology (Australia)", "confidence": 0.99, "page": 1, "provenance": "Clause 1"},
                {"key": "visa_fallback", "label": "Visa Fallback MoU", "value": "Executed (Local Continuation)", "confidence": 0.98, "page": 1, "provenance": "Clause 5"}
            ]),
            "bounding_boxes": json.dumps([
                {"x": 10, "y": 30, "width": 80, "height": 8, "label": "Partner: Melbourne Institute of Tech", "page": 1},
                {"x": 10, "y": 60, "width": 80, "height": 8, "label": "Visa Fallback Accommodation MoU Executed", "page": 1}
            ]),
            "remarks": "Affidavit-11 for Twinning Programme verified with Australia degree equivalence and Visa fallback.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth02-2",
            "application_id": "app-oth-02",
            "original_filename": "MoU_Format_4_Foreign_Partner.pdf",
            "mapped_type": "MoU with Partner / SKP (Format-4)",
            "mapping_confidence": 0.97,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "MoU with Partner / SKP (Format-4)", "score": 0.97}]),
            "ocr_status": "COMPLETED",
            "page_count": 4,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 207-209)
FORMAT-4 (MoU Agreement)
MEMORANDUM OF UNDERSTANDING executed at New Delhi between Symbiosis Society Pune and Melbourne Institute of Technology Pty Ltd, Melbourne, Victoria, Australia.
Mutual credit recognition, tuition fee sharing (1st & 2nd year India, 3rd year Australia), and student welfare adherence under Ministry of External Affairs regulations.""",
            "extracted_fields": json.dumps([{"key": "mou", "label": "MoU Status", "value": "EXECUTED & BINDING", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "MoU Executed with Australian University", "page": 1}]),
            "remarks": "Format-4 MoU agreement verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth02-3",
            "application_id": "app-oth-02",
            "original_filename": "Trust_Resolution_Twinning.pdf",
            "mapped_type": "Resolution of the Trust (Format-3)",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Resolution of the Trust (Format-3)", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 205)
FORMAT-3 (Resolution of Trust)
Symbiosis Society Governing Body Meeting: Resolved to enter into collaboration with Melbourne Institute of Technology for 60 intake and establish International Student Welfare Office.""",
            "extracted_fields": json.dumps([{"key": "res", "label": "Resolution", "value": "APPROVED", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 40, "width": 80, "height": 8, "label": "Trust Resolution for Twinning", "page": 1}]),
            "remarks": "Resolution verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth02-4",
            "application_id": "app-oth-02",
            "original_filename": "Architect_Certificate_International_Hostel.pdf",
            "mapped_type": "Certificate of an Architect (Certificate-2)",
            "mapping_confidence": 0.95,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Certificate of an Architect (Certificate-2)", "score": 0.95}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """CERTIFICATE-2 (Architect Certificate)
Architect B. S. Joshi (CA/95/18204), Pune.
Certified that International standard residential accommodation and smart seminar suites of 8,200.00 Sq.M. have been created at Lavale Campus for Twinning students.""",
            "extracted_fields": json.dumps([{"key": "area", "label": "Hostel Area", "value": "8,200.00 Sq.M.", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "International Suites: 8,200 Sq.M.", "page": 1}]),
            "remarks": "Architect certified international hostel suites.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth02-5",
            "application_id": "app-oth-02",
            "original_filename": "Maharashtra_Fire_NOC_Lavale.pdf",
            "mapped_type": "Fire Safety Certificate",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Fire Safety Certificate", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """PMRDA FIRE SAFETY DEPARTMENT, Pune Metropolitan Region.
Certificate No. PMRDA/FIRE/2024/9912. Valid till 20-03-2027.
Fire safety measures for Lavale International Campus verified.""",
            "extracted_fields": json.dumps([{"key": "validity", "label": "Validity", "value": "20-03-2027", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Valid till 20-03-2027", "page": 1}]),
            "remarks": "Fire safety valid.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth02-6",
            "application_id": "app-oth-02",
            "original_filename": "PMRDA_Occupancy_Certificate.pdf",
            "mapped_type": "Occupancy Certificate",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Occupancy Certificate", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """PMRDA Occupancy Certificate No. PMRDA/OCC/2023/1120. Occupation granted for Educational Complex, 8,200.00 Sq.M.""",
            "extracted_fields": json.dumps([{"key": "occ", "label": "Occupancy", "value": "GRANTED", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "PMRDA Occupation Granted", "page": 1}]),
            "remarks": "PMRDA Occupancy verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth02-7",
            "application_id": "app-oth-02",
            "original_filename": "TER_Payment_Receipt_Twinning.pdf",
            "mapped_type": "TER / Payment Receipt",
            "mapping_confidence": 0.98,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "TER / Payment Receipt", "score": 0.98}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """AICTE PAYMENT RECEIPT: Transaction ID: AICTE2025TW0094. Amount: Rs. 3,00,000/-. Status: SUCCESSFUL.""",
            "extracted_fields": json.dumps([{"key": "ter", "label": "TER Fee", "value": "Rs. 3,00,000/-", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Rs. 3,00,000/- SUCCESS", "page": 1}]),
            "remarks": "TER receipt verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        }
    ]

    # -------------------------------------------------------------
    # APP-OTH-03: Aditya Institute (Tekkali) - Change in Bank Account Details (Affidavit-9)
    # -------------------------------------------------------------
    docs["app-oth-03"] = [
        {
            "id": "doc-oth03-1",
            "application_id": "app-oth-03",
            "original_filename": "Affidavit_9_Bank_Change_Aditya.pdf",
            "mapped_type": "Affidavit 9 (Change in Bank Details)",
            "mapping_confidence": 0.98,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Affidavit 9 (Change in Bank Details)", "score": 0.98}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 195)
AFFIDAVIT-9
(For change in the Bank details)

I/we, Prof. V. V. Nageswara Rao, Secretary, Sri Aditya Educational Society, Tekkali, Srikakulam District, Andhra Pradesh, do hereby solemnly affirm and declare:
1. That I/we have applied for change in the Name of the Bank of our Institution Aditya Institute of Technology & Management vide application AICTE-2025-OTH-0503 dated 13-03-2025.
2. Abiding by all terms and conditions laid down in Approval Process Handbook 2024-27;
3. That there is no commercial or business angle for change of Andhra Bank (Old Bank) to Union Bank of India (New Bank);
4. That the change in bank name is by virtue of amalgamation/merger of Andhra Bank into Union Bank of India under Government of India amalgamation scheme;
5. That there are no legal issues or financial liabilities pending with old bank.
DEPONENT: Prof. V. V. Nageswara Rao. Notary Tekkali, AP.""",
            "extracted_fields": json.dumps([
                {"key": "reason", "label": "Merger Clause", "value": "Amalgamation of Andhra Bank into Union Bank of India", "confidence": 0.99, "page": 1, "provenance": "Clause 4"}
            ]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Merger of Andhra Bank -> Union Bank", "page": 1}]),
            "remarks": "Affidavit-9 for nationalized bank amalgamation verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth03-2",
            "application_id": "app-oth-03",
            "original_filename": "Union_Bank_Manager_Certificate.pdf",
            "mapped_type": "Certificate of the Bank Manager (Certificate-3)",
            "mapping_confidence": 0.97,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Certificate of the Bank Manager (Certificate-3)", "score": 0.97}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 213)
CERTIFICATE-3 (Bank Manager Certificate)
Union Bank of India (Erstwhile Andhra Bank), Tekkali Branch, Srikakulam.
Certified that Account No. 04221110004921 belongs to Aditya Institute of Technology & Management. New IFSC: UBIN0804221. Operational balance: Rs. 1,84,30,000/-. All accounts smoothly migrated with zero liabilities.
Chief Manager, Union Bank of India.""",
            "extracted_fields": json.dumps([{"key": "ifsc", "label": "New IFSC", "value": "UBIN0804221", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "New IFSC: UBIN0804221", "page": 1}]),
            "remarks": "Union Bank certificate verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth03-3",
            "application_id": "app-oth-03",
            "original_filename": "Trust_Resolution_BankChange.pdf",
            "mapped_type": "Resolution of the Trust (Format-3)",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Resolution of the Trust (Format-3)", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """FORMAT-3 (Resolution of Trust)
Sri Aditya Educational Society Resolution No. 04/2025: Resolved to update AICTE web portal bank records to Union Bank of India following public sector bank amalgamation.""",
            "extracted_fields": json.dumps([{"key": "res", "label": "Resolution", "value": "PASSED", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Resolution for Bank Update", "page": 1}]),
            "remarks": "Resolution verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth03-4",
            "application_id": "app-oth-03",
            "original_filename": "AP_Fire_Safety_NOC_Tekkali.pdf",
            "mapped_type": "Fire Safety Certificate",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Fire Safety Certificate", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """GOVERNMENT OF ANDHRA PRADESH - STATE DISASTER RESPONSE & FIRE SERVICES
Rc.No. 882/MSB/SR/SKLM/2024. Valid for 5 years up to 10-01-2029 for Aditya Institute Campus, Tekkali.""",
            "extracted_fields": json.dumps([{"key": "validity", "label": "Validity", "value": "10-01-2029", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Valid up to 10-01-2029", "page": 1}]),
            "remarks": "Fire NOC valid.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth03-5",
            "application_id": "app-oth-03",
            "original_filename": "Tekkali_Panchayat_Occupancy.pdf",
            "mapped_type": "Occupancy Certificate",
            "mapping_confidence": 0.95,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Occupancy Certificate", "score": 0.95}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """GRAM PANCHAYAT TEKKALI / NAGAR PANCHAYAT
Occupancy Certificate for Aditya Institute of Technology & Management, 11,200.00 Sq.M.""",
            "extracted_fields": json.dumps([{"key": "occ", "label": "Occupancy", "value": "GRANTED", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Occupancy Granted", "page": 1}]),
            "remarks": "Occupancy verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth03-6",
            "application_id": "app-oth-03",
            "original_filename": "TER_Payment_Receipt_BankChange.pdf",
            "mapped_type": "TER / Payment Receipt",
            "mapping_confidence": 0.98,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "TER / Payment Receipt", "score": 0.98}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """AICTE PAYMENT RECEIPT: Transaction ID: AICTE2025BK0014. Amount: Rs. 50,000/-. Status: SUCCESSFUL.""",
            "extracted_fields": json.dumps([{"key": "fee", "label": "TER Fee", "value": "Rs. 50,000/-", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Rs. 50,000/- SUCCESS", "page": 1}]),
            "remarks": "TER receipt verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        }
    ]

    # -------------------------------------------------------------
    # APP-OTH-04: Dr. D.Y. Patil Institute (Pimpri, Pune) - Change of Trust Name (Affidavit-10)
    # -------------------------------------------------------------
    docs["app-oth-04"] = [
        {
            "id": "doc-oth04-1",
            "application_id": "app-oth-04",
            "original_filename": "Affidavit_10_Trust_Name_Change.pdf",
            "mapped_type": "Affidavit 10 (Change in Trust / Society Name)",
            "mapping_confidence": 0.98,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Affidavit 10 (Change in Trust / Society Name)", "score": 0.98}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 196)
AFFIDAVIT-10
(For Change in the Name / Address of the Trust / Society / Company)

I/we, Dr. Somnath P. Patil, Secretary, Dr. D.Y. Patil Educational Pratishthan, Pimpri, Pune, solemnly affirm:
1. Applied for change in Name of Trust of our Institution Dr. D.Y. Patil Institute of Engineering & Technology vide application AICTE-2025-OTH-0504 dated 14-03-2025.
2. From old name 'Dr. D.Y. Patil Pratishthan' to new name 'Dr. D.Y. Patil Educational Pratishthan';
3. There is no commercial or business angle for change of name;
4. No legal issues or financial liabilities pending in old trust name;
5. Land and Building measuring 14,500.00 Sq.M. mutated into the name of new trust;
DEPONENT: Dr. Somnath P. Patil. Notary Pimpri-Chinchwad.""",
            "extracted_fields": json.dumps([
                {"key": "trust_old", "label": "Old Trust Name", "value": "Dr. D.Y. Patil Pratishthan", "confidence": 0.99, "page": 1, "provenance": "Clause 2"},
                {"key": "trust_new", "label": "New Trust Name", "value": "Dr. D.Y. Patil Educational Pratishthan", "confidence": 0.99, "page": 1, "provenance": "Clause 2"}
            ]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 35, "width": 80, "height": 8, "label": "Old: Pratishthan -> New: Educational Pratishthan", "page": 1}]),
            "remarks": "Affidavit-10 for change of trust name verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth04-2",
            "application_id": "app-oth-04",
            "original_filename": "Charity_Commissioner_Certificate.pdf",
            "mapped_type": "Trust / Society Registration Certificate",
            "mapping_confidence": 0.97,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Trust / Society Registration Certificate", "score": 0.97}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """GOVERNMENT OF MAHARASHTRA - OFFICE OF CHARITY COMMISSIONER, PUNE DIVISION.
Certificate of Registration under Bombay Public Trusts Act, 1950.
Change Report No. 4410/2023 accepted. New Name: Dr. D.Y. Patil Educational Pratishthan (Reg. No. F-10924/Pune).
Joint Charity Commissioner, Pune.""",
            "extracted_fields": json.dumps([{"key": "reg", "label": "Registration", "value": "F-10924/Pune (Accepted)", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Charity Commissioner Change Report Accepted", "page": 1}]),
            "remarks": "Charity Commissioner registration verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth04-3",
            "application_id": "app-oth-04",
            "original_filename": "PCMC_Occupancy_Certificate.pdf",
            "mapped_type": "Occupancy Certificate",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Occupancy Certificate", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """PIMPRI CHINCHWAD MUNICIPAL CORPORATION (PCMC)
Occupancy Certificate for Sant Tukaram Nagar Campus, 14,500.00 Sq.M. Full Occupation Granted.
City Engineer, PCMC.""",
            "extracted_fields": json.dumps([{"key": "occ", "label": "Occupancy", "value": "GRANTED", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "PCMC Occupation Granted", "page": 1}]),
            "remarks": "PCMC Occupancy verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth04-4",
            "application_id": "app-oth-04",
            "original_filename": "Maharashtra_Fire_NOC_Pimpri.pdf",
            "mapped_type": "Fire Safety Certificate",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Fire Safety Certificate", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """PCMC FIRE SERVICES DEPARTMENT
Fire Safety NOC No. PCMC/FIRE/2024/1104. Valid up to 14-02-2027.""",
            "extracted_fields": json.dumps([{"key": "validity", "label": "Validity", "value": "14-02-2027", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Valid up to 14-02-2027", "page": 1}]),
            "remarks": "Fire safety valid.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth04-5",
            "application_id": "app-oth-04",
            "original_filename": "Architect_Certificate_LandTransfer.pdf",
            "mapped_type": "Certificate of an Architect (Certificate-2)",
            "mapping_confidence": 0.95,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Certificate of an Architect (Certificate-2)", "score": 0.95}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """CERTIFICATE-2 (Architect Certificate)
Architect Sunil Mane (CA/2005/32910), Pune.
Certified that all campus infrastructure measuring 14,500.00 Sq.M. is intact and verified under the updated trust name.""",
            "extracted_fields": json.dumps([{"key": "builtup", "label": "Area", "value": "14,500.00 Sq.M.", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Built-Up: 14,500.00 Sq.M.", "page": 1}]),
            "remarks": "Architect certificate verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth04-6",
            "application_id": "app-oth-04",
            "original_filename": "SPPU_Pune_University_Format2_NOC.pdf",
            "mapped_type": "NOC from Affiliating University (Format-2)",
            "mapping_confidence": 0.97,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "NOC from Affiliating University (Format-2)", "score": 0.97}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """FORMAT-2 (Affiliating University NOC)
SAVITRIBAI PHULE PUNE UNIVERSITY (SPPU), Pune.
Ref: SPPU/AFF/2025/1109. No objection for updating trust name in affiliation records to Dr. D.Y. Patil Educational Pratishthan.
Registrar, SPPU Pune.""",
            "extracted_fields": json.dumps([{"key": "univ_noc", "label": "University NOC", "value": "NO OBJECTION", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "SPPU No Objection for Trust Name Change", "page": 1}]),
            "remarks": "SPPU University NOC verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-oth04-7",
            "application_id": "app-oth-04",
            "original_filename": "TER_Payment_Receipt_NameChange.pdf",
            "mapped_type": "TER / Payment Receipt",
            "mapping_confidence": 0.99,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "TER / Payment Receipt", "score": 0.99}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """AICTE PAYMENT RECEIPT: Transaction ID: AICTE2025TR0089. Amount: Rs. 1,00,000/-. Status: SUCCESSFUL.""",
            "extracted_fields": json.dumps([{"key": "fee", "label": "TER Fee", "value": "Rs. 1,00,000/-", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Rs. 1,00,000/- SUCCESS", "page": 1}]),
            "remarks": "TER receipt verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        }
    ]

    # Additional Intake Increase applications
    # -------------------------------------------------------------
    # APP-II-02: Kumaraguru College of Technology (Coimbatore)
    # -------------------------------------------------------------
    docs["app-ii-02"] = [
        {
            "id": "doc-ii02-1",
            "application_id": "app-ii-02",
            "original_filename": "Affidavit_8_Intake_Kumaraguru.pdf",
            "mapped_type": "Affidavit 8 (Additional Course/Increase in Intake)",
            "mapping_confidence": 0.98,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Affidavit 8 (Additional Course/Increase in Intake)", "score": 0.98}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 194)
AFFIDAVIT-8
(For Additional Course / Increase in Intake)

I/we, Shankar Vanavarayar, Joint Correspondent, Ramanadha Adigalar Educational Trust, Coimbatore affirm:
1. Applied for increase in intake in Computer Science & Engineering (from 420 to 540 seats) vide AICTE-2025-ENG-0423 dated 14-03-2025.
2. Paid requisite TER charges of Rs. 2,00,000/-;
3. Created additional infrastructure of 1,450 Sq.M., equipped advanced coding laboratories, and appointed faculty as per 1:15 ratio.
4. Liabilities arising out of increase in intake shall be solely of the Trust.
DEPONENT: Shankar Vanavarayar. Notary Public Coimbatore.""",
            "extracted_fields": json.dumps([
                {"key": "intake_change", "label": "Intake Increase", "value": "420 -> 540 (CSE & IT)", "confidence": 0.99, "page": 1, "provenance": "Clause 1"},
                {"key": "additional_area", "label": "Additional Infrastructure", "value": "1,450.00 Sq.M.", "confidence": 0.98, "page": 1, "provenance": "Clause 3"}
            ]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 35, "width": 80, "height": 8, "label": "Intake Increase: 420 -> 540 (+120 Seats)", "page": 1}]),
            "remarks": "Affidavit-8 for 120 intake increase verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-ii02-2",
            "application_id": "app-ii-02",
            "original_filename": "Architect_Certificate_2_Surplus.pdf",
            "mapped_type": "Certificate of an Architect (Certificate-2)",
            "mapping_confidence": 0.97,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Certificate of an Architect (Certificate-2)", "score": 0.97}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 212)
CERTIFICATE-2 (Architect Certificate)
Architect R. Sundaram (CA/89/12490), Coimbatore.
Certified that total built-up area is 12,800.00 Sq.M. with surplus carpet area of 1,450.00 Sq.M. readily available to meet additional 120 student intake without deficit.""",
            "extracted_fields": json.dumps([{"key": "surplus", "label": "Surplus Area", "value": "1,450.00 Sq.M. Surplus", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Surplus Carpet Area: 1,450 Sq.M.", "page": 1}]),
            "remarks": "Architect certified surplus carpet area meeting APH Table 2.1 norms.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-ii02-3",
            "application_id": "app-ii-02",
            "original_filename": "Anna_Univ_Format2_IntakeIncrease.pdf",
            "mapped_type": "NOC from Affiliating University (Format-2)",
            "mapping_confidence": 0.98,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "NOC from Affiliating University (Format-2)", "score": 0.98}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """Approval Process Handbook 2024-2027 (Page 202)
FORMAT-2 (Affiliating University NOC)
ANNA UNIVERSITY, Chennai.
Ref: AU/AFF/2025/INC-889. No objection granted for increase in intake from 420 to 540 seats for Kumaraguru College of Technology.
Registrar, Anna University.""",
            "extracted_fields": json.dumps([{"key": "noc", "label": "University NOC", "value": "GRANTED (420 -> 540 Seats)", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Anna Univ NOC for Intake Increase", "page": 1}]),
            "remarks": "University NOC verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-ii02-4",
            "application_id": "app-ii-02",
            "original_filename": "Trust_Resolution_Format3_Intake.pdf",
            "mapped_type": "Resolution of the Trust (Format-3)",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Resolution of the Trust (Format-3)", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """FORMAT-3 (Resolution of Trust)
Ramanadha Adigalar Educational Trust Meeting: Resolved to increase CSE intake to 540 and allocated Rs. 2.0 Crores for computing infrastructure.""",
            "extracted_fields": json.dumps([{"key": "res", "label": "Resolution", "value": "PASSED", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 40, "width": 80, "height": 8, "label": "Trust Resolution for Intake Increase", "page": 1}]),
            "remarks": "Trust resolution verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-ii02-5",
            "application_id": "app-ii-02",
            "original_filename": "TamilNadu_Fire_NOC_KCT.pdf",
            "mapped_type": "Fire Safety Certificate",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Fire Safety Certificate", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 2,
            "document_body_text": """TN FIRE AND RESCUE SERVICES - COIMBATORE. Certificate No. 119/2024. Valid till 15-02-2027.""",
            "extracted_fields": json.dumps([{"key": "validity", "label": "Validity", "value": "15-02-2027", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Valid till 15-02-2027", "page": 1}]),
            "remarks": "Fire safety valid.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-ii02-6",
            "application_id": "app-ii-02",
            "original_filename": "Corporation_Occupancy_KCT.pdf",
            "mapped_type": "Occupancy Certificate",
            "mapping_confidence": 0.96,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Occupancy Certificate", "score": 0.96}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """Coimbatore Municipal Corporation Occupancy Certificate: Full Occupation Granted for 12,800.00 Sq.M.""",
            "extracted_fields": json.dumps([{"key": "occ", "label": "Occupancy", "value": "GRANTED", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Occupancy Granted", "page": 1}]),
            "remarks": "Occupancy verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-ii02-7",
            "application_id": "app-ii-02",
            "original_filename": "Canara_Bank_Certificate_KCT.pdf",
            "mapped_type": "Certificate of the Bank Manager (Certificate-3)",
            "mapping_confidence": 0.95,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "Certificate of the Bank Manager (Certificate-3)", "score": 0.95}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """Canara Bank, Chinnavedampatti Branch. Certified operational balance of Rs. 2,80,00,000/- without lien.""",
            "extracted_fields": json.dumps([{"key": "balance", "label": "Balance", "value": "Rs. 2,80,00,000/-", "confidence": 0.98, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Balance: Rs. 2,80,00,000/-", "page": 1}]),
            "remarks": "Bank certificate verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        },
        {
            "id": "doc-ii02-8",
            "application_id": "app-ii-02",
            "original_filename": "TER_Payment_Receipt_Intake.pdf",
            "mapped_type": "TER / Payment Receipt",
            "mapping_confidence": 0.99,
            "mapping_stage": "Content Confirmation (OCR)",
            "candidate_types": json.dumps([{"type": "TER / Payment Receipt", "score": 0.99}]),
            "ocr_status": "COMPLETED",
            "page_count": 1,
            "document_body_text": """AICTE PAYMENT RECEIPT: Transaction ID: AICTE2025IN88124. Amount: Rs. 2,00,000/-. Status: SUCCESSFUL.""",
            "extracted_fields": json.dumps([{"key": "fee", "label": "TER Fee", "value": "Rs. 2,00,000/-", "confidence": 0.99, "page": 1, "provenance": "Body"}]),
            "bounding_boxes": json.dumps([{"x": 10, "y": 45, "width": 80, "height": 8, "label": "Rs. 2,00,000/- SUCCESS", "page": 1}]),
            "remarks": "TER receipt verified.",
            "is_mandatory": True,
            "upload_status": "Uploaded",
            "document_status": "Reviewed"
        }
    ]

    return docs
