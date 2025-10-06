import hashlib
import base64

def sha256_hex(s: str) -> str:
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

def b64_encode(s: str) -> str:
    return base64.b64encode(s.encode('utf-8')).decode('utf-8')

def b64_decode(s: str) -> str:
    return base64.b64decode(s.encode('utf-8')).decode('utf-8')
