# SentinelX AI Contracts Version 1

This directory defines the authoritative contracts for AI analysis
orchestration.

## Contracts

- `analysis-command.schema.json`: Policy-governed request for AI analysis.
- `analysis-result.schema.json`: Auditable analysis output.
- `finding.schema.json`: Evidence-backed security conclusion.
- `attack-reference.schema.json`: Evidence-backed ATT&CK mapping.
- `model-execution.schema.json`: Model and execution provenance.

## Requirements

- Every command belongs to one tenant.
- Every result belongs to the same tenant as its command.
- AI services receive event identifiers rather than unrestricted raw
  evidence.
- Every security finding contains field-level evidence references.
- ATT&CK mappings identify the knowledge-source version.
- Model outputs identify the model artifact digest.
- AI services cannot authorize response execution.
- Recommendations are stored in the response domain and referenced by
  identifier.