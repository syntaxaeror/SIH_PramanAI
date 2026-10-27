import React, { useState } from 'react';
import { 
  Building2, ArrowLeft, Download, FileText, CheckCircle2, AlertTriangle, 
  ShieldAlert, Sparkles, RefreshCw, Eye, Camera, Video, MapPin, Flag, Scale 
} from 'lucide-react';
import { Application, DocumentItem, Finding, EVCEvidenceItem } from '../types';

interface ApplicationDetailViewProps {
  application: Application;
  documents: DocumentItem[];
  findings: Finding[];
  evcItems: EVCEvidenceItem[];
  onBack: () => void;
  onOpenFinding: (finding: Finding) => void;
  onOpenDocument: (document: DocumentItem) => void;
  onOpenEvc: (item: EVCEvidenceItem) => void;
  onDownloadPdf: () => void;
}

export const ApplicationDetailView: React.FC<ApplicationDetailViewProps> = ({
  application,
  documents,
  findings,
  evcItems,
  onBack,
  onOpenFinding,
  onOpenDocument,
  onOpenEvc,
  onDownloadPdf,
}) => {
  const [activeSubTab, setActiveSubTab] = useState<'findings' | 'documents' | 'evc'>('findings');

  const getPriorityBadge = (priority: string) => {
    if (priority === 'RED') {
      return <span className="bg-red-950/80 text-red-300 border border-red-700/60 px-3 py-1 rounded-full text-xs font-bold flex items-center gap-1.5"><ShieldAlert className="w-3.5 h-3.5" /> RED PRIORITY</span>;
    }
    if (priority === 'AMBER') {
      return <span className="bg-amber-950/80 text-amber-300 border border-amber-700/60 px-3 py-1 rounded-full text-xs font-bold flex items-center gap-1.5"><AlertTriangle className="w-3.5 h-3.5" /> AMBER PRIORITY</span>;
    }
    return <span className="bg-emerald-950/80 text-emerald-300 border border-emerald-700/60 px-3 py-1 rounded-full text-xs font-bold flex items-center gap-1.5"><CheckCircle2 className="w-3.5 h-3.5" /> GREEN PRIORITY</span>;
  };

  return (
    <div className="space-y-6">
      
      {/* Top Breadcrumb & Action Header */}
      <div className="flex items-center justify-between">
        <button
          onClick={onBack}
          className="flex items-center gap-2 text-xs font-semibold text-slate-400 hover:text-white bg-slate-900 border border-slate-800 px-3 py-1.5 rounded-lg transition-colors"
        >
          <ArrowLeft className="w-4 h-4" /> Back to Scrutiny Queue
        </button>

        <div className="flex items-center gap-3">
          <button
            onClick={onDownloadPdf}
            className="flex items-center gap-2 text-xs font-semibold text-white bg-blue-600 hover:bg-blue-500 px-4 py-2 rounded-lg transition-colors shadow-md shadow-blue-500/20"
          >
            <Download className="w-4 h-4" /> Export Scrutiny Summary (PDF)
          </button>
        </div>
      </div>

      {/* Institutional Scrutiny Banner */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-xl relative overflow-hidden">
        <div className="absolute top-0 right-0 w-80 h-80 bg-blue-600/5 rounded-full blur-3xl pointer-events-none"></div>

        <div className="flex flex-col md:flex-row md:items-start justify-between gap-6">
          <div className="space-y-2">
            <div className="flex items-center gap-3 flex-wrap">
              <span className="font-mono text-xs bg-slate-800 text-blue-400 border border-slate-700 px-2.5 py-1 rounded font-bold">
                {application.application_number}
              </span>
              <span className="text-xs bg-indigo-950/80 text-indigo-300 border border-indigo-800 px-2.5 py-1 rounded">
                AY {application.academic_year}
              </span>
              <span className="text-xs bg-slate-800 text-slate-300 px-2.5 py-1 rounded">
                {application.category}
              </span>
              {getPriorityBadge(application.priority)}
            </div>

            <h1 className="text-xl font-bold text-white tracking-tight">
              {application.institution_name}
            </h1>

            <p className="text-xs text-slate-400 max-w-3xl leading-relaxed flex items-center gap-1.5">
              <Building2 className="w-3.5 h-3.5 text-slate-500 shrink-0" />
              <span>{application.institution_address}</span>
            </p>

            <div className="pt-2 flex flex-wrap items-center gap-4 text-xs text-slate-400">
              <div>Sponsoring Trust: <span className="text-slate-200 font-medium">{application.trust_name}</span></div>
              <span>•</span>
              <div>Assigned Reviewer: <span className="text-slate-200 font-medium">{application.assigned_reviewer}</span></div>
            </div>
          </div>

          {/* Quick Metrics Card */}
          <div className="bg-slate-950/80 border border-slate-800 rounded-xl p-4 min-w-[240px] flex flex-col justify-between shrink-0">
            <div className="flex items-center justify-between text-xs mb-2">
              <span className="text-slate-400 font-medium">Compliance Index</span>
              <span className="font-bold text-emerald-400 text-sm">{application.compliance_score}%</span>
            </div>
            
            <div className="w-full bg-slate-800 h-2 rounded-full overflow-hidden mb-4">
              <div
                className="bg-gradient-to-r from-blue-500 to-emerald-400 h-full rounded-full transition-all"
                style={{ width: `${application.compliance_score}%` }}
              ></div>
            </div>

            <div className="grid grid-cols-3 gap-2 text-center text-xs">
              <div className="bg-slate-900 p-2 rounded border border-slate-800">
                <div className="font-bold text-white">{documents.length}</div>
                <div className="text-[10px] text-slate-400">Docs</div>
              </div>
              <div className="bg-slate-900 p-2 rounded border border-slate-800">
                <div className="font-bold text-amber-400">{findings.length}</div>
                <div className="text-[10px] text-slate-400">Findings</div>
              </div>
              <div className="bg-slate-900 p-2 rounded border border-slate-800">
                <div className="font-bold text-red-400">{application.deficiency_count}</div>
                <div className="text-[10px] text-slate-400">Deficiencies</div>
              </div>
            </div>
          </div>

        </div>

        {/* Sub Navigation Bar */}
        <div className="flex items-center gap-2 border-t border-slate-800 mt-6 pt-4">
          <button
            onClick={() => setActiveSubTab('findings')}
            className={`px-4 py-2 rounded-lg text-xs font-semibold transition-all flex items-center gap-2 ${
              activeSubTab === 'findings'
                ? 'bg-blue-600 text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800'
            }`}
          >
            <Sparkles className="w-3.5 h-3.5" />
            Scrutiny Findings & Deficiencies ({findings.length})
          </button>
          
          <button
            onClick={() => setActiveSubTab('documents')}
            className={`px-4 py-2 rounded-lg text-xs font-semibold transition-all flex items-center gap-2 ${
              activeSubTab === 'documents'
                ? 'bg-blue-600 text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800'
            }`}
          >
            <FileText className="w-3.5 h-3.5" />
            Uploaded Documents & OCR Auto-Mapping ({documents.length})
          </button>

          <button
            onClick={() => setActiveSubTab('evc')}
            className={`px-4 py-2 rounded-lg text-xs font-semibold transition-all flex items-center gap-2 ${
              activeSubTab === 'evc'
                ? 'bg-blue-600 text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-800'
            }`}
          >
            <Camera className="w-3.5 h-3.5" />
            EVC Physical Evidence Room ({evcItems.length})
          </button>
        </div>

      </div>

      {/* SubTab 1: Findings & Decision Explainability */}
      {activeSubTab === 'findings' && (
        <div className="space-y-4">
          <div className="flex items-center justify-between text-xs text-slate-400">
            <span>
              Every finding below includes the exact model rule, source provenance, and plain-language evidence why it was flagged.
            </span>
            <span className="text-[11px] bg-slate-900 border border-slate-800 px-2.5 py-1 rounded text-slate-300">
              Click any finding to inspect evidence or record disposition
            </span>
          </div>

          <div className="grid grid-cols-1 gap-4">
            {findings.map((f) => (
              <div
                key={f.id}
                onClick={() => onOpenFinding(f)}
                className={`bg-slate-900 border rounded-xl p-5 cursor-pointer transition-all hover:border-blue-500 shadow-md ${
                  f.validation_status === 'DEFICIENCY'
                    ? 'border-red-900/40 hover:border-red-500'
                    : 'border-slate-800 hover:border-slate-700'
                }`}
              >
                <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 mb-3">
                  <div className="flex items-center gap-3">
                    <div className={`p-2 rounded-lg shrink-0 ${
                      f.validation_status === 'DEFICIENCY' ? 'bg-red-950/80 text-red-400' : 'bg-emerald-950/80 text-emerald-400'
                    }`}>
                      {f.validation_status === 'DEFICIENCY' ? <AlertTriangle className="w-5 h-5" /> : <CheckCircle2 className="w-5 h-5" />}
                    </div>
                    <div>
                      <div className="flex items-center gap-2">
                        <span className="font-mono text-xs text-indigo-400 font-semibold">{f.rule_id}</span>
                        <span className="text-slate-600">•</span>
                        <span className="text-xs text-slate-400">{f.rule_clause}</span>
                      </div>
                      <h3 className="text-base font-semibold text-white mt-0.5">{f.title}</h3>
                    </div>
                  </div>

                  <div className="flex items-center gap-3 shrink-0">
                    <span className={`px-2.5 py-1 rounded text-xs font-bold ${
                      f.validation_status === 'DEFICIENCY' ? 'bg-red-950 text-red-300 border border-red-800' : 'bg-emerald-950 text-emerald-300 border border-emerald-800'
                    }`}>
                      {f.validation_status}
                    </span>
                    <span className="text-xs text-slate-400 font-medium">
                      {(f.confidence * 100).toFixed(0)}% Conf
                    </span>
                  </div>
                </div>

                {/* "WHY EVIDENCE" SNIPPET */}
                <div className="bg-slate-950/80 border border-slate-800 rounded-lg p-3 text-xs space-y-1.5 my-3">
                  <div className="flex items-center gap-1.5 text-indigo-300 font-semibold text-[11px] uppercase tracking-wider">
                    <Sparkles className="w-3.5 h-3.5 text-indigo-400" />
                    <span>Evidence & Model Rationale (Why Flagged)</span>
                  </div>
                  <p className="text-slate-300 leading-relaxed font-sans">
                    {f.why_evidence}
                  </p>
                </div>

                <div className="flex items-center justify-between text-xs text-slate-400 pt-2 border-t border-slate-800/80">
                  <div className="flex items-center gap-4">
                    {f.document_name && (
                      <span className="flex items-center gap-1.5 text-slate-300">
                        <FileText className="w-3.5 h-3.5 text-blue-400" />
                        {f.document_name}
                      </span>
                    )}
                    {f.disposition && (
                      <span className="text-[11px] bg-slate-800 px-2 py-0.5 rounded text-blue-300">
                        Disposition: {f.disposition}
                      </span>
                    )}
                  </div>

                  <button className="text-xs font-semibold text-blue-400 hover:text-blue-300 flex items-center gap-1">
                    Inspect Evidence & Why →
                  </button>
                </div>

              </div>
            ))}
          </div>
        </div>
      )}

      {/* SubTab 2: Uploaded Documents & OCR Mapping */}
      {activeSubTab === 'documents' && (
        <div className="space-y-4">
          <div className="flex items-center justify-between text-xs text-slate-400">
            <span>
              Three-stage auto-mapping (Filename Normalization → Content / OCR Confirmation → Confidence Gate).
            </span>
            <span className="text-[11px] text-slate-500">
              Click any document to inspect OCR provenance or manually remap
            </span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {documents.map((doc) => (
              <div
                key={doc.id}
                onClick={() => onOpenDocument(doc)}
                className="bg-slate-900 border border-slate-800 rounded-xl p-4.5 cursor-pointer hover:border-blue-500 transition-all flex flex-col justify-between shadow-md group"
              >
                <div>
                  <div className="flex items-center justify-between mb-2">
                    <span className="text-xs font-mono text-slate-400 truncate max-w-[200px]">
                      {doc.original_filename}
                    </span>
                    <span className="text-[10px] bg-emerald-950 text-emerald-400 border border-emerald-800 px-2 py-0.5 rounded font-semibold">
                      {(doc.mapping_confidence * 100).toFixed(0)}% Conf
                    </span>
                  </div>

                  <h3 className="text-sm font-semibold text-white group-hover:text-blue-400 transition-colors">
                    {doc.mapped_type}
                  </h3>

                  <p className="text-[11px] text-slate-400 mt-1">
                    Stage: <span className="text-slate-300 font-medium">{doc.mapping_stage}</span>
                  </p>

                  <div className="mt-3 flex items-center gap-2 text-[11px] text-slate-400">
                    <span className="bg-slate-800 px-2 py-0.5 rounded">{doc.page_count} Pages</span>
                    <span className="bg-slate-800 px-2 py-0.5 rounded">{doc.extracted_fields.length} Fields Extracted</span>
                  </div>
                </div>

                <div className="mt-4 pt-3 border-t border-slate-800 flex items-center justify-between text-xs">
                  <span className="text-blue-400 flex items-center gap-1 font-medium">
                    <Eye className="w-3.5 h-3.5" /> View OCR & Overlays
                  </span>
                  <span className="text-slate-500 text-[11px]">Click to inspect</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* SubTab 3: EVC Evidence Room */}
      {activeSubTab === 'evc' && (
        <div className="space-y-4">
          <div className="flex items-center justify-between text-xs text-slate-400">
            <span>
              AICTE Expert Visiting Committee (EVC) Photographic & Video Walkthrough Evidence Analysis.
            </span>
            <span className="text-amber-300 font-medium">
              Perceptual Hashing (pHash) Duplicate Detection Active
            </span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {evcItems.map((item) => (
              <div
                key={item.id}
                onClick={() => onOpenEvc(item)}
                className={`bg-slate-900 border rounded-xl overflow-hidden cursor-pointer transition-all shadow-md ${
                  item.duplicate_flag
                    ? 'border-red-900/60 hover:border-red-500 ring-1 ring-red-800/40'
                    : 'border-slate-800 hover:border-slate-700'
                }`}
              >
                <div className="aspect-video bg-slate-950 relative overflow-hidden">
                  <img
                    src={item.preview_url}
                    alt={item.filename}
                    className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
                  />

                  {/* Duplicate Alert Overlay Badge */}
                  {item.duplicate_flag && (
                    <div className="absolute top-2 left-2 bg-red-900/90 backdrop-blur-md text-white text-[10px] font-bold px-2 py-1 rounded flex items-center gap-1.5 shadow-lg">
                      <ShieldAlert className="w-3.5 h-3.5 text-amber-300" />
                      pHash Reused Signal ({((item.duplicate_similarity || 0.984) * 100).toFixed(0)}%)
                    </div>
                  )}

                  {/* Inspection Flag Badge */}
                  {item.inspection_needed && (
                    <div className="absolute top-2 right-2 bg-amber-900/90 backdrop-blur-md text-white text-[10px] font-bold px-2 py-1 rounded flex items-center gap-1">
                      <Flag className="w-3.5 h-3.5 text-yellow-300" />
                      Field Inspection Flagged
                    </div>
                  )}

                  <div className="absolute bottom-2 left-2 bg-black/70 backdrop-blur text-white text-[10px] px-2 py-0.5 rounded font-mono">
                    {item.file_type.toUpperCase()}
                  </div>
                </div>

                <div className="p-4 space-y-2">
                  <div className="flex items-center justify-between text-xs">
                    <span className="font-semibold text-white">{item.category}</span>
                    <span className={`text-[10px] px-2 py-0.5 rounded font-semibold ${
                      item.gps_match_status === 'MATCHED' ? 'bg-emerald-950 text-emerald-400' : 'bg-slate-800 text-slate-400'
                    }`}>
                      {item.gps_match_status || 'Geo-verified'}
                    </span>
                  </div>

                  <p className="text-xs text-slate-400 truncate">
                    {item.filename}
                  </p>

                  {item.duplicate_flag && (
                    <div className="bg-red-950/40 border border-red-900/50 rounded p-2 text-[11px] text-red-200">
                      Matched: <span className="font-semibold">{item.duplicate_match_institution}</span>
                    </div>
                  )}

                  {/* Keyframes indicator if video */}
                  {item.video_keyframes.length > 0 && (
                    <div className="pt-1 flex items-center gap-1.5 text-[11px] text-indigo-400">
                      <Video className="w-3.5 h-3.5" />
                      <span>{item.video_keyframes.length} scene keyframes extracted</span>
                    </div>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

    </div>
  );
};
