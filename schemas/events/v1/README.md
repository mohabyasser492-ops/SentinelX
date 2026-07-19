# SentinelX Security Event Contracts

Security integrations convert source-native telemetry into canonical
SentinelX security events.

AI services must not depend directly on Wazuh, Sysmon, Suricata, or
other vendor-native field names.

## Event structure

Every normalized event contains:

- SentinelX event identity
- Tenant identity
- Observation and ingestion timestamps
- OCSF-compatible normalized payload
- Normalization provenance
- Immutable raw-evidence reference

## Extensibility

The SentinelX wrapper is strict.

The nested OCSF payload is extensible because different OCSF event
classes contain different attributes.

Vendor-specific information must be mapped into standard OCSF
attributes or a governed SentinelX OCSF extension.