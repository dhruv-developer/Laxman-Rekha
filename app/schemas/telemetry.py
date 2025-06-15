from pydantic import BaseModel
from typing import Literal, Dict, Any
from datetime import datetime

class TelemetryEvent(BaseModel):
    event_type: Literal[
        "app_open","tap","swipe","hover","back","sensor","location","battery"
    ]
    timestamp: datetime
    details: Dict[str, Any]

class TelemetryBatch(BaseModel):
    session_id: str
    events: list[TelemetryEvent]
