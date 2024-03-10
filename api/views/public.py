from rest_framework.decorators import api_view
from rest_framework.response import Response
from globals_var import logger
import utils.web
@api_view(["GET"])
def service_state(request):
    logger.info((request.META))
    return Response({"code":200,"msg":"succeed","data":{"ip":utils.web.get_real_ip(request),"UA":utils.web.get_ua(request)}})