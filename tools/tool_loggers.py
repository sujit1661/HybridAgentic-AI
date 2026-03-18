import logging
from functools import wraps  # ✅ ADD THIS

logging.basicConfig(
    filename="agent.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)


def tool_logger(tool_func):
    @wraps(tool_func)  # ✅ THIS FIXES EVERYTHING
    def wrapper(*args, **kwargs):
        try:
            log_info(f"Tool Start: {tool_func.__name__} | Args: {args} | Kwargs: {kwargs}")
            result = tool_func(*args, **kwargs)
            log_info(f"Tool End: {tool_func.__name__} | Result: {result}")
            return result

        except Exception as e:
            log_error(f"Tool Error: {tool_func.__name__} | Error: {str(e)}")
            raise e
    return wrapper