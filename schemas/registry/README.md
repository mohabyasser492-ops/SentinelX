# SentinelX Contract Registry

The registry manifest records all published SentinelX wire contracts.

## Status values

- `development`: Contract is under active design and is not yet stable.
- `active`: Contract is approved for production producers and consumers.
- `deprecated`: Contract remains supported but must not be used for new
  integrations.
- `retired`: Contract is outside the supported lifecycle.

## Rules

- A contract is marked active only after architecture review.
- A path cannot be reused for incompatible semantics.
- Ownership changes require a manifest update.
- Breaking changes require a new major-version path.
- The manifest version describes registry metadata, not individual
  contract versions.