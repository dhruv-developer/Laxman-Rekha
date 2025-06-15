import hashlib

def sha256_bytes(data: bytes) -> bytes:
    return hashlib.sha256(data).digest()

def sha256_hexdigest(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()
