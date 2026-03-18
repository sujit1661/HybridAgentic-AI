from langchain.tools import tool
import os
import shutil
from .tool_loggers import tool_logger


@tool(description="Create a new empty file. Input should be the file name including extension like notes.txt")
@tool_logger
def create_empty_file(filename: str) -> str:
    try:
        with open(filename, "w") as f:
            pass
        return f"File '{filename}' created successfully"
    except Exception as e:
        return str(e)

@tool(description="create a new empty file with content into it")
@tool_logger
def create_file_with_content(filename: str,content:str) -> str:
    try:
        with open(filename, "w") as f:
            f.writelines(content)
        return f"File '{filename}' created successfully along with content into it"
    except Exception as e:
        print("not able to create file")
        return str(e)




@tool(description="Read and return the contents of a file. Input should be the file name.")
@tool_logger
def read_file(filename: str) -> str:
    try:
        with open(filename, "r") as f:
            content =f.read()
        return f"📄 File: {filename}\n\n{content}"
    except:
        return "File not found or cannot be read"

@tool(description="write content to a file. Input should be the file name and the content to be written.")
@tool_logger
def write_file(filename: str, content: str) -> str:
    try:
        with open(filename, "w") as f:
            f.write(content)
        return f"File '{filename}' written successfully"
    except Exception as e:
        return str(e)

@tool(description="Delete a file from the current directory. Input should be the file name.")
@tool_logger
def remove_file(filename: str) -> str:
    try:
        if os.path.exists(filename):
            os.remove(filename)
            return f"File '{filename}' removed successfully"
        return "File not found"
    except Exception as e:
        return str(e)

@tool(description="Create a folder in the current directory. Input should be the folder name.")
@tool_logger
def create_folder(folder_name: str) -> str:
    try:
        os.makedirs(folder_name, exist_ok=True)
        return f"Folder '{folder_name}' created successfully"
    except Exception as e:
        return str(e)

@tool(description="Delete a folder and all its contents. Input should be the folder name.")
@tool_logger
def remove_folder(folder_name: str) -> str:
    try:
        if os.path.exists(folder_name):
            shutil.rmtree(folder_name)
            return f"Folder '{folder_name}' removed successfully"
        return "Folder not found"
    except Exception as e:
        return str(e)

@tool(description="List files and folders in a directory")
@tool_logger
def list_files(path: str = ".") -> str:
    try:
        files = os.listdir(path)
        if not files:
            return "Directory is empty"
        return "\n".join(files)
    except Exception as e:
        return str(e)

@tool(description="Rename a file")
@tool_logger
def rename_file(source_file: str, file_to_renamed: str) -> str:
    try:
        os.rename(source_file, file_to_renamed)
        return f"File '{source_file}' renamed to '{file_to_renamed}' successfully"
    except Exception as e:
        return str(e)

@tool(description="copy a file")
@tool_logger
def copy_file(source_file: str, destination: str) -> str:
    try:
        # move with metadata
        shutil.copy2(source_file, destination)
        return f"File '{source_file}' copied to '{destination}' successfully"
    except Exception as e:
        return str(e)

@tool(description="move file from one folder to another folder")
@tool_logger
def move_file(source_folder: str, destination_folder: str) -> str:
    try:
        shutil.move(source_folder, destination_folder)
        return f"File '{source_folder}' moved to '{destination_folder}' successfully"
    except Exception as e:
        return str(e)

@tool(description="search file exist or not")
@tool_logger
def search_file(filename: str) -> str:
    try:
        if os.path.exists(filename):
            return f"File '{filename}' exists"
        return f"File '{filename}' does not exist"
    except Exception as e:
        return str(e)

@tool(description="get the size of file from its name")
@tool_logger
def get_file_size(filename: str) -> str:
    try:
        size = os.path.getsize(filename)
        size_gb=size/(1024**3)
        return f"{round(size_gb,3)} GB"
    except Exception as e:
        return str(e)

@tool(description="Append content to an existing document")
@tool_logger
def append_doc(file_path: str, content: str) -> str:
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write("\n" + content)
        return f"✏️ Content appended to {file_path}"
    except Exception as e:
        return f"⚠️ Could not append to file {file_path}. Error: {str(e)}"

@tool(description="summarize the current project folder")
@tool_logger
def summarize_current_project_folder() -> str:
    files = os.listdir(os.getcwd())
    return f"project contains {len(files)} files:\n"+"\n".join(files[:30])

@tool(description="tool will create a zip of project folder")
@tool_logger
def create_zip_folder(project_folder: str) -> str:
    try:
        shutil.make_archive(project_folder, "zip", project_folder)
        return f"Project folder '{project_folder}' created successfully"
    except Exception as e:
        print("create_zip_folder error")
        return str(e)


