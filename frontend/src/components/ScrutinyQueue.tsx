import React from 'react';
import { 
  Building2, Search, Filter, ShieldAlert, AlertTriangle, CheckCircle2, 
  ArrowRight, FileCheck, Camera, Layers, Sparkles 
} from 'lucide-react';
import { Application, ReviewPriority } from '../types';

interface ScrutinyQueueProps {
  applications: Application[];
  stats: any;
  searchTerm: string;
  onSearchChange: (val: string) => void;
  selectedCategory: string;
  onCategoryChange: (val: string) => void;
  selectedPriority: string;
  onPriorityChange: (val: string) => void;
  onSelectApplication: (app: Application) => void;
}

export const ScrutinyQueue: React.FC<ScrutinyQueueProps> = ({
  applications,
  stats,
  searchTerm,
  onSearchChange,
  selectedCategory,
  onCategoryChange,
  selectedPriority,
  onPriorityChange,
  onSelectApplication,
}) => {
  const getPriorityBadge = (priority: ReviewPriority) => {
    if (priority === 'RED') {
      return (
        <span className="bg-red-950/80 text-red-300 border border-red-700/60 px-2.5 py-0.5 rounded-full text-xs font-bold flex items-center gap-1">
          <ShieldAlert className="w-3.5 h-3.5" /> RED
        </span>
      );
    }
    if (priority === 'AMBER') {
      return (
        <span className="bg-amber-950/80 text-amber-300 border border-amber-700/60 px-2.5 py-0.5 rounded-full text-xs font-bold flex items-center gap-1">
          <AlertTriangle className="w-3.5 h-3.5" /> AMBER
        </span>
      );
    }
    return (
      <span className="bg-emerald-950/80 text-emerald-300 border border-emerald-700/60 px-2.5 py-0.5 rounded-full text-xs font-bold flex items-center gap-1">
        <CheckCircle2 className="w-3.5 h-3.5" /> GREEN
      </span>
    );
  };

  return (
    <div className="space-y-6">
      
      {/* Metrics Overview Cards */}
      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        
        <div className="bg-slate-900 border border-slate-800 rounded-xl p-4.5 shadow-md">
          <div className="flex items-center justify-between text-xs text-slate-400 mb-1">
            <span>Imported Applications</span>
            <Building2 className="w-4 h-4 text-blue-400" />
          </div>
          <div className="text-2xl font-bold text-white">
            {stats?.total_applications || applications.length}
          </div>
          <div className="text-[11px] text-slate-400 mt-1 flex items-center gap-1">
            <span className="text-emerald-400 font-semibold">{stats?.under_scrutiny || 3}</span> Under Active Review
          </div>
        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-xl p-4.5 shadow-md">
          <div className="flex items-center justify-between text-xs text-slate-400 mb-1">
            <span>Deficiencies Flagged</span>
            <AlertTriangle className="w-4 h-4 text-amber-400" />
          </div>
          <div className="text-2xl font-bold text-amber-300">
            {stats?.deficiencies_count || 2}
          </div>
          <div className="text-[11px] text-slate-400 mt-1">
            Requiring Reviewer Determination
          </div>
        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-xl p-4.5 shadow-md">
          <div className="flex items-center justify-between text-xs text-slate-400 mb-1">
            <span>EVC Duplicate Signals</span>
            <Camera className="w-4 h-4 text-red-400" />
          </div>
          <div className="text-2xl font-bold text-red-400">
            {stats?.duplicate_evc_flags || 1}
          </div>
          <div className="text-[11px] text-slate-400 mt-1">
            pHash Visual Matches Across Institutes
          </div>
        </div>

        <div className="bg-slate-900 border border-slate-800 rounded-xl p-4.5 shadow-md">
          <div className="flex items-center justify-between text-xs text-slate-400 mb-1">
            <span>Priority Triage Queue</span>
            <Layers className="w-4 h-4 text-indigo-400" />
          </div>
          <div className="flex items-center gap-3 mt-1">
            <span className="text-sm font-bold text-red-400">{stats?.priority_red || 1} Red</span>
            <span className="text-slate-600">•</span>
            <span className="text-sm font-bold text-amber-300">{stats?.priority_amber || 2} Amber</span>
            <span className="text-slate-600">•</span>
            <span className="text-sm font-bold text-emerald-400">{stats?.priority_green || 1} Green</span>
          </div>
          <div className="text-[11px] text-slate-400 mt-1">
            Triage Workflow by Risk Category
          </div>
        </div>

      </div>

      {/* Search & Filtering Controls */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-4 flex flex-col md:flex-row items-center justify-between gap-4">
        
        {/* Search input */}
        <div className="relative w-full md:w-96">
          <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            placeholder="Search by Application ID, Institution Name, or Trust..."
            value={searchTerm}
            onChange={(e) => onSearchChange(e.target.value)}
            className="w-full bg-slate-950 border border-slate-700 rounded-lg pl-9 pr-3 py-2 text-xs text-slate-200 focus:outline-none focus:border-blue-500 placeholder-slate-500"
          />
        </div>

        {/* Filter Dropdowns */}
        <div className="flex items-center gap-3 w-full md:w-auto">
          <div className="flex items-center gap-2 text-xs text-slate-400">
            <Filter className="w-3.5 h-3.5" />
            <span>Category:</span>
            <select
              value={selectedCategory}
              onChange={(e) => onCategoryChange(e.target.value)}
              className="bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-slate-200 focus:outline-none focus:border-blue-500"
            >
              <option value="ALL">All Categories</option>
              <option value="Extension of Approval (EoA)">Extension of Approval (EoA)</option>
              <option value="Intake Increase">Intake Increase</option>
              <option value="New Technical Institution">New Technical Institution</option>
            </select>
          </div>

          <div className="flex items-center gap-2 text-xs text-slate-400">
            <span>Priority:</span>
            <select
              value={selectedPriority}
              onChange={(e) => onPriorityChange(e.target.value)}
              className="bg-slate-950 border border-slate-700 rounded-lg px-2.5 py-1.5 text-xs text-slate-200 focus:outline-none focus:border-blue-500"
            >
              <option value="ALL">All Priorities</option>
              <option value="RED">RED (High Review)</option>
              <option value="AMBER">AMBER (Medium)</option>
              <option value="GREEN">GREEN (Standard)</option>
            </select>
          </div>
        </div>

      </div>

      {/* Applications List */}
      <div className="space-y-3">
        {applications.map((app) => (
          <div
            key={app.id}
            onClick={() => onSelectApplication(app)}
            className="bg-slate-900 border border-slate-800 rounded-xl p-5 hover:border-blue-500 transition-all cursor-pointer shadow-md group flex flex-col md:flex-row md:items-center justify-between gap-4"
          >
            <div className="space-y-1.5 max-w-2xl">
              <div className="flex items-center gap-2.5 flex-wrap">
                <span className="font-mono text-xs font-bold text-blue-400 bg-slate-950 px-2.5 py-0.5 rounded border border-slate-800">
                  {app.application_number}
                </span>
                <span className="text-xs bg-slate-800 text-slate-300 px-2 py-0.5 rounded">
                  {app.category}
                </span>
                <span className="text-xs text-slate-400">
                  AY {app.academic_year}
                </span>
                {getPriorityBadge(app.priority)}
              </div>

              <h3 className="text-base font-semibold text-white group-hover:text-blue-400 transition-colors">
                {app.institution_name}
              </h3>

              <p className="text-xs text-slate-400 truncate max-w-xl">
                {app.institution_address}
              </p>

              <div className="text-[11px] text-slate-500 flex items-center gap-3 pt-1">
                <span>Trust: <span className="text-slate-400">{app.trust_name}</span></span>
                <span>•</span>
                <span>Reviewer: <span className="text-slate-400">{app.assigned_reviewer}</span></span>
              </div>
            </div>

            {/* Right Status Columns */}
            <div className="flex items-center gap-6 shrink-0 border-t md:border-t-0 pt-3 md:pt-0 border-slate-800">
              
              <div className="text-right">
                <div className="text-xs text-slate-400">Compliance Index</div>
                <div className="text-sm font-bold text-emerald-400">{app.compliance_score}%</div>
                <div className="text-[10px] text-slate-500">{app.documents_count} Docs Mapped</div>
              </div>

              <div className="text-right">
                <div className="text-xs text-slate-400">Findings</div>
                <div className={`text-sm font-bold ${app.deficiency_count > 0 ? 'text-red-400' : 'text-slate-200'}`}>
                  {app.deficiency_count > 0 ? `${app.deficiency_count} Deficiencies` : 'Compliant'}
                </div>
                <div className="text-[10px] text-slate-500">{app.findings_count} Rules Checked</div>
              </div>

              <div className="pl-2">
                <div className="w-8 h-8 rounded-full bg-slate-800 group-hover:bg-blue-600 flex items-center justify-center text-slate-400 group-hover:text-white transition-colors">
                  <ArrowRight className="w-4 h-4" />
                </div>
              </div>

            </div>

          </div>
        ))}

        {applications.length === 0 && (
          <div className="bg-slate-900 border border-slate-800 rounded-xl p-12 text-center text-slate-400">
            <Building2 className="w-10 h-10 mx-auto text-slate-600 mb-2" />
            <p className="text-sm font-medium text-slate-300">No applications found matching current filters.</p>
            <p className="text-xs text-slate-500 mt-1">Try resetting search filters or import new application records.</p>
          </div>
        )}
      </div>

    </div>
  );
};
