import hashlib


def md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()
def sha1(s):
    return hashlib.sha1(s.encode('utf-8')).hexdigest()
def sha256(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()
def sha3_256(s):
    return hashlib.sha3_256(s.encode('utf-8')).hexdigest()
