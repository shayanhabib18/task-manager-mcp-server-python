# Task Manager MCP Server

A Python-based **Model Context Protocol (MCP) server** that allows AI assistants to interact with a task management system through MCP tools.

This project demonstrates how an AI application can communicate with an MCP server to perform task-management operations such as creating, retrieving, updating, and deleting tasks.

## 🚀 Overview

The **Task Manager MCP Server** is built to demonstrate the communication flow between an AI application, an MCP client, and an MCP server.

Instead of directly connecting an AI model to application-specific APIs, MCP provides a standardized way for AI applications to discover and use external tools.

### Architecture

```text
┌─────────────────┐
│   AI Assistant  │
│     Claude      │
└────────┬────────┘
         │
         │ MCP
         ▼
┌─────────────────┐
│    MCP Client   │
└────────┬────────┘
         │
         │ MCP Protocol
         ▼
┌─────────────────┐
│   MCP Server    │
│    Python       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Task Manager   │
│     System      │
└─────────────────┘
```

### How It Works

1. The user gives a task-related instruction to the AI assistant.
2. The AI determines which MCP tool is required.
3. The MCP client sends the request to the MCP server.
4. The Python MCP server executes the requested operation.
5. The server returns the result to the MCP client.
6. The MCP client passes the result back to the AI assistant.
7. The AI presents the result to the user.

## ✨ Features

* Create tasks
* Retrieve tasks
* Update tasks
* Delete tasks
* MCP tool integration
* Python-based MCP server
* MCP client for testing
* Claude Desktop integration
* MCPB extension support
* Simple and modular project structure

## 🛠️ Technologies

* **Python**
* **Model Context Protocol (MCP)**
* **Claude Desktop**
* **MCPB**
* **AsyncIO**
* **JSON**

## 📁 Project Structure

```text
task-manager-mcp-server/
│
├── server.py
├── mcpClient.py
├── manifest.json
├── pyproject.toml
├── README.md
├── .gitignore
│
└── ...
```

> Project files may change as the MCP server evolves.

## ⚙️ Requirements

Before running the project, make sure you have:

* Python 3.14+
* MCP Python SDK
* Claude Desktop (for Claude integration)

It is recommended to use a Python virtual environment.

## 🔧 Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/task-manager-mcp-server.git
```

Move into the project directory:

```bash
cd task-manager-mcp-server
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

Linux/macOS:

```bash
source .venv/bin/activate
```

Windows:

```powershell
.venv\Scripts\activate
```

### 4. Install dependencies

If the project uses `pyproject.toml`:

```bash
pip install -e .
```

Or install the required MCP package:

```bash
pip install mcp
```

## ▶️ Running the MCP Server

Activate your virtual environment:

```bash
source .venv/bin/activate
```

Then start the server:

```bash
python server.py
```

The MCP server communicates using the transport configured by the application/client.

> For Claude Desktop integration, the server is normally launched by Claude Desktop rather than manually from the terminal.

## 🧪 Testing with the MCP Client

The project also includes an MCP client for testing communication with the server.

Run:

```bash
python mcpClient.py
```

The client establishes communication with the MCP server and can be used to test the available MCP tools.

## 🤖 Claude Desktop Integration

The MCP server can be connected to Claude Desktop so that Claude can use the task-management tools.

A typical MCP configuration follows this concept:

```json
{
  "mcpServers": {
    "task-manager": {
      "command": "python",
      "args": [
        "/path/to/task-manager-mcp-server/server.py"
      ]
    }
  }
}
```

Replace:

```text
/path/to/task-manager-mcp-server/server.py
```

with the actual path to your server.

The exact configuration may vary depending on your operating system and Claude Desktop setup.

## 🔌 MCP Tools

The server exposes task-management functionality through MCP tools.

Example operations include:

| Tool          | Purpose                 |
| ------------- | ----------------------- |
| `create_task` | Create a new task       |
| `list_tasks`   | Retrieve existing tasks |
| `complete_task` | Update an existing task to mark complete |
| `delete_task` | Delete a task           |

The available tools may change as the project develops.

## 💡 Example Interaction

A user could ask an AI assistant:

```text
Create a task called "Learn RAG" with high priority.
```

The communication flow would be:

```text
User
  ↓
AI Assistant
  ↓
MCP Client
  ↓
MCP Server
  ↓
create_task()
  ↓
Task Manager
  ↓
Result
  ↓
MCP Client
  ↓
AI Assistant
  ↓
User
```

The AI does not need to know the internal implementation of the task manager. It uses the tools exposed by the MCP server.

## 🔐 Security

Do not commit sensitive information to this repository.

Make sure files such as the following are excluded:

```text
.env
.env.*
.venv/
__pycache__/
*.pyc
```

Never commit:

* API keys
* Access tokens
* Passwords
* Private credentials
* Personal secrets

## 📚 What This Project Demonstrates

This project was created as a practical implementation for learning and understanding:

* Model Context Protocol
* MCP clients and servers
* MCP tools
* AI-to-tool communication
* Python asynchronous programming
* Claude Desktop MCP integration
* MCPB extensions
* AI application architecture

## 🔮 Future Improvements

Potential future improvements include:

* Persistent database storage
* Task priorities
* Task categories
* Due dates
* Task searching and filtering
* Task completion status
* Authentication
* REST API integration
* More MCP tools
* Improved error handling
* Automated tests
* Docker support

## 👨‍💻 Author

**Shayan Habib**

Software Engineer | Full Stack Developer | AI & MCP Learner

GitHub: [@shayanhabib18](https://github.com/shayanhabib18)



⭐ If you find this project useful for learning MCP and AI integrations, consider giving the repository a star.
