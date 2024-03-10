from rest_framework.decorators import api_view
from rest_framework.response import Response
from globals_var import logger
from utils import string,emailer
@api_view(["GET"])
def service_state(request):
    logger.info(dir(request.META))
    return Response({"code":200,"data":{"ip":request.META.get("HTTP_X_FORWARDED_FOR").split(',')[0],"UA":request.META.get("HTTP_USER_AGENT")}})