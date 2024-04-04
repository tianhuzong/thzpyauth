import requests  

class RequestBasic():
    """API请求的基础类"""
    def __init__(self,url):
        """
        构造函数
        :param url:str 服务器后端的地址结尾不带/,前面要带http或https,有端口记得带端口,例如https://myapi.domain.com
        """
        self.url = url  
    def call_api(self,api_path,method,data,to_dict=True,**kwargs):
        """
        调用API
        :param api_path:str api路径,不带?参数,但是要带path参数,例如/api/public/connect
        :param method:str 请求方法,支持例如get,post,大小写皆可
        :param data:dict 请求参数如果是get,a=b&c=d则此处写作{"a":"b","c":"d"}
        :param to_dict:bool 请求结果是否转为dict,默认为是
        :param **kwargs 更多参数,可以传入例如headers的

        :return str|dict 返回原式字符串或者解析为json返回字典
        
        Exception:
            RuntimeError 在连接失败或者连接超时时会抛出这个错误
            ValueError URL缺失或者无效时抛出这个错误
            其他错误为requests.exceptions下的错误


        """
        try:
            response = requests.request(method=method.lower(),url=self.url+api_path,data=data,**kwargs)
        except requests.exceptions.ConnectionError as e: 
            raise RuntimeError("连接失败,可能是由于DNS解析错误等")
        except requests.exceptions.Timeout as e:  
            raise RuntimeError("连接超时")
        except requests.exceptions.URLRequired as e: 
            raise ValueError("无效的URL")
        return response.json() if to_dict else response.text