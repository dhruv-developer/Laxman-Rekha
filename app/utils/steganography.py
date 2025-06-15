import numpy as np

def embed_data(cover: np.ndarray, secret: bytes) -> np.ndarray:
    """
    Embed secret bytes into the LSB of the integer cover array.
    If cover is too small, auto-pads it with random integers.

    Args:
        cover (np.ndarray): Integer array to hold the bits
        secret (bytes): Data to embed

    Returns:
        np.ndarray: Stego array with secret embedded
    """
    if not isinstance(cover, np.ndarray):
        raise TypeError("Cover must be a NumPy array")
    if not np.issubdtype(cover.dtype, np.integer):
        raise TypeError("Cover must be of integer type")
    if not isinstance(secret, (bytes, bytearray)):
        raise TypeError("Secret must be bytes")

    secret_bits = np.unpackbits(np.frombuffer(secret, dtype=np.uint8))
    required_len = secret_bits.size

    flat_cover = cover.flatten()

    # If cover too small, extend it with random integers
    if flat_cover.size < required_len:
        padding = np.random.randint(0, 256, size=(required_len - flat_cover.size), dtype=cover.dtype)
        flat_cover = np.concatenate([flat_cover, padding])

    # Embed secret bits in LSBs
    flat_cover[:required_len] = (flat_cover[:required_len] & ~1) | secret_bits

    return flat_cover.reshape((-1,))  # Return as 1D stego for simplicity
