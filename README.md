# 🤖 HybridAgentic AI

> An autonomous AI system assistant built with **LangChain** and **Groq** that transforms natural language into real system actions. It can manage files, execute code, automate GitHub workflows, monitor system resources, retrieve information from the web, and maintain persistent memory—all through an intelligent conversational interface.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Agent-green)
![Groq](https://img.shields.io/badge/Groq-LLM-orange)
![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688?logo=fastapi)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Overview

HybridAgentic AI is a modular AI automation agent designed to bridge the gap between **Large Language Models (LLMs)** and real operating system capabilities.

Unlike traditional AI chatbots that can only generate text, HybridAgentic AI can actually perform tasks on behalf of the user by intelligently selecting and executing tools.

The system combines **LangChain Agents**, **Groq's ultra-fast inference**, and a collection of custom-built tools that enable interaction with:

- Local files and folders
- Python & JavaScript execution
- GitHub repositories
- System resources
- Web APIs
- Persistent memory

The result is an intelligent assistant capable of performing complex automation tasks using simple natural language instructions.

---

# 🎯 Motivation

Modern LLMs are incredibly powerful at reasoning but cannot directly interact with the operating system.

HybridAgentic AI was built to solve this limitation by providing the model with carefully designed tools that allow it to perform real actions.

Instead of simply explaining how to perform a task, the agent can:

- Create files
- Modify projects
- Execute programs
- Search repositories
- Manage GitHub
- Monitor system health

through a conversational interface.

This project demonstrates how LLMs can evolve from passive chatbots into autonomous software agents capable of solving practical development and productivity tasks.

---

# ✨ Features

## 🧠 Intelligent AI Agent

- Natural language understanding
- Multi-step reasoning
- Autonomous tool selection
- Context-aware responses
- Persistent memory
- Conversation history

---

## 📁 File System Automation

Perform common file operations directly through natural language.

Features include:

- Create folders
- Create empty files
- Create files with content
- Read files
- Update existing files
- Append content
- Rename files
- Move files
- Copy files
- Delete files
- Delete folders
- Search files
- Calculate file size
- Compress folders
- Summarize project structures

---

## 💻 Development Automation

Developer-focused tools that automate coding workflows.

Capabilities include:

- Execute Python scripts
- Execute JavaScript programs
- Install Python packages
- Install Node packages
- Run terminal commands
- Display project hierarchy
- Search documentation online

---

## 🐙 GitHub Automation

The agent integrates directly with GitHub using Personal Access Tokens.

Supported operations include:

- Create repositories
- Delete repositories
- Upload project files
- Delete repository files
- List repositories
- Download repositories
- Read repository README files
- Search public repositories

---

## 🌐 Internet Utilities

Retrieve information directly from external services.

Available utilities include:

- Web Search
- GitHub Search
- Weather Information
- Current Time
- Download Random Images

---

## 🖥️ System Monitoring

Monitor computer performance directly from the AI assistant.

Available metrics include:

- CPU Usage
- RAM Usage
- Running Processes
- Operating System Information

---

## 💾 Persistent Memory

The agent remembers previous conversations using local JSON storage.

Memory enables:

- Context-aware conversations
- Multi-step tasks
- Conversation history
- Better long-term interaction

---

# 🏛️ System Architecture

```text
                         User
                           │
                           ▼
                Natural Language Query
                           │
                           ▼
               Groq Large Language Model
                           │
                           ▼
              LangChain Agent Reasoning
                           │
                Tool Selection Engine
                           │
     ┌──────────────┬──────────────┬──────────────┐
     ▼              ▼              ▼              ▼
 File Tools     GitHub Tools   System Tools   Web Tools
     │              │              │              │
     └──────────────┴──────────────┴──────────────┘
                           │
                           ▼
                   Tool Execution
                           │
                           ▼
                    Response Generated
                           │
                           ▼
                  JSON Memory Storage
```

---

# 🔄 Agent Workflow

```text
User Request
      │
      ▼
Groq LLM
      │
      ▼
Reasoning
      │
      ▼
Tool Selection
      │
      ▼
Execute Tool
      │
      ▼
Collect Output
      │
      ▼
Generate Response
      │
      ▼
Store Conversation Memory
```

---

# 🚀 Key Capabilities

HybridAgentic AI can perform tasks such as:

- 📁 Organize project folders
- 📄 Generate source code files
- 💻 Execute Python programs
- 🌐 Search the internet
- 🐙 Manage GitHub repositories
- 📦 Compress projects
- 📊 Monitor CPU & RAM
- 📂 Read project structures
- ⚙️ Execute terminal commands
- 🧠 Maintain long-term memory

---

# 🧰 Available Tools

The project is built around a modular tool architecture.

Each tool focuses on a specific category of tasks, allowing the AI agent to reason about which action should be performed before executing it.

---

# 📁 File System Tools

These tools allow the AI to directly interact with the local file system.

| Tool | Description |
|------|-------------|
| create_folder | Create new directories |
| create_empty_file | Create empty files |
| create_file_with_content | Create files with initial content |
| read_file | Read file contents |
| write_file | Overwrite file contents |
| append_doc | Append text to existing files |
| rename_file | Rename files |
| move_file | Move files |
| copy_file | Copy files |
| remove_file | Delete files |
| remove_folder | Delete folders |
| list_files | List files inside directories |
| search_file | Search files |
| get_file_size | Calculate file size |
| summarize_project | Summarize project structure |
| create_zip_folder | Compress folders |

---

# 💻 Coding & Shell Tools

Designed for software development automation.

| Tool | Description |
|------|-------------|
| run_python_script | Execute Python programs |
| run_js_script | Execute JavaScript programs |
| install_python_packages | Install pip packages |
| install_node_packages | Install npm packages |
| execute_terminal_command | Execute shell commands |
| print_project_hierarchy | Display project tree |
| search_web | Search the web |

---

# 🐙 GitHub Automation Tools

GitHub integration allows the AI to automate repository management.

| Tool | Description |
|------|-------------|
| create_github_repo | Create repositories |
| delete_github_repo | Delete repositories |
| list_github_repos | List repositories |
| create_github_file | Upload repository files |
| delete_github_file | Delete repository files |
| add_folder_to_github | Upload project folders |

---

# 🌐 GitHub Public API Tools

Interact with public repositories.

| Tool | Description |
|------|-------------|
| search_github | Search repositories |
| get_repo_readme | Retrieve README |
| list_repo_files | List repository files |
| download_github_repo | Download repositories |
| download_random_image | Download random images |

---

# 🖥️ System Tools

Monitor system resources.

| Tool | Description |
|------|-------------|
| get_cpu_RAM_usage | CPU & Memory usage |
| get_os_info | Operating System information |
| list_processes | Running processes |

---

# ☁️ Utility Tools

| Tool | Description |
|------|-------------|
| get_current_time | Current local time |
| get_weather | Weather information |

---

# 🛠️ Technology Stack

| Category | Technologies |
|-----------|-------------|
| Programming Language | Python |
| AI Framework | LangChain |
| LLM | Groq |
| API Framework | FastAPI |
| Memory | FileChatMessageHistory |
| GitHub Integration | PyGithub |
| Networking | Requests |
| System Monitoring | psutil |
| Environment | python-dotenv |
| Standard Libraries | os, shutil, subprocess |

---

# 📂 Project Structure

```text
HybridAgenticAI/
│
├── main.py
├── tools_registry.py
├── agent.log
│
├── tools/
│   ├── file_tool.py
│   ├── coding_shell_tools.py
│   ├── github_tools.py
│   ├── general_github_api_tools.py
│   ├── System_tools.py
│   └── general_tools.py
│
├── memory/
│
├── .env
├── requirements.txt
└── README.md
```

---

# ⚙️ Getting Started

Follow these steps to set up HybridAgentic AI on your local machine.

---

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/sujit1661/HybridAgenticAI.git

cd HybridAgenticAI
```

---

## 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

## 3️⃣ Install Dependencies

Install all required Python packages.

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install langchain
pip install langchain-groq
pip install langchain-community
pip install python-dotenv
pip install requests
pip install psutil
pip install PyGithub
pip install fastapi
pip install uvicorn
```

> **Note:** Install **Node.js** if you plan to use JavaScript execution or npm package installation.

---

# ⚙️ Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key

GITHUB_TOKEN=your_github_personal_access_token
```

---

# 🔑 GitHub Token Setup

To enable GitHub automation:

1. Open **GitHub Settings**
2. Navigate to

```
Developer Settings
        ↓
Personal Access Tokens
```

3. Generate a new token.

Recommended permissions:

- repo
- delete_repo

Save the generated token inside the `.env` file.

---

# ▶️ Running the Agent

Start the AI assistant.

```bash
python main.py
```

The terminal-based AI assistant will start and begin accepting natural language commands.

---

# ⚡ Running FastAPI

If the API layer is enabled:

```bash
uvicorn main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Swagger Documentation:

```
http://127.0.0.1:8000/docs
```

---

# 📡 API Endpoint

## POST `/run-agent`

Send a natural language request to the AI agent.

### Request

```json
{
  "query": "Create a folder called AIProject and add README.md"
}
```

### Response

```json
{
  "status": "success",
  "response": "Folder created successfully."
}
```

---

# 💬 Example Commands

## 📁 File Management

```
Create a folder called Portfolio.
```

```
Create a file named notes.txt.
```

```
Rename report.txt to final_report.txt.
```

```
Move app.py into the src folder.
```

```
Delete the temporary folder.
```

---

## 💻 Development

```
Run calculator.py
```

```
Install pandas and numpy.
```

```
Run npm install.
```

```
Print project folder hierarchy.
```

```
Execute this shell command:
git status
```

---

## 🐙 GitHub

```
Create a GitHub repository named AI-Agent.
```

```
Upload this project to GitHub.
```

```
List all my repositories.
```

```
Delete repository old-project.
```

---

## 🌐 Internet

```
Search LangChain documentation.
```

```
Search GitHub for FastAPI projects.
```

```
Download the repository.
```

```
Show today's weather.
```

---

## 🖥️ System Monitoring

```
Check CPU usage.
```

```
How much RAM is currently being used?
```

```
Show running processes.
```

```
What operating system am I using?
```

---

# 🧠 Memory System

HybridAgentic AI maintains conversation history using **JSON-based local storage**.

The memory system enables:

- Context-aware conversations
- Follow-up questions
- Multi-step task execution
- Persistent chat history
- Improved reasoning

Memory is automatically updated after every interaction.

---

# 📊 Logging & Monitoring

Every important operation performed by the agent is logged.

The logging system records:

- Tool execution
- Successful operations
- Failed operations
- Exceptions
- Execution time
- Debugging information

Example log:

```text
[INFO] Tool: create_folder
[INFO] Folder created successfully.

[INFO] Tool: run_python_script
[INFO] Execution completed.

[ERROR] GitHub authentication failed.
```

Logs are stored in:

```
agent.log
```

---

# 🔒 Security Considerations

HybridAgentic AI executes real system operations.

Capabilities include:

- File creation
- File deletion
- Folder deletion
- Shell command execution
- GitHub repository management

For safety:

- Use environment variables for API keys.
- Never commit secrets to GitHub.
- Run inside Docker or a Virtual Machine when testing unrestricted tools.
- Limit GitHub Personal Access Token permissions whenever possible.

---

# ⚠️ Warning

The following tools perform destructive operations:

- remove_file
- remove_folder
- delete_github_repo
- execute_terminal_command

Always verify commands before execution.

Running the agent with unrestricted permissions may result in permanent data loss.

---

# 🚀 Future Roadmap

### Phase 1

- Docker sandbox execution
- Improved logging
- Better error handling
- Permission-based tool execution

---

### Phase 2

- FastAPI Web Dashboard
- User Authentication
- Chat History UI
- SQLite Database Support

---

### Phase 3

- Vector Database Memory
- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Long-term Memory

---

### Phase 4

- Multi-Agent Collaboration
- Autonomous Planning Agent
- AI Code Review
- AI Debugging Agent
- Browser Automation
- Email Automation
- Calendar Integration

---

### Phase 5

- Voice Assistant
- Speech-to-Text
- Text-to-Speech
- Mobile Application
- Cloud Deployment
- Docker & Kubernetes Support

---

# 🤝 Contributing

Contributions are welcome.

To contribute:

1. Fork the repository.
2. Create a feature branch.

```bash
git checkout -b feature-name
```

3. Commit your changes.

```bash
git commit -m "Add new feature"
```

4. Push to your branch.

```bash
git push origin feature-name
```

5. Open a Pull Request.

---

# 👨‍💻 Author

**Sujit Sadalage**

**B.Tech in Artificial Intelligence & Data Science (2022–2026)**

Aspiring **AI Engineer | Backend Developer | Python Developer**

- GitHub: https://github.com/sujit1661

---

# ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub.

Your support helps improve the project and motivates future development.

---

# 📄 License

This project is intended for learning, experimentation, and educational purposes.

Feel free to fork, modify, and build upon it while providing appropriate attribution.

---

## 🙏 Acknowledgements

Special thanks to the open-source community and the developers behind:

- LangChain
- Groq
- FastAPI
- PyGithub
- Requests
- psutil
- Python

Their tools and libraries made this project possible.
