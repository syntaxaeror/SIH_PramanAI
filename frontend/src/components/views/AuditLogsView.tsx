import React, { useState } from 'react';
import { ShieldCheck, Search, Download, Filter, RotateCcw, Clock, User, Shield } from 'lucide-react';
import { AuditEvent } from '../../types';

interface AuditLogsViewProps {
  logs: AuditEvent[];
}

export const AuditLogsView: React.FC<AuditLogsViewProps> = ({ logs }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedAction, setSelectedAction] = useState('ALL');

  const filteredLogs = logs.filter(log => {
    if (selectedAction !== 'ALL' && log.action !== selectedAction) return false;
    if (searchTerm) {
      const s = searchTerm.toLowerCase();
      return (
        log.user_name.toLowerCase().includes(s) ||
        log.target_id.toLowerCase().includes(s) ||
        log.action.toLowerCase().includes(s) ||
        log.details.toLowerCase().includes(s)
      );
    }
    return true;
  });

  const handleExportCsv = () => {
    const headers = ["Timestamp", "User", "Role", "Action", "Target Type", "Target ID", "Details"];
    const rows = filteredLogs.map(l => [
      `"${l.timestamp}"`,
      `"${l.user_name}"`,
      `"${l.user_role}"`,
      `"${l.action}"`,
      `"${l.target_type}"`,
      `"${l.target_id}"`,
      `"${l.details.replace(/"/g, '""')}"`
    ]);

    const csvContent = "data:text/csv;charset=utf-8," + [headers.join(","), ...rows.map(e => e.join(","))].join("\n");
    const encodedUri = encodeURI(csvContent);
    const link = document.createElement("a");
    link.setAttribute("href", encodedUri);
    link.setAttribute("download", `AICTE_Audit_Log_${new Date().toISOString().slice(0, 10)}.csv`);
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="space-y-4 max-w-7xl mx-auto">
      
      {/* Page Header */}
      <div className="pb-3 border-b border-[#D9E2EC] flex flex-col sm:flex-row sm:items-center justify-between gap-2">
        <div>
          <h1 className="text-xl font-bold text-[#17365D] tracking-tight">
            Security & System Audit Logs
          </h1>
          <p className="text-xs text-[#667085] mt-0.5">
            Immutable, append-only audit trail capturing user identities, actions, affected resources, and system events.
          </p>
        </div>

        <button
          onClick={handleExportCsv}
          className="bg-white border border-[#245A8D] hover:bg-[#EAF2FA] text-[#245A8D] text-xs font-semibold px-3 py-1.5 rounded flex items-center gap-1.5 transition-colors self-start sm:self-auto"
        >
          <Download className="w-3.5 h-3.5" />
          <span>Export Audit Log (CSV)</span>
        </button>
      </div>

      {/* Filter / Search Bar */}
      <div className="bg-white border border-[#D9E2EC] rounded p-3 shadow-2xs flex flex-col md:flex-row items-center justify-between gap-3 text-xs">
        
        <div className="relative flex-1 w-full md:max-w-md">
          <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            placeholder="Search by User, Action, Resource ID, or Keyword..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full bg-[#F7F9FC] border border-[#D9E2EC] rounded pl-9 pr-3 py-1.5 text-xs text-[#243447] focus:outline-none focus:border-[#245A8D] focus:bg-white"
          />
        </div>

        <div className="flex items-center gap-2 w-full md:w-auto">
          <span className="text-[#667085] font-medium shrink-0">Filter Action:</span>
          <select
            value={selectedAction}
            onChange={(e) => setSelectedAction(e.target.value)}
            className="bg-white border border-[#D9E2EC] text-[#243447] text-xs rounded px-2.5 py-1.5 focus:outline-none focus:border-[#245A8D]"
          >
            <option value="ALL">All Recorded Actions</option>
            <option value="DATA_IMPORT">DATA_IMPORT</option>
            <option value="DOCUMENT_MAPPING">DOCUMENT_MAPPING</option>
            <option value="DOCUMENT_REMAP">DOCUMENT_REMAP</option>
            <option value="DEFICIENCY_UPHELD">DEFICIENCY_UPHELD</option>
            <option value="EVC_FLAG_ASSIGNED">EVC_FLAG_ASSIGNED</option>
            <option value="REPORT_EXPORT_PDF">REPORT_EXPORT_PDF</option>
          </select>
        </div>

      </div>

      {/* Audit Logs Table */}
      <div className="bg-white border border-[#D9E2EC] rounded shadow-2xs overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse gov-table">
            <thead>
              <tr>
                <th className="w-36">Timestamp</th>
                <th className="w-48">User & Role</th>
                <th className="w-40">Action</th>
                <th className="w-44">Target Resource</th>
                <th>Audit Details & Parameters</th>
              </tr>
            </thead>
            <tbody>
              {filteredLogs.map((log) => (
                <tr key={log.id} className="hover:bg-[#F3F7FB]">
                  <td className="font-mono text-xs text-[#667085] whitespace-nowrap">
                    {log.timestamp}
                  </td>
                  <td>
                    <div className="font-semibold text-xs text-[#17365D]">
                      {log.user_name}
                    </div>
                    <div className="text-[10px] text-[#667085]">
                      {log.user_role}
                    </div>
                  </td>
                  <td>
                    <span className="font-mono text-[11px] font-semibold text-[#17365D] bg-[#EAF2FA] px-2 py-0.5 rounded border border-[#D9E2EC]">
                      {log.action}
                    </span>
                  </td>
                  <td>
                    <div className="text-xs font-semibold text-[#243447]">
                      {log.target_type}
                    </div>
                    <div className="font-mono text-[11px] text-[#245A8D]">
                      {log.target_id}
                    </div>
                  </td>
                  <td className="text-xs text-[#243447] leading-relaxed font-sans">
                    {log.details}
                  </td>
                </tr>
              ))}

              {filteredLogs.length === 0 && (
                <tr>
                  <td colSpan={5} className="text-center py-10 text-[#667085]">
                    No audit events match your search criteria.
                  </td>
                </tr>
              )}
            </tbody>
          </table>
        </div>
      </div>

    </div>
  );
};
