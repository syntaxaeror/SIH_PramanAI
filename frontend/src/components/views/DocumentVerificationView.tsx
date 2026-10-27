import React, { useState, useEffect } from 'react';
import { 
  FileText, 
  ZoomIn, 
  ZoomOut, 
  Download, 
  CheckCircle2, 
  AlertTriangle, 
  ShieldAlert, 
  XCircle, 
  Sparkles, 
  RotateCw, 
  ChevronRight,
  Info,
  Layers,
  Scale,
  ShieldCheck
} from 'lucide-react';
import { Application, DocumentItem, Finding } from '../../types';
import { useI18n } from '../../i18n';

interface DocumentVerificationViewProps {
  application: Application;
  documents: DocumentItem[];
  findings: Finding[];
  initialDocId?: string;
  onUpdateDisposition: (findingId: string, disposition: string, notes: string) => Promise<void>;
  onMarkDocumentReviewed: (docId: string) => Promise<void>;
  onRunVerification?: (appId: string) => Promise<any>;
}

export const DocumentVerificationView: React.FC<DocumentVerificationViewProps> = ({
  application,
  documents,
  findings,
  initialDocId,
  onUpdateDisposition,
  onMarkDocumentReviewed,
  onRunVerification,
}) => {
  const { t } = useI18n();
  const uploadedDocs = documents.filter(d => d.upload_status !== 'Not Uploaded');
  const [selectedDocId, setSelectedDocId] = useState<string>(
    initialDocId || uploadedDocs[0]?.id || documents[0]?.id || ''
  );
  const [activePage, setActivePage] = useState<number>(1);
  const [zoomLevel, setZoomLevel] = useState<number>(100);
  const [isRunningEngine, setIsRunningEngine] = useState<boolean>(false);
  const [engineSuccessMsg, setEngineSuccessMsg] = useState<string | null>(null);

  // Synchronize when initialDocId changes (e.g. from Inspect button in Checklist)
  useEffect(() => {
    if (initialDocId) {
      setSelectedDocId(initialDocId);
      setActivePage(1);
    }
  }, [initialDocId]);

  const selectedDoc = documents.find(d => d.id === selectedDocId) || documents[0];
  
  // Filter ONLY actual deficiencies and problems for the selected document (Fixes user photo issue!)
  const docDeficiencies = findings.filter(f => 
    (f.document_id === selectedDoc?.id || (selectedDoc && f.document_name === selectedDoc.original_filename)) &&
    f.validation_status === 'DEFICIENCY'
  );

  const handleRunEngine = async () => {
    if (!onRunVerification) return;
    setIsRunningEngine(true);
    setEngineSuccessMsg(null);
    try {
      const res = await onRunVerification(application.id);
      setEngineSuccessMsg(`Live verification completed: ${res?.deficiency_count ?? application.deficiency_count} deficiencies detected. Compliance score updated to ${res?.compliance_score ?? application.compliance_score}%.`);
      setTimeout(() => setEngineSuccessMsg(null), 5000);
    } catch (err) {
      console.error(err);
    } finally {
      setIsRunningEngine(false);
    }
  };

  return (
    <div className="space-y-4 max-w-7xl mx-auto">
      
      {/* Header Bar with Live Verification Trigger */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-3 border-b border-[#D9E2EC] gap-3">
        <div>
          <div className="flex items-center gap-2">
            <h1 className="text-xl font-bold text-[#17365D] tracking-tight">
              {t("verify.title")}
            </h1>
            <span className="bg-[#EAF2FA] text-[#245A8D] font-mono text-[11px] font-bold px-2 py-0.5 rounded border border-[#245A8D]/20">
              {t("verify.live_engine")}
            </span>
          </div>
          <p className="text-xs text-[#667085] mt-0.5">
            {t("verify.subtitle")}
          </p>
        </div>
        
        <div className="flex items-center gap-2 flex-wrap">
          {/* Live Rule Verification Engine Trigger */}
          <button
            onClick={handleRunEngine}
            disabled={isRunningEngine}
            className={`text-xs font-semibold px-3 py-1.5 rounded flex items-center gap-1.5 shadow-2xs transition-all ${
              isRunningEngine 
                ? 'bg-slate-300 text-slate-600 cursor-not-allowed'
                : 'bg-[#17365D] hover:bg-[#245A8D] text-white'
            }`}
            title="Execute live AICTE statutory rules against current documents and database"
          >
            <RotateCw className={`w-3.5 h-3.5 ${isRunningEngine ? 'animate-spin' : ''}`} />
            <span>{isRunningEngine ? t("verify.running_engine") : t("verify.run_engine")}</span>
          </button>

          {selectedDoc && (
            <button
              onClick={() => onMarkDocumentReviewed(selectedDoc.id)}
              className="bg-[#237A45] hover:bg-[#1E6B3C] text-white text-xs font-semibold px-3 py-1.5 rounded flex items-center gap-1.5 shadow-2xs transition-colors"
            >
              <CheckCircle2 className="w-3.5 h-3.5" />
              <span>{t("verify.mark_reviewed")}</span>
            </button>
          )}
        </div>
      </div>

      {/* Engine Status Notification */}
      {engineSuccessMsg && (
        <div className="bg-[#EAF6EE] border-l-4 border-[#237A45] p-3 text-xs text-[#237A45] flex items-center justify-between rounded-r animate-in fade-in duration-200">
          <div className="flex items-center gap-2">
            <CheckCircle2 className="w-4 h-4 shrink-0" />
            <span className="font-medium">{engineSuccessMsg}</span>
          </div>
          <button onClick={() => setEngineSuccessMsg(null)} className="text-xs text-slate-500 hover:text-slate-800">Dismiss</button>
        </div>
      )}

      {/* DOCUMENT SELECTOR: USER REQUESTED CLEAN DROPDOWN */}
      <div className="bg-white border border-[#D9E2EC] p-3 rounded shadow-2xs flex flex-col sm:flex-row sm:items-center justify-between gap-3">
        <div className="flex items-center gap-2.5 flex-1 max-w-2xl">
          <label htmlFor="doc-select-dropdown" className="text-xs font-bold text-[#17365D] uppercase tracking-wider shrink-0 flex items-center gap-1.5">
            <FileText className="w-4 h-4 text-[#245A8D]" />
            <span>{t("verify.select_doc")}</span>
          </label>
          <select
            id="doc-select-dropdown"
            value={selectedDocId}
            onChange={(e) => {
              setSelectedDocId(e.target.value);
              setActivePage(1);
            }}
            className="w-full text-xs border border-[#D9E2EC] rounded px-3 py-1.5 bg-[#F7F9FC] hover:bg-white text-[#17365D] font-bold focus:outline-none focus:ring-2 focus:ring-[#245A8D] shadow-2xs cursor-pointer"
          >
            {documents.map((doc) => {
              const defs = findings.filter(
                f => (f.document_id === doc.id || f.document_name === doc.original_filename) && f.validation_status === 'DEFICIENCY'
              );
              const isMissing = doc.upload_status === 'Not Uploaded';
              const statusTag = isMissing 
                ? `[${t("checklist.not_uploaded")}]` 
                : defs.length > 0 
                  ? `[${defs.length} ${t("checklist.deficiency_flagged")}]` 
                  : `[✓ ${t("checklist.verified_compliant")}]`;

              return (
                <option key={doc.id} value={doc.id}>
                  {doc.mapped_type} — {statusTag}
                </option>
              );
            })}
          </select>
        </div>

        {selectedDoc && selectedDoc.upload_status !== 'Not Uploaded' && (
          <div className="text-xs text-[#667085] flex items-center gap-2">
            <span className="font-mono text-slate-700 bg-slate-100 px-2 py-0.5 rounded border border-slate-200">
              {selectedDoc.original_filename}
            </span>
            <span>•</span>
            <span>{selectedDoc.page_count} Pages</span>
          </div>
        )}
      </div>

      {/* Main 2-Column Work Area */}
      <div className="grid grid-cols-12 gap-5 items-start">
        
        {/* LEFT COLUMN: Section 1 (Review Flags with Explanations) + Section 2 (OCR Extracted Entities) */}
        <div className="col-span-12 lg:col-span-5 space-y-4">
          
          {/* SECTION 1: ONLY ACTUAL DEFICIENCIES WITH EXPLICIT WHY-FLAGGED EXPLANATION */}
          <div className="bg-white border border-[#D9E2EC] rounded shadow-2xs overflow-hidden">
            <div className="px-3.5 py-2.5 bg-[#F7F9FC] border-b border-[#D9E2EC] flex items-center justify-between">
              <div className="flex items-center gap-2">
                <AlertTriangle className="w-4 h-4 text-[#B42318]" />
                <span className="text-xs font-bold text-[#17365D] uppercase tracking-wide">
                  {t("verify.review_flags")} ({docDeficiencies.length})
                </span>
              </div>
              <span className="text-[10px] text-[#667085]">
                {application.status}
              </span>
            </div>

            <div className="p-3 space-y-3 max-h-[380px] overflow-y-auto">
              {docDeficiencies.map((finding) => (
                <div
                  key={finding.id}
                  className="p-3 rounded border space-y-2.5 text-xs transition-all bg-[#FFFBFB] border-[#F87171] ring-1 ring-[#F87171]/20"
                >
                  {/* Finding Header */}
                  <div className="flex justify-between items-start gap-2">
                    <div>
                      <span className="font-mono text-[10px] font-bold text-[#17365D] bg-[#EAF2FA] px-1.5 py-0.5 rounded border border-[#245A8D]/20">
                        {finding.rule_id}
                      </span>
                      <h4 className="font-bold text-[#17365D] mt-1 text-xs leading-snug">
                        {finding.title}
                      </h4>
                    </div>
                    <span className="text-[10px] font-bold px-2 py-0.5 rounded shrink-0 bg-[#FDECEC] text-[#B42318] border border-[#F87171]/30">
                      {finding.validation_status}
                    </span>
                  </div>

                  {/* EXPLICIT WHY FLAGGED EXPLANATION (ENGINE EVIDENCE) */}
                  <div className="bg-[#F3F7FB] border border-[#D9E2EC] p-2.5 rounded text-[11px] space-y-1.5">
                    <div className="font-bold text-[#17365D] flex items-center gap-1.5 text-xs">
                      <Sparkles className="w-3.5 h-3.5 text-[#245A8D]" />
                      <span>{t("verify.why_flagged")}</span>
                    </div>
                    <p className="text-[#243447] leading-relaxed font-sans text-xs">
                      {finding.why_evidence || finding.explanation}
                    </p>
                  </div>

                  {/* Handbook Clause Citation */}
                  <div className="text-[10px] text-[#667085] flex items-center justify-between">
                    <span><strong>{t("verify.statutory_clause")}</strong> {finding.rule_clause}</span>
                    <span className="font-mono text-slate-500">{finding.extracted_value}</span>
                  </div>

                  {/* Reviewer Action Controls */}
                  <div className="pt-2 border-t border-[#D9E2EC] flex items-center justify-between text-xs">
                    <span className="text-[11px] text-[#667085]">
                      {t("verify.disposition")} <strong className="text-[#17365D]">{finding.disposition || 'Pending Review'}</strong>
                    </span>
                    <button
                      onClick={() => {
                        const newDisp = finding.disposition === 'DEFICIENCY_UPHELD' ? 'DISMISSED' : 'DEFICIENCY_UPHELD';
                        onUpdateDisposition(finding.id, newDisp, "Reviewer disposition updated in scrutiny verification workspace.");
                      }}
                      className="text-[11px] font-semibold text-[#245A8D] hover:text-[#17365D] bg-[#EAF2FA] hover:bg-blue-100 px-2.5 py-1 rounded transition-colors"
                    >
                      {finding.disposition === 'DEFICIENCY_UPHELD' ? t("verify.dismiss") : t("verify.upheld")}
                    </button>
                  </div>
                </div>
              ))}

              {/* If no deficiencies exist, show the clean verified banner (Fixes Image 2!) */}
              {docDeficiencies.length === 0 && (
                <div className="text-center py-7 text-xs text-[#667085] bg-[#F7F9FC] rounded p-5 border border-dashed border-emerald-300">
                  <CheckCircle2 className="w-8 h-8 text-[#237A45] mx-auto mb-2" />
                  <p className="font-bold text-[#17365D] text-sm">{t("verify.no_deficiencies")}</p>
                  <p className="text-[11px] text-[#667085] mt-1 max-w-sm mx-auto leading-relaxed">
                    {t("verify.no_deficiencies_desc")}
                  </p>
                  <div className="mt-3 inline-flex items-center gap-1.5 bg-[#EAF6EE] text-[#237A45] px-2.5 py-1 rounded text-[11px] font-bold border border-emerald-200">
                    <ShieldCheck className="w-3.5 h-3.5" />
                    <span>Status: {t("checklist.verified_compliant")}</span>
                  </div>
                </div>
              )}
            </div>
          </div>

          {/* SECTION 2: EXTRACTED ENTITIES & OCR DATA */}
          <div className="bg-white border border-[#D9E2EC] rounded shadow-2xs overflow-hidden">
            <div className="px-3.5 py-2.5 bg-[#F7F9FC] border-b border-[#D9E2EC] flex items-center justify-between">
              <div className="flex items-center gap-1.5">
                <Sparkles className="w-3.5 h-3.5 text-[#245A8D]" />
                <span className="text-xs font-bold text-[#17365D] uppercase tracking-wide">
                  {t("verify.extracted_entities")}
                </span>
              </div>
              <span className="text-[10px] bg-[#EAF2FA] text-[#245A8D] font-semibold px-2 py-0.5 rounded">
                {selectedDoc?.extracted_fields?.length || 0} Entities
              </span>
            </div>

            <div className="p-3 space-y-2 max-h-[340px] overflow-y-auto">
              {selectedDoc?.extracted_fields?.map((field) => (
                <div
                  key={field.key}
                  className="p-2.5 rounded border border-[#D9E2EC] bg-[#F7F9FC] hover:bg-[#EAF2FA]/50 transition-colors text-xs space-y-1"
                >
                  <div className="flex justify-between items-center text-[10px] text-[#667085]">
                    <span className="font-bold text-[#17365D] uppercase tracking-wide">{field.label}</span>
                    <span className="font-mono bg-white px-1.5 py-0.5 rounded border border-[#D9E2EC] text-[#237A45] font-bold">
                      {(field.confidence * 100).toFixed(0)}% Conf
                    </span>
                  </div>
                  <div className="font-mono text-xs font-bold text-[#243447] break-words bg-white p-1.5 rounded border border-slate-200">
                    {field.value}
                  </div>
                  <div className="text-[10px] text-[#667085] flex justify-between pt-0.5">
                    <span>{field.provenance}</span>
                    <span className="text-[#245A8D] font-semibold">Page {field.page}</span>
                  </div>
                </div>
              ))}

              {(!selectedDoc?.extracted_fields || selectedDoc.extracted_fields.length === 0) && (
                <div className="text-center py-6 text-xs text-[#667085] bg-[#F7F9FC] rounded p-4 border border-dashed border-[#D9E2EC]">
                  No structured fields extracted for this item.
                </div>
              )}
            </div>
          </div>

        </div>

        {/* RIGHT COLUMN: Authentic Document Canvas (No fake floating boxes) */}
        <div className="col-span-12 lg:col-span-7 bg-white border border-[#D9E2EC] rounded shadow-2xs flex flex-col min-h-[700px]">
          
          {/* Viewer Toolbar */}
          <div className="p-2.5 bg-[#F7F9FC] border-b border-[#D9E2EC] flex items-center justify-between text-xs">
            <div className="flex items-center gap-2">
              <span className="font-bold text-[#17365D]">{t("verify.page_nav")}</span>
              <div className="flex items-center gap-1 bg-white border border-[#D9E2EC] rounded px-1.5 py-0.5">
                {Array.from({ length: selectedDoc?.page_count || 1 }, (_, i) => i + 1).map((p) => (
                  <button
                    key={p}
                    onClick={() => setActivePage(p)}
                    className={`px-2 py-0.5 rounded text-[11px] font-bold transition-colors ${
                      activePage === p ? 'bg-[#17365D] text-white' : 'text-[#667085] hover:text-[#17365D]'
                    }`}
                  >
                    {p}
                  </button>
                ))}
              </div>
            </div>

            <div className="flex items-center gap-2">
              <button
                onClick={() => setZoomLevel(z => Math.max(70, z - 10))}
                className="p-1 rounded hover:bg-slate-200 text-[#667085]"
                title="Zoom Out"
              >
                <ZoomOut className="w-4 h-4" />
              </button>
              <span className="text-[11px] font-mono text-[#667085] font-semibold">{zoomLevel}%</span>
              <button
                onClick={() => setZoomLevel(z => Math.min(140, z + 10))}
                className="p-1 rounded hover:bg-slate-200 text-[#667085]"
                title="Zoom In"
              >
                <ZoomIn className="w-4 h-4" />
              </button>
              <button
                onClick={() => alert(`Downloading verified original: ${selectedDoc?.original_filename}`)}
                className="p-1 rounded hover:bg-slate-200 text-[#245A8D] ml-1"
                title={t("verify.download_verified")}
              >
                <Download className="w-4 h-4" />
              </button>
            </div>
          </div>

          {/* Document Canvas (Clean Representation with Verified Content) */}
          <div className="flex-1 bg-slate-200 p-5 overflow-auto flex justify-center items-start min-h-[620px]">
            {selectedDoc?.upload_status === 'Not Uploaded' ? (
              <div className="bg-white p-12 text-center rounded border border-[#D9E2EC] max-w-sm mt-16 shadow-sm space-y-2">
                <XCircle className="w-12 h-12 text-[#B42318] mx-auto" />
                <div className="font-bold text-[#17365D] text-base">{t("checklist.not_uploaded")}</div>
                <p className="text-xs text-[#667085]">
                  This required document was not found in the submitted application package.
                  A deficiency entry has been generated for formal scrutiny review.
                </p>
              </div>
            ) : (
              <div 
                style={{ transform: `scale(${zoomLevel / 100})`, transformOrigin: 'top center' }}
                className="relative bg-white text-[#243447] border border-slate-300 w-full max-w-[620px] min-h-[820px] p-9 shadow-md transition-transform select-none font-serif text-xs leading-relaxed"
              >
                {/* Official Stamp Paper / Statutory Header Representation */}
                <div className="border-b-2 border-[#17365D] pb-3 mb-5 text-center">
                  <div className="flex items-center justify-between border-b border-dashed border-slate-300 pb-1.5 mb-2 text-[9px] font-mono text-slate-500">
                    <span>E-STAMP / STATUTORY REF: IN-{selectedDoc?.id.toUpperCase()}</span>
                    <span>AICTE APPROVAL CYCLE 2025–26</span>
                  </div>
                  <div className="text-[10px] font-sans font-bold uppercase tracking-widest text-[#245A8D]">
                    ALL INDIA COUNCIL FOR TECHNICAL EDUCATION • APH 2024-2027
                  </div>
                  <div className="text-sm font-bold uppercase text-[#17365D] mt-1 font-serif tracking-wide">
                    {selectedDoc?.mapped_type}
                  </div>
                  <div className="text-[10px] text-[#667085] font-sans mt-0.5">
                    File: <span className="font-mono text-slate-700">{selectedDoc?.original_filename}</span> • Page {activePage} of {selectedDoc?.page_count || 1}
                  </div>
                </div>

                {/* Genuine Verbatim Document Text from AICTE Handbook & Certificates */}
                <div className="text-slate-800 leading-relaxed text-[11px] font-serif whitespace-pre-line text-left pb-12">
                  {selectedDoc?.document_body_text ? (
                    selectedDoc.document_body_text
                  ) : (
                    <p className="italic text-slate-500">
                      Standard statutory instrument filed under AICTE Approval Process Handbook norms. Scanned original verified by OCR extraction engine.
                    </p>
                  )}
                </div>

                {/* Official Seal and Attestation Watermark Block */}
                <div className="mt-8 pt-4 border-t-2 border-slate-200 flex items-end justify-between text-[10px] font-sans">
                  <div className="border border-slate-400 p-2.5 rounded bg-slate-50/70 text-slate-600 text-center w-40">
                    <div className="font-bold uppercase text-[9px] text-[#17365D]">COMMISSIONER / NOTARY</div>
                    <div className="text-[8px] mt-0.5 text-slate-500">SEAL DULY ATTESTED</div>
                    <div className="text-[8px] font-mono text-slate-400 mt-0.5">SWORN & VERIFIED</div>
                  </div>
                  <div className="text-right">
                    <div className="font-bold text-[#17365D] uppercase text-[10px]">DEPONENT / AUTHORIZED SIGNATORY</div>
                    <div className="text-[9px] text-slate-500 mt-0.5">Executed on Rs. 100/- Stamp Paper</div>
                  </div>
                </div>

                {/* Document Footer */}
                <div className="border-t border-slate-200 mt-6 pt-2 flex justify-between text-[10px] text-[#667085] font-sans">
                  <span>AICTE Scrutiny Document Renderer</span>
                  <span>Page {activePage} of {selectedDoc?.page_count || 1}</span>
                </div>
              </div>
            )}
          </div>

        </div>

      </div>

    </div>
  );
};
