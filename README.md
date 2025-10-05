# GitGenie 🧞‍♂️

**Supercharge your development workflow with intelligent repository management, automated insights, and seamless collaboration tools that make coding magical.**

GitGenie is a comprehensive repository management and development platform that revolutionizes how developers interact with their GitHub repositories. Built with Next.js 15, TypeScript, and modern web technologies, it provides an intelligent, automated solution for repository cloning, project analysis, and seamless development workflow management.

![GitGenie](https://img.shields.io/badge/GitGenie-Repository%20Management-blue?style=for-the-badge)
![Next.js](https://img.shields.io/badge/Next.js-15.3.5-black?style=flat&logo=next.js)
![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue?style=flat&logo=typescript)
![Prisma](https://img.shields.io/badge/Prisma-ORM-darkgreen?style=flat&logo=prisma)
![TailwindCSS](https://img.shields.io/badge/TailwindCSS-4.0-38B2AC?style=flat&logo=tailwind-css)

## 🎥 **Project Demo**

Watch GitGenie in action! See how the platform streamlines repository management and provides intelligent development tools.

[![GitGenie Demo Video](https://img.shields.io/badge/▶️%20Watch%20Demo-YouTube-red?style=for-the-badge&logo=youtube)](https://youtu.be/206Ojy7Mvtw)

**🔗 Direct Link:** https://youtu.be/DOt7I4D32g4

## ✨ Features

### 🔍 **Intelligent Repository Discovery**
- **Advanced GitHub Search**: Search and discover repositories with sophisticated filtering options
- **Smart Filtering**: Filter by programming language, creation date, stars, and more
- **Repository Insights**: Get detailed information about repositories including README content, languages used, and project statistics
- **Pagination Support**: Efficiently browse through large result sets

### 🔐 **Secure Authentication & User Management**
- **NextAuth.js Integration**: Secure authentication with GitHub OAuth
- **User Registration**: Custom user registration with email verification
- **Session Management**: Persistent sessions with automatic token refresh
- **User Profiles**: Personalized user experience with profile management

### 📚 **Repository Management System**
- **One-Click Cloning**: Seamlessly clone repositories with automated setup
- **Project Tracking**: Keep track of all your cloned repositories in one place
- **Connection Status**: Monitor the status of repository connections and synchronization
- **Repository Mapping**: Intelligent mapping between GitHub repositories and local instances

### 🚀 **Project Runner & Development Environment**
- **Automated Project Analysis**: Intelligent detection of project types, frameworks, and build systems
- **Smart Build Detection**: Automatic identification of build commands and dependencies
- **Live Project Running**: Run projects in isolated environments with real-time monitoring
- **Port Management**: Automatic port allocation and management for running projects
- **Project Status Monitoring**: Real-time status updates and health checks

### 🤖 **AI-Powered Assistance**
- **Interactive Chat Interface**: Get help and insights about your running projects
- **Project Analysis**: AI-powered analysis of project structure and recommendations
- **Debugging Support**: Intelligent debugging assistance and error resolution
- **Code Insights**: Smart suggestions for code improvements and best practices

### 🛠️ **Infrastructure Management**
- **GCP Integration**: Seamless integration with Google Cloud Platform
- **VM Management**: Automated virtual machine provisioning and management
- **SSH Connectivity**: Secure shell access to remote development environments
- **Resource Monitoring**: Track resource usage and performance metrics

### 📊 **Admin Dashboard**
- **User Management**: Admin interface for managing users and permissions
- **Repository Mappings**: Overview and management of all repository connections
- **System Health**: Monitor system performance and health metrics
- **Analytics**: Detailed analytics on repository usage and user activity

## 🏗️ **Technology Stack**

### **Frontend**
- **Next.js 15** - React framework with App Router and Turbopack
- **TypeScript** - Type-safe development
- **TailwindCSS 4** - Modern utility-first CSS framework
- **React 19** - Latest React with improved performance

### **Backend & Database**
- **Prisma ORM** - Type-safe database access with PostgreSQL
- **NextAuth.js** - Authentication and session management
- **PostgreSQL** - Robust relational database

### **Cloud & Infrastructure**
- **Google Cloud Platform** - VM management and infrastructure
- **Node SSH** - Secure shell connections
- **Simple Git** - Git repository operations

### **AI & Integration**
- **OpenAI API** - AI-powered project analysis and assistance
- **GitHub API** - Repository discovery and management
- **WebAuthn** - Secure authentication methods

## 🚀 **Getting Started**

### Prerequisites
- Node.js 18+ and npm/yarn
- PostgreSQL database
- Google Cloud Platform account
- GitHub OAuth App
- OpenAI API key


### AI Usage (During Development)
- Used AI tools to draft the initial structure for the API endpoints, authentication flow, and Git server integration logic.
- Generated initial PostgreSQL schema for users, repositories, sessions, and AI-assisted coding sessions.
- Used AI to scaffold React components, dashboard layouts, and state management logic.
- Consulted AI tools for integrating OpenAI/Claude APIs securely, managing tokens, and designing prompt structures for code generation and explanations.
- AI assisted in generating README content, feature explanations, and usage instructions for better presentation.


### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ShubhamDevPro/GitGenie.git
   cd GitGenie
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Environment Setup**
   Create a `.env.local` file with the following variables:
   ```env
   # Database
   DATABASE_URL="postgresql://username:password@localhost:5432/gitgenie"
   
   # NextAuth
   NEXTAUTH_SECRET="your-nextauth-secret"
   NEXTAUTH_URL="http://localhost:3000"
   
   # GitHub OAuth
   GITHUB_CLIENT_ID="your-github-client-id"
   GITHUB_CLIENT_SECRET="your-github-client-secret"
   
   # OpenAI
   OPENAI_API_KEY="your-openai-api-key"
   
   # GCP Configuration
   GCP_PROJECT_ID="your-gcp-project-id"
   GCP_ZONE="your-gcp-zone"
   GCP_VM_NAME="your-vm-name"
   ```

4. **Database Setup**
   ```bash
   npx prisma generate
   npx prisma db push
   ```

5. **Start Development Server**
   ```bash
   npm run dev
   ```

6. **Access the Application**
   Open [http://localhost:3000](http://localhost:3000) in your browser

## 📖 **Usage Guide**

### **Repository Discovery**
1. Navigate to the Dashboard after signing in
2. Use the search functionality to find GitHub repositories
3. Apply filters to narrow down results by language, date, or other criteria
4. View detailed repository information including README content

### **Repository Cloning**
1. Go to "My Repositories" section
2. Click "Connect to Project" for any discovered repository
3. The system will automatically clone and set up the repository
4. Monitor the connection status in real-time

### **Running Projects**
1. From your cloned repositories, click "Run Project"
2. The system will automatically analyze the project structure
3. AI-powered detection will identify the best way to run your project
4. Access your running project through the integrated viewer
5. Use the chat interface for assistance and debugging

### **Admin Features**
1. Access the admin panel (admin users only)
2. View and manage user repository mappings
3. Monitor system health and performance
4. Manage user permissions and access

## 🗂️ **Project Organization Structure**

GitGenie implements a sophisticated project organization system on the GCP VM to ensure consistent naming and better management of projects for each user.

### **Directory Structure**
```
/home/{vm_username}/projects/
├── {gitea_username_1}/
│   ├── {project_1}/
│   ├── {project_2}/
│   └── {project_n}/
├── {gitea_username_2}/
│   ├── {project_1}/
│   └── {project_2}/
└── legacy/
    ├── {old_project_1}/
    └── {old_project_2}/
```

### **User-Specific Folders**
- **Path**: `/home/{vm_username}/projects/{gitea_username}/`
- **Purpose**: Each Gitea user gets their own folder to store all their projects
- **Benefits**: 
  - Prevents naming conflicts between users
  - Easy to identify project ownership
  - Clear separation of user workspaces
  - Facilitates AI agent navigation

### **API Endpoints for AI Agents**
GitGenie provides specialized API endpoints that AI agents can use to understand and manage the project structure:

```javascript
// Get current user's projects
GET /api/agent/projects-info?scope=user&format=detailed

// Get all projects overview
GET /api/agent/projects-info?scope=all&format=summary

// Get specific user's projects
POST /api/agent/projects-info
{
  "giteaUsername": "john-doe",
  "format": "detailed"
}
```

# **AI Agent (Python)**
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


### **AI Agent Integration**
The project structure is designed to be easily understood by AI agents:
- Clear path construction: `/home/{vm_username}/projects/{gitea_username}/{project_name}`
- Utility functions provided in `src/utils/aiAgentHelpers.ts`
- Permission checking and ownership validation
- Consistent naming conventions across all projects

For detailed documentation about the project organization structure, see [docs/project-organization.md](docs/project-organization.md).

## 🏢 **Architecture Overview**

GitGenie follows a modern microservices-inspired architecture:

- **Frontend Layer**: Next.js with React components and TailwindCSS
- **API Layer**: Next.js API routes handling business logic
- **Authentication Layer**: NextAuth.js with GitHub OAuth integration
- **Database Layer**: PostgreSQL with Prisma ORM
- **Infrastructure Layer**: GCP integration for VM management
- **AI Layer**: OpenAI integration for intelligent assistance

## 🔒 **Security Features**

- **OAuth Authentication**: Secure GitHub integration
- **Session Management**: Encrypted sessions with automatic expiration
- **Input Validation**: Comprehensive input sanitization and validation
- **Secure API Communication**: HTTPS enforcement and API key protection
- **Database Security**: Parameterized queries and connection encryption

## 🤝 **Contributing**

We welcome contributions to GitGenie! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### **Development Guidelines**
- Follow TypeScript best practices
- Write comprehensive tests for new features
- Maintain consistent code formatting with Prettier and ESLint
- Update documentation for new features

## 📝 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 **Acknowledgments**

- **Next.js Team** for the amazing React framework
- **Vercel** for deployment platform and tools
- **Prisma Team** for the excellent ORM
- **OpenAI** for AI capabilities
- **GitHub** for API access and OAuth integration
- **Google Cloud Platform** for infrastructure services

## 📞 **Support**

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/Naveen-NaS/GitGenie/issues) section
2. Create a new issue with detailed information
3. Contact the development team

---

**Built with ❤️ by:**
- **[Naveen Sharma](https://github.com/naveen-nas)** 
- **[ShubhamDevPro](https://github.com/ShubhamDevPro)** 

*Making repository management magical, one commit at a time* ✨
