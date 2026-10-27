import React, { useState } from 'react';
import { 
  FileBarChart, 
  Download, 
  CheckCircle2, 
  AlertTriangle, 
  ShieldAlert, 
  RefreshCw, 
  History, 
  FileText, 
  Printer, 
  Check, 
  ArrowRight,
  Sparkles,
  Info
} from 'lucide-react';
import { Application, DocumentItem, Finding, EVCEvidenceItem } from '../../types';
import { useI18n } from '../../i18n';

interface FinalSummaryViewProps {
  application: Application;
  documents: DocumentItem[];
  findings: Finding[];
  evcItems: EVCEvidenceItem[];
  onDownloadPdf: () => void;
  onMarkScrutinized: (note: string) => Promise<void>;
  onRequestReevaluation: (reason: string) => Promise<void>;
  onViewHistory: () => void;
}

export const FinalSummaryView: React.FC<FinalSummaryViewProps> = ({
  application,
  documents,
  findings,
  evcItems,
  onDownloadPdf,
  onMarkScrutinized,
  onRequestReevaluation,
  onViewHistory,
}) => {
  const { t } = useI18n();
  const [showScrutinizeModal, setShowScrutinizeModal] = useState(false);
  const [showReevalModal, setShowReevalModal] = useState(false);
  const [scrutinyNote, setScrutinyNote] = useState('Scrutiny completed in accordance with APH 2025-26 norms. Deficiencies recorded in official summary.');
  const [reevalReason, setReevalReason] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);

  const missingDocs = documents.filter(d => d.upload_status === 'Not Uploaded');
  const confirmedDeficiencies = findings.filter(f => f.validation_status === 'DEFICIENCY');
  const duplicateEvc = evcItems.filter(i => i.duplicate_flag);
  const physicalNeeded = evcItems.filter(i => i.inspection_needed);

  // Compute recommendation state
  const getRecommendation = () => {
    if (confirmedDeficiencies.length > 0) {
      return {
        title: "Deficiencies Identified — Formal Letter Required",
        badge: "DEFICIENCIES CONFIRMED",
        color: "text-[#B42318] bg-[#FDECEC] border-[#F87171]",
        desc: "One or more confirmed document deficiencies or regulatory non-compliances were identified during scrutiny. A deficiency letter must be issued before further processing."
      };
    }
    if (physicalNeeded.length > 0) {
      return {
        title: "Physical Verification Required by EVC Committee",
        badge: "PHYSICAL INSPECTION FLAGGED",
        color: "text-[#946200] bg-[#FFF5D9] border-[#FCD34D]",
        desc: "Photographic or video evidence triggered review signals (such as duplicate pHash matches). An authorized physical inspection committee should conduct on-site verification."
      };
    }
    return {
      title: "No Outstanding Issues Identified",
      badge: "SCRUTINY COMPLIANT",
      color: "text-[#237A45] bg-[#EAF6EE] border-[#86EFAC]",
      desc: "All submitted documents and evidence meet the configured requirements for this application category. (Note: This is an evidence synthesis, not a statutory approval)."
    };
  };

  const rec = getRecommendation();

  const handleConfirmScrutiny = async () => {
    setIsSubmitting(true);
    await onMarkScrutinized(scrutinyNote);
    setIsSubmitting(false);
    setShowScrutinizeModal(false);
  };

  const handleConfirmReeval = async () => {
    if (!reevalReason.trim()) {
      alert("Please provide a reason for re-evaluation.");
      return;
    }
    setIsSubmitting(true);
    await onRequestReevaluation(reevalReason);
    setIsSubmitting(false);
    setShowReevalModal(false);
  };

  return (
    <div className="space-y-6 max-w-7xl mx-auto">
      
      {/* 11.1 Application Overview & Action Header */}
      <div className="flex flex-col md:flex-row md:items-center justify-between pb-3 border-b border-[#D9E2EC] gap-3">
        <div>
          <h1 className="text-xl font-bold text-[#17365D] tracking-tight">
            {t("summary.title")}
          </h1>
          <p className="text-xs text-[#667085] mt-0.5">
            {t("summary.subtitle")} <strong>{application.institution_name}</strong>.
          </p>
        </div>

        {/* Top Actions */}
        <div className="flex items-center gap-2 flex-wrap">
          <button
            onClick={onViewHistory}
            className="px-3 py-1.5 rounded border border-[#D9E2EC] bg-white hover:bg-[#F3F7FB] text-xs font-semibold text-[#17365D] flex items-center gap-1.5 transition-colors cursor-pointer"
          >
            <History className="w-3.5 h-3.5" />
            <span>{t("summary.view_history")}</span>
          </button>

          <button
            onClick={onDownloadPdf}
            className="px-3.5 py-1.5 rounded bg-white border border-[#245A8D] hover:bg-[#EAF2FA] text-xs font-semibold text-[#245A8D] flex items-center gap-1.5 transition-colors cursor-pointer"
          >
            <Download className="w-3.5 h-3.5" />
            <span>{t("summary.download_pdf")}</span>
          </button>

          <button
            onClick={() => setShowReevalModal(true)}
            className="px-3 py-1.5 rounded border border-[#D9E2EC] bg-white hover:bg-[#FFF5D9] text-xs font-semibold text-[#946200] flex items-center gap-1.5 transition-colors cursor-pointer"
          >
            <RefreshCw className="w-3.5 h-3.5" />
            <span>{t("summary.request_reeval")}</span>
          </button>

          <button
            onClick={() => setShowScrutinizeModal(true)}
            className="px-4 py-1.5 rounded bg-[#17365D] hover:bg-[#245A8D] text-white text-xs font-semibold flex items-center gap-1.5 shadow-2xs transition-colors cursor-pointer"
          >
            <CheckCircle2 className="w-4 h-4" />
            <span>{t("summary.mark_scrutinized")}</span>
          </button>
        </div>
      </div>

      {/* 11.4 Prominent Neutral Scrutiny Recommendation Panel */}
      <div className={`p-4 rounded border-l-4 ${rec.color} space-y-1.5 shadow-2xs`}>
        <div className="flex items-center justify-between">
          <div className="font-bold text-sm tracking-tight">{rec.title}</div>
          <span className="text-[10px] font-bold uppercase tracking-wider px-2 py-0.5 rounded bg-white/80 border">
            {rec.badge}
          </span>
        </div>
        <p className="text-xs leading-relaxed text-[#243447]">
          {rec.desc}
        </p>
        <div className="text-[10px] text-[#667085] pt-1">
          * Regulatory Safeguard: All recommendations are prepared for authorized human scrutiny committees. Final approval decisions rest with the Competent Authority.
        </div>
      </div>

      {/* 11.2 Consolidated Summary Cards A, B, C, D */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        
        {/* A. Checklist Summary */}
        <div className="bg-white border border-[#D9E2EC] rounded p-4 shadow-2xs space-y-2">
          <div className="text-xs font-bold text-[#17365D] uppercase tracking-wide border-b border-[#D9E2EC] pb-2">
            A. Checklist Summary
          </div>
          <div className="space-y-1.5 text-xs">
            <div className="flex justify-between">
              <span className="text-[#667085]">Expected Documents:</span>
              <strong className="text-[#17365D]">{documents.length}</strong>
            </div>
            <div className="flex justify-between">
              <span className="text-[#667085]">Uploaded & Mapped:</span>
              <strong className="text-[#237A45]">{documents.filter(d => d.upload_status !== 'Not Uploaded').length}</strong>
            </div>
            <div className="flex justify-between">
              <span className="text-[#667085]">Missing Documents:</span>
              <strong className="text-[#B42318]">{missingDocs.length}</strong>
            </div>
          </div>
        </div>

        {/* B. Document Verification */}
        <div className="bg-white border border-[#D9E2EC] rounded p-4 shadow-2xs space-y-2">
          <div className="text-xs font-bold text-[#17365D] uppercase tracking-wide border-b border-[#D9E2EC] pb-2">
            B. Document Verification
          </div>
          <div className="space-y-1.5 text-xs">
            <div className="flex justify-between">
              <span className="text-[#667085]">Verified Compliant:</span>
              <strong className="text-[#237A45]">{findings.filter(f => f.validation_status === 'PASS').length}</strong>
            </div>
            <div className="flex justify-between">
              <span className="text-[#667085]">Confirmed Deficiencies:</span>
              <strong className="text-[#B42318]">{confirmedDeficiencies.length}</strong>
            </div>
            <div className="flex justify-between">
              <span className="text-[#667085]">Manual Review Needed:</span>
              <strong className="text-[#946200]">{findings.filter(f => f.verification_status === 'MANUAL REVIEW').length}</strong>
            </div>
          </div>
        </div>

        {/* C. EVC Evidence */}
        <div className="bg-white border border-[#D9E2EC] rounded p-4 shadow-2xs space-y-2">
          <div className="text-xs font-bold text-[#17365D] uppercase tracking-wide border-b border-[#D9E2EC] pb-2">
            C. EVC Evidence Room
          </div>
          <div className="space-y-1.5 text-xs">
            <div className="flex justify-between">
              <span className="text-[#667085]">Evidence Files Reviewed:</span>
              <strong className="text-[#17365D]">{evcItems.length}</strong>
            </div>
            <div className="flex justify-between">
              <span className="text-[#667085]">pHash Duplicate Flags:</span>
              <strong className="text-[#B42318]">{duplicateEvc.length}</strong>
            </div>
            <div className="flex justify-between">
              <span className="text-[#667085]">Physical Inspection Req.:</span>
              <strong className="text-[#946200]">{physicalNeeded.length}</strong>
            </div>
          </div>
        </div>

        {/* D. Scrutiny Officer Notes */}
        <div className="bg-white border border-[#D9E2EC] rounded p-4 shadow-2xs space-y-2">
          <div className="text-xs font-bold text-[#17365D] uppercase tracking-wide border-b border-[#D9E2EC] pb-2">
            D. Reviewer Allocation
          </div>
          <div className="space-y-1 text-xs">
            <div className="text-[#667085]">Assigned Officer:</div>
            <div className="font-semibold text-[#17365D] truncate">{application.assigned_reviewer}</div>
            <div className="text-[#667085] pt-1">Review Cycle:</div>
            <div className="font-bold text-[#245A8D]">Cycle #{application.review_cycle || 1}</div>
          </div>
        </div>

      </div>

      {/* 11.3 Evidence-Linked Findings Table */}
      <div className="bg-white border border-[#D9E2EC] rounded shadow-2xs overflow-hidden">
        <div className="px-4 py-3 bg-[#F7F9FC] border-b border-[#D9E2EC] flex items-center justify-between">
          <h3 className="text-xs font-bold text-[#17365D] uppercase tracking-wider">
            Consolidated Evidence-Linked Findings ({findings.length})
          </h3>
          <span className="text-[10px] text-[#667085]">Linked to Exact Source Files & Clauses</span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse gov-table">
            <thead>
              <tr>
                <th className="w-36">Rule & Clause</th>
                <th>Finding Title & Explanation</th>
                <th>Evidence Provenance</th>
                <th className="text-center w-28">Validation Status</th>
                <th className="text-center w-28">Priority</th>
                <th className="text-center w-36">Reviewer Disposition</th>
              </tr>
            </thead>
            <tbody>
              {findings.map((f) => (
                <tr key={f.id} className="hover:bg-[#F3F7FB]">
                  <td className="font-mono text-xs font-bold text-[#17365D]">
                    {f.rule_id}
                    <div className="text-[10px] text-[#667085] font-sans font-normal mt-0.5">
                      {f.rule_clause}
                    </div>
                  </td>
                  <td>
                    <div className="font-semibold text-[#17365D]">{f.title}</div>
                    <div className="text-[11px] text-[#667085] mt-0.5">{f.explanation}</div>
                  </td>
                  <td>
                    <div className="text-[11px] text-[#243447] bg-[#F7F9FC] p-2 rounded border border-[#D9E2EC]">
                      {f.why_evidence}
                    </div>
                    {f.document_name && (
                      <div className="text-[10px] text-[#667085] mt-1 flex items-center gap-1">
                        <FileText className="w-3 h-3 text-[#245A8D]" />
                        <span>{f.document_name}</span>
                        {f.page_number && <span>(Page {f.page_number})</span>}
                      </div>
                    )}
                  </td>
                  <td className="text-center">
                    <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                      f.validation_status === 'DEFICIENCY' ? 'bg-[#FDECEC] text-[#B42318]' : 'bg-[#EAF6EE] text-[#237A45]'
                    }`}>
                      {f.validation_status}
                    </span>
                  </td>
                  <td className="text-center">
                    <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                      f.priority === 'RED' ? 'bg-[#FDECEC] text-[#B42318]' :
                      f.priority === 'AMBER' ? 'bg-[#FFF5D9] text-[#946200]' :
                      'bg-[#EAF6EE] text-[#237A45]'
                    }`}>
                      {f.priority}
                    </span>
                  </td>
                  <td className="text-center">
                    <span className="bg-[#EAF2FA] text-[#17365D] text-xs font-semibold px-2 py-0.5 rounded border border-[#D9E2EC]">
                      {f.disposition || 'ACCEPTED'}
                    </span>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {/* Confirmation Modal: Mark as Scrutinized */}
      {showScrutinizeModal && (
        <div className="fixed inset-0 z-50 bg-black/50 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white border border-[#D9E2EC] rounded max-w-lg w-full p-6 shadow-2xl space-y-4">
            <div className="flex items-center gap-2.5 text-[#17365D]">
              <CheckCircle2 className="w-6 h-6 text-[#237A45]" />
              <h3 className="font-bold text-base">Mark Application as Scrutinized</h3>
            </div>

            <p className="text-xs text-[#243447] leading-relaxed">
              This action finalizes the current scrutiny cycle for <strong>{application.institution_name}</strong> ({application.application_number}).
              A permanent, immutable audit event will be recorded with your reviewer credentials.
            </p>

            <div>
              <label className="text-xs font-semibold text-[#17365D] block mb-1">
                Final Reviewer Directive / Endorsement Note:
              </label>
              <textarea
                value={scrutinyNote}
                onChange={(e) => setScrutinyNote(e.target.value)}
                rows={3}
                className="w-full border border-[#D9E2EC] rounded p-2 text-xs focus:outline-none focus:border-[#245A8D]"
              />
            </div>

            <div className="flex justify-end gap-2 pt-2">
              <button
                onClick={() => setShowScrutinizeModal(false)}
                className="px-3 py-1.5 rounded border border-[#D9E2EC] text-xs font-semibold text-[#243447]"
              >
                Cancel
              </button>
              <button
                onClick={handleConfirmScrutiny}
                disabled={isSubmitting}
                className="px-4 py-1.5 rounded bg-[#17365D] hover:bg-[#245A8D] text-white text-xs font-semibold shadow-2xs"
              >
                {isSubmitting ? 'Recording...' : 'Confirm Scrutinized State'}
              </button>
            </div>
          </div>
        </div>
      )}

      {/* Confirmation Modal: Request Re-evaluation */}
      {showReevalModal && (
        <div className="fixed inset-0 z-50 bg-black/50 backdrop-blur-xs flex items-center justify-center p-4">
          <div className="bg-white border border-[#D9E2EC] rounded max-w-lg w-full p-6 shadow-2xl space-y-4">
            <div className="flex items-center gap-2.5 text-[#946200]">
              <RefreshCw className="w-6 h-6 text-[#946200]" />
              <h3 className="font-bold text-base">Request Application Re-evaluation</h3>
            </div>

            <p className="text-xs text-[#243447] leading-relaxed">
              Initiates a new scrutiny cycle (Cycle #{ (application.review_cycle || 1) + 1 }) while fully preserving 
              all prior reviewer findings, notes, and deficiency letters.
            </p>

            <div>
              <label className="text-xs font-semibold text-[#17365D] block mb-1">
                Mandatory Reason for Re-evaluation:
              </label>
              <textarea
                value={reevalReason}
                onChange={(e) => setReevalReason(e.target.value)}
                placeholder="Specify regulatory grounds, new evidence submission, or appellate directives..."
                rows={3}
                className="w-full border border-[#D9E2EC] rounded p-2 text-xs focus:outline-none focus:border-[#245A8D]"
              />
            </div>

            <div className="flex justify-end gap-2 pt-2">
              <button
                onClick={() => setShowReevalModal(false)}
                className="px-3 py-1.5 rounded border border-[#D9E2EC] text-xs font-semibold text-[#243447]"
              >
                Cancel
              </button>
              <button
                onClick={handleConfirmReeval}
                disabled={isSubmitting}
                className="px-4 py-1.5 rounded bg-[#946200] hover:bg-[#784F00] text-white text-xs font-semibold shadow-2xs"
              >
                {isSubmitting ? 'Submitting...' : 'Create New Review Cycle'}
              </button>
            </div>
          </div>
        </div>
      )}

    </div>
  );
};
