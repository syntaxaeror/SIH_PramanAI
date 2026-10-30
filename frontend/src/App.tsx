import React, { useState, useEffect } from 'react';
import { AppSidebar } from './components/layout/AppSidebar';
import { TopHeader } from './components/layout/TopHeader';
import { DashboardView } from './components/views/DashboardView';
import { ApplicationsListView } from './components/views/ApplicationsListView';
import { ChecklistView } from './components/views/ChecklistView';
import { DocumentVerificationView } from './components/views/DocumentVerificationView';
import { EvcEvidenceRoomView } from './components/views/EvcEvidenceRoomView';
import { FinalSummaryView } from './components/views/FinalSummaryView';
import { ApplicationHistoryView } from './components/views/ApplicationHistoryView';
import { AuditLogsView } from './components/views/AuditLogsView';
import { AdminViews } from './components/views/AdminViews';
import { ProfileModal } from './components/modals/ProfileModal';
import { SignOutDialog } from './components/modals/SignOutDialog';
import { DocumentViewerModal } from './components/DocumentViewerModal';
import { ExplainabilityModal } from './components/ExplainabilityModal';
import { 
  Application, DocumentItem, Finding, EVCEvidenceItem, 
  RuleDefinition, AuditEvent, UserRole, WorkflowStage 
} from './types';

const API_BASE = (import.meta.env.VITE_API_BASE_URL || '').replace(/\/$/, '');

