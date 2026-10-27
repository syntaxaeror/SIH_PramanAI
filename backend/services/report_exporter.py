import io
import datetime
from typing import Dict, Any, List
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle

def generate_scrutiny_pdf(application: Dict[str, Any],
                          documents: List[Dict[str, Any]],
                          findings: List[Dict[str, Any]],
                          evc_items: List[Dict[str, Any]]) -> bytes:
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(
        buffer,
        pagesize=letter,
        rightMargin=36,
        leftMargin=36,
        topMargin=36,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontSize=18,
        leading=22,
        textColor=colors.HexColor('#1e3a8a'),
        alignment=1
    )
    subtitle_style = ParagraphStyle(
        'DocSubTitle',
        parent=styles['Normal'],
        fontSize=11,
        leading=14,
        textColor=colors.HexColor('#475569'),
        alignment=1
    )
    disclaimer_style = ParagraphStyle(
        'Disclaimer',
        parent=styles['Normal'],
        fontSize=8.5,
        leading=11,
        textColor=colors.HexColor('#991b1b'),
        backColor=colors.HexColor('#fef2f2'),
        borderColor=colors.HexColor('#f87171'),
        borderWidth=1,
        borderPadding=6,
        spaceAfter=12
    )
    section_style = ParagraphStyle(
        'SectionHeader',
        parent=styles['Heading2'],
        fontSize=13,
        leading=16,
        textColor=colors.HexColor('#0f172a'),
        spaceBefore=12,
        spaceAfter=6
    )
    body_style = ParagraphStyle(
        'Body',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#1e293b')
    )
    bold_style = ParagraphStyle(
        'BoldBody',
        parent=styles['Normal'],
        fontSize=9,
        leading=12,
        textColor=colors.HexColor('#0f172a'),
        fontName='Helvetica-Bold'
    )

    story = []

    # Title & Header
    story.append(Paragraph("ALL INDIA COUNCIL FOR TECHNICAL EDUCATION (AICTE)", title_style))
    story.append(Paragraph("<b>AI-ASSISTED APPLICATION SCRUTINY & EVC REVIEW SUMMARY REPORT</b>", subtitle_style))
    story.append(Paragraph(f"Generated on {datetime.datetime.now().strftime('%d-%b-%Y %H:%M:%S')} | Scrutiny Cycle AY 2025-26", subtitle_style))
    story.append(Spacer(1, 10))

    # Mandatory Legal Non-Statutory Disclaimer
    disclaimer_text = (
        "<b>STATUTORY NOTICE & LEGAL DISCLAIMER:</b> This document is an AI-assisted evidence synthesis report "
        "prepared strictly to assist authorized scrutiny committee reviewers and EVC inspectors. "
        "This platform does <b>NOT</b> issue statutory approval, grant approval, or reject any application. "
        "All final regulatory and statutory decisions rest exclusively with the Competent Authority "
        "under the All India Council for Technical Education Act, 1987 and applicable regulations."
    )
    story.append(Paragraph(disclaimer_text, disclaimer_style))
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor('#cbd5e1'), spaceAfter=10))

    # Institutional Metadata
    story.append(Paragraph("1. Institutional & Application Overview", section_style))
    overview_data = [
        [Paragraph("<b>Application ID:</b>", body_style), Paragraph(application.get("application_number", "N/A"), bold_style),
         Paragraph("<b>Academic Year:</b>", body_style), Paragraph(application.get("academic_year", "2025-26"), body_style)],
        [Paragraph("<b>Institution Name:</b>", body_style), Paragraph(application.get("institution_name", "N/A"), bold_style),
         Paragraph("<b>Permanent ID:</b>", body_style), Paragraph(application.get("institution_id", "N/A"), body_style)],
        [Paragraph("<b>Application Category:</b>", body_style), Paragraph(application.get("category", "N/A"), body_style),
         Paragraph("<b>Current Priority:</b>", body_style), Paragraph(f"<b>{application.get('priority', 'N/A')}</b>", bold_style)],
        [Paragraph("<b>Sponsoring Trust:</b>", body_style), Paragraph(application.get("trust_name", "N/A"), body_style),
         Paragraph("<b>Assigned Reviewer:</b>", body_style), Paragraph(application.get("assigned_reviewer", "N/A"), body_style)],
        [Paragraph("<b>Declared Campus:</b>", body_style), Paragraph(application.get("institution_address", "N/A"), body_style),
         Paragraph("<b>Compliance Index:</b>", body_style), Paragraph(f"{application.get('compliance_score', 0)}% (Scrutiny Ready)", bold_style)]
    ]
    t_overview = Table(overview_data, colWidths=[100, 170, 100, 170])
    t_overview.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor('#f8fafc')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#e2e8f0')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_overview)
    story.append(Spacer(1, 10))

    # Key Scrutiny Findings & Deficiencies (with Explainability)
    story.append(Paragraph("2. Scrutiny Findings & Deficiencies (With Explainable Evidence)", section_style))
    findings_data = [
        [Paragraph("<b>Rule & Clause</b>", bold_style),
         Paragraph("<b>Finding Title & Classification</b>", bold_style),
         Paragraph("<b>Validation / Status</b>", bold_style),
         Paragraph("<b>Why? Model Evidence & Source Provenance</b>", bold_style)]
    ]
    for f in findings:
        status_color = "#dc2626" if f.get("validation_status") == "DEFICIENCY" else "#16a34a"
        findings_data.append([
            Paragraph(f"<b>{f.get('rule_id')}</b><br/>{f.get('rule_clause')}", body_style),
            Paragraph(f"<b>{f.get('title')}</b><br/><font color='#64748b'>{f.get('explanation')}</font>", body_style),
            Paragraph(f"<font color='{status_color}'><b>{f.get('validation_status')}</b></font><br/>Priority: {f.get('priority')}", body_style),
            Paragraph(f"<b>Evidence:</b> {f.get('why_evidence')}<br/><b>Disposition:</b> {f.get('disposition', 'PENDING')}", body_style)
        ])

    t_findings = Table(findings_data, colWidths=[110, 150, 90, 190])
    t_findings.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_findings)
    story.append(Spacer(1, 10))

    # EVC Evidence Integrity & Duplicate Signals
    story.append(Paragraph("3. EVC Evidence Room Summary (Perceptual Hash & Geo-Tag Signals)", section_style))
    evc_data = [
        [Paragraph("<b>Category</b>", bold_style),
         Paragraph("<b>File / Media</b>", bold_style),
         Paragraph("<b>pHash / Integrity Status</b>", bold_style),
         Paragraph("<b>Geo Distance / Inspection Flag</b>", bold_style)]
    ]
    for evc in evc_items:
        dup_text = f"<font color='#dc2626'><b>DUPLICATE SUSPECTED</b></font><br/>{evc.get('duplicate_explanation', '')}" if evc.get("duplicate_flag") else "<font color='#16a34a'>UNIQUE</font>"
        inspect_text = f"<b>FLAGGED ON-SITE</b>: {evc.get('inspection_reason')}" if evc.get("inspection_needed") else "Standard Verification"
        evc_data.append([
            Paragraph(evc.get("category", "General"), body_style),
            Paragraph(f"{evc.get('filename')}<br/><font color='#64748b'>{evc.get('file_type').upper()}</font>", body_style),
            Paragraph(dup_text, body_style),
            Paragraph(f"GPS Status: {evc.get('gps_match_status')}<br/>{inspect_text}", body_style)
        ])

    t_evc = Table(evc_data, colWidths=[100, 130, 160, 150])
    t_evc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#e2e8f0')),
        ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#cbd5e1')),
        ('INNERGRID', (0,0), (-1,-1), 0.5, colors.HexColor('#e2e8f0')),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_evc)
    story.append(Spacer(1, 15))

    # Sign-off Blocks for Scrutiny Committee
    story.append(Paragraph("4. Committee Signatures & Review Dispositions", section_style))
    sign_data = [
        [Paragraph("<b>Scrutiny Reviewer:</b>", body_style), Paragraph("<b>EVC Chairman / Member:</b>", body_style), Paragraph("<b>Competent Authority:</b>", body_style)],
        [Paragraph("<br/><br/>______________________<br/>Prof. S. R. Sharma<br/>Senior Scrutiny Officer", body_style),
         Paragraph("<br/><br/>______________________<br/>Dr. M. K. Ananth<br/>EVC Committee Member", body_style),
         Paragraph("<br/><br/>______________________<br/>Authorized Officer<br/>AICTE Approvals Bureau", body_style)]
    ]
    t_sign = Table(sign_data, colWidths=[180, 180, 180])
    t_sign.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor('#cbd5e1')),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_sign)

    doc.build(story)
    pdf_bytes = buffer.getvalue()
    buffer.close()
    return pdf_bytes
