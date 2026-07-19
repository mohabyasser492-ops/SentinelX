# SentinelX Domain Event Types

## Naming convention

Domain-event names use:

`io.sentinelx.<domain>.<resource>.<action>.v<major>`

The major version changes only when the event semantics become
incompatible.

## Registered version 1 event types

- `io.sentinelx.security.event.ingested.v1`
- `io.sentinelx.security.event.normalized.v1`
- `io.sentinelx.security.event.rejected.v1`
- `io.sentinelx.ai.analysis.requested.v1`
- `io.sentinelx.ai.analysis.completed.v1`
- `io.sentinelx.ai.analysis.failed.v1`
- `io.sentinelx.ai.recommendation.created.v1`
- `io.sentinelx.ai.feedback.recorded.v1`

## Rules

- Existing event types cannot be repurposed.
- Compatible optional fields do not require a new event type.
- Breaking semantic changes require a new major version.
- Producers must publish only registered event types.
- Consumers must not depend on global event ordering.