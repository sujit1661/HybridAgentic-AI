from langchain_core.tools import tool
import requests
import datetime
from .tool_loggers import tool_logger

@tool(description="Get the current system time. Use when the user asks for the current time.")
@tool_logger
def get_current_time() -> str:
    return datetime.datetime.now().strftime("%I:%M %p")

@tool(description="Get current weather for a given city. Input should be a city name.")
@tool_logger
def get_weather(city: str) -> str:
    try:
        res = requests.get(
            f"https://wttr.in/{city}?format=%l:+%t+%C",
            timeout=5
        )
        return res.text.strip()
    except:
        return "Weather service unavailable"
