import React from 'react';
import { 
  LayoutDashboard, 
  FileText, 
  History, 
  ShieldCheck, 
  Users, 
  Sliders, 
  Scale, 
  Settings, 
  LogOut,
  ChevronRight,
  ShieldAlert,
  Building2
} from 'lucide-react';
import { UserRole } from '../../types';
import { useI18n } from '../../i18n';

interface AppSidebarProps {
  currentView: string;
  onNavigate: (view: string) => void;
  currentRole: UserRole;
  officerName: string;
  hasActiveApplication: boolean;
  onOpenProfile: () => void;
  onOpenSignOut: () => void;
}

export const AppSidebar: React.FC<AppSidebarProps> = ({
  currentView,
  onNavigate,
  currentRole,
  officerName,
  hasActiveApplication,
  onOpenProfile,
  onOpenSignOut,
}) => {
  const { t } = useI18n();
  const isAdmin = currentRole === 'System Administrator';

  const navItemClass = (viewKey: string, disabled: boolean = false) => {
    const isActive = currentView === viewKey;
    if (disabled) {
      return "flex items-center justify-between px-3.5 py-2 text-xs font-medium text-slate-400 cursor-not-allowed opacity-60 rounded";
    }
    return `flex items-center justify-between px-3.5 py-2 text-xs font-medium rounded transition-colors ${
      isActive 
        ? "bg-[#EAF2FA] text-[#17365D] font-semibold border-l-3 border-[#245A8D]" 
        : "text-[#243447] hover:bg-[#F3F7FB] hover:text-[#17365D]"
    }`;
  };

  return (
    <aside className="w-[260px] bg-white border-r border-[#D9E2EC] flex flex-col justify-between shrink-0 h-screen sticky top-0 select-none z-30">
      
      {/* Top Section: Header & Navigation */}
      <div className="flex flex-col flex-1 overflow-y-auto">
        
        {/* Government Branding Header */}
        <div className="px-5 py-4 border-b border-[#D9E2EC] bg-[#F7F9FC]">
          <div className="flex items-center gap-2.5">
            <div className="w-9 h-9 rounded bg-[#17365D] text-white flex items-center justify-center font-bold text-sm shadow-sm shrink-0">
              AICTE
            </div>
            <div>
              <div className="text-xs font-bold text-[#17365D] leading-tight tracking-tight uppercase">
                {t("portal.title")}
              </div>
              <div className="text-[10px] text-[#667085] leading-tight mt-0.5 font-medium">
                {t("portal.subtitle")}
              </div>
            </div>
          </div>
          <div className="mt-2 text-[10px] bg-[#EAF2FA] text-[#245A8D] font-semibold px-2 py-0.5 rounded flex items-center justify-between">
            <span>{t("portal.academic_cycle")}</span>
            <span>{t("portal.ay")}</span>
          </div>
        </div>

        {/* Navigation Sections */}
        <div className="p-3 space-y-4">
          
          {/* Section: WORKSPACE */}
          <div>
            <div className="px-3.5 text-[10px] font-bold text-[#667085] uppercase tracking-wider mb-1">
              {t("nav.workspace")}
            </div>
            <nav className="space-y-0.5">
              <button
                onClick={() => onNavigate('dashboard')}
                className={navItemClass('dashboard')}
              >
                <div className="flex items-center gap-2.5">
                  <LayoutDashboard className="w-4 h-4 text-[#245A8D]" />
                  <span>{t("nav.dashboard")}</span>
                </div>
              </button>

              <button
                onClick={() => onNavigate('applications')}
                className={navItemClass('applications')}
              >
                <div className="flex items-center gap-2.5">
                  <FileText className="w-4 h-4 text-[#245A8D]" />
                  <span>{t("nav.applications")}</span>
                </div>
              </button>
            </nav>
          </div>

          {/* Section: RECORDS */}
          <div>
            <div className="px-3.5 text-[10px] font-bold text-[#667085] uppercase tracking-wider mb-1">
              {t("nav.records")}
            </div>
            <nav className="space-y-0.5">
              <button
                onClick={() => onNavigate('application_history')}
                className={navItemClass('application_history')}
              >
                <div className="flex items-center gap-2.5">
                  <History className="w-4 h-4 text-[#667085]" />
                  <span>{t("nav.history")}</span>
                </div>
              </button>

              <button
                onClick={() => onNavigate('audit_logs')}
                className={navItemClass('audit_logs')}
              >
                <div className="flex items-center gap-2.5">
                  <ShieldCheck className="w-4 h-4 text-[#667085]" />
                  <span>{t("nav.audit")}</span>
                </div>
              </button>
            </nav>
          </div>

          {/* Section: ADMINISTRATION (Admin Role Only) */}
          {isAdmin && (
            <div>
              <div className="px-3.5 text-[10px] font-bold text-[#946200] uppercase tracking-wider mb-1 flex items-center justify-between">
                <span>{t("nav.admin_settings")}</span>
                <span className="bg-[#FFF5D9] text-[#946200] text-[9px] font-semibold px-1 rounded">Admin</span>
              </div>
              <nav className="space-y-0.5">
                <button
                  onClick={() => onNavigate('admin_users')}
                  className={navItemClass('admin_users')}
                >
                  <div className="flex items-center gap-2.5">
                    <Users className="w-4 h-4 text-[#667085]" />
                    <span>{t("nav.admin_users")}</span>
                  </div>
                </button>

                <button
                  onClick={() => onNavigate('admin_checklists')}
                  className={navItemClass('admin_checklists')}
                >
                  <div className="flex items-center gap-2.5">
                    <Sliders className="w-4 h-4 text-[#667085]" />
                    <span>{t("nav.admin_checklists")}</span>
                  </div>
                </button>

                <button
                  onClick={() => onNavigate('admin_rules')}
                  className={navItemClass('admin_rules')}
                >
                  <div className="flex items-center gap-2.5">
                    <Scale className="w-4 h-4 text-[#667085]" />
                    <span>{t("nav.admin_rules")}</span>
                  </div>
                </button>

                <button
                  onClick={() => onNavigate('admin_settings')}
                  className={navItemClass('admin_settings')}
                >
                  <div className="flex items-center gap-2.5">
                    <Settings className="w-4 h-4 text-[#667085]" />
                    <span>{t("nav.admin_settings")}</span>
                  </div>
                </button>
              </nav>
            </div>
          )}

        </div>

      </div>

      {/* Anchored Bottom: Profile & Sign Out */}
      <div className="border-t border-[#D9E2EC] p-3 bg-[#F7F9FC]">
        {/* Officer Profile Card */}
        <button
          onClick={onOpenProfile}
          className="w-full text-left p-2 rounded hover:bg-[#EAF2FA] transition-colors flex items-center justify-between mb-2 group cursor-pointer"
        >
          <div className="flex items-center gap-2.5 min-w-0">
            <div className="w-8 h-8 rounded-full bg-[#17365D] text-white flex items-center justify-center text-xs font-bold shrink-0">
              {officerName.split(' ').map(n => n[0]).slice(0, 2).join('')}
            </div>
            <div className="min-w-0">
              <div className="text-xs font-semibold text-[#17365D] truncate leading-tight">
                {officerName}
              </div>
              <div className="text-[10px] text-[#667085] truncate leading-tight mt-0.5">
                {currentRole === 'Scrutiny Reviewer' ? t("portal.role.scrutiny") :
                 currentRole === 'EVC Reviewer/Inspector' ? t("portal.role.evc") :
                 currentRole === 'System Administrator' ? t("portal.role.admin") :
                 t("portal.role.auditor")}
              </div>
            </div>
          </div>
          <ChevronRight className="w-3.5 h-3.5 text-slate-400 group-hover:text-[#17365D] shrink-0" />
        </button>

        {/* Sign Out Button */}
        <button
          onClick={onOpenSignOut}
          className="w-full flex items-center justify-center gap-2 px-3 py-1.5 rounded border border-[#D9E2EC] bg-white hover:bg-[#FDECEC] hover:text-[#B42318] hover:border-[#F87171] text-xs font-medium text-[#243447] transition-colors cursor-pointer"
        >
          <LogOut className="w-3.5 h-3.5 text-[#667085]" />
          <span>{t("portal.sign_out")}</span>
        </button>
      </div>

    </aside>
  );
};
