import React, { useState } from 'react';
import { History, Search, Filter, RotateCcw, Building2, User, Clock, ArrowRight } from 'lucide-react';
import { ApplicationHistoryEvent } from '../../types';

interface ApplicationHistoryViewProps {
  events: ApplicationHistoryEvent[];
}

const SAMPLE_HISTORY: ApplicationHistoryEvent[] = [
  {
    id: "hist-001",
    application_id: "AICTE-2025-ENG-0891",
    institution_name: "Vishwa Bharati Institute of Technology & Science",
    timestamp: "12-Mar-2025 10:14:02 AM",
    event_type: "APPLICATION_IMPORTED",
    previous_status: "SUBMITTED_EXTERNAL",
    new_status: "UNDER_SCRUTINY",
    performed_by: "System Batch Ingestion",
    review_cycle: 1,
    remarks: "Imported from central submission database. Batch BATCH-2025-03-12-01."
  },
  {
    id: "hist-002",
    application_id: "AICTE-2025-ENG-0891",
    institution_name: "Vishwa Bharati Institute of Technology & Science",
    timestamp: "12-Mar-2025 10:15:20 AM",
    event_type: "DOCUMENTS_AUTO_MAPPED",
    previous_status: "UNDER_SCRUTINY",
    new_status: "UNDER_SCRUTINY",
    performed_by: "AI Auto-Mapper Pipeline",
    review_cycle: 1,
    remarks: "7 documents mapped using regex and OCR keyword confirmation."
  },
  {
    id: "hist-003",
    application_id: "AICTE-2025-ENG-0891",
    institution_name: "Vishwa Bharati Institute of Technology & Science",
    timestamp: "12-Mar-2025 11:20:15 AM",
    event_type: "DEFICIENCY_UPHELD",
    previous_status: "UNDER_SCRUTINY",
    new_status: "DEFICIENCY_FLAGGED",
    performed_by: "Prof. S. R. Sharma (Senior Scrutiny Officer)",
    review_cycle: 1,
    remarks: "Upheld deficiency on Fire Safety Certificate expiry (expired 15-01-2025). Deficiency letter drafted."
  },
  {
    id: "hist-004",
    application_id: "AICTE-2025-ENG-0891",
    institution_name: "Vishwa Bharati Institute of Technology & Science",
    timestamp: "12-Mar-2025 11:45:30 AM",
    event_type: "EVC_FLAG_ASSIGNED",
    previous_status: "DEFICIENCY_FLAGGED",
    new_status: "DEFICIENCY_FLAGGED",
    performed_by: "Dr. M. K. Ananth (EVC Committee Member)",
    review_cycle: 1,
    remarks: "Computer Lab 3 photo flagged for on-site physical inspection due to 98.4% visual pHash match."
  },
  {
    id: "hist-005",
    application_id: "AICTE-2025-ENG-0422",
    institution_name: "Apex Institute of Technology & Research",
    timestamp: "14-Mar-2025 14:32:00 PM",
    event_type: "APPLICATION_IMPORTED",
    previous_status: "SUBMITTED_EXTERNAL",
    new_status: "UNDER_SCRUTINY",
    performed_by: "System Batch Ingestion",
    review_cycle: 1,
    remarks: "Imported intake increase application for 600 seats."
  }
];

export const ApplicationHistoryView: React.FC<ApplicationHistoryViewProps> = () => {
  const [searchTerm, setSearchTerm] = useState('');

  const filtered = SAMPLE_HISTORY.filter(h => 
    h.application_id.toLowerCase().includes(searchTerm.toLowerCase()) ||
    h.institution_name.toLowerCase().includes(searchTerm.toLowerCase()) ||
    h.event_type.toLowerCase().includes(searchTerm.toLowerCase())
  );

  return (
    <div className="space-y-4 max-w-7xl mx-auto">
      
      {/* Page Header */}
      <div className="pb-3 border-b border-[#D9E2EC]">
        <h1 className="text-xl font-bold text-[#17365D] tracking-tight">
          Application Lifecycle History
        </h1>
        <p className="text-xs text-[#667085] mt-0.5">
          Chronological record of every imported application's scrutiny lifecycle, review cycles, and reviewer transitions.
        </p>
      </div>

      {/* Filter / Search Bar */}
      <div className="bg-white border border-[#D9E2EC] rounded p-3 shadow-2xs flex items-center justify-between gap-3">
        <div className="relative flex-1 max-w-md">
          <Search className="w-4 h-4 text-slate-400 absolute left-3 top-1/2 -translate-y-1/2" />
          <input
            type="text"
            placeholder="Search by Application ID, Institution Name, or Event..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
            className="w-full bg-[#F7F9FC] border border-[#D9E2EC] rounded pl-9 pr-3 py-1.5 text-xs text-[#243447] focus:outline-none focus:border-[#245A8D] focus:bg-white"
          />
        </div>
        <div className="text-xs text-[#667085]">
          Showing <strong className="text-[#17365D]">{filtered.length}</strong> lifecycle events
        </div>
      </div>

      {/* History Table */}
      <div className="bg-white border border-[#D9E2EC] rounded shadow-2xs overflow-hidden">
        <div className="overflow-x-auto">
          <table className="w-full text-left border-collapse gov-table">
            <thead>
              <tr>
                <th className="w-36">Date & Time</th>
                <th className="w-40">Application ID</th>
                <th>Institution Name</th>
                <th>Event Type</th>
                <th>Status Transition</th>
                <th>Performed By</th>
                <th className="text-center w-20">Cycle</th>
                <th>Remarks</th>
              </tr>
            </thead>
            <tbody>
              {filtered.map((item) => (
                <tr key={item.id} className="hover:bg-[#F3F7FB]">
                  <td className="font-mono text-xs text-[#667085] whitespace-nowrap">
                    {item.timestamp}
                  </td>
                  <td className="font-mono text-xs font-bold text-[#17365D]">
                    {item.application_id}
                  </td>
                  <td className="font-semibold text-xs text-[#243447]">
                    {item.institution_name}
                  </td>
                  <td>
                    <span className="font-mono text-[11px] font-semibold text-[#245A8D] bg-[#EAF2FA] px-2 py-0.5 rounded">
                      {item.event_type}
                    </span>
                  </td>
                  <td className="text-xs">
                    <span className="text-[#667085]">{item.previous_status}</span>
                    <span className="text-slate-400 mx-1">→</span>
                    <span className="font-bold text-[#17365D]">{item.new_status}</span>
                  </td>
                  <td className="text-xs font-medium text-[#243447]">
                    {item.performed_by}
                  </td>
                  <td className="text-center font-bold text-xs text-[#245A8D]">
                    #{item.review_cycle}
                  </td>
                  <td className="text-xs text-[#667085] max-w-xs truncate">
                    {item.remarks}
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

    </div>
  );
};
