import re
from typing import Dict, Any, List, Tuple
from models import DocumentItem, DocumentMappingHistory, ExtractedField, BoundingBox

ALIAS_DICTIONARY = {
    "Affidavit 2 (Self-Disclosure)": [
        r"affidavit.*2", r"affidavit.*format.*2", r"self.*disclosure", r"affidavit.*eoa", r"affidavit.*trust"
    ],
    "Fire Safety Certificate": [
        r"fire.*safety", r"fire.*noc", r"fire.*clearance", r"fes.*cert", r"k-fes"
    ],
    "TER / Payment Receipt": [
        r"ter.*receipt", r"payment.*receipt", r"fee.*receipt", r"aicte.*fee", r"transaction.*slip"
    ],
    "Occupancy Certificate": [
        r"occupancy", r"completion.*cert", r"building.*licence", r"form.*d", r"bbmp.*oc"
    ],
    "Structural Stability Certificate": [
        r"structural.*stability", r"stability.*cert", r"chartered.*engineer.*cert", r"fitness.*cert"
    ],
    "Satellite / Geolocation Map": [
        r"satellite.*map", r"google.*earth", r"geolocation", r"survey.*map", r"coordinates.*map"
    ],
    "Audited Financial Statement": [
        r"audited.*statement", r"balance.*sheet", r"financial.*statement", r"audit.*report", r"ca.*audited"
    ]
}

KEYWORDS_MAP = {
    "Affidavit 2 (Self-Disclosure)": ["AFFIDAVIT", "NON-JUDICIAL", "DEPONENT", "SWORN", "NOTARY", "AICTE"],
    "Fire Safety Certificate": ["FIRE", "EMERGENCY SERVICES", "NOC", "PREVENTION", "EXTINGUISHER", "HYDRANT"],
    "TER / Payment Receipt": ["PAYMENT RECEIPT", "TRANSACTION ID", "UTR", "SETTLED", "PROCESSING FEE", "AICTE"],
    "Occupancy Certificate": ["OCCUPANCY", "SANCTIONED PLAN", "BUILT UP AREA", "MUNICIPAL", "CORPORATION"],
    "Structural Stability Certificate": ["STRUCTURAL", "SOUNDNESS", "CHARTERED ENGINEER", "FITNESS", "SEISMIC"],
    "Satellite / Geolocation Map": ["LATITUDE", "LONGITUDE", "COORDINATES", "SATELLITE", "ENTRANCE", "SURVEY"],
    "Audited Financial Statement": ["BALANCE SHEET", "INCOME AND EXPENDITURE", "CHARTERED ACCOUNTANT", "UDIN", "AUDITOR"]
}

def clean_filename(filename: str) -> str:
    cleaned = filename.lower()
    cleaned = re.sub(r"[_\-\.]+", " ", cleaned)
    return cleaned

def map_document_filename(filename: str) -> Tuple[str, float, List[Dict[str, Any]]]:
    """Stage 1: Normalized filename alias pattern matching"""
    candidates = []
    cleaned = clean_filename(filename)

    for doc_type, patterns in ALIAS_DICTIONARY.items():
        score = 0.0
        for pattern in patterns:
            if re.search(pattern, cleaned):
                score = max(score, 0.90)
                break
        if score > 0:
            candidates.append({"type": doc_type, "score": score})

    candidates.sort(key=lambda x: x["score"], reverse=True)

    if candidates:
        best = candidates[0]
        return best["type"], best["score"], candidates
    return "Unmapped / Manual review", 0.30, []

def confirm_with_content(doc_type_candidate: str, ocr_text: str, filename_score: float) -> Tuple[str, float, str]:
    """Stage 2 & 3: Content verification with OCR text and confidence workflow"""
    if not ocr_text:
        return doc_type_candidate, filename_score, "Filename & Alias"

    ocr_upper = ocr_text.upper()
    best_type = doc_type_candidate
    best_score = filename_score

    # Check keyword density
    expected_keywords = KEYWORDS_MAP.get(doc_type_candidate, [])
    matches = sum(1 for kw in expected_keywords if kw in ocr_upper)
    ratio = matches / max(len(expected_keywords), 1)

    if ratio >= 0.5:
        # Boost confidence
        best_score = min(0.99, filename_score + 0.08)
        stage = "Content Confirmation (OCR)"
    elif ratio > 0.2:
        best_score = max(0.75, filename_score)
        stage = "Content Probing"
    else:
        best_score = 0.65
        stage = "Low Confidence / Needs Review"

    return best_type, round(best_score, 2), stage
