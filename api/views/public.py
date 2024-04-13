from rest_framework.decorators import api_view
from rest_framework.response import Response
from globals_var import logger
import utils.web
import time
@api_view(["GET"])
def service_state(request):
    接口路径 = request.META.get("PATH_INFO")
    请求参数 = request.META.get("QUERY_STRING")
    headers = {key: value for key, value in request.META.items() if key.startswith('HTTP_')}
    logger.info({"time":time.time(),"ip":(readip := utils.web.get_real_ip(request)),"path":接口路径,"data":请求参数,"headers":headers,"method":request.method})
    return Response({"code":200,"msg":"succeed","data":{"ip":readip,"UA":utils.web.get_ua(request)}})