import React from 'react';
import { 
  Building2, 
  ChevronRight, 
  Shield, 
  UserCheck, 
  Eye, 
  Sparkles, 
  CheckCircle2, 
  AlertTriangle, 
  Clock, 
  ArrowRight,
  ExternalLink,
  Languages
} from 'lucide-react';
import { Application, UserRole, WorkflowStage } from '../../types';
import { useI18n } from '../../i18n';

interface TopHeaderProps {
  currentView: string;
  activeApplication: Application | null;
  currentRole: UserRole;
  onRoleChange: (role: UserRole) => void;
  onNavigateWorkflow: (stage: WorkflowStage) => void;
  onClearApplication: () => void;
}

export const TopHeader: React.FC<TopHeaderProps> = ({
  currentView,
  activeApplication,
  currentRole,
  onRoleChange,
  onNavigateWorkflow,
  onClearApplication,
}) => {
  const { language, setLanguage, t } = useI18n();

  const getBreadcrumbs = () => {
    const crumbs = [{ label: t("nav.portal"), onClick: () => onClearApplication() }];

    if (currentView === 'dashboard') {
      crumbs.push({ label: t("nav.dashboard"), onClick: () => {} });
    } else if (currentView === 'applications') {
      crumbs.push({ label: t("nav.applications"), onClick: () => {} });
    } else if (activeApplication) {
      crumbs.push({ label: t("nav.applications"), onClick: () => onClearApplication() });
      crumbs.push({ label: activeApplication.application_number, onClick: () => {} });

      const stageLabels: Record<string, string> = {
        checklist: t("step.checklist"),
        document_verification: t("step.verification"),
        evc_evidence: t("step.evc"),
        final_summary: t("step.summary"),
      };
      if (stageLabels[currentView]) {
        crumbs.push({ label: stageLabels[currentView], onClick: () => {} });
      }
    } else {
      crumbs.push({ label: currentView, onClick: () => {} });
    }

    return crumbs;
  };

  const crumbs = getBreadcrumbs();

  return (
    <header className="bg-white border-b border-[#D9E2EC] sticky top-0 z-20 shadow-xs">
      
      {/* Top Utility Bar */}
      <div className="px-6 py-2 border-b border-[#E5EBF2] bg-[#F7F9FC] flex flex-wrap items-center justify-between text-xs gap-3">
        {/* Breadcrumbs */}
        <nav className="flex items-center gap-1.5 text-slate-500 font-medium">
          {crumbs.map((c, i) => (
            <React.Fragment key={i}>
              {i > 0 && <ChevronRight className="w-3.5 h-3.5 text-slate-400" />}
              <span
                onClick={c.onClick}
                className={i === crumbs.length - 1 ? "text-[#17365D] font-bold" : "hover:text-[#245A8D] cursor-pointer"}
              >
                {c.label}
              </span>
            </React.Fragment>
          ))}
        </nav>

        {/* Right Session Controls, Academic Year, and Language Selector */}
        <div className="flex items-center gap-3">
          <div className="text-[11px] bg-[#EAF2FA] text-[#17365D] border border-[#D9E2EC] px-2 py-0.5 rounded font-medium">
            {t("portal.review_context")}: <strong className="text-[#245A8D]">{t("portal.ay")}</strong>
          </div>

          {/* Officer Role Selector */}
          <div className="flex items-center gap-1.5 text-xs bg-white border border-[#D9E2EC] px-2.5 py-1 rounded">
            <span className="text-[#667085] text-[11px]">{t("portal.officer_role")}</span>
            <select
              value={currentRole}
              onChange={(e) => onRoleChange(e.target.value as UserRole)}
              className="bg-transparent font-semibold text-[#17365D] focus:outline-none cursor-pointer text-xs border-none p-0"
            >
              <option value="Scrutiny Reviewer">{t("portal.role.scrutiny")}</option>
              <option value="EVC Reviewer/Inspector">{t("portal.role.evc")}</option>
              <option value="System Administrator">{t("portal.role.admin")}</option>
              <option value="Read-only Auditor">{t("portal.role.auditor")}</option>
            </select>
          </div>

          {/* Hindi / English Language Selector at Top Right Area */}
          <div className="flex items-center gap-1.5 text-xs bg-white border border-[#245A8D]/40 px-2.5 py-1 rounded shadow-2xs">
            <Languages className="w-3.5 h-3.5 text-[#245A8D]" />
            <select
              value={language}
              onChange={(e) => setLanguage(e.target.value as any)}
              className="bg-transparent font-bold text-[#17365D] focus:outline-none cursor-pointer text-xs border-none p-0"
            >
              <option value="en">English (EN)</option>
              <option value="hi">हिन्दी (Hindi)</option>
            </select>
          </div>
        </div>
      </div>

      {/* Contextual Active Application Banner & Simple Stepper (if application is selected) */}
      {activeApplication && (
        <div className="px-6 py-3 bg-[#F3F7FB] border-b border-[#D9E2EC]">
          <div className="flex flex-col lg:flex-row lg:items-center justify-between gap-3">
            
            {/* Institution & Application Identifier */}
            <div className="space-y-0.5">
              <div className="flex items-center gap-2 flex-wrap">
                <span className="font-mono text-xs font-bold text-[#17365D] bg-white border border-[#D9E2EC] px-2 py-0.5 rounded shadow-2xs">
                  {activeApplication.application_number}
                </span>
                <span className="text-xs bg-[#EAF2FA] text-[#245A8D] font-semibold px-2 py-0.5 rounded">
                  {t(`cat.${activeApplication.category}`) || activeApplication.category}
                </span>
                <span className={`text-[10px] font-bold px-2 py-0.5 rounded ${
                  activeApplication.priority === 'RED' ? 'bg-[#FDECEC] text-[#B42318] border border-[#F87171]' :
                  activeApplication.priority === 'AMBER' ? 'bg-[#FFF5D9] text-[#946200] border border-[#FCD34D]' :
                  'bg-[#EAF6EE] text-[#237A45] border border-[#86EFAC]'
                }`}>
                  {t("common.priority")}: {activeApplication.priority}
                </span>
                <span className="text-[11px] text-[#667085]">
                  {t("common.cycle")} #{activeApplication.review_cycle || 1}
                </span>
              </div>
              <h1 className="text-base font-bold text-[#17365D] tracking-tight">
                {activeApplication.institution_name}
              </h1>
              <p className="text-xs text-[#667085]">
                {activeApplication.institution_address}
              </p>
            </div>

            {/* Simple Workflow Stepper: Without Subtext and Without Status Badges */}
            <div className="flex items-center gap-1.5 bg-white border border-[#D9E2EC] p-1 rounded-lg shadow-2xs overflow-x-auto shrink-0">
              
              <button
                onClick={() => onNavigateWorkflow('checklist')}
                className={`px-3 py-1.5 rounded text-xs font-bold transition-all ${
                  currentView === 'checklist' 
                    ? 'bg-[#17365D] text-white shadow-xs' 
                    : 'hover:bg-[#F3F7FB] text-[#243447]'
                }`}
              >
                {t("step.checklist")}
              </button>

              <ArrowRight className="w-3.5 h-3.5 text-slate-300 shrink-0" />

              <button
                onClick={() => onNavigateWorkflow('document_verification')}
                className={`px-3 py-1.5 rounded text-xs font-bold transition-all ${
                  currentView === 'document_verification' 
                    ? 'bg-[#17365D] text-white shadow-xs' 
                    : 'hover:bg-[#F3F7FB] text-[#243447]'
                }`}
              >
                {t("step.verification")}
              </button>

              <ArrowRight className="w-3.5 h-3.5 text-slate-300 shrink-0" />

              <button
                onClick={() => onNavigateWorkflow('evc_evidence')}
                className={`px-3 py-1.5 rounded text-xs font-bold transition-all ${
                  currentView === 'evc_evidence' 
                    ? 'bg-[#17365D] text-white shadow-xs' 
                    : 'hover:bg-[#F3F7FB] text-[#243447]'
                }`}
              >
                {t("step.evc")}
              </button>

              <ArrowRight className="w-3.5 h-3.5 text-slate-300 shrink-0" />

              <button
                onClick={() => onNavigateWorkflow('final_summary')}
                className={`px-3 py-1.5 rounded text-xs font-bold transition-all ${
                  currentView === 'final_summary' 
                    ? 'bg-[#17365D] text-white shadow-xs' 
                    : 'hover:bg-[#F3F7FB] text-[#243447]'
                }`}
              >
                {t("step.summary")}
              </button>

            </div>

          </div>
        </div>
      )}

    </header>
  );
};
