import os
from pathlib import Path
from agents import function_tool
import socket_service

IGNORED_TOPDIRS = {
    "node_modules", "venv", "__pycache__", ".git", "dist", "build", "env", ".venv", ".next", ".vite"
}

def read_dir_tree_raw(project_root: str) -> dict[str, list[str]]:
    socket_service.emit_log(f"📂 Starting directory tree analysis for: {project_root}", 'info')
    print(f"Reading directory tree...")

    tree: dict[str, list[str]] = {}
    for dirpath, dirnames, filenames in os.walk(project_root):
        rel = os.path.relpath(dirpath, project_root)
        parts = rel.split(os.sep)
        if parts and parts[0] in IGNORED_TOPDIRS:
            dirnames[:] = []
            continue
        dirnames[:] = [d for d in dirnames if d not in IGNORED_TOPDIRS]
        reldir = "" if rel == "." else rel
        tree.setdefault(reldir, []).extend(filenames)

    socket_service.emit_log(f"✅ Directory analysis complete: {len(tree)} directories", 'success')

    return tree

def read_file_raw(path: str) -> str:
    socket_service.emit_file_operation("read", path, "started")
    socket_service.emit_log(f"📖 Reading file: {path}", 'info')
    print(f"Reading file: {path}")

    with open(path, "r", encoding="utf-8", errors="replace") as f:
        socket_service.emit_file_operation("read", path, "completed")
        socket_service.emit_log(f"✅ Successfully read file: {path}", 'success')
        
        return f.read()

@function_tool
def read_dir_tree(project_root: str) -> dict[str, list[str]]:
    return read_dir_tree_raw(project_root)

@function_tool
def read_file(path: str) -> str:
    return read_file_raw(path)
