# Area51 Project IBM Agent

A sophisticated AI-powered project analysis and auto-fixing system built for IBM's Area51 project. This agent automatically analyzes codebases, detects issues through linting, and applies fixes with real-time progress tracking via WebSocket communication.

## 🚀 Features

- **Automated Project Analysis**: Intelligently scans project directories and identifies project types
- **Multi-Language Linting**: Supports Python (pylint) and Node.js (ESLint) projects
- **Real-time Progress Tracking**: WebSocket-based live updates during agent execution
- **Intelligent Code Patching**: Generates and applies patches to fix detected issues
- **File Management**: Create, read, and modify files as needed
- **Session Logging**: Comprehensive logging of all actions performed
- **RESTful API**: Easy integration with external systems
- **CORS Support**: Cross-origin resource sharing enabled for web applications

## 🏗️ Architecture

The system is built with a modular architecture consisting of:

### Core Components

- **`main.py`**: Flask web server with WebSocket support for real-time communication
- **`my_agent.py`**: Main agent entry point with validation and orchestration
- **`orchestrator.py`**: Session orchestrator that manages the AI agent workflow
- **`socket_service.py`**: WebSocket service for real-time communication

### Agent Tools (`agent_tools/`)

- **`file_tools.py`**: File system operations (read directories, read files)
- **`lint_tools.py`**: Code linting for Python and Node.js projects
- **`patch_tools.py`**: Code patching and file creation utilities
- **`logging_tools.py`**: Action logging and session management

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)
- Node.js (for ESLint support)
- pylint (for Python linting)
- patch utility (for applying patches)

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd agent_tools
   ```

2. **Install Python dependencies**:
   ```bash
   pip install flask flask-socketio flask-cors python-dotenv pydantic
   ```

3. **Install linting tools**:
   ```bash
   # For Python projects
   pip install pylint
   
   # For Node.js projects (if needed)
   npm install -g eslint
   ```

4. **Set up environment variables** (optional):
   ```bash
   # Create .env file
   echo "SECRET_KEY=your-secret-key-here" > .env
   ```

## 🚀 Usage

### Starting the Server

```bash
python main.py
```

The server will start on `http://localhost:5000` with WebSocket support.

### API Endpoints

#### 1. Health Check
```http
GET /
```
Returns a welcome message confirming the server is running.

#### 2. Start Agent Session
```http
POST /fix
Content-Type: application/json

{
    "project_path": "/path/to/your/project",
    "session_id": "unique-session-id",
    "user_instructions": "Optional instructions for the agent"
}
```

**Response**:
```json
{
    "message": "Agent started",
    "session_id": "unique-session-id"
}
```

### WebSocket Events

The server emits real-time updates via WebSocket:

#### Client → Server Events
- `connect`: Establish connection
- `disconnect`: Close connection

#### Server → Client Events
- `status`: Connection status updates
- `agent_log`: Log messages with timestamps
- `agent_progress`: Progress updates with percentages
- `file_operation`: File operation status updates
- `agent_complete`: Session completion notification
- `agent_error`: Error notifications

### Example WebSocket Client (JavaScript)

```javascript
const socket = io('http://localhost:5000');

socket.on('connect', () => {
    console.log('Connected to agent server');
});

socket.on('agent_log', (data) => {
    console.log(`[${data.type}] ${data.message}`);
});

socket.on('agent_progress', (data) => {
    console.log(`Progress: ${data.percentage}% - ${data.message}`);
});

socket.on('agent_complete', (data) => {
    console.log('Agent session completed:', data.log);
});

// Start an agent session
fetch('/fix', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        project_path: '/path/to/project',
        session_id: 'session-123',
        user_instructions: 'Fix all linting issues'
    })
});
```

## 🔧 Agent Workflow

The AI agent follows this automated workflow:

1. **Project Analysis**: Scans the project directory structure
2. **Project Type Detection**: Identifies the project type (Python, Node.js, etc.)
3. **Linting**: Runs appropriate linters to detect issues
4. **Issue Resolution**: Generates and applies patches for detected problems
5. **Custom Instructions**: Processes any user-provided instructions
6. **File Creation**: Creates new files if needed
7. **Action Logging**: Logs all actions performed during the session
8. **Summary Generation**: Provides a comprehensive summary of changes

## 📁 Project Structure

```
agent_tools/
├── main.py                 # Flask web server
├── my_agent.py            # Main agent entry point
├── orchestrator.py        # Session orchestrator
├── socket_service.py      # WebSocket communication
├── agent_tools/           # Agent tool modules
│   ├── file_tools.py      # File system operations
│   ├── lint_tools.py      # Code linting
│   ├── patch_tools.py     # Code patching
│   └── logging_tools.py   # Action logging
└── README.md              # This file
```

## 🔍 Supported Project Types

- **Python**: Uses pylint for code analysis
- **Node.js**: Uses ESLint for code analysis
- **Generic**: Basic file operations and patching

## 📊 Logging

All agent actions are logged to JSONL format files in the `log/` directory within the project being analyzed. Log entries include:

- Timestamp
- Action type
- Action details
- Session ID

## 🛡️ Security Considerations

- CORS is enabled for all origins (configure as needed for production)
- Secret key is generated automatically if not provided
- File operations are restricted to the specified project directory
- WebSocket connections are session-based

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in `main.py` (line 107)
2. **Linting tools not found**: Ensure pylint/ESLint are installed and in PATH
3. **Permission errors**: Ensure the agent has read/write access to the project directory
4. **WebSocket connection issues**: Check CORS settings and firewall configuration

### Debug Mode

The server runs in debug mode by default. To disable:
```python
socketio.run(app, debug=False, host='0.0.0.0', port=5000)
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is part of IBM's Area51 initiative. Please refer to your organization's licensing terms.

## 🆘 Support

For support and questions:
- Check the troubleshooting section above
- Review the WebSocket event logs
- Contact your IBM Area51 project team

---

**Note**: This agent has full permission to modify files and create new files. Always backup your projects before running the agent, especially in production environments.
