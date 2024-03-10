import re

emailp = re.compile(r"^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$")
ipv4p = re.compile(r"((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})(\.((2(5[0-5]|[0-4]\d))|[0-1]?\d{1,2})){3}")
def email(string : str)->bool:
    """
    判断字符串是否为合法的邮箱地址
    """
    try:
        return emailp.match(string).group() == string
    except AttributeError:
        return False

def ipv4(string : str)->bool:
    """
    判断字符串是否为合法的ipv4
    """
    try:
        return ipv4p.match(string).group() == string
    except AttributeError:
        return False
