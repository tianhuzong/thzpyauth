import requests  

class RequestBasic():
    """API请求的基础类"""
    def __init__(self,url):
        """
        构造函数
        :param url:str 服务器后端的地址结尾不带/,前面要带http或https,有端口记得带端口,例如https://myapi.domain.com
        """
        self.url = url  
    def call_api(self,api_path,method,data,to_dict=True):
        """
        调用API
        :param api_path:str api路径,不带?参数,但是要带path参数,例如/api/public/connect
        :param method:str 请求方法,支持例如get,post,大小写皆可
        :param data:dict 请求参数如果是get,a=b&c=d则此处写作{"a":"b","c":"d"}
        :param to_dict:bool 请求结果是否转为dict,默认为是
        """
        response = requests.request(method=method.lower(),url=self.url+api_path,data=data )
        return response.json() if to_dict else response.text