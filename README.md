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

HybridAgentic AI is equipped with a modular tool registry. Below is a detailed description of every capability available to the agent.

### 📂 File System Operations (`tools/file_tool.py`)
These tools allow the agent to manipulate the local file system extensively.

| Tool Name | Description |
| :--- | :--- |
| **create_folder** | Creates a new directory at the specified path. |
| **create_empty_file** | Creates a new file (0 bytes). |
| **create_file_with_content** | Creates a file and immediately writes text content to it. |
| **read_file** | Reads the contents of a file and returns it to the agent context. |
| **write_file** | Overwrites an existing file with new content. |
| **append_doc** | Appends text to the end of an existing file (useful for logs/journals). |
| **rename_file** | Renames a specific file. |
| **move_file** | Moves a file from a source folder to a destination folder. |
| **copy_file** | Copies a file (preserving metadata) to a new location. |
| **remove_file** | Permanently deletes a specific file. |
| **remove_folder** | Recursively deletes a folder and all its contents. |
| **list_files** | Lists all files and directories in the current path. |
| **search_file** | Checks if a specific file exists. |
| **get_file_size** | Returns the file size converted to GB. |
| **summarize_project** | Lists the first 30 files to give the agent an overview of the directory. |
| **create_zip_folder** | Compresses a target folder into a `.zip` archive. |

### 💻 Coding & Shell Execution (`tools/coding_shell_tools.py`)
Tools designed for developers to automate coding workflows.

| Tool Name | Description |
| :--- | :--- |
| **run_python_script** | Executes a `.py` file using the system's Python interpreter. |
| **run_js_script** | Executes a `.js` file using Node.js. |
| **install_python_packages** | Runs `pip install <package>` to add dependencies. |
| **install_node_packages** | Runs `npm install <package>` for Node.js projects. |
| **execute_terminal_command** | **(High Power)** Executes arbitrary shell commands and captures output. |
| **print_project_hierarchy** | Uses the `tree` command to visualize folder structure. |
| **search_web** | Queries DuckDuckGo via API to retrieve real-time information. |

### 🐙 GitHub Automation (Authenticated) (`tools/github_tools.py`)
Tools that require a Personal Access Token to manage your repositories.

| Tool Name | Description |
| :--- | :--- |
| **create_github_repo** | Creates a new public or private repository on your account. |
| **delete_github_repo** | **(Destructive)** Permanently deletes a repository by name. |
| **list_github_repos** | Lists all repositories associated with the authenticated user. |
| **create_github_file** | Creates a new file inside a specific remote repository. |
| **delete_github_file** | Removes a file from a remote repository. |
| **add_folder_to_github** | Adds a folder structure to a repo (via `.gitkeep` or direct file creation). |

### 🌐 GitHub Data & Media (`tools/general_github_api_tools.py`)
Public API tools for exploration and data retrieval.

| Tool Name | Description |
| :--- | :--- |
| **search_github** | Searches for public repositories based on keywords. |
| **get_repo_readme** | Fetches and decodes the README.md of any public repo. |
| **list_repo_files** | Lists the root file structure of any public repo. |
| **download_github_repo** | Downloads a repo as a ZIP and extracts it to the current folder. |
| **download_random_image** | Fetches a random image from Lorem Picsum and saves it locally. |

### 🖥️ System Monitoring (`tools/System_tools.py`)
Tools for checking the health of the machine running the agent.

| Tool Name | Description |
| :--- | :--- |
| **get_cpu_RAM_usage** | Returns current CPU % and RAM usage (Total/Used/Free). |
| **get_os_info** | Returns System, Node Name, Release, Version, and Machine type. |
| **list_processes** | Lists the top 20 currently running process names. |

### ☁️ General Utilities (`tools/general_tools.py`)
| Tool Name | Description |
| :--- | :--- |
| **get_current_time** | Returns the local system time. |
| **get_weather** | Fetches current weather for a city via `wttr.in`. |

---

## 🛠️ Installation & Setup
## 1. Install Python Dependencies

Run the following command to install all required Python packages:

```bash
pip install langchain langchain-groq langchain-community python-dotenv requests psutil PyGithub
```

**Note:**  
You must have **Node.js installed** to use the `run_js_script` and `npm` tools.

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

```bash
pip install langchain langchain-groq langchain-community python-dotenv requests psutil PyGithub
=
