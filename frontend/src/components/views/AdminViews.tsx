import React, { useState } from 'react';
import { Users, Sliders, Scale, Settings, CheckCircle2, XCircle, Shield, Plus, Lock } from 'lucide-react';
import { RuleDefinition, UserRole } from '../../types';

interface AdminViewsProps {
  viewType: 'admin_users' | 'admin_checklists' | 'admin_rules' | 'admin_settings';
  rules: RuleDefinition[];
  currentRole: UserRole;
  onToggleRule: (ruleId: string) => Promise<void>;
}

export const AdminViews: React.FC<AdminViewsProps> = ({
  viewType,
  rules,
  currentRole,
  onToggleRule,
}) => {
  const [togglingId, setTogglingId] = useState<string | null>(null);

  const handleToggle = async (id: string) => {
    setTogglingId(id);
    await onToggleRule(id);
    setTogglingId(null);
  };

  if (viewType === 'admin_users') {
    return (
      <div className="space-y-4 max-w-7xl mx-auto">
        <div className="pb-3 border-b border-[#D9E2EC]">
          <h1 className="text-xl font-bold text-[#17365D] tracking-tight">
            Users and Role-Based Access Control (RBAC)
          </h1>
          <p className="text-xs text-[#667085] mt-0.5">
            Manage authorized scrutiny officers, EVC inspectors, administrators, and read-only auditors.
          </p>
        </div>

        <div className="bg-white border border-[#D9E2EC] rounded shadow-2xs overflow-hidden">
          <table className="w-full text-left border-collapse gov-table">
            <thead>
              <tr>
                <th>Officer Name</th>
                <th>Institutional ID</th>
                <th>Assigned Role</th>
                <th>Department / Region</th>
                <th>Status</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td className="font-semibold text-[#17365D]">Prof. S. R. Sharma</td>
                <td className="font-mono text-xs text-[#667085]">AICTE-OFF-101</td>
                <td><span className="bg-[#EAF2FA] text-[#245A8D] px-2 py-0.5 rounded text-xs font-semibold">Scrutiny Reviewer</span></td>
                <td className="text-xs">South-Western Regional Office (Bengaluru)</td>
                <td><span className="bg-[#EAF6EE] text-[#237A45] px-2 py-0.5 rounded text-[11px] font-bold">Active</span></td>
              </tr>
              <tr>
                <td className="font-semibold text-[#17365D]">Dr. M. K. Ananth</td>
                <td className="font-mono text-xs text-[#667085]">AICTE-OFF-102</td>
                <td><span className="bg-[#FFF5D9] text-[#946200] px-2 py-0.5 rounded text-xs font-semibold">EVC Reviewer/Inspector</span></td>
                <td className="text-xs">Karnataka EVC Standing Committee</td>
                <td><span className="bg-[#EAF6EE] text-[#237A45] px-2 py-0.5 rounded text-[11px] font-bold">Active</span></td>
              </tr>
              <tr>
                <td className="font-semibold text-[#17365D]">S. K. Bansal</td>
                <td className="font-mono text-xs text-[#667085]">AICTE-ADM-001</td>
                <td><span className="bg-[#F1F3F5] text-[#243447] px-2 py-0.5 rounded text-xs font-semibold">System Administrator</span></td>
                <td className="text-xs">Approvals Bureau, AICTE HQ New Delhi</td>
                <td><span className="bg-[#EAF6EE] text-[#237A45] px-2 py-0.5 rounded text-[11px] font-bold">Active</span></td>
              </tr>
              <tr>
                <td className="font-semibold text-[#17365D]">CMA Rajesh Singhania</td>
                <td className="font-mono text-xs text-[#667085]">AICTE-AUD-204</td>
                <td><span className="bg-[#F1F3F5] text-[#667085] px-2 py-0.5 rounded text-xs font-semibold">Read-only Auditor</span></td>
                <td className="text-xs">Independent Quality Audit Directorate</td>
                <td><span className="bg-[#EAF6EE] text-[#237A45] px-2 py-0.5 rounded text-[11px] font-bold">Active</span></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    );
  }

  if (viewType === 'admin_checklists') {
    return (
      <div className="space-y-4 max-w-7xl mx-auto">
        <div className="pb-3 border-b border-[#D9E2EC]">
          <h1 className="text-xl font-bold text-[#17365D] tracking-tight">
            Category & Checklist Configuration
          </h1>
          <p className="text-xs text-[#667085] mt-0.5">
            Configure expected document types, mandatory conditions, and aliases per category and academic year.
          </p>
        </div>

        <div className="bg-white border border-[#D9E2EC] rounded shadow-2xs p-4 space-y-4 text-xs">
          <div className="flex justify-between items-center border-b border-[#D9E2EC] pb-3">
            <span className="font-bold text-sm text-[#17365D]">Configured Regulatory Profiles (AY 2025–26)</span>
            <span className="bg-[#EAF2FA] text-[#245A8D] px-2.5 py-1 rounded font-semibold">APH Version 2025.2</span>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div className="p-3 border border-[#D9E2EC] rounded space-y-2 bg-[#F7F9FC]">
              <div className="font-bold text-[#17365D]">Extension of Approval (EoA)</div>
              <p className="text-[#667085] text-[11px]">7 Required Documents: Affidavit 2, TER Fee Slip, Fire Safety NOC, Occupancy Cert, Structural Stability, Geolocation Map, Audited Balance Sheet.</p>
              <div className="text-[10px] text-[#237A45] font-semibold">Enforced in Pipeline • Active</div>
            </div>

            <div className="p-3 border border-[#D9E2EC] rounded space-y-2 bg-[#F7F9FC]">
              <div className="font-bold text-[#17365D]">New Technical Institution</div>
              <p className="text-[#667085] text-[11px]">9 Required Documents: Land Ownership Deed, Master Building Plan, Form D, Affidavit 1 & 2, Trust Registration, Fixed Deposit Security Deposit.</p>
              <div className="text-[10px] text-[#237A45] font-semibold">Enforced in Pipeline • Active</div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  if (viewType === 'admin_rules') {
    return (
      <div className="space-y-4 max-w-7xl mx-auto">
        <div className="pb-3 border-b border-[#D9E2EC]">
          <h1 className="text-xl font-bold text-[#17365D] tracking-tight">
            Rules and Regulations Administration (APH 2025–26)
          </h1>
          <p className="text-xs text-[#667085] mt-0.5">
            Manage versioned regulatory rules with authoritative citations from the AICTE Approval Process Handbook.
          </p>
        </div>

        <div className="space-y-3">
          {rules.map((rule) => (
            <div key={rule.id} className="bg-white border border-[#D9E2EC] rounded p-4 shadow-2xs flex flex-col md:flex-row justify-between gap-4">
              <div className="space-y-1.5 flex-1 text-xs">
                <div className="flex items-center gap-2">
                  <span className="font-mono text-[11px] font-bold text-[#17365D] bg-[#EAF2FA] px-2 py-0.5 rounded">
                    {rule.id}
                  </span>
                  <span className="text-[11px] bg-slate-100 text-[#667085] px-2 py-0.5 rounded font-medium">
                    {rule.category}
                  </span>
                  <span className={`text-[10px] font-bold px-1.5 py-0.2 rounded ${
                    rule.is_active ? 'bg-[#EAF6EE] text-[#237A45]' : 'bg-[#F1F3F5] text-[#667085]'
                  }`}>
                    {rule.is_active ? 'Active' : 'Retired'}
                  </span>
                </div>
                <h3 className="font-bold text-[#17365D] text-sm">{rule.title}</h3>
                <div className="text-[#243447]">
                  <strong>Citation:</strong> {rule.clause} ({rule.source_title})
                </div>
                <div className="text-[#667085] text-[11px]">
                  <strong>Algorithm:</strong> {rule.validation_logic}
                </div>
              </div>

              <div className="shrink-0 flex items-center">
                <button
                  onClick={() => handleToggle(rule.id)}
                  disabled={togglingId === rule.id}
                  className={`text-xs font-semibold px-3 py-1.5 rounded transition-colors ${
                    rule.is_active 
                      ? 'bg-slate-100 hover:bg-[#FDECEC] text-[#B42318] border border-[#D9E2EC]'
                      : 'bg-[#237A45] hover:bg-[#1E6B3C] text-white'
                  }`}
                >
                  {togglingId === rule.id ? 'Saving...' : rule.is_active ? 'Deactivate Rule' : 'Activate Rule'}
                </button>
              </div>
            </div>
          ))}
        </div>
      </div>
    );
  }

  return (
    <div className="space-y-4 max-w-7xl mx-auto">
      <div className="pb-3 border-b border-[#D9E2EC]">
        <h1 className="text-xl font-bold text-[#17365D] tracking-tight">
          System and Security Settings
        </h1>
        <p className="text-xs text-[#667085] mt-0.5">
          Configure security protocols, storage adapters, and statutory audit retention parameters.
        </p>
      </div>

      <div className="bg-white border border-[#D9E2EC] rounded shadow-2xs p-6 space-y-4 text-xs">
        <div className="space-y-3">
          <div className="flex justify-between items-center py-2 border-b border-[#D9E2EC]">
            <div>
              <div className="font-bold text-[#17365D]">Statutory Audit Retention</div>
              <div className="text-[11px] text-[#667085]">Immutable audit events preserved for minimum regulatory inquiry window.</div>
            </div>
            <span className="font-mono font-bold text-[#245A8D]">7 Years (Mandatory)</span>
          </div>

          <div className="flex justify-between items-center py-2 border-b border-[#D9E2EC]">
            <div>
              <div className="font-bold text-[#17365D]">OCR Engine Adapter</div>
              <div className="text-[11px] text-[#667085]">Default text extraction and bounding box engine.</div>
            </div>
            <span className="font-semibold text-[#17365D]">PaddleOCR / PyMuPDF Adapter</span>
          </div>

          <div className="flex justify-between items-center py-2 border-b border-[#D9E2EC]">
            <div>
              <div className="font-bold text-[#17365D]">Perceptual Hash Duplicate Threshold</div>
              <div className="text-[11px] text-[#667085]">pHash Hamming distance similarity triggering review flag.</div>
            </div>
            <span className="font-mono font-bold text-[#B42318]">≥ 95% Match</span>
          </div>
        </div>
      </div>
    </div>
  );
};
