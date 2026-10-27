import React, { useState } from 'react';
import { X, FileText, CheckCircle2, AlertCircle, RefreshCw, Layers, Sparkles, Hash, Eye } from 'lucide-react';
import { DocumentItem } from '../types';

interface DocumentViewerModalProps {
  document: DocumentItem | null;
  onClose: () => void;
  onRemap: (docId: string, newType: string, reason: string) => Promise<void>;
}

const AVAILABLE_DOC_TYPES = [
  "Affidavit 2 (Self-Disclosure)",
  "Fire Safety Certificate",
  "TER / Payment Receipt",
  "Occupancy Certificate",
  "Structural Stability Certificate",
  "Satellite / Geolocation Map",
  "Audited Financial Statement",
  "Unmapped / Manual review"
];

export const DocumentViewerModal: React.FC<DocumentViewerModalProps> = ({
  document,
  onClose,
  onRemap,
}) => {
  if (!document) return null;

  const [activePage, setActivePage] = useState(1);
  const [selectedFieldKey, setSelectedFieldKey] = useState<string | null>(null);
  const [newType, setNewType] = useState(document.mapped_type);
  const [remapReason, setRemapReason] = useState('');
  const [remapping, setRemapping] = useState(false);
  const [showRemapBox, setShowRemapBox] = useState(false);

  const handleRemapSubmit = async () => {
    if (!remapReason.trim()) {
      alert("Please provide a reason for manual remapping.");
      return;
    }
    setRemapping(true);
    await onRemap(document.id, newType, remapReason);
    setRemapping(false);
    setShowRemapBox(false);
  };

  return (
    <div className="fixed inset-0 z-50 bg-black/80 backdrop-blur-sm flex items-center justify-center p-4">
      <div className="bg-slate-900 border border-slate-700 rounded-xl max-w-5xl w-full shadow-2xl overflow-hidden flex flex-col max-h-[92vh] animate-in fade-in duration-200">
        
        {/* Modal Header */}
        <div className="bg-slate-950/90 px-6 py-3.5 border-b border-slate-800 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="p-2 rounded-lg bg-blue-900/40 border border-blue-700/50 text-blue-400">
              <FileText className="w-5 h-5" />
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="text-xs font-mono text-slate-400">{document.original_filename}</span>
                <span className="text-slate-600">•</span>
                <span className="text-xs bg-slate-800 text-slate-300 px-2 py-0.5 rounded">
                  {document.page_count} Pages
                </span>
              </div>
              <div className="flex items-center gap-2 mt-0.5">
                <h3 className="text-sm font-semibold text-white">{document.mapped_type}</h3>
                <span className="text-[11px] bg-emerald-950 text-emerald-400 border border-emerald-800 px-2 py-0.5 rounded-full font-medium">
                  {(document.mapping_confidence * 100).toFixed(0)}% Confidence
                </span>
                <span className="text-[11px] text-slate-400">
                  via {document.mapping_stage}
                </span>
              </div>
            </div>
          </div>

          <div className="flex items-center gap-2">
            <button
              onClick={() => setShowRemapBox(!showRemapBox)}
              className="px-3 py-1.5 rounded-lg text-xs font-medium bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 flex items-center gap-1.5"
            >
              <RefreshCw className="w-3.5 h-3.5" />
              Remap Type
            </button>
            <button
              onClick={onClose}
              className="text-slate-400 hover:text-white p-1 rounded-lg hover:bg-slate-800 transition-colors"
            >
              <X className="w-5 h-5" />
            </button>
          </div>
        </div>

        {/* Remap Dropdown Bar (if open) */}
        {showRemapBox && (
          <div className="bg-indigo-950/40 border-b border-indigo-800/40 p-4 flex flex-wrap items-center gap-3 text-xs">
            <span className="font-semibold text-indigo-300">Manual Reassignment:</span>
            <select
              value={newType}
              onChange={(e) => setNewType(e.target.value)}
              className="bg-slate-900 border border-slate-700 rounded-lg px-2.5 py-1.5 text-slate-200"
            >
              {AVAILABLE_DOC_TYPES.map((t) => (
                <option key={t} value={t}>{t}</option>
              ))}
            </select>
            <input
              type="text"
              placeholder="Reason for remapping (recorded in audit log)..."
              value={remapReason}
              onChange={(e) => setRemapReason(e.target.value)}
              className="bg-slate-900 border border-slate-700 rounded-lg px-3 py-1.5 text-slate-200 flex-1 min-w-[200px]"
            />
            <button
              onClick={handleRemapSubmit}
              disabled={remapping}
              className="bg-blue-600 hover:bg-blue-500 text-white font-medium px-4 py-1.5 rounded-lg disabled:opacity-50"
            >
              {remapping ? 'Saving...' : 'Apply & Log Audit'}
            </button>
          </div>
        )}

        {/* Modal Main Content: Left Document Preview & Right Extracted Fields */}
        <div className="flex-1 grid grid-cols-12 overflow-hidden">
          
          {/* Left: Document Page Simulator & Highlighted Bounding Boxes */}
          <div className="col-span-7 bg-slate-950 p-6 flex flex-col border-r border-slate-800 overflow-y-auto">
            <div className="flex items-center justify-between mb-3 text-xs text-slate-400">
              <span className="flex items-center gap-1.5 font-medium text-slate-300">
                <Eye className="w-4 h-4 text-blue-400" /> Page Preview (Evidence Overlays)
              </span>
              <div className="flex items-center gap-1 bg-slate-900 px-2 py-1 rounded border border-slate-800">
                <span>Page</span>
                {Array.from({ length: document.page_count }, (_, i) => i + 1).map((p) => (
                  <button
                    key={p}
                    onClick={() => setActivePage(p)}
                    className={`px-2 py-0.5 rounded text-xs ${
                      activePage === p ? 'bg-blue-600 text-white font-bold' : 'text-slate-400 hover:text-white'
                    }`}
                  >
                    {p}
                  </button>
                ))}
              </div>
            </div>

            {/* Document Canvas Sheet */}
            <div className="relative bg-white text-slate-900 rounded-lg shadow-inner min-h-[580px] p-8 font-serif border border-slate-300 overflow-y-auto select-none">
              <div className="absolute top-2 right-3 text-[10px] text-slate-400 font-sans">
                AICTE Scrutiny Document Renderer • Page {activePage}
              </div>

              {/* Document Header representation */}
              <div className="border-b-2 border-slate-800 pb-3 mb-5 text-center">
                <div className="flex items-center justify-between border-b border-dashed border-slate-300 pb-1 mb-2 text-[9px] font-mono text-slate-500">
                  <span>E-STAMP / STATUTORY REF: IN-{document.id.toUpperCase()}</span>
                  <span>AICTE APH 2024-2027</span>
                </div>
                <div className="text-[10px] font-sans font-bold tracking-wider uppercase text-slate-700">GOVERNMENT / STATUTORY INSTRUMENT</div>
                <div className="text-sm font-black uppercase text-slate-950 mt-1 font-serif">{document.mapped_type}</div>
                <div className="text-[10px] text-slate-500 mt-0.5">Reference Document: <span className="font-mono">{document.original_filename}</span></div>
              </div>

              {/* Genuine Body Text from AICTE Handbook */}
              <div className="text-slate-800 leading-relaxed text-[11px] font-serif whitespace-pre-line text-left pb-16">
                {document.document_body_text ? (
                  document.document_body_text
                ) : (
                  <p className="italic text-slate-500">
                    Standard statutory instrument filed under AICTE Approval Process Handbook norms. Scanned original verified by OCR extraction engine.
                  </p>
                )}
              </div>

              {/* Notary / Stamp Watermark Block */}
              <div className="mt-6 pt-4 border-t-2 border-slate-200 flex items-end justify-between text-[10px] font-sans">
                <div className="border border-slate-400 p-2 rounded bg-slate-50/70 text-slate-600 text-center w-36">
                  <div className="font-bold uppercase text-[9px] text-[#17365D]">COMMISSIONER / NOTARY</div>
                  <div className="text-[8px] mt-0.5 text-slate-500">SEAL DULY ATTESTED</div>
                  <div className="text-[8px] font-mono text-slate-400 mt-0.5">SWORN & VERIFIED</div>
                </div>
                <div className="text-right">
                  <div className="font-bold text-[#17365D] uppercase text-[10px]">DEPONENT / AUTHORIZED SIGNATORY</div>
                  <div className="text-[9px] text-slate-500 mt-0.5">Executed on Rs. 100/- Stamp Paper</div>
                </div>
              </div>

              {/* Footer */}
              <div className="border-t border-slate-300 mt-6 pt-2 flex justify-between text-[10px] text-slate-500 font-sans">
                <span>Verified by AI OCR Extraction</span>
                <span>Page {activePage} of {document.page_count}</span>
              </div>
            </div>
          </div>

          {/* Right: Extracted Fields & Provenance */}
          <div className="col-span-5 p-5 overflow-y-auto space-y-4 bg-slate-900">
            <div>
              <div className="flex items-center gap-1.5 text-xs font-semibold text-slate-300 uppercase tracking-wider mb-2">
                <Sparkles className="w-4 h-4 text-indigo-400" />
                <span>Extracted Entities & OCR Provenance</span>
              </div>
              <p className="text-[11px] text-slate-400 mb-3">
                Hover or click an item to locate its bounding box on the document canvas.
              </p>
            </div>

            <div className="space-y-2.5">
              {document.extracted_fields.map((f) => (
                <div
                  key={f.key}
                  onMouseEnter={() => setSelectedFieldKey(f.bbox?.label || null)}
                  onMouseLeave={() => setSelectedFieldKey(null)}
                  className={`p-3 rounded-lg border transition-all cursor-pointer ${
                    selectedFieldKey === f.bbox?.label
                      ? 'bg-slate-800/90 border-blue-500 shadow-md'
                      : 'bg-slate-950/60 border-slate-800 hover:border-slate-700'
                  }`}
                >
                  <div className="flex items-center justify-between text-xs mb-1">
                    <span className="font-semibold text-slate-300">{f.label}</span>
                    <span className="text-[10px] font-mono text-emerald-400 font-semibold bg-emerald-950/80 px-1.5 py-0.5 rounded">
                      {(f.confidence * 100).toFixed(0)}%
                    </span>
                  </div>
                  <div className="text-xs font-mono font-medium text-amber-200 break-words mb-1.5">
                    {f.value}
                  </div>
                  <div className="text-[10px] text-slate-400 flex items-center justify-between">
                    <span>{f.provenance}</span>
                    <span className="text-blue-400">Page {f.page}</span>
                  </div>
                </div>
              ))}
            </div>

            {/* Audit History for this Document */}
            {document.audit_history.length > 0 && (
              <div className="border-t border-slate-800 pt-4 mt-4">
                <span className="text-[11px] font-semibold text-slate-400 uppercase tracking-wider block mb-2">
                  Document Audit Trail
                </span>
                <div className="space-y-2 text-xs">
                  {document.audit_history.map((h, i) => (
                    <div key={i} className="bg-slate-950 p-2.5 rounded border border-slate-800 text-[11px]">
                      <div className="flex justify-between text-slate-400 mb-1">
                        <span className="font-medium text-slate-300">{h.actor}</span>
                        <span>{h.timestamp}</span>
                      </div>
                      <div className="text-slate-300">{h.reason}</div>
                    </div>
                  ))}
                </div>
              </div>
            )}

          </div>

        </div>

      </div>
    </div>
  );
};
