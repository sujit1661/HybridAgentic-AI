# HybridAgentic AI 🤖

**HybridAgentic AI** is a powerful, autonomous system automation agent powered by **LangChain** and **Groq**. It functions as an intelligent operating assistant capable of interacting with your local file system, executing code, managing GitHub repositories, monitoring system resources, and fetching real-time web information—all through a natural language chat interface.

The agent utilizes **persistent memory** to maintain context across sessions and employs a robust suite of tools to perform complex tasks without manual intervention.

---

## 🚀 Features

### 📂 File System Management
Full control over local files and directories:
*   **Create/Delete:** Create folders, empty files, or files with content.
*   **Organize:** Copy, move, and rename files.
*   **Read/Write:** Read file contents, write new data, or append to existing documents.
*   **Analyze:** Get file sizes, search for file existence, and list directory contents.
*   **Archive:** Create ZIP archives of project folders.
*   **Summarize:** Generate summaries of the current project structure.

### 💻 Coding & Execution
Automate development tasks:
*   **Run Code:** Execute Python (`.py`) and JavaScript (`.js`) scripts directly.
*   **Package Management:** Install dependencies via `pip` (Python) and `npm` (Node.js).
*   **Shell Commands:** Execute terminal commands.
*   **Project Analysis:** Visualize project hierarchy (tree structure).

### 🐙 GitHub Automation
Manage repositories via authenticated and public APIs:
*   **Management:** Create, list, and delete repositories.
*   **File Ops:** Create files, delete files, and upload folders to GitHub.
*   **Exploration:** Search GitHub, download repositories (ZIP), and read READMEs.
*   **Public Data:** List repository files and search for projects.

### 🖥️ System Monitoring
Keep track of your machine's health:
*   **Resources:** Monitor real-time CPU and RAM usage.
*   **Processes:** List top running processes.
*   **OS Info:** Retrieve detailed operating system specifications.

### 🌐 Utilities
*   **Web Search:** Search the web using DuckDuckGo.
*   **Media:** Download random images based on keywords.
*   **Info:** Get current time and weather updates for any city.

### 🧠 Memory
*   **Persistence:** Chat history is saved locally in JSON format (`memory/user1.json`), allowing the agent to remember context between restarts.

---

## 🛠️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/HybridAgenticAI.git
cd HybridAgenticAI
2. Install Dependencies
Ensure you have Python installed. Install the required libraries using pip:

Bash

pip install langchain langchain-groq langchain-community python-dotenv requests psutil PyGithub
Note: You may also need tree installed on your system for the hierarchy tool (or it will default to error handling).

3. Project Structure
Ensure your files are organized as follows:

text

HybridAgenticAI/
│
├── main.py                       # Entry point (Agent logic)
├── tools_registry.py             # Loads all tools into the agent
├── memory/                       # Stores chat history (auto-created)
│
├── tools/                        # Tool definitions
│   ├── __init__.py
│   ├── file_tool.py              # File system operations
│   ├── coding_shell_tools.py     # Code execution & Shell
│   ├── System_tools.py           # CPU/RAM/OS stats
│   ├── general_tools.py          # Time & Weather
│   ├── github_tools.py           # Authenticated GitHub actions
│   └── general_github_api_tools.py # Public GitHub API actions
│
└── .env                          # Environment variables
⚙️ Configuration
1. Environment Variables
Create a .env file in the root directory to store your API keys safely:

ini

GROQ_API_KEY=gsk_your_groq_api_key_here
2. GitHub Token Setup
To use the authenticated GitHub tools (create/delete repos), you need a Personal Access Token.

Go to GitHub Settings -> Developer Settings -> Personal Access Tokens (Classic).
Generate a token with repo and delete_repo permissions.
Important: Open tools/github_tools.py and update the token variable, or ideally, load it from your .env file for security.
Python

# In tools/github_tools.py
token = "your_actual_github_token_here" 
# OR use os.getenv("GITHUB_TOKEN")
▶️ Usage
Run the main script to start the agent:

Bash

python main.py
You will see:

text

🤖 AI System Agent Ready
Type 'exit' to quit

You: 
Example Commands
File Operations:

"Create a folder named 'ProjectX' and add a file notes.txt inside it with the text 'Meeting at 5pm'."
"Zip the 'ProjectX' folder."

Coding:

"Create a python script called hello.py that prints 'Hello World' and run it."
"Install the numpy package."

GitHub:

"Create a private github repo called 'ai-test-repo'."
"List my repositories."
"Download the repository 'owner/repo_name'."

System Info:

"Show me the current CPU and RAM usage."
"What is the weather in London?"

⚠️ Security Warning
Powerful Tool: This agent has access to your file system, shell, and GitHub account.

Code Execution: It can run arbitrary code and shell commands. Do not use this on a production server without proper sandboxing.
GitHub Access: The delete_repo tool is powerful. Use with caution to avoid accidental data loss.
Dependencies: Ensure you review code generated by the agent before executing it if you are unsure.
📝 License
This project is open-source. Feel free to modify and expand it!

👤 Author
Sujit Sadalage

