import React from 'react';
import { History, Shield, Clock, User, Layers, ArrowUpRight } from 'lucide-react';
import { AuditEvent } from '../types';

interface AuditTrailViewProps {
  logs: AuditEvent[];
}

export const AuditTrailView: React.FC<AuditTrailViewProps> = ({ logs }) => {
  return (
    <div className="space-y-6">
      
      {/* Header Banner */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-xl flex items-center justify-between">
        <div>
          <div className="flex items-center gap-2 text-indigo-400 text-xs font-semibold uppercase tracking-wider mb-1">
            <History className="w-4 h-4" />
            <span>Statutory Scrutiny Audit Log</span>
          </div>
          <h2 className="text-xl font-bold text-white tracking-tight">
            Immutable Audit Trail & Regulatory Event History
          </h2>
          <p className="text-xs text-slate-400 mt-1 max-w-2xl">
            Append-only record of all application imports, automated document mappings, manual remappings, 
            rule evaluations, reviewer notes, and report exports. Ensures complete forensic accountability.
          </p>
        </div>

        <div className="bg-slate-950 px-3.5 py-2 rounded-lg border border-slate-800 text-xs text-slate-300 font-mono">
          {logs.length} Logged Events
        </div>
      </div>

      {/* Events Table / Timeline */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl overflow-hidden shadow-md">
        <div className="p-4 border-b border-slate-800 flex justify-between items-center text-xs text-slate-400 font-medium">
          <span>Forensic Activity Timeline</span>
          <span className="text-slate-500">Sorted Newest First</span>
        </div>

        <div className="divide-y divide-slate-800/80">
          {logs.map((log) => (
            <div key={log.id} className="p-4 hover:bg-slate-950/40 transition-colors flex flex-col md:flex-row md:items-center justify-between gap-3 text-xs">
              
              <div className="space-y-1 max-w-3xl">
                <div className="flex items-center gap-2 flex-wrap">
                  <span className="font-mono text-[11px] text-blue-400 font-semibold bg-slate-950 px-2 py-0.5 rounded border border-slate-800">
                    {log.action}
                  </span>
                  <span className="text-slate-600">•</span>
                  <span className="text-slate-300 font-medium">
                    {log.target_type}: <span className="font-mono text-indigo-300">{log.target_id}</span>
                  </span>
                </div>

                <p className="text-slate-200 text-xs leading-relaxed font-sans">
                  {log.details}
                </p>
              </div>

              <div className="shrink-0 text-right md:text-right space-y-0.5">
                <div className="text-slate-300 font-medium flex items-center md:justify-end gap-1.5">
                  <User className="w-3.5 h-3.5 text-slate-400" />
                  <span>{log.user_name}</span>
                </div>
                <div className="text-[11px] text-slate-500 font-mono flex items-center md:justify-end gap-1">
                  <Clock className="w-3 h-3" />
                  <span>{log.timestamp}</span>
                </div>
              </div>

            </div>
          ))}
        </div>
      </div>

    </div>
  );
};
