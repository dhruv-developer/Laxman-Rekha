from pydantic import BaseModel, Field

class Profile(BaseModel):
    user_id: str = Field(..., alias="_id")
    baseline_aura_hash: str
