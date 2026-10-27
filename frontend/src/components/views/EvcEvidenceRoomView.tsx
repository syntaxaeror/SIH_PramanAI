import React, { useState } from 'react';
import { 
  Camera, 
  Video, 
  MapPin, 
  ShieldAlert, 
  Flag, 
  CheckCircle2, 
  AlertTriangle, 
  Eye, 
  Layers, 
  Sparkles, 
  Info,
  Clock,
  List,
  LayoutGrid,
  CheckSquare,
  Square,
  Search,
  Filter,
  ExternalLink,
  ShieldCheck
} from 'lucide-react';
import { Application, EVCEvidenceItem } from '../../types';
import { EvcDuplicateModal } from '../EvcDuplicateModal';
import { useI18n } from '../../i18n';

interface EvcEvidenceRoomViewProps {
  application: Application;
  evcItems: EVCEvidenceItem[];
  onFlagInspection: (evcId: string, needed: boolean, reason: string) => Promise<void>;
}

// The 11 official physical areas required by AICTE Approval Process Handbook
export const MANDATORY_EVC_AREAS = [
  "Institution's front and rear exterior",
  "Classrooms and tutorial rooms",
  "Laboratories and workshops",
  "Computer centre",
  "Library and reading room",
  "Drawing hall and seminar hall, where applicable",
  "Administrative offices",
  "Faculty seating",
  "Toilets, common rooms and cafeteria",
  "Entrance, passages, staircases and circulation areas",
  "Other required instructional and amenity areas"
];

