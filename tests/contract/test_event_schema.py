import json
from pathlib import Path
def test_event_schema_version():
    schema=json.loads(Path("schemas/events/security-event-v1.schema.json").read_text())
    assert schema["properties"]["schema_version"]["const"] == "1.0.0"
