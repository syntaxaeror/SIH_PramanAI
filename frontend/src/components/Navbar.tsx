import React from 'react';
import { Shield, UserCheck, Eye, Sparkles, Building2, ChevronDown, RefreshCw } from 'lucide-react';
import { UserRole } from '../types';

interface NavbarProps {
  currentRole: UserRole;
  onRoleChange: (role: UserRole) => void;
  activeTab: string;
  onTabChange: (tab: string) => void;
  reviewerName: string;
}

export const Navbar: React.FC<NavbarProps> = ({
  currentRole,
  onRoleChange,
  activeTab,
  onTabChange,
  reviewerName,
}) => {
  return (
    <header className="bg-slate-900 border-b border-slate-800 sticky top-0 z-40 backdrop-blur-md bg-opacity-95">
      {/* Top utility alert banner */}
      <div className="bg-blue-950/60 border-b border-blue-900/40 px-4 py-1.5 text-xs flex justify-between items-center text-blue-200">
        <div className="flex items-center gap-2">
          <span className="inline-block w-2 h-2 rounded-full bg-emerald-400 animate-pulse"></span>
          <span className="font-medium text-slate-300">AICTE Internal Scrutiny Network</span>
          <span className="text-slate-500">|</span>
          <span className="text-amber-300 font-medium">AY 2025-26 Approval Cycle</span>
          <span className="text-slate-500">|</span>
          <span className="text-slate-400">Strictly for Authorized Reviewers (Non-Statutory Decision Support)</span>
        </div>
        <div className="text-slate-400 flex items-center gap-3">
          <span className="bg-slate-800 px-2 py-0.5 rounded text-[11px] text-slate-300">Session Secure (RBAC Enforced)</span>
        </div>
      </div>

      {/* Main Navbar */}
      <div className="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
        <div className="flex items-center gap-4">
          <div className="flex items-center gap-3 cursor-pointer" onClick={() => onTabChange('queue')}>
            <div className="w-10 h-10 rounded-lg bg-gradient-to-br from-blue-600 to-indigo-700 flex items-center justify-center shadow-lg shadow-blue-500/20 text-white font-bold text-xl">
              A
            </div>
            <div>
              <div className="flex items-center gap-2">
                <span className="font-bold text-lg tracking-tight text-white">AICTE Scrutiny Assistant</span>
                <span className="bg-indigo-900/80 text-indigo-300 border border-indigo-700/50 text-[10px] font-semibold px-2 py-0.5 rounded uppercase">
                  Evidence-First AI
                </span>
              </div>
              <p className="text-xs text-slate-400">Application Scrutiny & EVC Physical Evidence Review</p>
            </div>
          </div>
        </div>

        {/* Navigation Tabs */}
        <nav className="flex items-center gap-1 bg-slate-950/70 p-1 rounded-lg border border-slate-800">
          <button
            onClick={() => onTabChange('queue')}
            className={`px-3 py-1.5 rounded-md text-sm font-medium transition-all ${
              activeTab === 'queue'
                ? 'bg-blue-600 text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
            }`}
          >
            Scrutiny Queue
          </button>
          <button
            onClick={() => onTabChange('evc_room')}
            className={`px-3 py-1.5 rounded-md text-sm font-medium transition-all ${
              activeTab === 'evc_room'
                ? 'bg-blue-600 text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
            }`}
          >
            EVC Evidence Room
          </button>
          <button
            onClick={() => onTabChange('rules')}
            className={`px-3 py-1.5 rounded-md text-sm font-medium transition-all ${
              activeTab === 'rules'
                ? 'bg-blue-600 text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
            }`}
          >
            Rules & Checklists
          </button>
          <button
            onClick={() => onTabChange('ingestion')}
            className={`px-3 py-1.5 rounded-md text-sm font-medium transition-all ${
              activeTab === 'ingestion'
                ? 'bg-blue-600 text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
            }`}
          >
            Import Ingestion
          </button>
          <button
            onClick={() => onTabChange('audit')}
            className={`px-3 py-1.5 rounded-md text-sm font-medium transition-all ${
              activeTab === 'audit'
                ? 'bg-blue-600 text-white shadow-sm'
                : 'text-slate-400 hover:text-slate-200 hover:bg-slate-900'
            }`}
          >
            Audit Trail
          </button>
        </nav>

        {/* User Role Switcher */}
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-2 bg-slate-800/80 border border-slate-700/80 rounded-lg px-3 py-1.5">
            <div className="w-7 h-7 rounded-full bg-slate-700 flex items-center justify-center text-xs text-blue-400 font-semibold">
              {currentRole === 'System Administrator' && <Shield className="w-3.5 h-3.5" />}
              {currentRole === 'Scrutiny Reviewer' && <UserCheck className="w-3.5 h-3.5" />}
              {currentRole === 'EVC Reviewer/Inspector' && <Building2 className="w-3.5 h-3.5" />}
              {currentRole === 'Read-only Auditor' && <Eye className="w-3.5 h-3.5" />}
            </div>
            <div className="text-left">
              <div className="text-xs font-semibold text-slate-200 leading-tight">{reviewerName}</div>
              <div className="text-[10px] text-slate-400 flex items-center gap-1">
                <span>Role:</span>
                <select
                  value={currentRole}
                  onChange={(e) => onRoleChange(e.target.value as UserRole)}
                  className="bg-transparent text-blue-300 font-medium focus:outline-none cursor-pointer border-none p-0 text-[10px]"
                >
                  <option value="Scrutiny Reviewer" className="bg-slate-900 text-white">Scrutiny Reviewer</option>
                  <option value="EVC Reviewer/Inspector" className="bg-slate-900 text-white">EVC Reviewer/Inspector</option>
                  <option value="System Administrator" className="bg-slate-900 text-white">System Administrator</option>
                  <option value="Read-only Auditor" className="bg-slate-900 text-white">Read-only Auditor</option>
                </select>
              </div>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};
