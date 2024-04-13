from loguru import logger
logger.add("logs/{time:YYYY-MM-DD}.log",encoding="utf8",enqueue=True,rotation="00:00",level="DEBUG")
"""
日志格式一般：{"time":time,"ip":ip,"path":接口路径,"data":请求参数,"headers":headers,"method":请求方法}
"""