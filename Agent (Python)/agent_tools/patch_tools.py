import os
import tempfile
import subprocess
from pathlib import Path
import difflib
from agents import function_tool
import socket_service

def patch_generator_raw(
    source_path: str,
    original_source: str,
    lint_summary: str,
    instructions: str | None = None
) -> str:
    socket_service.emit_log(f"🛠️ Generating patch for: {source_path}", 'info')
    socket_service.emit_progress("Patch Generation", 0, 3, "Analyzing source code")
    
    new_source = original_source
    if instructions:
        socket_service.emit_log(f"📝 Processing instructions: {instructions[:100]}...", 'info')
        # Demo: append instruction as comment
        new_source = original_source + f"\n<!-- {instructions} -->\n"

    socket_service.emit_progress("Patch Generation", 1, 3, "Analyzing lint issues")

    if new_source == original_source:
        return ""

    diff = difflib.unified_diff(
        original_source.splitlines(),
        new_source.splitlines(),
        fromfile=source_path,
        tofile=source_path,
        lineterm=""
    )

    socket_service.emit_progress("Patch Generation", 2, 3, "Preparing patch template")
    socket_service.emit_progress("Patch Generation", 3, 3, "Patch template ready")
    socket_service.emit_log(f"✅ Patch template generated for {source_path}", 'success')
    
    return "\n".join(diff)

def apply_patch_raw(project_root: str, filename: str, diff: str) -> str:
    socket_service.emit_file_operation("patch", filename, "started")
    socket_service.emit_log(f"🔧 Applying changes to: {filename}", 'info')
    
    print(f"Applying patch to {filename}")
    
    diff_file = tempfile.NamedTemporaryFile(delete=False, mode="w", encoding="utf-8", suffix=".diff")
    diff_file.write(diff)
    diff_file.flush()
    diff_file.close()
    try:
        proc = subprocess.run(
            ["patch", "-p0", "-d", project_root, "--batch", diff_file.name],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )

        socket_service.emit_progress("File Update", 1, 3, f"Target file: {filename}")
    
        return proc.stdout + proc.stderr
    finally:
        os.unlink(diff_file.name)

def create_new_file_raw(project_root: str, path: str, content: str) -> str:
    socket_service.emit_file_operation("create", path, "started")
    socket_service.emit_log(f"📝 Creating new file: {path}", 'info')
    
    print(f"Creating new file: {path}")
    full = Path(project_root) / path
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(content, encoding="utf-8")

    socket_service.emit_progress("File Creation", 3, 3, "File creation complete")
    socket_service.emit_file_operation("create", path, "completed")
    socket_service.emit_log(f"✅ Successfully created file: {path}", 'success')
        
    return f"Created new file: {path}"

@function_tool
def patch_generator(source_path: str, original_source: str, lint_summary: str, instructions: str | None = None) -> str:
    return patch_generator_raw(source_path, original_source, lint_summary, instructions)

@function_tool
def apply_patch(project_root: str, filename: str, diff: str) -> str:
    return apply_patch_raw(project_root, filename, diff)

@function_tool
def create_new_file(project_root: str, path: str, content: str) -> str:
    return create_new_file_raw(project_root, path, content)
