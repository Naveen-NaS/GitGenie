import os
import asyncio
from agents import Agent, Runner
from agent_tools.file_tools import read_dir_tree, read_file
from agent_tools.lint_tools import lint_summary
from agent_tools.patch_tools import patch_generator, apply_patch, create_new_file
from agent_tools.logging_tools import log_action
import socket_service

def build_orchestrator():
    return Agent(
        name="SessionOrchestrator",
        instructions=(
            "You are an automated project fixer. "
            "You have FULL permission to directly modify files, create new files, and apply changes. "
            "Never ask for confirmation. "
            "\nWorkflow:\n"
            "1. Use read_dir_tree to analyze the project.\n"
            "2. Detect project type (python/node/html/etc).\n"
            "3. Run lint_summary to find issues.\n"
            "4. For each file with issues, generate a patch with patch_generator and immediately apply it with apply_patch.\n"
            "5. If user_instruction exists, generate & apply the required changes without asking.\n"
            "6. Use create_new_file if new files are needed.\n"
            "7. Call log_action after each applied change.\n"
            "8. Summarize: project type, issues fixed, user changes, and log file path."
        ),
        tools=[
            read_dir_tree,
            read_file,
            lint_summary,
            patch_generator,
            apply_patch,
            create_new_file,
            log_action
        ],
    )

async def run_session_async(project_root: str, session_id: str, user_instruction: str | None = None):
    socket_service.emit_log("🤖 Initializing Session Orchestrator", 'info')
    orchestrator = build_orchestrator()

    socket_service.emit_log(f"🎯 Session ID: {session_id}", 'info')
    socket_service.emit_log(f"📁 Project Root: {project_root}", 'info')

    input_text = (
        f"project_root={project_root}\n"
        f"session_id={session_id}\n"
        f"user_instruction={user_instruction or 'None'}"
    )

    socket_service.emit_log("🚀 Starting agent execution...", 'info')
    socket_service.emit_progress("Session Execution", 0, 1, "Running orchestrator agent")

    result = await Runner.run(starting_agent=orchestrator, input=input_text, max_turns=50)

    socket_service.emit_progress("Session Execution", 1, 1, "Agent execution completed")
    socket_service.emit_log("✅ Session orchestrator completed successfully", 'success')    

    return result.final_output


def run_session(project_root: str, session_id: str, user_instruction: str | None = None):
    return asyncio.run(run_session_async(project_root, session_id, user_instruction))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Run project analyzer and auto-fixer.")
    parser.add_argument("--project-root", "-r", required=True, help="Path to project folder")
    parser.add_argument("--session-id", "-s", required=True, help="Unique session identifier")
    parser.add_argument("--user-instruction", "-u", help="Optional free-form instruction")
    args = parser.parse_args()
    print(run_session(args.project_root, args.session_id, args.user_instruction))
