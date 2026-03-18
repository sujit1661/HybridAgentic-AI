import subprocess
from langchain.tools import tool
import requests
from .tool_loggers import tool_logger

@tool(description="install packages for python. user need to provide correct package name.")
@tool_logger
def install_python_packages(package_name: str) -> str:
    try:
        subprocess.run(["pip", "install", package_name],check=True)
        return f"Package '{package_name}' installed successfully"
    except Exception as e:
        return str(e)

@tool(description="install packages for node. user need to provide correct package name.")
@tool_logger
def install_node_packages(package_name: str) -> str:
    try:
        subprocess.run(["npm", "install", package_name],check=True)
        return f"Package '{package_name}' installed successfully"
    except Exception as e:
        return str(e)

@tool(description="run any .py file.")
@tool_logger
def run_python_script(filename: str) -> str:
    try:
        subprocess.run(["python", filename],check=True,text=True,capture_output=True)
        return f"Script '{filename}' run successfully"
    except Exception as e:
        return str(e)


@tool(description="run any .js file.")
@tool_logger
def run_js_script(filename: str) -> str:
    try:
        subprocess.run(["node", filename],check=True,text=True,capture_output=True)
        return f"Script '{filename}' run successfully"
    except Exception as e:
        return str(e)


# capture_output display output right next in cmd
@tool(description="display project hierarchy")
@tool_logger
def print_project_hierarchy(project_name: str = ".") -> str:
    try:
        result = subprocess.run(["tree", "/F", project_name],capture_output=True,
            text=True
        )
        return result.stdout
    except Exception as e:
        return str(e)


@tool(description="web search tool that searches through websites")
@tool_logger
def search_web(search_term: str = "website") -> str:
    try:
        res=requests.get(f"https://api.duckduckgo.com/?q={search_term}&format=json")
        data= res.json()
        return data.get("AbstractText")
    except Exception as e:
        return str(e)


@tool(description="Execute a terminal command and return the output")
@tool_logger
def execute_terminal_command(command: str = "") -> str:
    try:
        result=subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
        )
        return result.stdout if result.stdout else result.stderr
    except Exception as e:
        print("command failed")
        return str(e)
