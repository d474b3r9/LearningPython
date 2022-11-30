import numpy as np
import hashlib

def generate_hash_table(min,max,n_buckets):
    # generate bins
    # avoid to create 1 bucket less
    n_buckets += 1
    # bins will define the range and the n wanted bins
    bins = np.linspace(min,max,n_buckets)
    print(bins)
    # generate labels
    labels = []
    lst = list(range(1,n_buckets))
    print(lst)
    return bins,lst

def hash_to_hashes(value):
    # 64 bits trucated sha256 to int
    hashed = int.from_bytes(hashlib.sha256(value.encode('utf-8')).digest()[:7], 'little')
    return hashed