from fastapi import APIRouter, Header, Request, HTTPException
from ..schemas.telemetry import TelemetryBatch
from ..schemas.session import TrustResponse
from ..services.profiling import extract_features
from ..services.aura import generate_steganographic_data, hash_data
from ..services.anomaly import compute_trust_score

router = APIRouter()

@router.post("/telemetry", response_model=TrustResponse)
async def ingest_telemetry(
    batch: TelemetryBatch,
    request: Request,
    x_user_id: str = Header(..., alias="X-User-Id"),
    x_mac: str    = Header(..., alias="X-Mac-Id"),
    x_uuid: str   = Header(..., alias="X-Device-Uuid"),
):
    # 1. IP Address
    client_ip = request.client.host
    # 2. Extract behavioral features
    features = extract_features([e.dict() for e in batch.events])
    # 3. Produce aura‐stego data & hash
    stego = generate_steganographic_data(features)
    aura_hash = hash_data(stego)
    # 4. Compute/store trust score
    score = await compute_trust_score(
        user_id=x_user_id,
        session_id=batch.session_id,
        ip=client_ip,
        mac=x_mac,
        uuid=x_uuid,
        features=features,
        aura_hash=aura_hash
    )
    return TrustResponse(aura_hash=aura_hash, trust_score=score)
