import React from 'react';
import { LogOut, AlertTriangle } from 'lucide-react';

interface SignOutDialogProps {
  onConfirm: () => void;
  onCancel: () => void;
}

export const SignOutDialog: React.FC<SignOutDialogProps> = ({
  onConfirm,
  onCancel,
}) => {
  return (
    <div className="fixed inset-0 z-50 bg-black/50 backdrop-blur-xs flex items-center justify-center p-4">
      <div className="bg-white border border-[#D9E2EC] rounded-lg max-w-sm w-full p-5 shadow-2xl space-y-3 animate-in fade-in duration-150">
        
        <div className="flex items-center gap-2.5 text-[#B42318]">
          <div className="w-8 h-8 rounded-full bg-[#FDECEC] flex items-center justify-center shrink-0">
            <LogOut className="w-4 h-4 text-[#B42318]" />
          </div>
          <div>
            <h3 className="font-bold text-sm text-[#17365D]">Sign Out of Portal</h3>
            <div className="text-[11px] text-[#667085]">End Scrutiny Session</div>
          </div>
        </div>

        <p className="text-xs text-[#243447] leading-relaxed">
          Are you sure you want to sign out? Any unsaved review notes on the active document will be discarded.
        </p>

        <div className="flex justify-end gap-2 pt-2 border-t border-[#D9E2EC]">
          <button
            onClick={onCancel}
            className="px-3 py-1.5 rounded border border-[#D9E2EC] text-xs font-semibold text-[#243447] hover:bg-slate-50"
          >
            Cancel
          </button>
          <button
            onClick={onConfirm}
            className="px-4 py-1.5 rounded bg-[#B42318] hover:bg-[#991B1B] text-white text-xs font-semibold shadow-2xs"
          >
            Sign Out
          </button>
        </div>

      </div>
    </div>
  );
};
