import os
import subprocess


def run_python_file(working_directory, file_path, args=[]):
    
    full_path = os.path.join(working_directory, file_path)
    abs_work = os.path.abspath(working_directory)
    abs_full = os.path.abspath(full_path)

    if not abs_full.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    if not os.path.commonpath([abs_work, abs_full]) == abs_work:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_full):
        return f'Error: File "{file_path}" not found.'
    
    try:
        completed = subprocess.run(["python", file_path, *args], cwd=abs_work, timeout=30, capture_output=True, text=True)
        out_line = f'STDOUT: {completed.stdout}'
        err_line = f'STDERR: {completed.stderr}'
        
        if completed.stdout.strip() == "" and completed.stderr.strip() == "":
            return "No output produced"
        lines = [out_line, err_line]
        if completed.returncode != 0:
            lines.append(f"Process exited with code {completed.returncode}")
        return "\n".join(lines)
        
    except Exception as e:
        return f"Error: executing Python file: {e}"