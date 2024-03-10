# cython: language_level=3
from .verify cimport email_c,ipv4_c
cpdef bint email(str string):
    """
    判断字符串是否为合法的邮箱地址
    """
    return email_c(string.encode('utf-8'))

cpdef bint ipv4(str string):
    """
    判断字符串是否为合法的ipv4
    """
    return ipv4_c(string.encode('utf-8'))
