# cython: language_level=3
import hashlib

cpdef str md5(str s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()
cpdef str sha1(str s):
    return hashlib.sha1(s.encode('utf-8')).hexdigest()
cpdef str sha256(str s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()
cpdef str sha3_256(str s):
    return hashlib.sha3_256(s.encode('utf-8')).hexdigest()
