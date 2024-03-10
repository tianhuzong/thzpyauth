from libcpp.string cimport string
cdef extern from "verify_c.h":
    bint email_c(string string)
    bint ipv4_c(string string)
