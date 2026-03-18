# HybridAgentic AI 🤖

**HybridAgentic AI** is an advanced, autonomous system automation agent designed to act as an intelligent operating system assistant. Built on the **LangChain** framework and powered by **Groq's** high-performance inference engine, this agent bridges the gap between natural language reasoning and low-level system operations.

It is capable of managing files, executing code, controlling version control systems (GitHub), monitoring system health, and interacting with the web — all through a conversational interface with persistent memory.

---

## 🏗️ Technology Stack

The project relies on a robust set of modern technologies:

- **Core Framework:** [LangChain](https://www.langchain.com/) (Agents, Tools, RunnableHistory)
- **LLM Engine:** [Groq API](https://groq.com/) (Running `openai/gpt-oss-20b` / Llama 3) for ultra-fast inference and tool calling
- **System Interaction:** `os`, `shutil`, `subprocess` (Python Standard Libraries)
- **System Monitoring:** `psutil` for CPU, RAM, and process management
- **Network/API:** `requests` for web searching and API calls
- **GitHub Integration:** `PyGithub` for repository management
- **Memory:** Local JSON storage via `FileChatMessageHistory` to maintain context across sessions

---

# 🚀 Features & Tool Breakdown

## 🧰 Available Tools

The agent includes multiple tool categories that allow it to interact with the system, execute code, manage files, automate GitHub tasks, and retrieve external information.

---

## 📁 File System Management (`tools/file_tool.py`)

These tools allow the agent to interact directly with the local file system.

| Tool Name | Description |
| :--- | :--- |
| **create_folder** | Creates a new directory at the specified path |
| **create_empty_file** | Creates a new file with **0 bytes** |
| **create_file_with_content** | Creates a file and writes content immediately |
| **read_file** | Reads file contents and returns it to the agent context |
| **write_file** | Overwrites an existing file with new content |
| **append_doc** | Appends text to the end of an existing file |
| **rename_file** | Renames a file |
| **move_file** | Moves a file to another directory |
| **copy_file** | Copies a file to a new location |
| **remove_file** | Permanently deletes a file |
| **remove_folder** | Recursively deletes a folder |
| **list_files** | Lists files and directories in a path |
| **search_file** | Checks if a file exists |
| **get_file_size** | Returns file size in **GB** |
| **summarize_project** | Lists first **30 files** to give project overview |
| **create_zip_folder** | Compresses a folder into `.zip` |

---

## 💻 Coding & Shell Execution (`tools/coding_shell_tools.py`)

Developer-focused tools for automating coding workflows.

| Tool Name | Description |
| :--- | :--- |
| **run_python_script** | Executes a `.py` file |
| **run_js_script** | Executes a `.js` file using Node.js |
| **install_python_packages** | Installs dependencies using `pip install` |
| **install_node_packages** | Installs Node packages using `npm install` |
| **execute_terminal_command** | ⚠️ Executes arbitrary shell commands |
| **print_project_hierarchy** | Displays folder structure using `tree` |
| **search_web** | Queries DuckDuckGo API for information |

---

## 🐙 GitHub Automation (`tools/github_tools.py`)

These tools require a **GitHub Personal Access Token**.

| Tool Name | Description |
| :--- | :--- |
| **create_github_repo** | Creates a new repository |
| **delete_github_repo** | ⚠️ Permanently deletes a repository |
| **list_github_repos** | Lists repositories for the user |
| **create_github_file** | Creates a file in a repository |
| **delete_github_file** | Removes a file from a repository |
| **add_folder_to_github** | Adds folder structure to repo |

---

## 🌐 GitHub Data & Media (`tools/general_github_api_tools.py`)

Public API tools for exploring GitHub.

| Tool Name | Description |
| :--- | :--- |
| **search_github** | Searches public repositories |
| **get_repo_readme** | Fetches repository README |
| **list_repo_files** | Lists repository files |
| **download_github_repo** | Downloads repository as ZIP |
| **download_random_image** | Downloads random image |

---

## 🖥️ System Monitoring (`tools/System_tools.py`)

Tools to monitor system health.

| Tool Name | Description |
| :--- | :--- |
| **get_cpu_RAM_usage** | Returns CPU % and RAM stats |
| **get_os_info** | Returns OS information |
| **list_processes** | Lists top 20 running processes |

---

## ☁️ General Utilities (`tools/general_tools.py`)

| Tool Name | Description |
| :--- | :--- |
| **get_current_time** | Returns local system time |
| **get_weather** | Fetches weather using `wttr.in` |

---

# 🛠️ Installation & Setup

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/HybridAgenticAI.git
cd HybridAgenticAI
```

---

## 2️⃣ Install Dependencies

```bash
pip install langchain langchain-groq langchain-community python-dotenv requests psutil PyGithub
```

**Note:** Node.js must be installed for `run_js_script` and `npm` tools.

---

## 3️⃣ Environment Configuration

Create `.env` in the root directory:

```ini
GROQ_API_KEY=gsk_your_groq_api_key_here
GITHUB_TOKEN=ghp_your_github_token_here
```

---

## 4️⃣ GitHub Token Setup

1. Go to **GitHub Settings → Developer Settings → Personal Access Tokens**
2. Generate a new token
3. Enable:
   - `repo`
   - `delete_repo`

Update `tools/github_tools.py` to load the token from `.env`.

---

# ▶️ Usage

Start the agent:

```bash
python main.py
```


---
## 🧠 Architecture Overview

HybridAgentic AI follows a **modular agent architecture** built on **LangChain** that connects natural language reasoning with system-level tool execution.

```
User Input
   │
   ▼
LLM Reasoning (Groq)
   │
   ▼
Tool Selection (LangChain Agent)
   │
   ▼
Tool Execution
   │
   ▼
Result Returned to User
   │
   ▼
Memory Stored (JSON Chat History)
```

### Key Flow

1. **User Input** – The user provides a natural language instruction.
2. **LLM Reasoning** – The Groq-powered LLM analyzes the request.
3. **Tool Selection** – LangChain determines which tool should be used.
4. **Tool Execution** – The selected system tool performs the action.
5. **Result Returned** – The output is sent back to the user.
6. **Memory Storage** – The conversation is stored in JSON for future context.
  
---

# 💬 Interaction Examples

### Web Development Setup

**User**

> Create a folder called `MyWebsite` with `index.html` and `style.css`

**Agent Actions**

- `create_folder`
- `create_file_with_content`

---

## 📊 Logging & Observability

The system includes a centralized logging mechanism to track tool execution and errors.

- Logs tool start and completion  
- Captures input arguments and outputs  
- Tracks errors for debugging  
- Logs stored in `agent.log`  

---

## ⚡ FastAPI Integration (API Layer)

The agent supports API-based interaction using FastAPI.

### 🚀 Features
- REST endpoint for agent queries  
- Integration with frontend or external apps  
- Multi-user support  

### 📌 Endpoint
POST /run-agent

### 📌 Request Body
```json
{
  "query": "Create a folder test and add a file hello.txt"
}
```



---
### System Diagnostics

**User**

> My computer feels slow. Check CPU and running processes.

**Agent Actions**

- `get_cpu_RAM_usage`
- `list_processes`

---

### GitHub Management

**User**

> Create a private repo `agent-backup` and upload project

**Agent Actions**

- `create_github_repo`
- `create_zip_folder`

---

# 📂 Project Structure

```text
HybridAgenticAI/
│
├── main.py
├── tools_registry.py
│
├── tools/
│   ├── file_tool.py
│   ├── coding_shell_tools.py
│   ├── System_tools.py
│   ├── general_tools.py
│   ├── github_tools.py
│   └── general_github_api_tools.py
│
├── memory/
└── .env
```


---

##  Future Improvements

Planned enhancements:

- Docker sandbox execution
- GUI dashboard
- Vector database memory
- Multi-agent collaboration
- Automatic debugging agent
---
'''

# ⚠️ Security Warning

This agent allows **arbitrary code execution and file system modification**.

- Shell access via `execute_terminal_command`
- Ability to delete files and repositories

⚠️ **Run inside a VM, Docker container, or restricted environment.**

---

# 👤 Author

Created by **Sujit Sadalage**
