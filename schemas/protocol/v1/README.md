# SentinelX Protocol Version 1

SentinelX uses a CloudEvents-compatible envelope for domain-event
transport.

The envelope remains separate from the domain payload.

This separation allows SentinelX to use HTTP, a message broker, batch
files, or future transports without redesigning the security-event or AI
contracts.

Every domain event includes:

- Globally unique event ID
- Source URI
- Registered event type
- Production timestamp
- Payload schema URI
- Tenant ID
- Correlation ID
- Distributed trace context
- Domain payload