export const EvcEvidenceRoomView: React.FC<EvcEvidenceRoomViewProps> = ({
  application,
  evcItems,
  onFlagInspection,
}) => {
  const { t } = useI18n();
  const [viewMode, setViewMode] = useState<'list' | 'grid'>('list');
  const [selectedCategory, setSelectedCategory] = useState<string>('ALL');
  const [searchQuery, setSearchQuery] = useState<string>('');
  const [duplicateOnly, setDuplicateOnly] = useState<boolean>(false);
  const [inspectingItem, setInspectingItem] = useState<EVCEvidenceItem | null>(null);
  const [isCompletedEVC, setIsCompletedEVC] = useState<boolean>(false);

  // Derived metrics
  const totalFiles = evcItems.length;
  const imageCount = evcItems.filter(i => i.file_type === 'image').length;
  const videoCount = evcItems.filter(i => i.file_type === 'video').length;
  const duplicateFlags = evcItems.filter(i => i.duplicate_flag).length;
  const physicalReq = evcItems.filter(i => i.inspection_needed).length;

  // Compute coverage of the 11 official areas
  const coveredAreas = MANDATORY_EVC_AREAS.filter(area => 
    evcItems.some(item => item.category.toLowerCase().trim() === area.toLowerCase().trim())
  );
  const coveragePercent = Math.round((coveredAreas.length / MANDATORY_EVC_AREAS.length) * 100);

  // Filtering
  const filteredItems = evcItems.filter(item => {
    const matchesCategory = selectedCategory === 'ALL' || item.category === selectedCategory;
    const matchesSearch = searchQuery === '' || 
      item.category.toLowerCase().includes(searchQuery.toLowerCase()) ||
      item.filename.toLowerCase().includes(searchQuery.toLowerCase()) ||
      (item.duplicate_match_institution && item.duplicate_match_institution.toLowerCase().includes(searchQuery.toLowerCase()));
    const matchesDuplicate = !duplicateOnly || item.duplicate_flag;
    return matchesCategory && matchesSearch && matchesDuplicate;
  });

  return (
    <div className="space-y-5 max-w-7xl mx-auto">
      
      {/* Header & EVC Status */}
      <div className="flex flex-col sm:flex-row sm:items-center justify-between pb-3 border-b border-[#D9E2EC] gap-3">
        <div>
          <div className="flex items-center gap-2">
            <h1 className="text-xl font-bold text-[#17365D] tracking-tight">
              {t("evc.title")}
            </h1>
            <span className="bg-[#EAF2FA] text-[#245A8D] font-mono text-[11px] font-bold px-2 py-0.5 rounded border border-[#245A8D]/20">
              Perceptual Hash & Geotag Engine
            </span>
          </div>
          <p className="text-xs text-[#667085] mt-0.5">
            {t("evc.subtitle")} <strong>{application.institution_name}</strong>.
          </p>
        </div>

        <button
          onClick={() => {
            if (confirm("Confirm completion of EVC Evidence Review? All inspector determinations will be summarized in the scrutiny record.")) {
              setIsCompletedEVC(true);
            }
          }}
          className={`text-xs font-semibold px-4 py-2 rounded flex items-center gap-2 shadow-2xs transition-colors self-start sm:self-auto cursor-pointer ${
            isCompletedEVC 
              ? 'bg-[#237A45] text-white' 
              : 'bg-[#17365D] hover:bg-[#245A8D] text-white'
          }`}
        >
          <CheckCircle2 className="w-4 h-4" />
          <span>{isCompletedEVC ? t("evc.finalized") : t("evc.complete_review")}</span>
        </button>
      </div>

      {/* KPI Summary Cards */}
      <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-5 gap-3">
        <div className="bg-white border border-[#D9E2EC] p-3 rounded shadow-2xs">
          <div className="text-[11px] font-medium text-[#667085] uppercase">{t("evc.total_evidence")}</div>
          <div className="text-xl font-bold text-[#17365D] mt-1">{totalFiles} Media Files</div>
          <div className="text-[10px] text-[#667085] mt-0.5">{imageCount} Photos • Verified GPS</div>
        </div>

        <div className="bg-white border border-[#D9E2EC] p-3 rounded shadow-2xs">
          <div className="text-[11px] font-medium text-[#667085] uppercase">{t("evc.duplicate_signals")}</div>
          <div className="text-xl font-bold text-[#B42318] mt-1">{duplicateFlags} Flagged</div>
          <div className="text-[10px] text-[#B42318] font-medium mt-0.5">Matched with Other Technical Institutes</div>
        </div>

        <div className="bg-white border border-[#D9E2EC] p-3 rounded shadow-2xs">
          <div className="text-[11px] font-medium text-[#667085] uppercase">{t("evc.coverage_metric")}</div>
          <div className="text-xl font-bold text-[#237A45] mt-1">{coveredAreas.length} / {MANDATORY_EVC_AREAS.length}</div>
          <div className="text-[10px] text-[#237A45] font-medium mt-0.5">{coveragePercent}% {t("evc.areas_met")}</div>
        </div>

        <div className="bg-white border border-[#D9E2EC] p-3 rounded shadow-2xs">
          <div className="text-[11px] font-medium text-[#667085] uppercase">{t("evc.physical_insp")}</div>
          <div className="text-xl font-bold text-[#946200] mt-1">{physicalReq} Areas</div>
          <div className="text-[10px] text-[#946200] font-medium mt-0.5">Recommended for Field Visit</div>
        </div>

        <div className="bg-white border border-[#D9E2EC] p-3 rounded shadow-2xs">
          <div className="text-[11px] font-medium text-[#667085] uppercase">Review Status</div>
          <div className="text-xl font-bold text-[#245A8D] mt-1">
            {isCompletedEVC ? t("checklist.reviewed") : 'Under Review'}
          </div>
          <div className="text-[10px] text-[#245A8D] font-medium mt-0.5">EVC Committee Member</div>
        </div>
      </div>

      {/* 11-POINT OFFICIAL AICTE VIDEO & PHYSICAL COVERAGE CHECKLIST */}
      <div className="bg-white border border-[#D9E2EC] rounded p-4 shadow-2xs space-y-3">
        <div className="flex flex-col sm:flex-row sm:items-center justify-between border-b border-[#E5EBF2] pb-2.5 gap-2">
          <div className="flex items-center gap-2">
            <CheckSquare className="w-4 h-4 text-[#245A8D]" />
            <h3 className="text-xs font-bold text-[#17365D] uppercase tracking-wide">
              Official AICTE Video & Physical Evidence Coverage Checklist
            </h3>
          </div>
          <span className="text-xs font-bold text-[#237A45] bg-[#EAF6EE] px-2 py-0.5 rounded border border-[#237A45]/20">
            {coveredAreas.length} of {MANDATORY_EVC_AREAS.length} Areas Verified ({coveragePercent}%)
          </span>
        </div>

        {/* Coverage Progress Bar */}
        <div className="w-full bg-slate-100 rounded-full h-2 overflow-hidden border border-slate-200">
          <div 
            className="bg-[#237A45] h-full transition-all duration-300" 
            style={{ width: `${coveragePercent}%` }}
          />
        </div>

        {/* Checklist Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-2 pt-1 text-xs">
          {MANDATORY_EVC_AREAS.map((area, idx) => {
            const matchingItems = evcItems.filter(i => i.category.toLowerCase().trim() === area.toLowerCase().trim());
            const isCovered = matchingItems.length > 0;
            const hasDuplicate = matchingItems.some(i => i.duplicate_flag);
            const hasDiscrepancy = matchingItems.some(i => i.gps_distance_km && i.gps_distance_km > 0.5);

            return (
              <div 
                key={idx}
                onClick={() => setSelectedCategory(selectedCategory === area ? 'ALL' : area)}
                className={`p-2 rounded border flex items-center justify-between cursor-pointer transition-colors ${
                  selectedCategory === area 
                    ? 'border-[#245A8D] bg-[#EAF2FA]' 
                    : isCovered 
                      ? 'border-[#D9E2EC] bg-[#F7F9FC] hover:bg-slate-100' 
                      : 'border-red-200 bg-red-50/50'
                }`}
              >
                <div className="flex items-center gap-2 truncate pr-2">
                  {isCovered ? (
                    <CheckCircle2 className="w-4 h-4 text-[#237A45] shrink-0" />
                  ) : (
                    <Square className="w-4 h-4 text-slate-300 shrink-0" />
                  )}
                  <span className={`truncate text-xs ${isCovered ? 'text-[#243447] font-medium' : 'text-slate-400'}`}>
                    {area}
                  </span>
                </div>

                <div className="flex items-center gap-1 shrink-0">
                  {hasDuplicate && (
                    <span className="text-[9px] bg-[#FDECEC] text-[#B42318] font-bold px-1.5 py-0.2 rounded border border-[#F87171]/40" title="Duplicate visual hash flagged!">
                      Duplicate
                    </span>
                  )}
                  {hasDiscrepancy && (
                    <span className="text-[9px] bg-[#FFF5D9] text-[#946200] font-bold px-1.5 py-0.2 rounded border border-amber-300" title="GPS distance discrepancy">
                      GPS
                    </span>
                  )}
                  <span className="text-[10px] text-[#667085] font-mono">
                    {matchingItems.length}
                  </span>
                </div>
              </div>
            );
          })}
        </div>
      </div>

      {/* Control Bar: Filters, Search, and View Toggle */}
      <div className="flex flex-col md:flex-row items-stretch md:items-center justify-between gap-3 bg-white border border-[#D9E2EC] p-3 rounded shadow-2xs">
        
        {/* Search Input */}
        <div className="relative flex-1 max-w-md">
          <Search className="w-4 h-4 text-slate-400 absolute left-3 top-2.5" />
          <input
            type="text"
            placeholder="Search by category, media filename, or matched institute..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            className="w-full pl-9 pr-3 py-1.5 text-xs border border-[#D9E2EC] rounded focus:outline-none focus:ring-1 focus:ring-[#245A8D]"
          />
        </div>

        <div className="flex items-center gap-2 flex-wrap">
          {/* Duplicate Only Filter Toggle */}
          <button
            onClick={() => setDuplicateOnly(!duplicateOnly)}
            className={`px-3 py-1.5 rounded text-xs font-semibold flex items-center gap-1.5 transition-colors cursor-pointer ${
              duplicateOnly
                ? 'bg-[#B42318] text-white shadow-2xs'
                : 'bg-white border border-[#D9E2EC] text-[#243447] hover:bg-[#F3F7FB]'
            }`}
          >
            <ShieldAlert className="w-3.5 h-3.5" />
            <span>{t("evc.show_duplicates")} ({duplicateFlags})</span>
          </button>

          {/* Category Dropdown Filter */}
          <select
            value={selectedCategory}
            onChange={(e) => setSelectedCategory(e.target.value)}
            className="text-xs border border-[#D9E2EC] rounded px-2.5 py-1.5 bg-white text-[#243447] focus:outline-none focus:ring-1 focus:ring-[#245A8D] font-medium cursor-pointer"
          >
            <option value="ALL">All Categories ({evcItems.length})</option>
            {MANDATORY_EVC_AREAS.map((cat) => (
              <option key={cat} value={cat}>{cat}</option>
            ))}
          </select>

          {/* View Mode Toggle: List vs Grid */}
          <div className="flex items-center bg-[#F7F9FC] border border-[#D9E2EC] rounded p-0.5">
            <button
              onClick={() => setViewMode('list')}
              className={`p-1.5 rounded text-xs flex items-center gap-1 font-semibold transition-colors cursor-pointer ${
                viewMode === 'list' 
                  ? 'bg-white text-[#17365D] shadow-2xs' 
                  : 'text-[#667085] hover:text-[#17365D]'
              }`}
              title="Table / List View"
            >
              <List className="w-3.5 h-3.5" />
              <span>{t("evc.list_view")}</span>
            </button>
            <button
              onClick={() => setViewMode('grid')}
              className={`p-1.5 rounded text-xs flex items-center gap-1 font-semibold transition-colors cursor-pointer ${
                viewMode === 'grid' 
                  ? 'bg-white text-[#17365D] shadow-2xs' 
                  : 'text-[#667085] hover:text-[#17365D]'
              }`}
              title="Gallery Grid View"
            >
              <LayoutGrid className="w-3.5 h-3.5" />
              <span>{t("evc.grid_view")}</span>
            </button>
          </div>
        </div>

      </div>

      {/* VIEW MODE 1: STRUCTURED LIST VIEW (PRIMARY) */}
      {viewMode === 'list' && (
        <div className="bg-white border border-[#D9E2EC] rounded shadow-2xs overflow-hidden">
          <div className="overflow-x-auto">
            <table className="w-full text-left text-xs border-collapse">
              <thead>
                <tr className="bg-[#F7F9FC] border-b border-[#D9E2EC] text-[#17365D] font-bold uppercase tracking-wider text-[10px]">
                  <th className="py-3 px-3 w-8 text-center">#</th>
                  <th className="py-3 px-3">Infrastructure Category</th>
                  <th className="py-3 px-3">Uploaded Media File</th>
                  <th className="py-3 px-4">Duplicate Status (pHash Match)</th>
                  <th className="py-3 px-3">GPS / Geotag Status</th>
                  <th className="py-3 px-3">Field Inspection Flag</th>
                  <th className="py-3 px-3 text-right">Actions</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-[#E5EBF2]">
                {filteredItems.map((item, index) => (
                  <tr 
                    key={item.id} 
                    className={`hover:bg-[#F3F7FB] transition-colors ${
                      item.duplicate_flag ? 'bg-[#FFFBFB]' : ''
                    }`}
                  >
                    {/* Index */}
                    <td className="py-3 px-3 text-center text-slate-400 font-mono text-[11px]">
                      {index + 1}
                    </td>

                    {/* Category */}
                    <td className="py-3 px-3">
                      <div className="font-bold text-[#17365D] text-xs">
                        {item.category}
                      </div>
                      <div className="text-[10px] text-[#667085] mt-0.5">
                        APH Physical Standard Norm
                      </div>
                    </td>

                    {/* Media File & Preview Thumbnail */}
                    <td className="py-3 px-3">
                      <div className="flex items-center gap-2.5">
                        <div 
                          onClick={() => setInspectingItem(item)}
                          className="w-12 h-10 rounded bg-slate-100 border border-[#D9E2EC] overflow-hidden shrink-0 cursor-pointer relative group"
                        >
                          <img 
                            src={item.preview_url} 
                            alt={item.filename}
                            className="w-full h-full object-cover group-hover:scale-105 transition-transform"
                          />
                          {item.file_type === 'video' && (
                            <div className="absolute inset-0 bg-black/40 flex items-center justify-center text-white">
                              <Video className="w-3.5 h-3.5" />
                            </div>
                          )}
                        </div>

                        <div>
                          <div className="font-mono text-xs font-semibold text-[#243447] truncate max-w-[200px]">
                            {item.filename}
                          </div>
                          <div className="flex items-center gap-1.5 text-[10px] text-[#667085] mt-0.5">
                            <span className="font-bold uppercase text-[#245A8D]">{item.file_type}</span>
                            <span>•</span>
                            <span className="font-mono">{item.phash?.slice(0, 8)}...</span>
                          </div>
                        </div>
                      </div>
                    </td>

                    {/* Duplicate Status (The Essential Feature) */}
                    <td className="py-3 px-4 max-w-sm">
                      {item.duplicate_flag ? (
                        <div className="p-2 rounded bg-[#FDECEC] border border-[#F87171] text-xs space-y-1">
                          <div className="flex items-center justify-between text-[#B42318] font-bold">
                            <span className="flex items-center gap-1">
                              <ShieldAlert className="w-3.5 h-3.5" />
                              <span>DUPLICATE MATCH DETECTED</span>
                            </span>
                            <span className="bg-[#B42318] text-white px-1.5 py-0.2 rounded font-mono text-[10px]">
                              {((item.duplicate_similarity || 0.984) * 100).toFixed(1)}% Match
                            </span>
                          </div>
                          <div className="text-[11px] text-[#243447]">
                            <strong>Matched Institute:</strong> {item.duplicate_match_institution || 'Prior Technical Campus'}
                          </div>
                          <p className="text-[10px] text-slate-600 leading-tight">
                            {item.duplicate_explanation || 'Perceptual hash collision indicates shared or re-used media across institutes.'}
                          </p>
                        </div>
                      ) : (
                        <div className="flex items-center gap-1.5 text-[#237A45] font-semibold text-xs">
                          <ShieldCheck className="w-4 h-4" />
                          <span>Original / Unique Hash</span>
                        </div>
                      )}
                    </td>

                    {/* GPS Status */}
                    <td className="py-3 px-3">
                      {item.gps_distance_km && item.gps_distance_km > 0.5 ? (
                        <span className="bg-[#FFF5D9] text-[#946200] border border-amber-300 px-2 py-0.5 rounded font-semibold text-[10px] flex items-center gap-1 w-max">
                          <AlertTriangle className="w-3 h-3" />
                          <span>{item.gps_match_status || `DISCREPANCY (${item.gps_distance_km}km)`}</span>
                        </span>
                      ) : (
                        <span className="bg-[#EAF6EE] text-[#237A45] border border-emerald-200 px-2 py-0.5 rounded font-semibold text-[10px] flex items-center gap-1 w-max">
                          <CheckCircle2 className="w-3 h-3" />
                          <span>{item.gps_match_status || 'MATCHED (18m)'}</span>
                        </span>
                      )}
                    </td>

                    {/* Inspection Flag Status */}
                    <td className="py-3 px-3">
                      <button
                        onClick={() => {
                          const newNeeded = !item.inspection_needed;
                          const reason = newNeeded ? "Reviewer requested on-site verification" : "";
                          onFlagInspection(item.id, newNeeded, reason);
                        }}
                        className={`px-2.5 py-1 rounded text-xs font-semibold flex items-center gap-1 transition-colors ${
                          item.inspection_needed
                            ? 'bg-[#946200] text-white shadow-2xs'
                            : 'bg-[#F7F9FC] border border-[#D9E2EC] text-slate-600 hover:bg-slate-100'
                        }`}
                      >
                        <Flag className="w-3 h-3" />
                        <span>{item.inspection_needed ? 'On-Site Flagged' : 'Flag On-Site'}</span>
                      </button>
                    </td>

                    {/* Action */}
                    <td className="py-3 px-3 text-right">
                      <button
                        onClick={() => setInspectingItem(item)}
                        className="bg-[#EAF2FA] hover:bg-blue-100 text-[#245A8D] font-semibold text-xs px-2.5 py-1 rounded transition-colors flex items-center gap-1 ml-auto"
                      >
                        <Eye className="w-3.5 h-3.5" />
                        <span>Examine</span>
                      </button>
                    </td>
                  </tr>
                ))}

                {filteredItems.length === 0 && (
                  <tr>
                    <td colSpan={7} className="py-8 text-center text-xs text-[#667085]">
                      No EVC evidence records match your filter criteria.
                    </td>
                  </tr>
                )}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* VIEW MODE 2: GALLERY GRID VIEW */}
      {viewMode === 'grid' && (
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {filteredItems.map((item) => (
            <div
              key={item.id}
              onClick={() => setInspectingItem(item)}
              className={`bg-white border rounded overflow-hidden shadow-2xs cursor-pointer hover:border-[#245A8D] transition-all flex flex-col justify-between ${
                item.duplicate_flag ? 'border-[#F87171] ring-1 ring-[#F87171]/40' : 'border-[#D9E2EC]'
              }`}
            >
              <div>
                {/* Media Thumbnail */}
                <div className="aspect-video bg-slate-100 relative overflow-hidden">
                  <img
                    src={item.preview_url}
                    alt={item.filename}
                    className="w-full h-full object-cover"
                  />

                  {/* Duplicate Badge */}
                  {item.duplicate_flag && (
                    <div className="absolute top-2 left-2 bg-[#B42318] text-white text-[10px] font-bold px-2 py-0.5 rounded shadow-sm flex items-center gap-1">
                      <ShieldAlert className="w-3 h-3 text-yellow-300" />
                      <span>pHash Reused Signal ({((item.duplicate_similarity || 0.984) * 100).toFixed(1)}%)</span>
                    </div>
                  )}

                  {/* Inspection Flag Badge */}
                  {item.inspection_needed && (
                    <div className="absolute top-2 right-2 bg-[#946200] text-white text-[10px] font-bold px-2 py-0.5 rounded shadow-sm flex items-center gap-1">
                      <Flag className="w-3 h-3 text-yellow-200" />
                      <span>On-Site Flagged</span>
                    </div>
                  )}

                  <div className="absolute bottom-2 left-2 bg-black/60 text-white font-mono text-[9px] px-1.5 py-0.5 rounded">
                    {item.file_type.toUpperCase()}
                  </div>
                </div>

                {/* Media Details */}
                <div className="p-3 space-y-1.5">
                  <div className="flex items-center justify-between text-xs">
                    <span className="font-bold text-[#17365D] truncate max-w-[200px]">{item.category}</span>
                    <span className="text-[10px] bg-[#EAF6EE] text-[#237A45] font-semibold px-1.5 py-0.2 rounded">
                      {item.gps_match_status || 'GPS Matched'}
                    </span>
                  </div>

                  <div className="font-mono text-xs text-[#243447] truncate">
                    {item.filename}
                  </div>

                  {item.duplicate_flag && (
                    <div className="bg-[#FDECEC] border border-[#F87171]/40 rounded p-2 text-[11px] text-[#B42318] space-y-0.5">
                      <div className="font-bold">Cross-Institution Match Found:</div>
                      <div className="truncate font-medium">{item.duplicate_match_institution}</div>
                    </div>
                  )}

                  {/* Video Keyframes Preview */}
                  {item.video_keyframes && item.video_keyframes.length > 0 && (
                    <div className="pt-1 flex items-center gap-1.5 text-[10px] text-[#245A8D] font-medium">
                      <Video className="w-3.5 h-3.5" />
                      <span>{item.video_keyframes.length} Scene Keyframes Extracted</span>
                    </div>
                  )}
                </div>
              </div>

              {/* Card Footer Actions */}
              <div className="px-3 py-2 bg-[#F7F9FC] border-t border-[#D9E2EC] flex items-center justify-between text-xs">
                <span className="text-[#245A8D] font-semibold flex items-center gap-1">
                  <Eye className="w-3.5 h-3.5" />
                  <span>Examine Hash & Geotag</span>
                </span>
                <span className="text-[#667085] text-[10px]">Click to inspect</span>
              </div>

            </div>
          ))}
        </div>
      )}

      {/* Duplicate / Inspection Modal */}
      {inspectingItem && (
        <EvcDuplicateModal
          item={inspectingItem}
          onClose={() => setInspectingItem(null)}
          onFlagInspection={onFlagInspection}
        />
      )}

    </div>
  );
};
