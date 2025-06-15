from datetime import datetime
from ..db import db
from ..models.profile import Profile
from ..models.session import SessionRecord

def hamming_score(h1: str, h2: str) -> int:
    # both hex‐strings
    b1 = bytes.fromhex(h1)
    b2 = bytes.fromhex(h2)
    bits1 = int.from_bytes(b1, "big")
    bits2 = int.from_bytes(b2, "big")
    diff = bits1 ^ bits2
    dist = diff.bit_count()
    score = max(0, int((1 - dist/(len(b1)*8)) * 100))
    return score

async def compute_trust_score(user_id: str, session_id: str,
                              ip: str, mac: str, uuid: str,
                              features: dict, aura_hash: str) -> int:
    col = db.profiles
    prof = await col.find_one({"_id": user_id})
    if not prof:
        # first session → baseline
        await col.insert_one({"_id": user_id, "baseline_aura_hash": aura_hash})
        score = 100
    else:
        baseline = prof["baseline_aura_hash"]
        score = hamming_score(baseline, aura_hash)
        if score > 85:
            # update baseline with gradual learning
            await col.update_one({"_id": user_id},
                                 {"$set": {"baseline_aura_hash": aura_hash}})
    # store session record
    await db.sessions.insert_one(SessionRecord(
        user_id=user_id, session_id=session_id, ip=ip,
        mac_id=mac, device_uuid=uuid,
        features=features, aura_hash=aura_hash,
        trust_score=score, timestamp=datetime.utcnow()
    ).dict())
    return score
