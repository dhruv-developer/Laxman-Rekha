from pydantic import BaseModel
from datetime import datetime

class SessionRecord(BaseModel):
    user_id: str
    session_id: str
    ip: str
    mac_id: str
    device_uuid: str
    features: dict
    aura_hash: str
    trust_score: int
    timestamp: datetime
