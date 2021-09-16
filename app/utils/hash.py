"""
Hashing library code
"""

from passlib.hash import pbkdf2_sha256

def hashed(pwd):
    return pbkdf2_sha256.hash(pwd)

def verify(pwd, hash_pwd):
    return pbkdf2_sha256.verify(pwd , hash_pwd)
