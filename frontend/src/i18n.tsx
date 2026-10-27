import React, { createContext, useContext, useState, useEffect } from 'react';

export type Language = 'en' | 'hi';

interface I18nContextType {
  language: Language;
  setLanguage: (lang: Language) => void;
  t: (key: string) => string;
}

const translations: Record<Language, Record<string, string>> = {
  en: {
    // Portal Header & Branding
    "portal.title": "Application Scrutiny Portal",
    "portal.subtitle": "AI-Assisted Verification System",
    "portal.academic_cycle": "Academic Cycle",
    "portal.ay": "AY 2025–26",
    "portal.review_context": "Review Context",
    "portal.officer_role": "Officer Role:",
    "portal.role.scrutiny": "Scrutiny Officer",
    "portal.role.evc": "EVC Officer",
    "portal.role.admin": "Administrator",
    "portal.role.auditor": "Auditor (Read-only)",
    "portal.language": "Language:",
    "portal.sign_out": "Sign Out",

    // Sidebar & Navigation
    "nav.portal": "Portal",
    "nav.workspace": "Workspace",
    "nav.records": "Records",
    "nav.dashboard": "Dashboard",
    "nav.applications": "Applications",
    "nav.history": "Application History",
    "nav.audit": "Audit Logs",
    "nav.admin_users": "Users & Roles",
    "nav.admin_checklists": "Checklist Setup",
    "nav.admin_rules": "Rules & Regulations",
    "nav.admin_settings": "System Settings",

    // Workflow Stepper
    "step.checklist": "1. Checklist",
    "step.verification": "2. Verification",
    "step.evc": "3. EVC Evidence",
    "step.summary": "4. Final Summary",

    // Categories
    "cat.ALL": "All Categories",
    "cat.New Technical Institution": "New Technical Institution",
    "cat.Extension of Approval (EoA)": "Extension of Approval (EoA)",
    "cat.New Programme / Level": "New Programme / Level",
    "cat.Intake Increase": "Intake Increase",
    "cat.Other Application Types": "Other Application Types",

    // Priorities
    "priority.RED": "RED (High Risk)",
    "priority.AMBER": "AMBER (Medium Risk)",
    "priority.GREEN": "GREEN (Compliant)",

    // Statuses
    "status.UNDER_SCRUTINY": "Under Scrutiny",
    "status.DEFICIENCY_FLAGGED": "Deficiency Flagged",
    "status.SCRUTINY_COMPLETED": "Scrutiny Completed",
    "status.IN_REVIEW": "In Review",
    "status.SCRUTINY_IN_PROGRESS": "In Review",

    // Dashboard View
    "dash.title": "Applications Scrutiny Dashboard",
    "dash.subtitle": "High-level overview of application processing and statutory compliance for academic cycle",
    "dash.total_applications": "Total Applications",
    "dash.under_scrutiny": "Pending Scrutiny",
    "dash.in_review": "In Review",
    "dash.under_active_check": "Under Active Check",
    "dash.deficiencies": "Deficiencies",
    "dash.letters_required": "Letters Required",
    "dash.evc_review_req": "EVC Review Req.",
    "dash.physical_photo_check": "Physical / Photo Check",
    "dash.reevaluations": "Re-evaluations",
    "dash.cycle2_requested": "Cycle 2 Requested",
    "dash.database_records": "Database Records",
    "dash.queue_backlog": "Queue Backlog",
    "dash.categories_title": "Application Categories & Scrutiny Backlog",
    "dash.categories_configured": "5 Categories Configured",
    "dash.col_category": "Application Category",
    "dash.col_total": "Total Applications",
    "dash.col_pending": "Pending Scrutiny",
    "dash.col_in_review": "In Review",
    "dash.col_action_required": "Action Required",
    "dash.col_action": "Action",
    "dash.view": "View",
    "dash.priority_cases": "Priority Scrutiny Cases (Triage Queue)",
    "dash.sorted_risk_date": "Sorted by Risk & Date",
    "dash.recent_actions": "Recent Scrutiny Actions & Lifecycle Events",
    "dash.live_audit": "Live Audit Stream",
    "dash.docs_mapped": "Docs Mapped",
    "dash.compliant": "Compliant",

    // Applications List View
    "apps.title": "All Imported Applications",
    "apps.subtitle": "Review imported institutional applications, supporting documents, and scrutiny verification progress.",
    "apps.showing_records": "matching records",
    "apps.search_placeholder": "Search by application number, institute name, or trust...",
    "apps.filter_category": "Filter by Category:",
    "apps.filter_priority": "Priority:",
    "apps.filter_status": "Status:",
    "apps.clear_filters": "Clear Filters",
    "apps.open_application": "Open Application",
    "apps.col_app_details": "Application & Institution Details",
    "apps.col_category_cycle": "Category & Academic Cycle",
    "apps.col_priority": "Priority",
    "apps.col_status": "Scrutiny Status",
    "apps.col_deficiencies": "Deficiencies",
    "apps.col_compliance": "Compliance Score",
    "apps.col_actions": "Action",

    // Checklist View
    "checklist.title": "Document Checklist & Applicability Norms",
    "checklist.subtitle": "Configured regulatory document requirements for",
    "checklist.generate_letter": "Generate Deficiency Letter",
    "checklist.total_expected": "Total Expected",
    "checklist.uploaded_files": "Uploaded Files",
    "checklist.not_uploaded": "Not Uploaded",
    "checklist.pending_review": "Pending Review",
    "checklist.reviewed": "Reviewed",
    "checklist.needs_attention": "Deficiencies",
    "checklist.col.number": "No.",
    "checklist.col.type": "Canonical Document Type",
    "checklist.col.applicability": "Applicability",
    "checklist.col.upload_status": "Upload Status",
    "checklist.col.original": "Uploaded Original File",
    "checklist.col.confidence": "Auto-Mapping",
    "checklist.col.status": "Document Status",
    "checklist.col.action": "Action",
    "checklist.mandatory": "Mandatory",
    "checklist.conditional": "Conditional",
    "checklist.mandatory_aph": "Mandatory under APH Appendix 16",
    "checklist.pages": "Pages",
    "checklist.stage": "Stage",
    "checklist.file_not_found": "File not found in uploaded batch package",
    "checklist.inspect": "Inspect",
    "checklist.add_deficiency": "Add to Deficiency",
    "checklist.verified_compliant": "Verified Compliant",
    "checklist.deficiency_flagged": "Deficiency Flagged",

    // Verification View
    "verify.title": "Document Scrutiny & Rule Verification",
    "verify.live_engine": "Live Engine Active",
    "verify.subtitle": "Cross-examine uploaded original documents against extracted OCR entities, APH regulations, and engine findings.",
    "verify.run_engine": "Run Live Rule Engine",
    "verify.running_engine": "Evaluating Rules...",
    "verify.mark_reviewed": "Mark Document Reviewed",
    "verify.select_doc": "Select Document:",
    "verify.review_flags": "Review Flags & Deficiencies",
    "verify.no_deficiencies": "No Deficiencies Found for this Document",
    "verify.no_deficiencies_desc": "All evaluated statutory clauses comply with AICTE Approval Process Handbook standards.",
    "verify.why_flagged": "Why Flagged (Engine Reasoning & Evidence):",
    "verify.statutory_clause": "Statutory Clause:",
    "verify.disposition": "Reviewer Disposition:",
    "verify.upheld": "Upheld Deficiency",
    "verify.dismiss": "Dismiss Flag",
    "verify.extracted_entities": "Extracted Entities (AI OCR Extraction)",
    "verify.page_nav": "Page Navigation:",
    "verify.download_verified": "Download Verified File",

    // EVC View
    "evc.title": "EVC Physical Evidence & Media Room",
    "evc.subtitle": "Photographic, video walkthrough, and cross-institutional perceptual hash (pHash) verification for",
    "evc.complete_review": "Complete EVC Review",
    "evc.finalized": "EVC Review Finalized",
    "evc.total_evidence": "Evidence Uploads",
    "evc.duplicate_signals": "Duplicate Signals",
    "evc.coverage_metric": "11-Area Coverage",
    "evc.areas_met": "Required Areas Met",
    "evc.physical_insp": "Physical Inspection",
    "evc.checklist_title": "Official AICTE Physical & Video Evidence Coverage Checklist",
    "evc.areas_verified": "Areas Verified",
    "evc.search_placeholder": "Search by category, media filename, or matched institute...",
    "evc.show_duplicates": "Show Duplicates Only",
    "evc.list_view": "List View",
    "evc.grid_view": "Grid View",
    "evc.duplicate_detected": "DUPLICATE MATCH DETECTED",
    "evc.matched_institute": "Matched Institute:",
    "evc.original_hash": "Original / Unique Hash",
    "evc.flag_on_site": "Flag On-Site",
    "evc.on_site_flagged": "On-Site Flagged",
    "evc.examine": "Examine",

    // Final Summary View
    "summary.title": "Final Scrutiny Summary & Recommendation",
    "summary.subtitle": "Comprehensive evaluation of application documents, physical inspection evidence, and statutory norms for",
    "summary.download_pdf": "Download Official PDF Report",
    "summary.mark_scrutinized": "Mark Scrutinized & Sign Off",
    "summary.request_reeval": "Request Re-evaluation",
    "summary.view_history": "View History & Audit Trail",
    "summary.recommendation": "Executive Scrutiny Recommendation",
    "summary.findings_overview": "Evaluated Findings Breakdown",
    "summary.checklist_overview": "Document Package Completeness",
    "summary.evc_overview": "Physical Evidence & Integrity Check",

    // General / Common
    "common.app_number": "Application No",
    "common.institute": "Institution",
    "common.category": "Category",
    "common.status": "Status",
    "common.priority": "Priority",
    "common.score": "Compliance Score",
    "common.actions": "Actions",
    "common.cycle": "Cycle",
    "common.inspect": "Inspect",
    "common.view": "View",
    "common.compliant": "Compliant",
    "common.deficiencies": "Deficiencies"
  },
  hi: {
    // Portal Header & Branding
    "portal.title": "आवेदन संवीक्षा पोर्टल",
    "portal.subtitle": "एआई-सहायित सत्यापन एवं जांच प्रणाली",
    "portal.academic_cycle": "शैक्षणिक सत्र",
    "portal.ay": "सत्र 2025–26",
    "portal.review_context": "समीक्षा संदर्भ",
    "portal.officer_role": "अधिकारी भूमिका:",
    "portal.role.scrutiny": "संवीक्षा अधिकारी",
    "portal.role.evc": "ई.वी.सी. अधिकारी",
    "portal.role.admin": "प्रशासक",
    "portal.role.auditor": "लेखा परीक्षक",
    "portal.language": "भाषा:",
    "portal.sign_out": "लॉग आउट",

    // Sidebar & Navigation
    "nav.portal": "पोर्टल",
    "nav.workspace": "कार्यक्षेत्र",
    "nav.records": "अभिलेख",
    "nav.dashboard": "डैशबोर्ड",
    "nav.applications": "आवेदन सूची",
    "nav.history": "आवेदन इतिहास",
    "nav.audit": "ऑडिट लॉग",
    "nav.admin_users": "उपयोगकर्ता एवं भूमिकाएं",
    "nav.admin_checklists": "चेकलिस्ट विन्यास",
    "nav.admin_rules": "नियम एवं विनियम",
    "nav.admin_settings": "सिस्टम सेटिंग्स",

    // Workflow Stepper
    "step.checklist": "1. चेकलिस्ट",
    "step.verification": "2. सत्यापन",
    "step.evc": "3. ई.वी.सी. साक्ष्य",
    "step.summary": "4. अंतिम सारांश",

    // Categories
    "cat.ALL": "सभी श्रेणियां",
    "cat.New Technical Institution": "नवीन तकनीकी संस्थान",
    "cat.Extension of Approval (EoA)": "अनुमोदन विस्तार (EoA)",
    "cat.New Programme / Level": "नवीन कार्यक्रम / स्तर",
    "cat.Intake Increase": "प्रवेश क्षमता में वृद्धि",
    "cat.Other Application Types": "अन्य आवेदन प्रकार",

    // Priorities
    "priority.RED": "उच्च जोखिम (लाल)",
    "priority.AMBER": "मध्यम जोखिम (अंबर)",
    "priority.GREEN": "अनुपालित (हरा)",

    // Statuses
    "status.UNDER_SCRUTINY": "संवीक्षाधीन",
    "status.DEFICIENCY_FLAGGED": "कमी पाई गई",
    "status.SCRUTINY_COMPLETED": "संवीक्षा पूर्ण",
    "status.IN_REVIEW": "समीक्षा जारी",
    "status.SCRUTINY_IN_PROGRESS": "समीक्षा प्रगति पर",

    // Dashboard View
    "dash.title": "आवेदन संवीक्षा डैशबोर्ड",
    "dash.subtitle": "शैक्षणिक सत्र हेतु आवेदन प्रसंस्करण एवं वैधानिक अनुपालन का समग्र अवलोकन",
    "dash.total_applications": "कुल आवेदन",
    "dash.under_scrutiny": "संवीक्षा लंबित",
    "dash.in_review": "समीक्षा जारी",
    "dash.under_active_check": "सक्रिय जांच में",
    "dash.deficiencies": "कमियां पाई गईं",
    "dash.letters_required": "कमी पत्र अपेक्षित",
    "dash.evc_review_req": "ई.वी.सी. समीक्षा अपेक्षित",
    "dash.physical_photo_check": "भौतिक / फ़ोटो जांच",
    "dash.reevaluations": "पुनर्मूल्यांकन",
    "dash.cycle2_requested": "चक्र 2 अनुरोधित",
    "dash.database_records": "डेटाबेस रिकॉर्ड्स",
    "dash.queue_backlog": "प्रतीक्षारत कतार",
    "dash.categories_title": "आवेदन श्रेणियां एवं संवीक्षा बैकलॉग",
    "dash.categories_configured": "5 श्रेणियां विन्यासित",
    "dash.col_category": "आवेदन श्रेणी",
    "dash.col_total": "कुल आवेदन",
    "dash.col_pending": "संवीक्षा लंबित",
    "dash.col_in_review": "समीक्षा जारी",
    "dash.col_action_required": "कार्रवाई आवश्यक",
    "dash.col_action": "कार्रवाई",
    "dash.view": "देखें",
    "dash.priority_cases": "उच्च प्राथमिकता संवीक्षा मामले (प्राथमिकता कतार)",
    "dash.sorted_risk_date": "जोखिम एवं दिनांक अनुसार क्रमबद्ध",
    "dash.recent_actions": "हालिया संवीक्षा कार्रवाइयां एवं जीवनचक्र घटनाएं",
    "dash.live_audit": "लाइव ऑडिट स्ट्रीम",
    "dash.docs_mapped": "दस्तावेज़ संबद्ध",
    "dash.compliant": "अनुपालित",

    // Applications List View
    "apps.title": "सभी आयातित आवेदन",
    "apps.subtitle": "आयातित संस्थागत आवेदन, सहायक दस्तावेज़ एवं संवीक्षा सत्यापन प्रगति की समीक्षा करें।",
    "apps.showing_records": "मिलते-जुलते रिकॉर्ड्स",
    "apps.search_placeholder": "आवेदन संख्या, संस्थान का नाम अथवा ट्रस्ट द्वारा खोजें...",
    "apps.filter_category": "श्रेणी अनुसार फ़िल्टर:",
    "apps.filter_priority": "प्राथमिकता अनुसार:",
    "apps.filter_status": "स्थिति अनुसार:",
    "apps.clear_filters": "फ़िल्टर हटाएं",
    "apps.open_application": "आवेदन खोलें",
    "apps.col_app_details": "आवेदन एवं संस्थान का विवरण",
    "apps.col_category_cycle": "श्रेणी एवं शैक्षणिक सत्र",
    "apps.col_priority": "प्राथमिकता",
    "apps.col_status": "संवीक्षा स्थिति",
    "apps.col_deficiencies": "कमियां",
    "apps.col_compliance": "अनुपालन अंक",
    "apps.col_actions": "कार्रवाई",

    // Checklist View
    "checklist.title": "दस्तावेज़ चेकलिस्ट एवं विनियामक मानक",
    "checklist.subtitle": "के लिए निर्धारित विनियामक दस्तावेज़ आवश्यकताएँ",
    "checklist.generate_letter": "कमी पत्र (Deficiency Letter) तैयार करें",
    "checklist.total_expected": "कुल अपेक्षित दस्तावेज़",
    "checklist.uploaded_files": "अपलोड की गई फ़ाइलें",
    "checklist.not_uploaded": "अपलोड नहीं किए गए",
    "checklist.pending_review": "समीक्षा लंबित",
    "checklist.reviewed": "समीक्षित",
    "checklist.needs_attention": "कमियां",
    "checklist.col.number": "क्र.सं.",
    "checklist.col.type": "मानक दस्तावेज़ प्रकार",
    "checklist.col.applicability": "लागू होना",
    "checklist.col.upload_status": "अपलोड स्थिति",
    "checklist.col.original": "अपलोड की गई मूल फ़ाइल",
    "checklist.col.confidence": "वर्गीकरण सटीकता",
    "checklist.col.status": "दस्तावेज़ स्थिति",
    "checklist.col.action": "कार्रवाई",
    "checklist.mandatory": "अनिवार्य",
    "checklist.conditional": "शर्तबद्ध",
    "checklist.mandatory_aph": "APH परिशिष्ट 16 के तहत अनिवार्य",
    "checklist.pages": "पृष्ठ",
    "checklist.stage": "चरण",
    "checklist.file_not_found": "अपलोड किए गए बैच पैकेज में फ़ाइल नहीं मिली",
    "checklist.inspect": "निरीक्षण करें",
    "checklist.add_deficiency": "कमी में जोड़ें",
    "checklist.verified_compliant": "सत्यापित एवं अनुपालन",
    "checklist.deficiency_flagged": "कमी पाई गई",

    // Verification View
    "verify.title": "दस्तावेज़ संवीक्षा एवं नियम सत्यापन",
    "verify.live_engine": "लाइव नियम इंजन सक्रिय",
    "verify.subtitle": "अपलोड किए गए मूल दस्तावेज़ों, ओसीआर निष्कर्षण और एआईसीटीई नियमों की लाइव जांच करें।",
    "verify.run_engine": "लाइव नियम इंजन चलाएं",
    "verify.running_engine": "नियमों का मूल्यांकन जारी...",
    "verify.mark_reviewed": "दस्तावेज़ को समीक्षित चिह्नित करें",
    "verify.select_doc": "दस्तावेज़ चुनें:",
    "verify.review_flags": "समीक्षा हेतु कमियां एवं चेतावनियां",
    "verify.no_deficiencies": "इस दस्तावेज़ में कोई कमी नहीं पाई गई",
    "verify.no_deficiencies_desc": "दस्तावेज़ के सभी खंड एआईसीटीई अनुमोदन प्रक्रिया पुस्तिका के मानकों के अनुरूप हैं।",
    "verify.why_flagged": "फ्लैग किए जाने का कारण (इंजन साक्ष्य एवं तर्क):",
    "verify.statutory_clause": "वैधानिक खंड:",
    "verify.disposition": "समीक्षक का निर्णय:",
    "verify.upheld": "कमी पुष्ट करें",
    "verify.dismiss": "फ्लैग निरस्त करें",
    "verify.extracted_entities": "निकाले गए मुख्य विवरण (एआई ओसीआर)",
    "verify.page_nav": "पृष्ठ संख्या:",
    "verify.download_verified": "सत्यापित फ़ाइल डाउनलोड करें",

    // EVC View
    "evc.title": "ई.वी.सी. भौतिक साक्ष्य एवं मीडिया कक्ष",
    "evc.subtitle": "की फ़ोटो, वीडियो वॉकथ्रू तथा क्रॉस-संस्थान पर्सेप्चुअल हैश (pHash) सत्यापन।",
    "evc.complete_review": "ई.वी.सी. समीक्षा पूर्ण करें",
    "evc.finalized": "ई.वी.सी. समीक्षा पूर्ण हुई",
    "evc.total_evidence": "कुल साक्ष्य फ़ाइलें",
    "evc.duplicate_signals": "डुप्लीकेट साक्ष्य संकेत",
    "evc.coverage_metric": "11-क्षेत्र कवरेज",
    "evc.areas_met": "अनिवार्य क्षेत्र पूर्ण",
    "evc.physical_insp": "स्थल निरीक्षण अनुशंसित",
    "evc.checklist_title": "एआईसीटीई आधिकारिक भौतिक एवं वीडियो साक्ष्य कवरेज चेकलिस्ट",
    "evc.areas_verified": "क्षेत्र सत्यापित",
    "evc.search_placeholder": "श्रेणी, फ़ाइल नाम अथवा संबंधित संस्थान द्वारा खोजें...",
    "evc.show_duplicates": "केवल डुप्लीकेट साक्ष्य दिखाएं",
    "evc.list_view": "सूची दृश्य",
    "evc.grid_view": "ग्रिड दृश्य",
    "evc.duplicate_detected": "अन्य संस्थान से मिलती-जुलती फ़ोटो/वीडियो पाई गई",
    "evc.matched_institute": "संबंधित अन्य संस्थान:",
    "evc.original_hash": "मूल / विशिष्ट साक्ष्य",
    "evc.flag_on_site": "स्थल निरीक्षण हेतु चिह्नित करें",
    "evc.on_site_flagged": "स्थल निरीक्षण हेतु चिह्नित",
    "evc.examine": "साक्ष्य जांचें",

    // Final Summary View
    "summary.title": "अंतिम संवीक्षा सारांश एवं सिफारिश",
    "summary.subtitle": "आवेदन दस्तावेज़ों, भौतिक साक्ष्य एवं वैधानिक मानकों का समग्र संवीक्षा मूल्यांकन",
    "summary.download_pdf": "आधिकारिक पीडीएफ रिपोर्ट डाउनलोड करें",
    "summary.mark_scrutinized": "संवीक्षा पूर्ण चिह्नित कर हस्ताक्षरित करें",
    "summary.request_reeval": "पुनर्मूल्यांकन का अनुरोध करें",
    "summary.view_history": "आवेदन इतिहास एवं ऑडिट लॉग देखें",
    "summary.recommendation": "कार्यकारी संवीक्षा सिफारिश",
    "summary.findings_overview": "मूल्यांकित कमियों का विवरण",
    "summary.checklist_overview": "दस्तावेज़ पैकेज की पूर्णता",
    "summary.evc_overview": "भौतिक साक्ष्य एवं सत्यनिष्ठा जांच",

    // General / Common
    "common.app_number": "आवेदन संख्या",
    "common.institute": "संस्थान का नाम",
    "common.category": "श्रेणी",
    "common.status": "स्थिति",
    "common.priority": "प्राथमिकता",
    "common.score": "अनुपालन अंक",
    "common.actions": "कार्रवाई",
    "common.cycle": "चक्र",
    "common.inspect": "निरीक्षण करें",
    "common.view": "देखें",
    "common.compliant": "अनुपालित",
    "common.deficiencies": "कमियां"
  }
};

const I18nContext = createContext<I18nContextType>({
  language: 'en',
  setLanguage: () => {},
  t: (key: string) => key,
});

export const LanguageProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [language, setLanguageState] = useState<Language>(() => {
    return (localStorage.getItem('aicte_lang') as Language) || 'en';
  });

  const setLanguage = (lang: Language) => {
    setLanguageState(lang);
    localStorage.setItem('aicte_lang', lang);
  };

  const t = (key: string): string => {
    return translations[language]?.[key] || translations['en']?.[key] || key;
  };

  return (
    <I18nContext.Provider value={{ language, setLanguage, t }}>
      {children}
    </I18nContext.Provider>
  );
};

export const useI18n = () => useContext(I18nContext);
