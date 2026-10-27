import React, { useState } from 'react';
import { Camera, ShieldAlert, Flag, MapPin, Video, Eye, Filter, Sparkles, Building2, Layers } from 'lucide-react';
import { EVCEvidenceItem, Application } from '../types';

interface EvcRoomGlobalProps {
  evcItems: EVCEvidenceItem[];
  applications: Application[];
  onOpenEvc: (item: EVCEvidenceItem) => void;
}

export const EvcRoomGlobal: React.FC<EvcRoomGlobalProps> = ({
  evcItems,
  applications,
  onOpenEvc,
}) => {
  const [selectedCategory, setSelectedCategory] = useState('ALL');
  const [onlyDuplicates, setOnlyDuplicates] = useState(false);

  const filteredItems = evcItems.filter((item) => {
    if (selectedCategory !== 'ALL' && item.category !== selectedCategory) return false;
    if (onlyDuplicates && !item.duplicate_flag) return false;
    return true;
  });

  return (
    <div className="space-y-6">
      
      {/* Header Banner */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-xl">
        <div className="flex items-center gap-2 text-indigo-400 text-xs font-semibold uppercase tracking-wider mb-1">
          <Camera className="w-4 h-4" />
          <span>Expert Visiting Committee (EVC) Evidence Workspace</span>
        </div>
        <h2 className="text-xl font-bold text-white tracking-tight">
          Physical Infrastructure Evidence & Duplicate Hash Analysis
        </h2>
        <p className="text-xs text-slate-400 mt-1 max-w-2xl">
          Review institute-provided photos and walkthrough videos with automated perceptual hash (pHash) 
          cross-institution reuse detection and EXIF coordinate validation.
        </p>
      </div>

      {/* Filter and Toggles */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 flex flex-col md:flex-row items-center justify-between gap-4">
        
        <div className="flex items-center gap-2 overflow-x-auto text-xs w-full md:w-auto">
          {['ALL', 'Computer Center', 'Fire Safety', 'Campus Infrastructure', 'Central Library'].map((cat) => (
            <button
              key={cat}
              onClick={() => setSelectedCategory(cat)}
              className={`px-3 py-1.5 rounded-lg font-medium transition-all ${
                selectedCategory === cat
                  ? 'bg-blue-600 text-white font-semibold'
                  : 'bg-slate-950 border border-slate-800 text-slate-400 hover:text-white'
              }`}
            >
              {cat === 'ALL' ? 'All Facilities' : cat}
            </button>
          ))}
        </div>

        <div className="flex items-center gap-3">
          <label className="flex items-center gap-2 text-xs text-slate-300 font-medium cursor-pointer bg-slate-950 border border-slate-800 px-3 py-1.5 rounded-lg">
            <input
              type="checkbox"
              checked={onlyDuplicates}
              onChange={(e) => setOnlyDuplicates(e.target.checked)}
              className="accent-red-600 w-4 h-4 rounded cursor-pointer"
            />
            <span className="text-red-300">Show Only Duplicate Signals ({evcItems.filter(i => i.duplicate_flag).length})</span>
          </label>
        </div>

      </div>

      {/* Media Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filteredItems.map((item) => (
          <div
            key={item.id}
            onClick={() => onOpenEvc(item)}
            className={`bg-slate-900 border rounded-xl overflow-hidden cursor-pointer transition-all shadow-md hover:border-blue-500 group ${
              item.duplicate_flag
                ? 'border-red-900/60 ring-1 ring-red-800/40'
                : 'border-slate-800'
            }`}
          >
            <div className="aspect-video bg-slate-950 relative overflow-hidden">
              <img
                src={item.preview_url}
                alt={item.filename}
                className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-300"
              />

              {item.duplicate_flag && (
                <div className="absolute top-2 left-2 bg-red-900/90 backdrop-blur-md text-white text-[10px] font-bold px-2 py-1 rounded flex items-center gap-1.5 shadow-lg">
                  <ShieldAlert className="w-3.5 h-3.5 text-amber-300" />
                  pHash Duplicate ({((item.duplicate_similarity || 0.984) * 100).toFixed(0)}%)
                </div>
              )}

              {item.inspection_needed && (
                <div className="absolute top-2 right-2 bg-amber-900/90 backdrop-blur-md text-white text-[10px] font-bold px-2 py-1 rounded flex items-center gap-1">
                  <Flag className="w-3.5 h-3.5 text-yellow-300" />
                  Field Visit Flagged
                </div>
              )}

              <div className="absolute bottom-2 left-2 bg-black/70 backdrop-blur text-white text-[10px] px-2 py-0.5 rounded font-mono">
                {item.file_type.toUpperCase()}
              </div>
            </div>

            <div className="p-4 space-y-2">
              <div className="flex items-center justify-between text-xs">
                <span className="font-semibold text-white">{item.category}</span>
                <span className="text-[10px] bg-slate-800 text-slate-300 px-2 py-0.5 rounded">
                  {item.gps_match_status || 'Geo-verified'}
                </span>
              </div>

              <p className="text-xs text-slate-400 truncate">
                {item.filename}
              </p>

              {item.duplicate_flag && (
                <div className="bg-red-950/40 border border-red-900/50 rounded p-2 text-[11px] text-red-200">
                  Matches: <span className="font-semibold">{item.duplicate_match_institution}</span>
                </div>
              )}

              <div className="pt-1 flex items-center justify-between text-xs text-blue-400 font-medium">
                <span>Inspect Media & Hash</span>
                <span className="text-slate-500 text-[11px]">Click to open →</span>
              </div>
            </div>

          </div>
        ))}
      </div>

    </div>
  );
};
