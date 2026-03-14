from langchain.tools import tool
import base64
import requests
import zipfile
import io
import os




@tool(description="search github repos")
def search_github(search_term: str = "github") -> str:
    try:
        res=requests.get(f"https://api.github.com/search/repositories?q={search_term}")
        data= res.json()

        result=[]
        for repo in data["items"][:5]:
            result.append(f"{repo['full_name']} - {repo['description']}")
        return "\n".join(result)
    except Exception as e:
        return str(e)



@tool(description="Get README of a GitHub repository")
def get_repo_readme(owner: str, repo: str) -> str:
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/readme"
        response = requests.get(url).json()
        content = base64.b64decode(response["content"]).decode("utf-8")
        return content[:10000]  # limit output
    except Exception as e:
        return str(e)


@tool(description="list all files in github repo from its name and owner name")
def list_repo_files(owner: str, repo: str) -> str:
    try:
        res = requests.get(f"https://api.github.com//repos/{owner}/{repo}/contents").json()
        files = [file["name"] for file in res]
        return "\n".join(files)
    except Exception as e:
        return str(e)


@tool(description="download github repo from its name owner and repo name and extract it into current working directory")
def download_github_repo(owner: str, repo: str) -> str:
    try:
        res = requests.get(f"https://github.com/{owner}/{repo}/archive/refs/heads/main.zip")
        if res.status_code != 200:
            return f"failed to download {owner}/{repo}"
#         download zip
        with zipfile.ZipFile(io.BytesIO(res.content)) as zf:
            zf.extractall(os.getcwd())
        return f"Downloaded and extracted repo to {os.getcwd()}"
    except Exception as e:
        return str(e)






@tool(description="download random images and save it using given name")
def download_random_image_by_name(name: str, width=600, height=400) -> str:
    try:
        url =requests.get(f"https://picsum.photos/{width}/{height}")
        filename = f"{name.replace(' ','_')}.png"
        if url.status_code != 200:
            return f"failed to download {name}"
        # paste image
        with open(filename, "wb") as f:
            f.write(url.content)
        return f"Downloaded and saved image to {os.getcwd()} as {filename}"
    except Exception as e:
        return str(e)



