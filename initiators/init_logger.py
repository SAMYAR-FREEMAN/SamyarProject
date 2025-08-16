from loguru import logger


def create_logger(app):
    logger.add("log/error.log", level="ERROR", rotation="1 MB")
    logger.add("log/info.log", level="INFO", rotation="1 MB")
    return logger


async def log_exception(request, call_next):
    try:
        response = await call_next(request)
        return response
    except Exception as e:
        logger.error(f"Exception occurred: {e}")