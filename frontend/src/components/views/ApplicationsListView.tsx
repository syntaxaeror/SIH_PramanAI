import React, { useState } from 'react';
import { 
  Search, 
  Filter, 
  RotateCcw, 
  Building2, 
  ChevronRight, 
  ArrowUpDown, 
  FileText, 
  CheckCircle2, 
  AlertTriangle, 
  ShieldAlert,
  ChevronLeft,
  X
} from 'lucide-react';
import { Application, ReviewPriority } from '../../types';
import { useI18n } from '../../i18n';

interface ApplicationsListViewProps {
  applications: Application[];
  selectedCategory: string;
  onCategoryChange: (cat: string) => void;
  onOpenApplication: (app: Application) => void;
}

export const ApplicationsListView: React.FC<ApplicationsListViewProps> = ({
  applications,
  selectedCategory,
  onCategoryChange,
  onOpenApplication,
}) => {
  const { t } = useI18n();
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedPriority, setSelectedPriority] = useState('ALL');
  const [selectedStatus, setSelectedStatus] = useState('ALL');
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 8;

  const handleClearFilters = () => {
    setSearchTerm('');
    setSelectedPriority('ALL');
    setSelectedStatus('ALL');
    onCategoryChange('ALL');
    setCurrentPage(1);
  };

  const filteredApps = applications.filter((app) => {
    if (selectedCategory !== 'ALL' && app.category !== selectedCategory) return false;
    if (selectedPriority !== 'ALL' && app.priority !== selectedPriority) return false;
    if (selectedStatus !== 'ALL' && app.status !== selectedStatus) return false;
    if (searchTerm) {
      const s = searchTerm.toLowerCase();
      return (
        app.application_number.toLowerCase().includes(s) ||
        app.institution_name.toLowerCase().includes(s) ||
        app.institution_address.toLowerCase().includes(s) ||
        (app.trust_name && app.trust_name.toLowerCase().includes(s))
      );
    }
    return true;
  });

  const totalPages = Math.ceil(filteredApps.length / itemsPerPage) || 1;
  const paginatedApps = filteredApps.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage);

  const getPriorityBadge = (priority: ReviewPriority) => {
    if (priority === 'RED') {
      return (
        <span className="bg-[#FDECEC] text-[#B42318] border border-[#F87171] px-2 py-0.5 rounded text-[11px] font-bold inline-flex items-center gap-1">
          <ShieldAlert className="w-3 h-3" /> RED
        </span>
      );
    }
    if (priority === 'AMBER') {
      return (
        <span className="bg-[#FFF5D9] text-[#946200] border border-[#FCD34D] px-2 py-0.5 rounded text-[11px] font-bold inline-flex items-center gap-1">
          <AlertTriangle className="w-3 h-3" /> AMBER
        </span>
      );
    }
    return (
      <span className="bg-[#EAF6EE] text-[#237A45] border border-[#86EFAC] px-2 py-0.5 rounded text-[11px] font-bold inline-flex items-center gap-1">
        <CheckCircle2 className="w-3 h-3" /> GREEN
      </span>
    );
  };

  return (
    <div className="space-y-4 max-w-7xl mx-auto">
      
      {/* Page Header */}
      <div className="pb-3 border-b border-[#D9E2EC] flex flex-col sm:flex-row sm:items-center justify-between gap-2">
        <div>
          <h1 className="text-xl font-bold text-[#17365D] tracking-tight">
            {selectedCategory === 'ALL' ? t("apps.title") : (t(`cat.${selectedCategory}`) || selectedCategory)}
          </h1>
          <p className="text-xs text-[#667085] mt-0.5">
            {t("apps.subtitle")}
          </p>
        </div>
        <div className="text-xs text-[#667085]">
          Showing <strong className="text-[#17365D]">{filteredApps.length}</strong> {t("apps.showing_records")}
        </div>
      </div>

      {/* 7.1 Search & 7.2 Filter Bar */}
      <div className="bg-white border border-[#D9E2EC] rounded p-3 shadow-2xs space-y-3">
        
        <div className="flex flex-col md:flex-row items-center gap-3">
          
          {/* Search Box */}
          <div className="relative flex-1 w-full">
            <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
            <input
              type="text"
              placeholder={t("apps.search_placeholder")}
              value={searchTerm}
              onChange={(e) => {
                setSearchTerm(e.target.value);
                setCurrentPage(1);
              }}
              className="w-full bg-[#F7F9FC] border border-[#D9E2EC] rounded pl-9 pr-3 py-1.5 text-xs text-[#243447] placeholder-slate-400 focus:outline-none focus:border-[#245A8D] focus:bg-white"
            />
          </div>

          {/* Category Dropdown */}
          <div className="flex items-center gap-1.5 w-full md:w-auto text-xs">
            <span className="text-[#667085] shrink-0 font-medium">{t("apps.filter_category")}</span>
            <select
              value={selectedCategory}
              onChange={(e) => {
                onCategoryChange(e.target.value);
                setCurrentPage(1);
              }}
              className="bg-white border border-[#D9E2EC] text-[#243447] text-xs rounded px-2.5 py-1.5 focus:outline-none focus:border-[#245A8D] cursor-pointer"
            >
              <option value="ALL">{t("cat.ALL")}</option>
              <option value="Extension of Approval (EoA)">{t("cat.Extension of Approval (EoA)")}</option>
              <option value="Intake Increase">{t("cat.Intake Increase")}</option>
              <option value="New Technical Institution">{t("cat.New Technical Institution")}</option>
              <option value="New Programme / Level">{t("cat.New Programme / Level")}</option>
              <option value="Other Application Types">{t("cat.Other Application Types")}</option>
            </select>
          </div>

          {/* Priority Dropdown */}
          <div className="flex items-center gap-1.5 w-full md:w-auto text-xs">
            <span className="text-[#667085] shrink-0 font-medium">{t("apps.filter_priority")}</span>
            <select
              value={selectedPriority}
              onChange={(e) => {
                setSelectedPriority(e.target.value);
                setCurrentPage(1);
              }}
              className="bg-white border border-[#D9E2EC] text-[#243447] text-xs rounded px-2.5 py-1.5 focus:outline-none focus:border-[#245A8D] cursor-pointer"
            >
              <option value="ALL">All Priorities</option>
              <option value="RED">{t("priority.RED")}</option>
              <option value="AMBER">{t("priority.AMBER")}</option>
              <option value="GREEN">{t("priority.GREEN")}</option>
            </select>
          </div>

          {/* Clear Filters Button */}
          {(searchTerm || selectedCategory !== 'ALL' || selectedPriority !== 'ALL') && (
            <button
              onClick={handleClearFilters}
              className="flex items-center gap-1 text-xs text-[#667085] hover:text-[#B42318] px-2 py-1.5 rounded hover:bg-[#FDECEC] transition-colors shrink-0 cursor-pointer"
            >
              <RotateCcw className="w-3.5 h-3.5" />
              <span>{t("apps.clear_filters")}</span>
            </button>
          )}

        </div>

      </div>

      {/* 7.3 Applications Table */}
      <div className="bg-white border border-[#D9E2EC] rounded shadow-2xs overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse gov-table">
            <thead>
              <tr>
                <th className="w-40">{t("common.app_number")}</th>
                <th>{t("apps.col_app_details")}</th>
                <th>{t("common.category")}</th>
                <th className="text-center w-24">{t("step.checklist")}</th>
                <th>{t("apps.col_status")}</th>
                <th>EVC {t("common.status")}</th>
                <th className="text-center w-28">{t("common.priority")}</th>
                <th className="text-center w-32">{t("apps.col_actions")}</th>
              </tr>
            </thead>
            <tbody>
              {paginatedApps.map((app) => (
                <tr 
                  key={app.id}
                  onClick={() => onOpenApplication(app)}
                  className="cursor-pointer hover:bg-[#F3F7FB] transition-colors"
                >
                  {/* ID */}
                  <td className="font-mono text-xs font-bold text-[#17365D]">
                    {app.application_number}
                    <div className="text-[10px] text-[#667085] font-sans font-normal">
                      {t("portal.academic_cycle")} {app.academic_year}
                    </div>
                  </td>

                  {/* Institution Name & Location */}
                  <td>
                    <div className="font-semibold text-[#17365D] hover:underline">
                      {app.institution_name}
                    </div>
                    <div className="text-[11px] text-[#667085] truncate max-w-md">
                      {app.institution_address}
                    </div>
                  </td>

                  {/* Category */}
                  <td className="text-xs text-[#243447]">
                    {t(`cat.${app.category}`) || app.category}
                  </td>

                  {/* Checklist Status */}
                  <td className="text-center">
                    <span className="font-semibold text-[#17365D] text-xs">
                      {app.documents_count}/{app.expected_documents_count || 7}
                    </span>
                    <div className="text-[10px] text-[#237A45] font-medium">{t("checklist.uploaded_files")}</div>
                  </td>

                  {/* Document Review Status */}
                  <td>
                    {app.deficiency_count > 0 ? (
                      <span className="bg-[#FDECEC] text-[#B42318] text-[11px] font-semibold px-2 py-0.5 rounded">
                        {app.deficiency_count} {t("common.deficiencies")}
                      </span>
                    ) : (
                      <span className="bg-[#EAF6EE] text-[#237A45] text-[11px] font-semibold px-2 py-0.5 rounded">
                        {t("dash.compliant")}
                      </span>
                    )}
                  </td>

                  {/* EVC Status */}
                  <td>
                    {app.priority === 'RED' ? (
                      <span className="bg-[#FDECEC] text-[#B42318] text-[11px] font-semibold px-2 py-0.5 rounded">
                        {t("evc.duplicate_signals")}
                      </span>
                    ) : (
                      <span className="bg-[#EAF2FA] text-[#245A8D] text-[11px] font-semibold px-2 py-0.5 rounded">
                        {app.evc_items_count} {t("dash.docs_mapped")}
                      </span>
                    )}
                  </td>

                  {/* Priority */}
                  <td className="text-center">
                    {getPriorityBadge(app.priority)}
                  </td>

                  {/* Open Button */}
                  <td className="text-center">
                    <button
                      onClick={(e) => {
                        e.stopPropagation();
                        onOpenApplication(app);
                      }}
                      className="bg-[#17365D] hover:bg-[#245A8D] text-white text-xs font-semibold px-3 py-1 rounded transition-colors shadow-2xs inline-flex items-center gap-1 cursor-pointer"
                    >
                      <span>{t("common.inspect")}</span>
                      <ChevronRight className="w-3.5 h-3.5" />
                    </button>
                  </td>
                </tr>
              ))}

              {paginatedApps.length === 0 && (
                <tr>
                  <td colSpan={8} className="text-center py-12 text-[#667085]">
                    <Building2 className="w-8 h-8 text-slate-300 mx-auto mb-2" />
                    <p className="text-sm font-medium text-[#243447]">No applications found matching current criteria.</p>
                    <p className="text-xs text-[#667085] mt-1">Try resetting the search keyword or changing category filters.</p>
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>

        {/* Table Footer / Pagination */}
        <div className="px-4 py-2.5 bg-[#F7F9FC] border-t border-[#D9E2EC] flex items-center justify-between text-xs text-[#667085]">
          <div>
            Showing {(currentPage - 1) * itemsPerPage + 1} to {Math.min(currentPage * itemsPerPage, filteredApps.length)} of {filteredApps.length} applications
          </div>
          <div className="flex items-center gap-1">
            <button
              onClick={() => setCurrentPage(p => Math.max(1, p - 1))}
              disabled={currentPage === 1}
              className="p-1 rounded border border-[#D9E2EC] bg-white hover:bg-slate-50 disabled:opacity-40 disabled:cursor-not-allowed"
            >
              <ChevronLeft className="w-4 h-4" />
            </button>
            <span className="px-2 font-medium">Page {currentPage} of {totalPages}</span>
            <button
              onClick={() => setCurrentPage(p => Math.min(totalPages, p + 1))}
              disabled={currentPage === totalPages}
              className="p-1 rounded border border-[#D9E2EC] bg-white hover:bg-slate-50 disabled:opacity-40 disabled:cursor-not-allowed"
            >
              <ChevronRight className="w-4 h-4" />
            </button>
          </div>
        </div>

      </div>

    </div>
  );
};
