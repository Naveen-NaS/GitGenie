import subprocess
from agents import function_tool
import socket_service

def lint_summary_raw(project_root: str, project_type: str) -> str:
    socket_service.emit_log(f"🔍 Starting lint analysis for {project_type} project", 'info')
    print(f"Running lint summary for project type: {project_type}")
    if project_type == "python":
        cmd = ["pylint", project_root]
        socket_service.emit_log("🐍 Running pylint analysis...", 'info')
    elif project_type == "node":
        cmd = ["npx", "eslint", "--format", "json", project_root]
        socket_service.emit_log("🟨 Running ESLint analysis...", 'info')
    else:
        socket_service.emit_log(f"⚠️ No linter configured for project type: {project_type}", 'warning')
        return ""
    
    result = subprocess.run(
        cmd, cwd=project_root,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )

    socket_service.emit_progress("Linting", 1, 1, "Lint analysis completed")
    
    return result.stdout + result.stderr

@function_tool
def lint_summary(project_root: str, project_type: str) -> str:
    return lint_summary_raw(project_root, project_type)
