import React, { useState } from 'react';
import { Upload, FileSpreadsheet, Archive, CheckCircle2, AlertCircle, Sparkles, Building2, Layers, RefreshCw } from 'lucide-react';

interface IngestionViewProps {
  onSimulateImport: (payload: any) => Promise<any>;
}

export const IngestionView: React.FC<IngestionViewProps> = ({ onSimulateImport }) => {
  const [instName, setInstName] = useState('National Institute of Advanced Technology & Management');
  const [appCategory, setAppCategory] = useState('Extension of Approval (EoA)');
  const [trustName, setTrustName] = useState('National Educational & Scientific Research Society');
  const [address, setAddress] = useState('Sector 62, Institutional Area, Noida, Uttar Pradesh - 201309');
  const [isImporting, setIsImporting] = useState(false);
  const [importResult, setImportResult] = useState<any>(null);

  const handleImportSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsImporting(true);
    try {
      const res = await onSimulateImport({
        institution_name: instName,
        category: appCategory,
        trust_name: trustName,
        address: address,
      });
      setImportResult(res);
    } catch (err) {
      console.error(err);
    } finally {
      setIsImporting(false);
    }
  };

  return (
    <div className="space-y-6">
      
      {/* Header Banner */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-xl">
        <div className="flex items-center gap-2 text-indigo-400 text-xs font-semibold uppercase tracking-wider mb-1">
          <Upload className="w-4 h-4" />
          <span>Section 4: Data Ingestion & Batch Document Package Processor</span>
        </div>
        <h2 className="text-xl font-bold text-white tracking-tight">
          Import Existing Application Records & Document Archives
        </h2>
        <p className="text-xs text-slate-400 mt-1 max-w-2xl">
          Ingest pre-existing institutional applications and ZIP document packages from the primary submission repository. 
          Per-row schema validation, duplicate detection, and three-stage auto-mapping run idempotently.
        </p>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-12 gap-6">
        
        {/* Left: Controlled Import Form */}
        <div className="md:col-span-7 bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-md space-y-4">
          <div className="flex items-center justify-between border-b border-slate-800 pb-3">
            <div className="flex items-center gap-2 text-sm font-semibold text-white">
              <FileSpreadsheet className="w-4.5 h-4.5 text-blue-400" />
              <span>Import Metadata & Supporting Document Package</span>
            </div>
            <span className="text-[11px] bg-slate-800 text-slate-300 px-2.5 py-0.5 rounded">
              CSV / ZIP Ingestion
            </span>
          </div>

          <form onSubmit={handleImportSubmit} className="space-y-4 text-xs">
            <div>
              <label className="text-slate-300 font-semibold block mb-1">
                Institution Name (From Submitted Record)
              </label>
              <input
                type="text"
                value={instName}
                onChange={(e) => setInstName(e.target.value)}
                required
                className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-blue-500"
              />
            </div>

            <div className="grid grid-cols-2 gap-4">
              <div>
                <label className="text-slate-300 font-semibold block mb-1">
                  Application Category
                </label>
                <select
                  value={appCategory}
                  onChange={(e) => setAppCategory(e.target.value)}
                  className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-blue-500"
                >
                  <option value="Extension of Approval (EoA)">Extension of Approval (EoA)</option>
                  <option value="Intake Increase">Intake Increase</option>
                  <option value="New Technical Institution">New Technical Institution</option>
                </select>
              </div>

              <div>
                <label className="text-slate-300 font-semibold block mb-1">
                  Academic Cycle
                </label>
                <input
                  type="text"
                  value="2025-26"
                  disabled
                  className="w-full bg-slate-900 border border-slate-800 rounded-lg px-3 py-2 text-slate-400 font-mono"
                />
              </div>
            </div>

            <div>
              <label className="text-slate-300 font-semibold block mb-1">
                Registered Sponsoring Trust / Society
              </label>
              <input
                type="text"
                value={trustName}
                onChange={(e) => setTrustName(e.target.value)}
                required
                className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-blue-500"
              />
            </div>

            <div>
              <label className="text-slate-300 font-semibold block mb-1">
                Campus Postal Address
              </label>
              <input
                type="text"
                value={address}
                onChange={(e) => setAddress(e.target.value)}
                required
                className="w-full bg-slate-950 border border-slate-700 rounded-lg px-3 py-2 text-slate-200 focus:outline-none focus:border-blue-500"
              />
            </div>

            {/* Simulated File Upload Dropzone */}
            <div className="border-2 border-dashed border-slate-700 rounded-xl p-5 text-center bg-slate-950/40 hover:bg-slate-950/70 transition-colors">
              <Archive className="w-8 h-8 text-blue-400 mx-auto mb-2" />
              <div className="text-slate-200 font-medium mb-1">
                Attach Supporting Document ZIP & EVC Media Package
              </div>
              <p className="text-[11px] text-slate-500">
                Supports .zip containing PDFs and geotagged JPGs (Auto-extracted with path traversal protection)
              </p>
            </div>

            <button
              type="submit"
              disabled={isImporting}
              className="w-full py-2.5 rounded-lg text-xs font-semibold bg-blue-600 hover:bg-blue-500 text-white transition-colors flex items-center justify-center gap-2 shadow-md shadow-blue-500/20 disabled:opacity-50"
            >
              {isImporting ? (
                <>
                  <RefreshCw className="w-4 h-4 animate-spin" /> Ingesting & Running Auto-Mapping...
                </>
              ) : (
                <>
                  <Upload className="w-4 h-4" /> Run Ingestion & Trigger Auto-Mapper
                </>
              )}
            </button>
          </form>

        </div>

        {/* Right: Ingestion Pipeline Specifications & Results */}
        <div className="md:col-span-5 space-y-4">
          
          <div className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-md space-y-3 text-xs">
            <span className="font-semibold text-slate-200 uppercase tracking-wider block">
              Ingestion Validation Architecture
            </span>

            <div className="space-y-2.5 text-slate-300">
              <div className="flex items-start gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                <span><strong>Idempotency:</strong> Re-importing existing applications updates records without generating duplicate IDs.</span>
              </div>
              <div className="flex items-start gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                <span><strong>Path Traversal Defense:</strong> ZIP extractors validate relative paths to eliminate zip-slip vulnerabilities.</span>
              </div>
              <div className="flex items-start gap-2">
                <CheckCircle2 className="w-4 h-4 text-emerald-400 shrink-0 mt-0.5" />
                <span><strong>Metadata Reconciliation:</strong> Cross-checks trust names, carpet area, and declared GPS against uploaded certificates.</span>
              </div>
            </div>
          </div>

          {/* Import Result Notification */}
          {importResult && (
            <div className="bg-emerald-950/40 border border-emerald-800/80 rounded-xl p-5 space-y-2 text-xs animate-in fade-in duration-300">
              <div className="flex items-center gap-2 text-emerald-300 font-bold">
                <CheckCircle2 className="w-4.5 h-4.5 text-emerald-400" />
                <span>Ingestion Successful</span>
              </div>
              <div className="text-slate-300">
                Application Number: <span className="font-mono text-emerald-200 font-bold">{importResult.application_number}</span>
              </div>
              <div className="text-slate-300">
                Status: <span className="text-white font-medium">{importResult.status}</span> (Added to Scrutiny Queue)
              </div>
              <div className="text-[11px] text-slate-400 pt-1">
                Auto-mapped 3 documents and generated initial checklist audit event.
              </div>
            </div>
          )}

        </div>

      </div>

    </div>
  );
};
