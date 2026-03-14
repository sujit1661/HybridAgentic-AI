# HybridAgentic AI 🤖

**HybridAgentic AI** is an advanced, autonomous system automation agent designed to act as an intelligent operating system assistant. Built on the **LangChain** framework and powered by **Groq's** high-performance inference engine, this agent bridges the gap between natural language reasoning and low-level system operations.

It is capable of managing files, executing code, controlling version control systems (GitHub), monitoring system health, and interacting with the web—all through a conversational interface with persistent memory.


---


## 🏗️ Technology Stack

The project relies on a robust set of modern technologies:

*   **Core Framework:** [LangChain](https://www.langchain.com/) (Agents, Tools, RunnableHistory)
*   **LLM Engine:** [Groq API](https://groq.com/) (Running `openai/gpt-oss-20b` / Llama 3) for ultra-fast inference and tool calling.
*   **System Interaction:** `os`, `shutil`, `subprocess` (Python Standard Libraries).
*   **System Monitoring:** `psutil` for real-time CPU, RAM, and process management.
*   **Network/API:** `requests` for web searching and API calls.
*   **GitHub Integration:** `PyGithub` for authenticated repository management.
*   **Memory:** Local JSON storage via `FileChatMessageHistory` to maintain context across sessions.


---


## 🚀 Features & Tool Breakdown
 🧰 Available Tools

The agent is equipped with multiple tool categories that allow it to interact with the system, execute code, manage files, automate GitHub tasks, and retrieve external information.


# 📁 File System Management (`tools/file_tool.py`)

These tools allow the agent to interact directly with the local file system.

| Tool Name | Description |
| :--- | :--- |
| **create_folder** | Creates a new directory at the specified path. |
| **create_empty_file** | Creates a new file with **0 bytes** (empty file). |
| **create_file_with_content** | Creates a new file and immediately writes provided text content into it. |
| **read_file** | Reads the contents of a file and returns it to the agent's context for processing. |
| **write_file** | Overwrites an existing file with new content. |
| **append_doc** | Appends additional text to the end of an existing file. Useful for logs, notes, or journals. |
| **rename_file** | Renames a specific file while keeping it in the same location. |
| **move_file** | Moves a file from a source directory to a destination directory. |
| **copy_file** | Creates a copy of a file while preserving metadata. |
| **remove_file** | Permanently deletes a specific file from the system. |
| **remove_folder** | Recursively deletes a folder along with all its contents. |
| **list_files** | Lists all files and directories in the current working directory. |
| **search_file** | Checks if a specific file exists within the directory structure. |
| **get_file_size** | Returns the file size converted to **GB**. |
| **summarize_project** | Lists the first **30 files** in a directory to provide a quick project overview. |
| **create_zip_folder** | Compresses a folder into a `.zip` archive. |


---


# 💻 Coding & Shell Execution (`tools/coding_shell_tools.py`)

Developer-focused tools for automating coding workflows and executing scripts.

| Tool Name | Description |
| :--- | :--- |
| **run_python_script** | Executes a `.py` file using the system’s Python interpreter. |
| **run_js_script** | Executes a `.js` file using **Node.js**. |
| **install_python_packages** | Installs Python dependencies using `pip install <package>`. |
| **install_node_packages** | Installs Node.js dependencies using `npm install <package>`. |
| **execute_terminal_command** | ⚠️ **High Power Tool** — Executes arbitrary shell commands and captures the output. |
| **print_project_hierarchy** | Uses the `tree` command to display a visual representation of the project folder structure. |
| **search_web** | Queries the DuckDuckGo API to retrieve real-time web information. |


---


# 🐙 GitHub Automation (Authenticated) (`tools/github_tools.py`)

These tools require a **GitHub Personal Access Token** and allow the agent to manage repositories.

| Tool Name | Description |
| :--- | :--- |
| **create_github_repo** | Creates a new repository (public or private) in the authenticated GitHub account. |
| **delete_github_repo** | ⚠️ **Destructive Action** — Permanently deletes a repository by name. |
| **list_github_repos** | Lists all repositories associated with the authenticated user. |
| **create_github_file** | Creates a new file inside a specific GitHub repository. |
| **delete_github_file** | Removes a file from a remote GitHub repository. |
| **add_folder_to_github** | Adds a folder structure to a repository (via `.gitkeep` or direct file creation). |


---


# 🌐 GitHub Data & Media (`tools/general_github_api_tools.py`)

Public API tools used for exploring repositories and retrieving GitHub data.

| Tool Name | Description |
| :--- | :--- |
| **search_github** | Searches public GitHub repositories based on keywords. |
| **get_repo_readme** | Fetches and decodes the `README.md` of any public repository. |
| **list_repo_files** | Lists the root file structure of any public repository. |
| **download_github_repo** | Downloads a repository as a ZIP file and extracts it locally. |
| **download_random_image** | Downloads a random image from **Lorem Picsum** and saves it locally. |


---


# 🖥️ System Monitoring (`tools/System_tools.py`)

Tools that allow the agent to monitor system health and machine information.

| Tool Name | Description |
| :--- | :--- |
| **get_cpu_RAM_usage** | Returns the current CPU usage percentage and RAM statistics (Total, Used, Free). |
| **get_os_info** | Retrieves operating system details such as System, Node Name, Version, and Machine type. |
| **list_processes** | Lists the top **20 currently running processes** on the machine. |


---


# ☁️ General Utilities (`tools/general_tools.py`)

Lightweight tools for retrieving common system and internet information.

| Tool Name | Description |
| :--- | :--- |
| **get_current_time** | Returns the current local system time. |
| **get_weather** | Fetches the current weather information for a city using `wttr.in`. |
---


## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository

First, download the project from GitHub:

```bash
git clone https://github.com/your-username/HybridAgenticAI.git
cd HybridAgenticAI
```




## 2. Install Python Dependencies

```bash
pip install langchain langchain-groq langchain-community python-dotenv requests psutil PyGithub
```

**Note:** You must have **Node.js installed** to use `run_js_script` and `npm` tools.


---


## 3. Environment Configuration

Create a `.env` file in the root directory:

```ini
GROQ_API_KEY=gsk_your_groq_api_key_here
GITHUB_TOKEN=ghp_your_github_token_here
```


---


## 4. GitHub Token Setup (Important)

1. Go to **GitHub Settings → Developer Settings → Personal Access Tokens (Classic)**  
2. Generate a new token  
3. Give the following permissions:
   - `repo` (Full control)
   - `delete_repo`

Update `tools/github_tools.py` to load the token from `.env`, or paste the token directly (not recommended for shared code).


---


# ▶️ Usage

Start the agent by running the main entry point:

```bash
python main.py
```

---


# Interaction Examples

## Scenario 1: Web Development Setup

**You:**
> "Create a folder called `MyWebsite`. Inside it, create an `index.html` with basic HTML content and a `style.css` file."

**AI:**
- Calls `create_folder`
- Calls `create_file_with_content` twice

Result:
> Created folder and files successfully.

---



## Scenario 2: System Diagnostics

**You:**
> "My computer feels slow. Check the CPU usage and list the running processes."

**AI:**
- Calls `get_cpu_RAM_usage`
- Calls `list_processes`

Result:
> CPU is at 85%. Here are the top processes...

---



## Scenario 3: GitHub Management

**You:**
> "Create a private repository called `agent-backup`. Zip my current project folder and upload it there."

**AI:**
- Calls `create_github_repo`
- Calls `create_zip_folder`
- Uploads the project or notifies if Git CLI is required

---



# 📂 Project Structure

```text
HybridAgenticAI/
│
├── main.py                       # Main agent loop and memory handling
├── tools_registry.py             # Aggregates all tool lists
│
├── tools/                        # Modular tool definitions
│   ├── file_tool.py              # Local file operations
│   ├── coding_shell_tools.py     # Code execution & Shell
│   ├── System_tools.py           # OS monitoring
│   ├── general_tools.py          # Time & Weather
│   ├── github_tools.py           # Authenticated GitHub actions
│   └── general_github_api_tools.py # Public GitHub data
│
├── memory/                       # Stores user session JSONs
└── .env                          # API Keys
```

---



# ⚠️ Security Warning

**Use with Caution**

This agent allows **Arbitrary Code Execution and File System Modification.**

- **Shell Access:**  
  The `execute_terminal_command` tool gives the AI full shell access.

- **Deletion:**  
  The agent can delete files and GitHub repositories permanently.

- **Sandboxing Recommended:**  
  Run this agent inside a **Virtual Machine**, **Docker container**, or a **restricted environment**.

---



# 👤 Author

Created by **Sujit Sadalage**

