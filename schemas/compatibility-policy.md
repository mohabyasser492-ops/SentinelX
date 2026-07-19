# SentinelX Contract Compatibility Policy

## Compatibility policy

SentinelX contracts follow backward-transitive compatibility within a
major version.

A consumer supporting version 1 must continue to process all supported
version 1 records produced before or after a compatible update.

## Compatible changes

The following changes may remain in the same major version:

- Adding an optional property
- Adding an optional nested object
- Adding a new domain-event type
- Adding a new OCSF event class
- Adding optional normalization metadata
- Adding optional evidence metadata
- Relaxing a size restriction when security is not reduced
- Adding an enum value only when consumers safely handle unknown values

## Breaking changes

The following changes require a new major version:

- Removing a property
- Renaming a property
- Changing a property data type
- Making an optional property required
- Changing identifier semantics
- Changing timestamp semantics
- Changing tenant-isolation semantics
- Changing evidence-integrity semantics
- Repurposing an existing event type
- Permitting AI services to execute response actions
- Changing a globally unique identifier into a locally unique identifier

## Enum policy

Open-ended concepts must remain extensible strings unless all consumers
can safely handle unknown enum values.

Security products, integration names, model providers, source vendors,
and storage providers must remain extensible.

Stable protocol states may use closed enums.

## Deprecation policy

A deprecated field or contract must document:

1. Deprecation date
2. Replacement
3. Migration instructions
4. Affected producers
5. Affected consumers
6. Earliest removal major version

Deprecated properties cannot be removed within the same major version.

## Deployment order

For backward-compatible additions:

1. Deploy consumers that accept the updated contract.
2. Publish the updated contract.
3. Deploy producers that emit the new properties.

For breaking changes:

1. Publish the new major version.
2. Add parallel support to consumers.
3. Migrate producers.
4. Monitor both versions.
5. Retire the old version after the support period.

## Review requirements

Every contract change requires review from:

- The contract owner
- At least one producer owner
- At least one consumer owner
- The security architecture owner