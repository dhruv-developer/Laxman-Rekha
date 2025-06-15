from pydantic import BaseModel

class TrustResponse(BaseModel):
    aura_hash: str
    trust_score: int
