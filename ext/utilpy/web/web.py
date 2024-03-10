"""
包含获取IP、UA的函数
"""

def get_real_ip(request):
    """
    获取用户真实IP
    :param request:request对象 函数视图的request对象
    :res str 返回IP
    """
    if (real_ip := request.META.get("HTTP_X_FORWARDED_FOR")) != None: 
        return real_ip.split()[0]
    elif (real_ip := request.META.get("HTTP_X_REAL_IP")) != None :
        return real_ip
    else: return request.META.get("REMOTE_ADDR")
def get_ua(request):
    """
    获取用户的UA
    :param request:request对象 函数视图的request对象
    :return str 用户的UA信息
    """
    return request.META.get("HTTP_USER_AGENT")