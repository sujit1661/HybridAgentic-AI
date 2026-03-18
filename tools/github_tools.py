from github import Github,Auth
from langchain.tools import tool
from tool_logger import tool_logger


# Personal Access Token
token = "ghp_xxxxxxxxxxxxxxxxxxxx"
auth=Auth.Token(token)
g=Github(auth=auth)
user=g.get_user()

@tool_logger
@tool(description="tool will create a repo in github")
def create_github_repo(repo_name: str,private=True) -> str:
    try:
        repo=user.create_repo(name=repo_name, private=private)
        return (f"repo created successfully"
                f"repo name: {repo_name}"
                f"repo url: {repo.html_url}")
    except Exception as e:
        return str(e)

@tool_logger
@tool(description="tool will list all the repos in github")
def list_github_repos():
    try:
        repos=[repo.name for repo in user.get_repos()]
        display="📂 **Repositories:**\n" + "\n".join(f"- {r}" for r in repos)
        return {"display":display}
    except Exception as e:
        print("repository in empty")
        return str(e)


@tool_logger
@tool(description="tool will delete repo from github from its name")
def delete_github_repo(repo_name: str) -> str:
    try:
        repo=user.get_repo(repo_name)
        repo.delete()
        return (f"repo deleted successfully"
                f"repo name: {repo_name}"
        )
    except Exception as e:
        print("could not delete repo")
        return str(e)

@tool_logger
@tool(description="tool will a new file in repo")
def create_github_file(repo_name: str,path, content: str,message) -> str:
    try:
        repo=user.get_repo(repo_name)
        repo.create_file(path=path, message=message, content=content)
        display=f"file {repo_name} created successfully at {path}"
        return f"File created successfully in {repo_name} at {path}"
    except Exception as e:
        print("could not create file")
        return str(e)

@tool_logger
@tool(description="tool will add folder and files to github you have to provide path repo name and message")
def add_folder_and_files_to_github(repo_name: str, path: str, message: str) -> str:
    try:
        repo=user.get_repo(repo_name)
        if path.endswith("/"):
            file_path=f"{path}.gitkeep"
            repo.create_file(path=file_path, message=message, content="")
            return "folder added successfully"
        else:
            repo.create_file(path=path, message=message, content="")
            return f"file {path} added successfully"
    except Exception as e:
        print("could not add folder and files")
        return str(e)

@tool_logger
@tool(description="tool will delete file in the github repo")
def delete_github_file(repo_name: str, path: str, message) -> str:
    try:
        repo=user.get_repo(repo_name)
        file=repo.get_contents(path)
        repo.delete_file(path,message,file.sha)
        return f"file{file} deleted successfully from {repo_name}"
    except Exception as e:
        print("could not delete file")
        return str(e)
