import React, { useState } from 'react';
import { X, AlertTriangle, CheckCircle2, FileText, Scale, Sparkles, Send, ShieldAlert, Info } from 'lucide-react';
import { Finding } from '../types';

interface ExplainabilityModalProps {
  finding: Finding | null;
  onClose: () => void;
  onUpdateDisposition: (findingId: string, disposition: string, notes: string) => Promise<void>;
}

export const ExplainabilityModal: React.FC<ExplainabilityModalProps> = ({
  finding,
  onClose,
  onUpdateDisposition,
}) => {
  if (!finding) return null;

  const [disposition, setDisposition] = useState(finding.disposition || 'ACCEPTED');
  const [notes, setNotes] = useState(finding.reviewer_notes || '');
  const [saving, setSaving] = useState(false);
  const [savedSuccess, setSavedSuccess] = useState(false);

  const handleSave = async () => {
    setSaving(true);
    await onUpdateDisposition(finding.id, disposition, notes);
    setSaving(false);
    setSavedSuccess(true);
    setTimeout(() => {
      setSavedSuccess(false);
      onClose();
    }, 800);
  };

  const getPriorityBadge = (priority: string) => {
    if (priority === 'RED') {
      return <span className="bg-red-950/80 text-red-300 border border-red-700/60 px-2.5 py-1 rounded text-xs font-bold flex items-center gap-1.5"><ShieldAlert className="w-3.5 h-3.5" /> High Review Priority (RED)</span>;
    }
    if (priority === 'AMBER') {
      return <span className="bg-amber-950/80 text-amber-300 border border-amber-700/60 px-2.5 py-1 rounded text-xs font-bold flex items-center gap-1.5"><AlertTriangle className="w-3.5 h-3.5" /> Medium Review Priority (AMBER)</span>;
    }
    return <span className="bg-emerald-950/80 text-emerald-300 border border-emerald-700/60 px-2.5 py-1 rounded text-xs font-bold flex items-center gap-1.5"><CheckCircle2 className="w-3.5 h-3.5" /> Normal Verification (GREEN)</span>;
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
      <div className="bg-slate-900 border border-slate-700 rounded-xl max-w-3xl w-full shadow-2xl overflow-hidden flex flex-col max-h-[90vh] animate-in fade-in duration-200">
        
        {/* Modal Header */}
        <div className="bg-slate-950/90 px-6 py-4 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="p-2 rounded-lg bg-indigo-900/40 border border-indigo-700/50 text-indigo-400">
              <Sparkles className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-xs font-mono text-indigo-400">{finding.rule_id}</span>
                <span className="text-slate-500">•</span>
                <span className="text-xs text-slate-400">Decision & Evidence Inspector</span>
              </div>
              <h3 className="text-base font-semibold text-white mt-0.5">{finding.title}</h3>
            </div>
          </div>
          <button
            onClick={onClose}
            className="text-slate-400 hover:text-white p-1 rounded-lg hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Modal Body */}
        <div className="p-6 overflow-y-auto space-y-6 text-sm">
          
          {/* Priority & Status Bar */}
          <div className="flex items-center justify-between bg-slate-950/60 p-3.5 rounded-lg border border-slate-800">
            <div className="flex items-center gap-3">
              {getPriorityBadge(finding.priority)}
              <div className="text-xs">
                <span className="text-slate-400">Validation Status: </span>
                <span className={`font-semibold ${finding.validation_status === 'DEFICIENCY' ? 'text-red-400' : 'text-emerald-400'}`}>
                  {finding.validation_status}
                </span>
              </div>
            </div>
            <div className="text-xs text-slate-400">
              Confidence: <span className="font-semibold text-white">{(finding.confidence * 100).toFixed(0)}%</span>
            </div>
          </div>

          {/* KEY SECTION: WHY DID THE MODEL MAKE THIS DECISION? */}
          <div className="bg-indigo-950/30 border border-indigo-800/60 rounded-xl p-4.5 space-y-3">
            <div className="flex items-center gap-2 text-indigo-300 font-semibold text-sm">
              <Sparkles className="w-4 h-4 text-indigo-400" />
              <span>Why Was This Flagged? (Model & Evidence Breakdown)</span>
            </div>
            <p className="text-slate-200 leading-relaxed text-sm bg-slate-950/40 p-3 rounded-lg border border-indigo-900/30">
              {finding.why_evidence}
            </p>
            <p className="text-xs text-slate-400 leading-normal">
              {finding.explanation}
            </p>
          </div>

          {/* Comparative Value Diff (Extracted vs Expected) */}
          <div className="grid grid-cols-2 gap-4">
            <div className="bg-slate-950/70 border border-slate-800 rounded-lg p-3.5">
              <span className="text-xs font-medium text-slate-400 uppercase tracking-wider block mb-1">
                Extracted Document Value
              </span>
              <div className="font-mono text-sm font-semibold text-amber-300 break-words">
                {finding.extracted_value || 'None extracted'}
              </div>
              {finding.document_name && (
                <div className="mt-2 text-[11px] text-slate-400 flex items-center gap-1.5">
                  <FileText className="w-3.5 h-3.5 text-blue-400" />
                  <span className="truncate">{finding.document_name}</span>
                  {finding.page_number && <span className="text-indigo-400 font-medium">(Page {finding.page_number})</span>}
                </div>
              )}
            </div>

            <div className="bg-slate-950/70 border border-slate-800 rounded-lg p-3.5">
              <span className="text-xs font-medium text-slate-400 uppercase tracking-wider block mb-1">
                Expected / Portal Benchmark Value
              </span>
              <div className="font-mono text-sm font-semibold text-emerald-300 break-words">
                {finding.expected_value || 'Compliant with prescribed APH norms'}
              </div>
              <div className="mt-2 text-[11px] text-slate-400 flex items-center gap-1.5">
                <Scale className="w-3.5 h-3.5 text-purple-400" />
                <span className="truncate">AICTE Approval Process Handbook</span>
              </div>
            </div>
          </div>

          {/* Applicable Rule Clause & Regulatory Source */}
          <div className="bg-slate-950/50 border border-slate-800 rounded-lg p-3.5 flex items-start gap-3">
            <Scale className="w-4 h-4 text-slate-400 mt-0.5 shrink-0" />
            <div>
              <div className="text-xs font-medium text-slate-400">Authoritative AICTE Rule & Handbook Source</div>
              <div className="text-xs font-semibold text-slate-200 mt-0.5">{finding.rule_clause}</div>
              <div className="text-[11px] text-slate-400 mt-1">
                Suggested Reviewer Action: <span className="text-slate-300">{finding.suggested_action}</span>
              </div>
            </div>
          </div>

          {/* Reviewer Disposition Section */}
          <div className="border-t border-slate-800 pt-4 space-y-3">
            <div className="flex items-center justify-between">
              <label className="text-xs font-semibold text-slate-300 uppercase tracking-wider">
                Reviewer Determination & Disposition
              </label>
              <span className="text-[11px] text-slate-500">Recorded into immutable audit trail</span>
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="text-xs text-slate-400 block mb-1">Disposition Action</label>
                <select
                  value={disposition}
                  onChange={(e) => setDisposition(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-sm text-slate-200 focus:outline-none focus:border-blue-500"
                >
                  <option value="ACCEPTED">ACCEPTED (Concur with Finding)</option>
                  <option value="DEFICIENCY_UPHELD">DEFICIENCY UPHELD (Requires Scrutiny Letter)</option>
                  <option value="NEED_CLARIFICATION">NEED CLARIFICATION (Query to Institute)</option>
                  <option value="DISMISSED">DISMISSED (Explanation Acceptable)</option>
                </select>
              </div>

              <div>
                <label className="text-xs text-slate-400 block mb-1">Reviewer Justification / Order Note</label>
                <textarea
                  value={notes}
                  onChange={(e) => setNotes(e.target.value)}
                  placeholder="Enter detailed reviewer rationale for the scrutiny record..."
                  rows={2}
                  className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-1.5 text-xs text-slate-200 focus:outline-none focus:border-blue-500 resize-none"
                />
              </div>
            </div>
          </div>

        </div>

        {/* Modal Footer */}
        <div className="bg-slate-950/80 px-6 py-3 border-t border-slate-800 flex items-center justify-between">
          <div className="text-[11px] text-slate-500 flex items-center gap-1.5">
            <Info className="w-3.5 h-3.5" />
            <span>AI acts in advisory mode. Reviewer retains statutory judgment.</span>
          </div>
          <div className="flex items-center gap-3">
            <button
              onClick={onClose}
              className="px-4 py-2 rounded-lg text-xs font-medium text-slate-300 hover:bg-slate-800 transition-colors"
            >
              Close
            </button>
            <button
              onClick={handleSave}
              disabled={saving}
              className="px-5 py-2 rounded-lg text-xs font-semibold bg-blue-600 hover:bg-blue-500 text-white transition-colors flex items-center gap-1.5 disabled:opacity-50 shadow-md shadow-blue-500/20"
            >
              {saving ? 'Updating...' : savedSuccess ? 'Saved!' : 'Confirm Disposition'}
            </button>
          </div>
        </div>

      </div>
    </div>
  );
};