export function App() {
  const [currentRole, setCurrentRole] = useState<UserRole>('Scrutiny Reviewer');
  const [officerName, setOfficerName] = useState('Prof. S. R. Sharma');
  const [currentView, setCurrentView] = useState<string>('dashboard');

  // Application and Data State
  const [applications, setApplications] = useState<Application[]>([]);
  const [stats, setStats] = useState<any>(null);
  const [rules, setRules] = useState<RuleDefinition[]>([]);
  const [auditLogs, setAuditLogs] = useState<AuditEvent[]>([]);
  
  // Active Scrutiny Application Context
  const [activeApplication, setActiveApplication] = useState<Application | null>(null);
  const [appDocuments, setAppDocuments] = useState<DocumentItem[]>([]);
  const [appFindings, setAppFindings] = useState<Finding[]>([]);
  const [appEvcItems, setAppEvcItems] = useState<EVCEvidenceItem[]>([]);

  // Filtering
  const [selectedCategory, setSelectedCategory] = useState<string>('ALL');

  // Modals & Navigation Selections
  const [inspectingDoc, setInspectingDoc] = useState<DocumentItem | null>(null);
  const [inspectingFinding, setInspectingFinding] = useState<Finding | null>(null);
  const [selectedVerificationDocId, setSelectedVerificationDocId] = useState<string | undefined>(undefined);
  const [showProfileModal, setShowProfileModal] = useState<boolean>(false);
  const [showSignOutDialog, setShowSignOutDialog] = useState<boolean>(false);

  // Fetch initial system data
  const fetchData = async () => {
    try {
      const [appsRes, statsRes, rulesRes, auditRes] = await Promise.all([
        fetch(`${API_BASE}/api/applications`),
        fetch(`${API_BASE}/api/stats`),
        fetch(`${API_BASE}/api/rules`),
        fetch(`${API_BASE}/api/audit`),
      ]);

      if (appsRes.ok) {
        const appsData = await appsRes.json();
        // Enrich applications with workflow stages if missing
        const enriched = appsData.map((a: Application) => ({
          ...a,
          expected_documents_count: a.expected_documents_count || 7,
          workflow_stage: a.workflow_stage || 'checklist',
          stage_progress: a.stage_progress || {
            checklist: 'Completed',
            document_verification: a.deficiency_count > 0 ? 'Action Required' : 'In Progress',
            evc_evidence: a.priority === 'RED' ? 'Action Required' : 'In Progress',
            final_summary: 'Not Started'
          },
          review_cycle: a.review_cycle || 1,
        }));
        setApplications(enriched);
        if (enriched.length > 0 && !activeApplication) {
          handleOpenApplication(enriched[0], false);
        }
      }
      if (statsRes.ok) setStats(await statsRes.json());
      if (rulesRes.ok) setRules(await rulesRes.json());
      if (auditRes.ok) setAuditLogs(await auditRes.json());
    } catch (err) {
      console.error("API error loading portal data:", err);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  // When an application is opened for scrutiny
  const handleOpenApplication = async (app: Application, navigateToWorkflow: boolean = true) => {
    setActiveApplication(app);
    if (navigateToWorkflow) {
      setCurrentView('checklist'); // Opens at Step 1 of the workflow
    }
    try {
      const [docsRes, findingsRes, evcRes] = await Promise.all([
        fetch(`${API_BASE}/api/applications/${app.id}/documents`),
        fetch(`${API_BASE}/api/applications/${app.id}/findings`),
        fetch(`${API_BASE}/api/applications/${app.id}/evc`),
      ]);

      if (docsRes.ok) {
        const docs = await docsRes.json();
        const formattedDocs = docs.map((d: DocumentItem) => ({
          ...d,
          is_mandatory: true,
          upload_status: d.upload_status || 'Uploaded',
          document_status: d.document_status || (d.mapped_type.includes('Fire') ? 'Needs Attention' : 'Reviewed'),
        }));
        setAppDocuments(formattedDocs);
      }
      if (findingsRes.ok) setAppFindings(await findingsRes.json());
      if (evcRes.ok) setAppEvcItems(await evcRes.json());
    } catch (err) {
      console.error("Error loading application detail records:", err);
    }
  };

  // Safe navigation handler that ensures active application exists for scrutiny views
  const handleNavigate = (view: string) => {
    if (['checklist', 'document_verification', 'evc_evidence', 'final_summary'].includes(view)) {
      if (!activeApplication && applications.length > 0) {
        handleOpenApplication(applications[0], false);
      }
    }
    setCurrentView(view);
  };

  // Category selection on Dashboard immediately filters the Applications list
  const handleSelectCategoryFromDashboard = (categoryName: string) => {
    setSelectedCategory(categoryName);
    setCurrentView('applications');
  };

  // Role change handler
  const handleRoleChange = async (role: UserRole) => {
    setCurrentRole(role);
    try {
      const res = await fetch(`${API_BASE}/api/auth/switch-role?role=${encodeURIComponent(role)}`, {
        method: 'POST',
      });
      if (res.ok) {
        const user = await res.json();
        setOfficerName(user.name.split(' (')[0]);
        fetchData();
      }
    } catch (err) {
      console.error(err);
    }
  };

  // Finding disposition update
  const handleUpdateDisposition = async (findingId: string, disposition: string, notes: string) => {
    try {
      const res = await fetch(`${API_BASE}/api/findings/${findingId}/disposition`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ disposition, reviewer_notes: notes }),
      });
      if (res.ok) {
        const updated = await res.json();
        setAppFindings((prev) => prev.map((f) => (f.id === findingId ? updated : f)));
        fetchData();
      }
    } catch (err) {
      console.error(err);
    }
  };

  // Document remap handler
  const handleRemapDocument = async (docId: string, newType: string, reason: string) => {
    try {
      const res = await fetch(`${API_BASE}/api/documents/${docId}/remap`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ new_type: newType, reason }),
      });
      if (res.ok) {
        const updated = await res.json();
        setAppDocuments((prev) => prev.map((d) => (d.id === docId ? updated : d)));
        if (inspectingDoc && inspectingDoc.id === docId) {
          setInspectingDoc(updated);
        }
        fetchData();
      }
    } catch (err) {
      console.error(err);
    }
  };

  // Mark document reviewed
  const handleMarkDocumentReviewed = async (docId: string) => {
    try {
      await fetch(`${API_BASE}/api/documents/${docId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ document_status: 'Reviewed' })
      });
    } catch (err) {
      console.error(err);
    }
    setAppDocuments(prev => prev.map(d => d.id === docId ? { ...d, document_status: 'Reviewed' } : d));
    fetchData();
  };

  // Run live statutory rule engine verification
  const handleRunVerification = async (appId: string) => {
    try {
      const res = await fetch(`${API_BASE}/api/applications/${appId}/run-verification`, {
        method: 'POST',
      });
      if (res.ok) {
        const data = await res.json();
        setActiveApplication(data.application);
        setAppFindings(data.findings);
        setApplications(prev => prev.map(a => a.id === appId ? data.application : a));
        fetchData();
        return data;
      }
    } catch (err) {
      console.error("Error executing rule verification engine:", err);
    }
  };

  // EVC flag inspection handler
  const handleFlagInspection = async (evcId: string, needed: boolean, reason: string) => {
    try {
      const res = await fetch(`${API_BASE}/api/evc/${evcId}/flag-inspection`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ inspection_needed: needed, inspection_reason: reason }),
      });
      if (res.ok) {
        const updated = await res.json();
        setAppEvcItems((prev) => prev.map((e) => (e.id === evcId ? updated : e)));
        fetchData();
      }
    } catch (err) {
      console.error(err);
    }
  };

  // Toggle rule
  const handleToggleRule = async (ruleId: string) => {
    try {
      const res = await fetch(`${API_BASE}/api/rules/${ruleId}/toggle`, { method: 'POST' });
      if (res.ok) {
        const updated = await res.json();
        setRules((prev) => prev.map((r) => (r.id === ruleId ? updated : r)));
        fetchData();
      }
    } catch (err) {
      console.error(err);
    }
  };

  // Mark as Scrutinized action
  const handleMarkScrutinized = async (note: string) => {
    if (!activeApplication) return;
    try {
      alert(`Application ${activeApplication.application_number} marked as Scrutinized.\nAudit recorded: "${note}"`);
      setActiveApplication(prev => prev ? {
        ...prev,
        status: 'SCRUTINY_COMPLETED',
        stage_progress: { ...prev.stage_progress, final_summary: 'Completed' }
      } : null);
      fetchData();
    } catch (err) {
      console.error(err);
    }
  };

  // Request Re-evaluation action
  const handleRequestReevaluation = async (reason: string) => {
    if (!activeApplication) return;
    try {
      alert(`New review cycle (Cycle #${ (activeApplication.review_cycle || 1) + 1 }) initiated for ${activeApplication.application_number}.\nReason: "${reason}"`);
      setActiveApplication(prev => prev ? {
        ...prev,
        review_cycle: (prev.review_cycle || 1) + 1,
        status: 'UNDER_SCRUTINY',
        stage_progress: {
          checklist: 'Completed',
          document_verification: 'In Progress',
          evc_evidence: 'In Progress',
          final_summary: 'Not Started'
        }
      } : null);
      fetchData();
    } catch (err) {
      console.error(err);
    }
  };

  // Download PDF Report
  const handleDownloadPdf = () => {
    if (!activeApplication) return;
    window.open(`${API_BASE}/api/applications/${activeApplication.id}/report/pdf`, '_blank');
  };

  // Sign out confirmation action
  const handleConfirmSignOut = () => {
    setShowSignOutDialog(false);
    setActiveApplication(null);
    setCurrentView('dashboard');
    alert("You have been signed out. Session credentials cleared.");
  };

  return (
    <div className="flex w-full min-h-screen bg-[#F7F9FC] text-[#243447]">
      
      {/* 4.1 Persistent Left Sidebar (260px) */}
      <AppSidebar
        currentView={currentView}
        onNavigate={(view) => handleNavigate(view as any)}
        currentRole={currentRole}
        officerName={officerName}
        hasActiveApplication={activeApplication !== null}
        onOpenProfile={() => setShowProfileModal(true)}
        onOpenSignOut={() => setShowSignOutDialog(true)}
      />

      {/* Main Right Content Layout */}
      <div className="flex-1 flex flex-col min-w-0">
        
        {/* 4.2 Top Header with Breadcrumbs, Application Stepper & Role Selector */}
        <TopHeader
          currentView={currentView}
          activeApplication={activeApplication}
          currentRole={currentRole}
          onRoleChange={handleRoleChange}
          onNavigateWorkflow={(stage: WorkflowStage) => setCurrentView(stage)}
          onClearApplication={() => {
            setActiveApplication(null);
            setCurrentView('applications');
          }}
        />

        {/* 4.3 Main Content Area */}
        <main className="flex-1 p-6 overflow-y-auto">
          
          {/* SCREEN 1: Scrutiny Officer Dashboard */}
          {currentView === 'dashboard' && (
            <DashboardView
              applications={applications}
              stats={stats}
              onSelectCategory={handleSelectCategoryFromDashboard}
              onOpenApplication={handleOpenApplication}
            />
          )}

          {/* SCREEN 2: Application List */}
          {currentView === 'applications' && (
            <ApplicationsListView
              applications={applications}
              selectedCategory={selectedCategory}
              onCategoryChange={setSelectedCategory}
              onOpenApplication={handleOpenApplication}
            />
          )}

          {/* SCREEN 3: Document Checklist */}
          {currentView === 'checklist' && activeApplication && (
            <ChecklistView
              application={activeApplication}
              documents={appDocuments}
              findings={appFindings}
              onOpenDocument={(doc) => setInspectingDoc(doc)}
              onOpenFinding={(f) => setInspectingFinding(f)}
              onInspectDocument={(docId) => {
                setSelectedVerificationDocId(docId);
                setCurrentView('document_verification');
              }}
            />
          )}

          {/* SCREEN 4: Document Verification */}
          {currentView === 'document_verification' && activeApplication && (
            <DocumentVerificationView
              application={activeApplication}
              documents={appDocuments}
              findings={appFindings}
              initialDocId={selectedVerificationDocId}
              onUpdateDisposition={handleUpdateDisposition}
              onMarkDocumentReviewed={handleMarkDocumentReviewed}
              onRunVerification={handleRunVerification}
            />
          )}

          {/* SCREEN 5: EVC Evidence Room */}
          {currentView === 'evc_evidence' && activeApplication && (
            <EvcEvidenceRoomView
              application={activeApplication}
              evcItems={appEvcItems}
              onFlagInspection={handleFlagInspection}
            />
          )}

          {/* SCREEN 6: Final Scrutiny Summary */}
          {currentView === 'final_summary' && activeApplication && (
            <FinalSummaryView
              application={activeApplication}
              documents={appDocuments}
              findings={appFindings}
              evcItems={appEvcItems}
              onDownloadPdf={handleDownloadPdf}
              onMarkScrutinized={handleMarkScrutinized}
              onRequestReevaluation={handleRequestReevaluation}
              onViewHistory={() => setCurrentView('application_history')}
            />
          )}

          {/* SCREEN 7: Application History */}
          {currentView === 'application_history' && (
            <ApplicationHistoryView events={[]} />
          )}

          {/* SCREEN 8: Audit Logs */}
          {currentView === 'audit_logs' && (
            <AuditLogsView logs={auditLogs} />
          )}

          {/* ADMINISTRATION VIEWS (Admin Role) */}
          {(currentView === 'admin_users' || 
            currentView === 'admin_checklists' || 
            currentView === 'admin_rules' || 
            currentView === 'admin_settings') && (
            <AdminViews
              viewType={currentView as any}
              rules={rules}
              currentRole={currentRole}
              onToggleRule={handleToggleRule}
            />
          )}

        </main>

        {/* Official Statutory Footer */}
        <footer className="border-t border-[#D9E2EC] bg-white py-3 px-6 text-center text-xs text-[#667085]">
          <div className="max-w-5xl mx-auto flex flex-col sm:flex-row items-center justify-between gap-2">
            <span>
              <strong>AICTE Internal Scrutiny Portal:</strong> Non-Statutory Administrative Verification System.
            </span>
            <span>
              All final approval and rejection powers remain exclusively with the Competent Authority under the AICTE Act, 1987.
            </span>
          </div>
        </footer>

      </div>

      {/* Global Modals */}
      <DocumentViewerModal
        document={inspectingDoc}
        onClose={() => setInspectingDoc(null)}
        onRemap={handleRemapDocument}
      />

      <ExplainabilityModal
        finding={inspectingFinding}
        onClose={() => setInspectingFinding(null)}
        onUpdateDisposition={handleUpdateDisposition}
      />

      {showProfileModal && (
        <ProfileModal
          officerName={officerName}
          role={currentRole}
          onClose={() => setShowProfileModal(false)}
        />
      )}

      {showSignOutDialog && (
        <SignOutDialog
          onConfirm={handleConfirmSignOut}
          onCancel={() => setShowSignOutDialog(false)}
        />
      )}

    </div>
  );
}

export default App;
