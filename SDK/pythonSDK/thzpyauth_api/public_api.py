"""这里面是公开API的类"""

from base import RequestBasic

class PublicApi(RequestBasic):
    """thzpyauth的公开接口"""
    def __init__(self,url):
        """
        构造函数
        """
        super().__init__(url)
    def service_state(self):
        """获取服务状态"""
        response = self.call_api("/api/public/service_state", "get", {})
        return response