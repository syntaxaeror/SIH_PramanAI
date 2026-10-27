import React from 'react';
import { X, User, Shield, Building2, Lock, CheckCircle2 } from 'lucide-react';
import { UserRole } from '../../types';

interface ProfileModalProps {
  officerName: string;
  role: UserRole;
  onClose: () => void;
}

export const ProfileModal: React.FC<ProfileModalProps> = ({
  officerName,
  role,
  onClose,
}) => {
  return (
    <div className="fixed inset-0 z-50 bg-black/50 backdrop-blur-xs flex items-center justify-center p-4">
      <div className="bg-white border border-[#D9E2EC] rounded-lg max-w-md w-full p-6 shadow-2xl space-y-4 animate-in fade-in duration-150">
        
        {/* Header */}
        <div className="flex items-center justify-between border-b border-[#D9E2EC] pb-3">
          <div className="flex items-center gap-2.5">
            <div className="w-10 h-10 rounded-full bg-[#17365D] text-white flex items-center justify-center text-sm font-bold">
              {officerName.split(' ').map(n => n[0]).slice(0, 2).join('')}
            </div>
            <div>
              <h3 className="font-bold text-sm text-[#17365D]">{officerName}</h3>
              <div className="text-[11px] text-[#667085]">{role}</div>
            </div>
          </div>
          <button
            onClick={onClose}
            className="text-slate-400 hover:text-[#243447] p-1 rounded hover:bg-slate-100"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        {/* Profile Details */}
        <div className="space-y-3 text-xs">
          <div className="bg-[#F7F9FC] border border-[#D9E2EC] p-3 rounded space-y-2">
            <div className="flex justify-between">
              <span className="text-[#667085]">Designation:</span>
              <strong className="text-[#17365D]">{role}</strong>
            </div>
            <div className="flex justify-between">
              <span className="text-[#667085]">Department / Bureau:</span>
              <span className="font-medium text-[#243447]">Approvals & Scrutiny Bureau</span>
            </div>
            <div className="flex justify-between">
              <span className="text-[#667085]">Regional Assignment:</span>
              <span className="font-medium text-[#243447]">South-Western Region (Karnataka / Kerala)</span>
            </div>
            <div className="flex justify-between">
              <span className="text-[#667085]">Assigned System ID:</span>
              <span className="font-mono font-bold text-[#245A8D]">AICTE-OFF-101</span>
            </div>
          </div>

          {/* Permissions Overview */}
          <div className="space-y-1.5 pt-1">
            <span className="font-bold text-[#17365D] uppercase text-[10px] tracking-wider block">
              Authorized Scrutiny Permissions
            </span>
            <div className="space-y-1 text-[#243447] text-[11px]">
              <div className="flex items-center gap-1.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#237A45]" />
                <span>Examine imported applications and supporting PDF packages</span>
              </div>
              <div className="flex items-center gap-1.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#237A45]" />
                <span>Record reviewer dispositions and uphold deficiencies</span>
              </div>
              <div className="flex items-center gap-1.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#237A45]" />
                <span>Flag photographic duplicate signals for on-site verification</span>
              </div>
              <div className="flex items-center gap-1.5">
                <CheckCircle2 className="w-3.5 h-3.5 text-[#237A45]" />
                <span>Generate and export official deficiency and scrutiny reports</span>
              </div>
            </div>
          </div>

          <div className="bg-[#FFF5D9] text-[#946200] p-2.5 rounded border border-[#FCD34D] text-[10px] leading-relaxed flex items-start gap-1.5">
            <Lock className="w-3.5 h-3.5 shrink-0 mt-0.5" />
            <span>
              Role privileges are managed by the System Administrator in accordance with official AICTE gazette notifications. Self-elevation is disabled.
            </span>
          </div>
        </div>

        <div className="pt-2 flex justify-end">
          <button
            onClick={onClose}
            className="px-4 py-1.5 rounded bg-[#17365D] hover:bg-[#245A8D] text-white text-xs font-semibold shadow-2xs"
          >
            Close
          </button>
        </div>

      </div>
    </div>
  );
};
