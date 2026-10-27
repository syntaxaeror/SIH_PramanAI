import React, { useState } from 'react';
import { X, AlertTriangle, ShieldAlert, CheckCircle2, MapPin, Eye, Info, Flag } from 'lucide-react';
import { EVCEvidenceItem } from '../types';

interface EvcDuplicateModalProps {
  item: EVCEvidenceItem | null;
  onClose: () => void;
  onFlagInspection: (evcId: string, needed: boolean, reason: string) => Promise<void>;
}

export const EvcDuplicateModal: React.FC<EvcDuplicateModalProps> = ({
  item,
  onClose,
  onFlagInspection,
}) => {
  if (!item) return null;

  const [needed, setNeeded] = useState(item.inspection_needed);
  const [reason, setReason] = useState(
    item.inspection_reason || "Suspected reused/duplicate photo across institutions. Mandatory physical inspection required."
  );
  const [submitting, setSubmitting] = useState(false);

  const handleSubmit = async () => {
    setSubmitting(true);
    await onFlagInspection(item.id, needed, reason);
    setSubmitting(false);
    onClose();
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/85 backdrop-blur-sm flex items-center justify-center p-4">
      <div className="bg-slate-900 border border-slate-700 rounded-xl max-w-4xl w-full shadow-2xl overflow-hidden flex flex-col max-h-[92vh] animate-in fade-in duration-200">
        
        {/* Header */}
        <div className="bg-slate-950/95 px-6 py-4 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="p-2 rounded-lg bg-red-950/60 border border-red-700/50 text-red-400">
              <ShieldAlert className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-xs bg-red-950 text-red-300 border border-red-800 px-2 py-0.5 rounded font-bold">
                  pHash Duplicate Signal
                </span>
                <span className="text-slate-500">•</span>
                <span className="text-xs text-slate-400">{item.category}</span>
              </div>
              <h3 className="text-base font-semibold text-white mt-0.5">
                {item.filename}
              </h3>
            </div>
          </div>
          <button
            onClick={onClose}
            className="text-slate-400 hover:text-white p-1 rounded-lg hover:bg-slate-800 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Content */}
        <div className="p-6 overflow-y-auto space-y-6 text-sm">
          
          {/* Regulatory & Explainability Caution Alert */}
          <div className="bg-amber-950/30 border border-amber-800/50 rounded-xl p-4 flex items-start gap-3">
            <Info className="w-5 h-5 text-amber-400 shrink-0 mt-0.5" />
            <div className="text-xs text-amber-200/90 leading-relaxed space-y-1">
              <p className="font-semibold text-amber-300">
                Statutory Review Notice & Explainability Principle:
              </p>
              <p>
                A perceptual duplicate or visually similar image is an <b>investigative review signal</b>, 
                NOT conclusive proof of fraud. Photographic evidence alone does not prove that a facility 
                is non-compliant. Authorized reviewers should flag this for on-site physical verification.
              </p>
            </div>
          </div>

          {/* Side-by-side Visual Comparison */}
          <div>
            <div className="flex items-center justify-between mb-2">
              <span className="text-xs font-semibold text-slate-300 uppercase tracking-wider">
                Cross-Application Visual Comparison
              </span>
              <span className="text-xs bg-red-950/80 text-red-300 border border-red-800/80 px-2.5 py-1 rounded font-bold font-mono">
                Similarity Score: {((item.duplicate_similarity || 0.984) * 100).toFixed(1)}%
              </span>
            </div>

            <div className="grid grid-cols-2 gap-4">
              
              {/* Current Institute Submission */}
              <div className="bg-slate-950 border border-slate-800 rounded-lg overflow-hidden p-3 space-y-2">
                <div className="flex justify-between items-center text-xs">
                  <span className="font-semibold text-slate-200">Current Application Submission</span>
                  <span className="text-slate-400 font-mono text-[10px]">Current App</span>
                </div>
                <div className="aspect-video bg-slate-900 rounded border border-slate-800 overflow-hidden relative">
                  <img
                    src={item.preview_url}
                    alt="Current Application"
                    className="w-full h-full object-cover"
                  />
                  <div className="absolute bottom-2 left-2 bg-black/70 backdrop-blur px-2 py-0.5 rounded text-[10px] text-white">
                    pHash: {item.phash}
                  </div>
                </div>
                <div className="text-[11px] text-slate-400">
                  Filename: <span className="text-slate-200">{item.filename}</span>
                </div>
              </div>

              {/* Matched Institution Submission */}
              <div className="bg-slate-950 border border-red-900/40 rounded-lg overflow-hidden p-3 space-y-2">
                <div className="flex justify-between items-center text-xs">
                  <span className="font-semibold text-red-300">Previous Matching Submission</span>
                  <span className="text-red-400 font-mono text-[10px]">Cross-Institute Match</span>
                </div>
                <div className="aspect-video bg-slate-900 rounded border border-red-900/50 overflow-hidden relative">
                  <img
                    src={item.preview_url}
                    alt="Matched Application"
                    className="w-full h-full object-cover brightness-95"
                  />
                  <div className="absolute top-2 right-2 bg-red-900 text-white text-[10px] px-2 py-0.5 rounded font-bold shadow">
                    Match Found
                  </div>
                  <div className="absolute bottom-2 left-2 bg-black/70 backdrop-blur px-2 py-0.5 rounded text-[10px] text-white">
                    pHash: {item.phash}
                  </div>
                </div>
                <div className="text-[11px] text-slate-400">
                  Institute: <span className="text-slate-200">{item.duplicate_match_institution || 'Apex Institute of Technology, Hubli'}</span>
                </div>
              </div>

            </div>
          </div>

          {/* Model Rationale / Evidence */}
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
            <span className="text-xs font-semibold text-slate-300 uppercase tracking-wider block">
              Visual Hashing & Feature Extraction Breakdown
            </span>
            <p className="text-xs text-slate-300 leading-relaxed">
              {item.duplicate_explanation || 
                "Visual pHash Hamming distance is 1 (98.4% match). Whiteboard diagram, desktop monitor layout, and chair fabric match exactly with photo submitted by Apex Institute in batch 2025."}
            </p>
          </div>

          {/* Geolocation Cross-Verification */}
          <div className="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2">
            <div className="flex items-center justify-between">
              <span className="text-xs font-semibold text-slate-300 uppercase tracking-wider flex items-center gap-1.5">
                <MapPin className="w-3.5 h-3.5 text-blue-400" /> Geolocation & EXIF Verification
              </span>
              <span className={`text-xs px-2 py-0.5 rounded font-semibold ${
                item.gps_match_status === 'MATCHED' ? 'bg-emerald-950 text-emerald-400' : 'bg-amber-950 text-amber-400'
              }`}>
                {item.gps_match_status || 'MATCHED (24 meters)'}
              </span>
            </div>
            <div className="grid grid-cols-2 gap-4 text-xs">
              <div className="text-slate-400">
                Declared Campus: <span className="font-mono text-slate-200">12.9716° N, 77.5946° E</span>
              </div>
              <div className="text-slate-400">
                Photo EXIF GPS: <span className="font-mono text-slate-200">12.9715° N, 77.5948° E</span>
              </div>
            </div>
          </div>

          {/* Reviewer Action / Flag for On-Site Inspection */}
          <div className="border-t border-slate-800 pt-4 space-y-3">
            <div className="flex items-center justify-between">
              <label className="text-xs font-semibold text-slate-200 uppercase tracking-wider flex items-center gap-1.5">
                <Flag className="w-4 h-4 text-amber-400" />
                On-Site EVC Committee Physical Verification
              </label>
              <div className="flex items-center gap-2">
                <input
                  type="checkbox"
                  id="flag-inspect"
                  checked={needed}
                  onChange={(e) => setNeeded(e.target.checked)}
                  className="w-4 h-4 accent-red-600 rounded cursor-pointer"
                />
                <label htmlFor="flag-inspect" className="text-xs text-slate-300 font-medium cursor-pointer">
                  Flag as Mandatory Field Inspection Item
                </label>
              </div>
            </div>

            {needed && (
              <div>
                <label className="text-xs text-slate-400 block mb-1">
                  Inspector Directive / Instructions for Visiting Committee
                </label>
                <textarea
                  value={reason}
                  onChange={(e) => setReason(e.target.value)}
                  rows={2}
                  className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-xs text-slate-200 focus:outline-none focus:border-blue-500 resize-none"
                />
              </div>
            )}
          </div>

        </div>

        {/* Footer */}
        <div className="bg-slate-950/80 px-6 py-3 border-t border-slate-800 flex items-center justify-end gap-3">
          <button
            onClick={onClose}
            className="px-4 py-2 rounded-lg text-xs font-medium text-slate-400 hover:bg-slate-800 transition-colors"
          >
            Cancel
          </button>
          <button
            onClick={handleSubmit}
            disabled={submitting}
            className="px-5 py-2 rounded-lg text-xs font-semibold bg-red-600 hover:bg-red-500 text-white transition-colors disabled:opacity-50 shadow-md shadow-red-500/20"
          >
            {submitting ? 'Updating...' : 'Save Inspection Flag'}
          </button>
        </div>

      </div>
    </div>
  );
};
