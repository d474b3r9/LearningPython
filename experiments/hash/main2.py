import hashlib

value='1-800-flowers'
def hash_to_hashes(value):
    # 64 bits trucated sha256 to int
    hashed = int.from_bytes(hashlib.sha256(value.encode('utf-8')).digest()[:8], 'little')
    return hashed

print(hash_to_hashes(value))

print(int('2063c1608d6e0baf80249c42e2be5804', base=16))

print() # 32-bit int