import React, { useState } from 'react';
import { Scale, CheckCircle2, XCircle, Shield, AlertTriangle, Layers, Calendar, User } from 'lucide-react';
import { RuleDefinition, UserRole } from '../types';

interface RulesManagerProps {
  rules: RuleDefinition[];
  currentRole: UserRole;
  onToggleRule: (ruleId: string) => Promise<void>;
}

export const RulesManager: React.FC<RulesManagerProps> = ({
  rules,
  currentRole,
  onToggleRule,
}) => {
  const [selectedCategory, setSelectedCategory] = useState('ALL');
  const [togglingId, setTogglingId] = useState<string | null>(null);

  const handleToggle = async (ruleId: string) => {
    if (currentRole !== 'System Administrator') {
      alert("Only System Administrators are authorized to activate, test, or retire regulatory rules.");
      return;
    }
    setTogglingId(ruleId);
    await onToggleRule(ruleId);
    setTogglingId(null);
  };

  const filteredRules = selectedCategory === 'ALL'
    ? rules
    : rules.filter((r) => r.category === selectedCategory || r.category === 'All Categories');

  return (
    <div className="space-y-6">
      
      {/* Header Banner */}
      <div className="bg-slate-900 border border-slate-800 rounded-xl p-6 shadow-xl flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <div className="flex items-center gap-2 text-indigo-400 text-xs font-semibold uppercase tracking-wider mb-1">
            <Scale className="w-4 h-4" />
            <span>AICTE Approval Process Handbook (APH) Regulatory Rule Base</span>
          </div>
          <h2 className="text-xl font-bold text-white tracking-tight">
            Configurable Scrutiny Rules & Checklists (AY 2025-26)
          </h2>
          <p className="text-xs text-slate-400 mt-1 max-w-2xl">
            All scrutiny rules are versioned and linked directly to published clauses in the AICTE Approval Process Handbook.
            AI models apply only active, approved rules without hallucinating requirements.
          </p>
        </div>

        <div className="bg-slate-950 p-3 rounded-lg border border-slate-800 text-xs text-slate-400 flex items-center gap-2 shrink-0">
          <Shield className="w-4 h-4 text-amber-400" />
          <span>Role: <strong className="text-white">{currentRole}</strong></span>
        </div>
      </div>

      {/* Category Filter Tabs */}
      <div className="flex items-center gap-2 overflow-x-auto pb-1 text-xs">
        {['ALL', 'Extension of Approval (EoA)', 'Intake Increase', 'All Categories'].map((cat) => (
          <button
            key={cat}
            onClick={() => setSelectedCategory(cat)}
            className={`px-3.5 py-2 rounded-lg font-medium transition-all ${
              selectedCategory === cat
                ? 'bg-blue-600 text-white font-semibold'
                : 'bg-slate-900 border border-slate-800 text-slate-400 hover:text-white'
            }`}
          >
            {cat === 'ALL' ? 'All Regulatory Norms' : cat}
          </button>
        ))}
      </div>

      {/* Rules List */}
      <div className="space-y-4">
        {filteredRules.map((rule) => (
          <div
            key={rule.id}
            className="bg-slate-900 border border-slate-800 rounded-xl p-5 shadow-md flex flex-col md:flex-row md:items-start justify-between gap-5"
          >
            <div className="space-y-2 flex-1">
              <div className="flex items-center gap-2.5 flex-wrap">
                <span className="font-mono text-xs font-bold text-indigo-300 bg-indigo-950/80 border border-indigo-800/80 px-2.5 py-0.5 rounded">
                  {rule.id}
                </span>
                <span className="text-xs bg-slate-800 text-slate-300 px-2 py-0.5 rounded">
                  {rule.category}
                </span>
                <span className="text-xs font-medium text-slate-400">
                  Version {rule.version}
                </span>
                <span className={`text-[10px] px-2 py-0.5 rounded font-bold ${
                  rule.is_active ? 'bg-emerald-950 text-emerald-400 border border-emerald-800' : 'bg-slate-800 text-slate-400'
                }`}>
                  {rule.is_active ? 'ACTIVE / ENFORCED' : 'RETIRED'}
                </span>
              </div>

              <h3 className="text-base font-semibold text-white">
                {rule.title}
              </h3>

              <div className="bg-slate-950 p-3 rounded-lg border border-slate-800/80 text-xs space-y-1">
                <div className="text-slate-400">
                  <strong className="text-slate-300">Handbook Source Clause:</strong> {rule.clause} ({rule.source_title})
                </div>
                <div className="text-slate-400">
                  <strong className="text-slate-300">Validation Algorithm:</strong> {rule.validation_logic}
                </div>
              </div>

              <div className="text-xs text-slate-400 flex flex-wrap items-center gap-4 pt-1">
                <span className="flex items-center gap-1">
                  <Calendar className="w-3.5 h-3.5 text-slate-500" />
                  Effective: {rule.effective_from} to {rule.effective_to}
                </span>
                <span>•</span>
                <span className="flex items-center gap-1">
                  <User className="w-3.5 h-3.5 text-slate-500" />
                  Drafted by: {rule.author}
                </span>
              </div>
            </div>

            {/* Admin Toggle Switch */}
            <div className="shrink-0 flex flex-col items-end justify-between self-stretch border-t md:border-t-0 pt-3 md:pt-0 border-slate-800">
              <span className={`text-xs px-2.5 py-1 rounded font-bold uppercase ${
                rule.severity === 'HIGH' ? 'bg-red-950 text-red-400 border border-red-900' : 'bg-amber-950 text-amber-400 border border-amber-900'
              }`}>
                {rule.severity} Severity
              </span>

              <button
                onClick={() => handleToggle(rule.id)}
                disabled={togglingId === rule.id}
                className={`mt-4 px-3.5 py-1.5 rounded-lg text-xs font-semibold transition-all flex items-center gap-1.5 ${
                  rule.is_active
                    ? 'bg-slate-800 hover:bg-red-950 hover:text-red-300 text-slate-300 border border-slate-700'
                    : 'bg-emerald-600 hover:bg-emerald-500 text-white'
                }`}
              >
                {togglingId === rule.id ? (
                  'Updating...'
                ) : rule.is_active ? (
                  <>
                    <XCircle className="w-3.5 h-3.5" /> Deactivate / Retire
                  </>
                ) : (
                  <>
                    <CheckCircle2 className="w-3.5 h-3.5" /> Activate Rule
                  </>
                )}
              </button>
            </div>

          </div>
        ))}
      </div>

    </div>
  );
};
