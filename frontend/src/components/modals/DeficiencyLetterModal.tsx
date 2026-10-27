import React, { useState } from 'react';
import { X, FileText, Download, Save, CheckCircle2, AlertTriangle, ShieldCheck, Printer } from 'lucide-react';
import { Application, DocumentItem, Finding } from '../../types';

interface DeficiencyLetterModalProps {
  application: Application;
  documents: DocumentItem[];
  findings: Finding[];
  onClose: () => void;
}

export const DeficiencyLetterModal: React.FC<DeficiencyLetterModalProps> = ({
  application,
  documents,
  findings,
  onClose,
}) => {
  const missingDocs = documents.filter(d => d.upload_status === 'Not Uploaded');
  const deficiencyFindings = findings.filter(f => f.validation_status === 'DEFICIENCY');

  const [refNumber, setRefNumber] = useState(`AICTE/SWRO/SCRUTINY/${application.academic_year}/${application.application_number}`);
  const [letterDate, setLetterDate] = useState(new Date().toLocaleDateString('en-GB', { day: '2-digit', month: 'short', year: 'numeric' }));
  const [remarks, setRemarks] = useState(
    "The institution is hereby requested to submit verified rectification / compliance documents for the deficiencies identified above within 7 working days through the authorized AICTE upload channel."
  );
  const [isSavedDraft, setIsSavedDraft] = useState(false);

  const handlePrint = () => {
    window.print();
  };

  const handleSaveDraft = () => {
    setIsSavedDraft(true);
    setTimeout(() => setIsSavedDraft(false), 2000);
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/60 backdrop-blur-xs flex items-center justify-center p-4">
      <div className="bg-white border border-[#D9E2EC] rounded-lg max-w-4xl w-full shadow-2xl overflow-hidden flex flex-col max-h-[92vh] animate-in fade-in duration-150">
        
        {/* Header */}
        <div className="bg-[#17365D] text-white px-6 py-3.5 flex items-center justify-between">
          <div className="flex items-center gap-2.5">
            <FileText className="w-5 h-5 text-blue-200" />
            <div>
              <h2 className="text-sm font-bold tracking-tight">
                Generate Description of Deficiencies Letter
              </h2>
              <div className="text-[11px] text-blue-200">
                Official AICTE Scrutiny Letter Template • Ref: {application.application_number}
              </div>
            </div>
          </div>
          <button
            onClick={onClose}
            className="text-blue-200 hover:text-white p-1 rounded hover:bg-white/10 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Official Letter Preview Body */}
        <div className="p-6 overflow-y-auto space-y-6 text-xs text-[#243447] bg-[#F7F9FC]">
          
          {/* Official Letterhead Container */}
          <div className="bg-white border border-[#D9E2EC] p-8 rounded shadow-xs space-y-5 font-serif select-text">
            
            {/* National Emblem & AICTE Header */}
            <div className="text-center border-b-2 border-[#17365D] pb-4 space-y-1 font-sans">
              <div className="text-sm font-black tracking-wider text-[#17365D] uppercase">
                ALL INDIA COUNCIL FOR TECHNICAL EDUCATION
              </div>
              <div className="text-xs font-semibold text-[#245A8D]">
                (A STATUTORY BODY OF THE GOVERNMENT OF INDIA)
              </div>
              <div className="text-[11px] text-[#667085]">
                Nelson Mandela Marg, Vasant Kunj, New Delhi-110070 • Website: www.aicte-india.org
              </div>
            </div>

            {/* Letter Reference & Date */}
            <div className="flex justify-between items-center text-xs font-sans pt-1">
              <div>
                <strong>Ref. No.:</strong> <span className="font-mono">{refNumber}</span>
              </div>
              <div>
                <strong>Date:</strong> <span>{letterDate}</span>
              </div>
            </div>

            {/* Recipient Addressee */}
            <div className="space-y-1 font-sans text-xs">
              <div><strong>To:</strong></div>
              <div className="font-semibold text-[#17365D]">{application.institution_name}</div>
              <div className="text-[#667085]">{application.institution_address}</div>
              <div className="text-[#667085]">Sponsoring Trust: <strong>{application.trust_name}</strong></div>
              <div>Permanent Institute ID: <strong className="font-mono">{application.institution_id}</strong></div>
            </div>

            {/* Subject Line */}
            <div className="bg-[#F3F7FB] border-l-4 border-[#17365D] p-3 font-sans text-xs">
              <strong>SUBJECT:</strong> Scrutiny Verification & Description of Deficiencies for 
              <strong> {application.category}</strong> (Academic Year {application.academic_year}).
            </div>

            {/* Body Introduction */}
            <div className="leading-relaxed font-sans text-xs text-[#243447] space-y-2">
              <p>Sir / Madam,</p>
              <p>
                The application submitted by your institution for <strong>{application.category}</strong> for the 
                Academic Year <strong>{application.academic_year}</strong> has been scrutinized by the authorized 
                Scrutiny Committee in accordance with the norms, procedures, and standards prescribed in the 
                AICTE Approval Process Handbook (APH).
              </p>
              <p>
                During the scrutiny of uploaded supporting records, the following non-compliances, missing documents, 
                and deficiencies have been formally identified:
              </p>
            </div>

            {/* Missing Documents Table */}
            {missingDocs.length > 0 && (
              <div className="space-y-2 font-sans">
                <div className="text-xs font-bold text-[#B42318] uppercase tracking-wide">
                  A. Mandatory Documents Not Uploaded ({missingDocs.length})
                </div>
                <table className="w-full border-collapse border border-[#D9E2EC] text-xs">
                  <thead>
                    <tr className="bg-[#FDECEC] text-[#B42318]">
                      <th className="border border-[#D9E2EC] p-2 text-left w-12">S.No</th>
                      <th className="border border-[#D9E2EC] p-2 text-left">Document Title</th>
                      <th className="border border-[#D9E2EC] p-2 text-left">Prescribed APH Requirement</th>
                    </tr>
                  </thead>
                  <tbody>
                    {missingDocs.map((doc, i) => (
                      <tr key={doc.id}>
                        <td className="border border-[#D9E2EC] p-2 text-center font-bold">{i + 1}</td>
                        <td className="border border-[#D9E2EC] p-2 font-semibold text-[#17365D]">{doc.mapped_type}</td>
                        <td className="border border-[#D9E2EC] p-2 text-[#667085]">Mandatory document required under APH Appendix 16 norms. File not uploaded in submitted package.</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}

            {/* Confirmed Deficiencies Table */}
            <div className="space-y-2 font-sans">
              <div className="text-xs font-bold text-[#B42318] uppercase tracking-wide">
                B. Document Deficiencies & Discrepancies ({deficiencyFindings.length})
              </div>
              <table className="w-full border-collapse border border-[#D9E2EC] text-xs">
                <thead>
                  <tr className="bg-[#FFF5D9] text-[#946200]">
                    <th className="border border-[#D9E2EC] p-2 text-left w-12">S.No</th>
                    <th className="border border-[#D9E2EC] p-2 text-left w-48">Rule & APH Clause</th>
                    <th className="border border-[#D9E2EC] p-2 text-left">Description of Deficiency</th>
                    <th className="border border-[#D9E2EC] p-2 text-left">Evidence / Discrepancy Found</th>
                  </tr>
                </thead>
                <tbody>
                  {deficiencyFindings.map((f, i) => (
                    <tr key={f.id}>
                      <td className="border border-[#D9E2EC] p-2 text-center font-bold">{i + 1}</td>
                      <td className="border border-[#D9E2EC] p-2 font-mono text-[11px] font-bold text-[#17365D]">
                        {f.rule_id}
                        <div className="text-[10px] text-[#667085] font-sans font-normal mt-0.5">{f.rule_clause}</div>
                      </td>
                      <td className="border border-[#D9E2EC] p-2 font-semibold text-[#243447]">
                        {f.title}
                        <div className="text-[11px] text-[#667085] font-normal mt-0.5">{f.explanation}</div>
                      </td>
                      <td className="border border-[#D9E2EC] p-2 font-sans text-[11px] text-[#243447] bg-[#F7F9FC]">
                        {f.why_evidence}
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>

            {/* Editable Officer Directives */}
            <div className="space-y-2 font-sans">
              <div className="text-xs font-bold text-[#17365D] uppercase tracking-wide">
                C. Scrutiny Committee Directives & Next Steps
              </div>
              <textarea
                value={remarks}
                onChange={(e) => setRemarks(e.target.value)}
                rows={3}
                className="w-full border border-[#D9E2EC] rounded p-2 text-xs font-sans text-[#243447] focus:outline-none focus:border-[#245A8D] bg-white"
              />
            </div>

            {/* Signature Block */}
            <div className="pt-6 font-sans text-xs flex justify-between items-end">
              <div className="text-[#667085] text-[11px]">
                <div>Computer Generated Scrutiny Letter</div>
                <div>Application ID: {application.application_number}</div>
              </div>
              <div className="text-right space-y-1">
                <div className="font-bold text-[#17365D]">Prof. S. R. Sharma</div>
                <div className="text-[#667085]">Senior Scrutiny Officer</div>
                <div className="text-[#667085]">AICTE Approvals Bureau</div>
              </div>
            </div>

          </div>

        </div>

        {/* Modal Actions Footer */}
        <div className="bg-[#F7F9FC] border-t border-[#D9E2EC] px-6 py-3 flex items-center justify-between">
          <div className="text-xs text-[#667085] flex items-center gap-1.5">
            <ShieldCheck className="w-4 h-4 text-[#237A45]" />
            <span>Letter generated using verified APH 2025-26 rules and reviewer dispositions.</span>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={onClose}
              className="px-3.5 py-1.5 rounded border border-[#D9E2EC] text-xs font-semibold text-[#243447] hover:bg-white"
            >
              Cancel
            </button>
            <button
              onClick={handleSaveDraft}
              className="px-3.5 py-1.5 rounded border border-[#245A8D] text-xs font-semibold text-[#245A8D] hover:bg-[#EAF2FA] flex items-center gap-1.5"
            >
              <Save className="w-3.5 h-3.5" />
              <span>{isSavedDraft ? 'Draft Saved!' : 'Save Draft'}</span>
            </button>
            <button
              onClick={handlePrint}
              className="px-4 py-1.5 rounded bg-[#17365D] hover:bg-[#245A8D] text-white text-xs font-semibold flex items-center gap-1.5 shadow-2xs"
            >
              <Printer className="w-3.5 h-3.5" />
              <span>Print / Export PDF</span>
            </button>
          </div>
        </div>

      </div>
    </div>
  );
};
