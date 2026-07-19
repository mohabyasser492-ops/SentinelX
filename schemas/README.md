# SentinelX Contracts

This directory contains the authoritative wire contracts exchanged
between SentinelX components.

## Contract domains

- `common`: Reusable identifiers, evidence references, tracing, errors,
  and model metadata.
- `protocol`: Transport envelopes and domain-event naming.
- `events`: Canonical normalized security telemetry.
- `alerts`: Detection and alert contracts.
- `incidents`: Correlated incidents and timelines.
- `ai`: AI commands, findings, model execution records, and results.
- `hunting`: Safe threat-hunting commands and intermediate
  representations.
- `responses`: Recommendations, approvals, execution requests, and
  execution results.
- `registry`: Contract inventory, ownership, and compatibility metadata.

## Source of truth

The JSON Schema documents in this directory are the authoritative
SentinelX wire contracts.

Services must not create incompatible local definitions.

Runtime models, OpenAPI definitions, generated clients, event producers,
and event consumers must remain compatible with these schemas.

## Versioning

Contract paths include the major version:

`schemas/<domain>/v1/<contract>.schema.json`

Breaking changes require a new major-version directory.

Backward-compatible additions remain in the existing major-version
directory.

## Contract requirements

Every production contract must define:

- Contract owner
- Producing component
- Consuming components
- Stability status
- Compatibility policy
- Data classification
- Contract version

## Security principles

- Every record belongs to a tenant security boundary.
- Original security evidence remains immutable.
- AI conclusions must reference evidence.
- AI recommendations never authorize execution.
- Secrets must not be included in AI prompts or domain events.
- All timestamps must contain timezone information and be normalized to
  UTC by producers.