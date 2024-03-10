from rest_framework.decorators import api_view
from rest_framework.response import Response
from globals_var import logger
import utilpy.web
@api_view(["GET"])
def service_state(request):
    logger.info((request.META))
    return Response({"code":200,"msg":"succeed","data":{"ip":utilpy.web.get_real_ip(request),"UA":utilpy.web.get_ua(request)}})