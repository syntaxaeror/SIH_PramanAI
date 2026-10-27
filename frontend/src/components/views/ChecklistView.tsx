import React, { useState } from 'react';
import {
  FileText,
  CheckCircle2,
  AlertTriangle,
  XCircle,
  Download,
  Eye,
  RefreshCw,
  FileSignature,
  ShieldAlert,
  ArrowRight
} from 'lucide-react';
import { Application, DocumentItem, Finding } from '../../types';
import { DeficiencyLetterModal } from '../modals/DeficiencyLetterModal';
import { useI18n } from '../../i18n';

interface ChecklistViewProps {
  application: Application;
  documents: DocumentItem[];
  findings: Finding[];
  onOpenDocument: (doc: DocumentItem) => void;
  onOpenFinding: (f: Finding) => void;
  onInspectDocument?: (docId: string) => void;
}

export const ChecklistView: React.FC<ChecklistViewProps> = ({
  application,
  documents,
  findings,
  onOpenDocument,
  onOpenFinding,
  onInspectDocument,
}) => {
  const { t } = useI18n();
  const [showLetterModal, setShowLetterModal] = useState(false);

  // Derive counts dynamically from live documents and rule verification findings
  const totalExpected = documents.length;
  const uploaded = documents.filter(d => d.upload_status !== 'Not Uploaded').length;
  const notUploaded = documents.filter(d => d.upload_status === 'Not Uploaded').length;

  const docsWithDeficiencies = documents.filter(d => {
    if (d.upload_status === 'Not Uploaded') return false;
    return findings.some(f => 
      ((f.document_id && f.document_id === d.id) || 
       (f.document_name && (f.document_name === d.original_filename || f.document_name === d.mapped_type))) &&
      f.validation_status === 'DEFICIENCY'
    );
  }).length;

  const reviewed = documents.filter(d => {
    if (d.upload_status === 'Not Uploaded') return false;
    const docFindings = findings.filter(f => 
      (f.document_id && f.document_id === d.id) || 
      (f.document_name && (f.document_name === d.original_filename || f.document_name === d.mapped_type))
    );
    return docFindings.length > 0 && docFindings.every(f => f.validation_status === 'PASS');
  }).length;

  const pendingReview = Math.max(0, uploaded - docsWithDeficiencies - reviewed);
  const needsAttention = docsWithDeficiencies;

  return (
    <div className="space-y-5 max-w-7xl mx-auto">

      {/* Top Header & Letter Action */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-3 border-b border-[#D9E2EC] gap-3">
        <div>
          <h1 className="text-xl font-bold text-[#17365D] tracking-tight">
            {t("checklist.title")}
          </h1>
          <p className="text-xs text-[#667085] mt-0.5">
            {t("checklist.subtitle")} <strong>{application.category}</strong> ({t("portal.ay")}).
          </p>
        </div>

        <button
          onClick={() => setShowLetterModal(true)}
          className="bg-[#B42318] hover:bg-[#991B1B] text-white text-xs font-semibold px-4 py-2 rounded flex items-center gap-2 shadow-2xs transition-colors self-start sm:self-auto cursor-pointer"
        >
          <FileSignature className="w-4 h-4" />
          <span>{t("checklist.generate_letter")}</span>
        </button>
      </div>

      {/* Summary KPI Tiles */}
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-3">
        <div className="bg-white border border-[#D9E2EC] p-3 rounded shadow-2xs">
          <div className="text-[11px] font-medium text-[#667085] uppercase">{t("checklist.total_expected")}</div>
          <div className="text-xl font-bold text-[#17365D] mt-1">{totalExpected}</div>
          <div className="text-[10px] text-[#667085] mt-0.5">APH Norms</div>
        </div>

        <div className="bg-white border border-[#D9E2EC] p-3 rounded shadow-2xs">
          <div className="text-[11px] font-medium text-[#667085] uppercase">{t("checklist.uploaded_files")}</div>
          <div className="text-xl font-bold text-[#237A45] mt-1">{uploaded}</div>
          <div className="text-[10px] text-[#237A45] font-medium mt-0.5">Package Verified</div>
        </div>

        <div className="bg-white border border-[#D9E2EC] p-3 rounded shadow-2xs">
          <div className="text-[11px] font-medium text-[#667085] uppercase">{t("checklist.not_uploaded")}</div>
          <div className="text-xl font-bold text-[#B42318] mt-1">{notUploaded}</div>
          <div className="text-[10px] text-[#B42318] font-medium mt-0.5">Mandatory Missing</div>
        </div>

        <div className="bg-white border border-[#D9E2EC] p-3 rounded shadow-2xs">
          <div className="text-[11px] font-medium text-[#667085] uppercase">{t("checklist.pending_review")}</div>
          <div className="text-xl font-bold text-[#946200] mt-1">{pendingReview}</div>
          <div className="text-[10px] text-[#946200] font-medium mt-0.5">In Scrutiny Queue</div>
        </div>

        <div className="bg-white border border-[#D9E2EC] p-3 rounded shadow-2xs">
          <div className="text-[11px] font-medium text-[#667085] uppercase">{t("checklist.reviewed")}</div>
          <div className="text-xl font-bold text-[#245A8D] mt-1">{reviewed}</div>
          <div className="text-[10px] text-[#245A8D] font-medium mt-0.5">Confirmed</div>
        </div>

        <div className="bg-white border border-[#D9E2EC] p-3 rounded shadow-2xs">
          <div className="text-[11px] font-medium text-[#667085] uppercase">{t("checklist.needs_attention")}</div>
          <div className="text-xl font-bold text-[#B42318] mt-1">{needsAttention}</div>
          <div className="text-[10px] text-[#B42318] font-medium mt-0.5">Deficiencies</div>
        </div>
      </div>

      {/* Checklist Table */}
      <div className="bg-white border border-[#D9E2EC] rounded shadow-2xs overflow-hidden">
        <div className="px-4 py-2.5 bg-[#F7F9FC] border-b border-[#D9E2EC] flex items-center justify-between text-xs">
          <span className="font-bold text-[#17365D] uppercase tracking-wider">
            {t("checklist.title")}
          </span>
        </div>

        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse gov-table">
            <thead>
              <tr>
                <th className="w-10 text-center">{t("checklist.col.number")}</th>
                <th className="w-64">{t("checklist.col.type")}</th>
                <th className="w-28 text-center">{t("checklist.col.applicability")}</th>
                <th className="w-32 text-center">{t("checklist.col.upload_status")}</th>
                <th>{t("checklist.col.original")}</th>
                <th className="text-center w-28">{t("checklist.col.confidence")}</th>
                <th className="w-40 text-center">{t("checklist.col.status")}</th>
                <th className="w-32 text-center">{t("checklist.col.action")}</th>
              </tr>
            </thead>
            <tbody>
              {documents.map((doc, idx) => {
                const isMissing = doc.upload_status === 'Not Uploaded';

                // Check live verification engine findings for this document
                const docFindings = findings.filter(f => 
                  (f.document_id && f.document_id === doc.id) || 
                  (f.document_name && (f.document_name === doc.original_filename || f.document_name === doc.mapped_type))
                );
                const hasDeficiency = docFindings.some(f => f.validation_status === 'DEFICIENCY');

                return (
                  <tr
                    key={doc.id}
                    className={isMissing ? "bg-[#FFFBFB]" : "hover:bg-[#F3F7FB] transition-colors"}
                  >
                    {/* Serial No. */}
                    <td className="text-center font-bold text-[#667085]">{idx + 1}</td>

                    {/* Required Title */}
                    <td>
                      <div className="font-semibold text-[#17365D]">
                        {doc.mapped_type}
                      </div>
                      <div className="text-[10px] text-[#667085]">
                        {doc.remarks || t("checklist.mandatory_aph")}
                      </div>
                    </td>

                    {/* Applicability */}
                    <td className="text-center">
                      <span className="bg-[#EAF2FA] text-[#17365D] text-[10px] font-semibold px-2 py-0.5 rounded">
                        {doc.is_mandatory !== false ? t("checklist.mandatory") : t("checklist.conditional")}
                      </span>
                    </td>

                    {/* Upload Status */}
                    <td className="text-center">
                      {isMissing ? (
                        <span className="bg-[#FDECEC] text-[#B42318] border border-[#F87171] text-[10px] font-bold px-2 py-0.5 rounded inline-flex items-center gap-1">
                          <XCircle className="w-3 h-3" /> {t("checklist.not_uploaded")}
                        </span>
                      ) : (
                        <span className="bg-[#EAF6EE] text-[#237A45] border border-[#86EFAC] text-[10px] font-bold px-2 py-0.5 rounded inline-flex items-center gap-1">
                          <CheckCircle2 className="w-3 h-3" /> {t("checklist.uploaded_files")}
                        </span>
                      )}
                    </td>

                    {/* Original File Name */}
                    <td>
                      {isMissing ? (
                        <span className="text-xs text-[#667085] italic">{t("checklist.file_not_found")}</span>
                      ) : (
                        <div className="font-mono text-xs text-[#243447] truncate max-w-xs">
                          {doc.original_filename}
                          <div className="text-[10px] text-[#667085] font-sans font-normal">
                            {doc.page_count} {t("checklist.pages")} • {t("checklist.stage")}: {doc.mapping_stage}
                          </div>
                        </div>
                      )}
                    </td>

                    {/* Auto-Mapping Confidence */}
                    <td className="text-center">
                      {isMissing ? (
                        <span className="text-slate-300">—</span>
                      ) : (
                        <span className="bg-[#EAF2FA] text-[#245A8D] font-mono text-[11px] font-semibold px-2 py-0.5 rounded">
                          {(doc.mapping_confidence * 100).toFixed(0)}%
                        </span>
                      )}
                    </td>

                    {/* Live Verification Document Status */}
                    <td className="text-center">
                      {isMissing ? (
                        <span className="bg-[#FDECEC] text-[#B42318] border border-[#F87171] text-[10px] font-bold px-2 py-0.5 rounded">
                          {t("checklist.not_uploaded")}
                        </span>
                      ) : hasDeficiency ? (
                        <span className="bg-[#FDECEC] text-[#B42318] border border-[#F87171] text-[10px] font-bold px-2 py-0.5 rounded inline-flex items-center gap-1">
                          <AlertTriangle className="w-3 h-3" />
                          {t("checklist.deficiency_flagged")}
                        </span>
                      ) : (
                        <span className="bg-[#EAF6EE] text-[#237A45] border border-[#86EFAC] text-[10px] font-bold px-2 py-0.5 rounded inline-flex items-center gap-1">
                          <CheckCircle2 className="w-3 h-3" />
                          {t("checklist.verified_compliant")}
                        </span>
                      )}
                    </td>

                    {/* Action: Inspect routes to Verification View */}
                    <td className="text-center">
                      {isMissing ? (
                        <button
                          onClick={() => setShowLetterModal(true)}
                          className="text-[11px] font-semibold text-[#B42318] hover:underline cursor-pointer"
                        >
                          {t("checklist.add_deficiency")}
                        </button>
                      ) : (
                        <button
                          onClick={() => {
                            if (onInspectDocument) {
                              onInspectDocument(doc.id);
                            } else {
                              onOpenDocument(doc);
                            }
                          }}
                          className="bg-white border border-[#245A8D] text-[#245A8D] hover:bg-[#EAF2FA] text-xs font-semibold px-2.5 py-1 rounded transition-colors inline-flex items-center gap-1 cursor-pointer shadow-2xs"
                        >
                          <Eye className="w-3.5 h-3.5" />
                          <span>{t("checklist.inspect")}</span>
                        </button>
                      )}
                    </td>
                  </tr>
                );
              })}
            </tbody>
          </table>
        </div>
      </div>

      {/* Deficiency Letter Modal */}
      {showLetterModal && (
        <DeficiencyLetterModal
          application={application}
          documents={documents}
          findings={findings}
          onClose={() => setShowLetterModal(false)}
        />
      )}

    </div>
  );
};
