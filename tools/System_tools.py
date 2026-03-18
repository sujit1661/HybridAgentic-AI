from langchain.tools import tool
import psutil, platform
from .tool_loggers import tool_logger


@tool(description="used to display the cpu as well as RAM usages")
@tool_logger
def get_cpu_RAM_usage() -> str:
    cpu= psutil.cpu_percent(interval=1)
    RAM = psutil.virtual_memory()
    Total_RAM = RAM.total / (1024**3)
    used = RAM.used / (1024**3)

    return (f"cup usage: {cpu}"
            f"Total RAM: {round(Total_RAM,2)}"
            f"Used RAM: {round(used,2)}")


@tool(description="get info about os")
@tool_logger
def get_os_info():
    return {"system" :platform.system(),
            "version" :platform.version(),
            "release" :platform.release(),
            "machine" :platform.machine(),
            "processor" :platform.processor()
            }

@tool(description="used to list currently running processes.By default return first 20 processes")
@tool_logger
def list_processes():
    processes = []
    for p in psutil.process_iter():
        processes.append(p.name())
    return processes[:20]



