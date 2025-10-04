import sys
import os
from orchestrator import run_session
import socket_service

def agent(project_root, session_id, user_instruction=None):
    project_root = str(project_root)
    session_id = str(session_id)

    socket_service.emit_log("🔍 Agent starting validation checks", 'info')

    if not os.path.isdir(project_root):
        error_msg = f"Error: project_root '{project_root}' is not a valid directory."
        socket_service.emit_log(error_msg, 'error')
        print(f"Error: project_root '{project_root}' is not a valid directory.")
        sys.exit(1)

    socket_service.emit_log(f"✅ Project directory validated: {project_root}", 'success')
    socket_service.emit_log("🚀 Starting orchestrator session...", 'info')
    
    summary = run_session(project_root, session_id, user_instruction)

    socket_service.emit_log("📊 Agent execution summary ready", 'success')
    print(summary)

    return summary
