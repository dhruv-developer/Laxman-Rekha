import numpy as np
from ..utils.hashing import sha256_bytes, sha256_hexdigest
from ..utils.steganography import embed_data

def generate_steganographic_data(features: dict) -> bytes:
    # 1. Vectorize & quantize
    keys = sorted(features.keys())
    arr = np.array([features[k] for k in keys], dtype=np.float32)
    ints = (arr * 1000).astype(np.int32)  # scale for precision
    # 2. Secret bits from raw features
    secret = sha256_bytes(arr.tobytes())
    # 3. Embed
    stego = embed_data(ints, secret)
    return stego.tobytes()

def hash_data(data: bytes) -> str:
    return sha256_hexdigest(data)
