import os
from google.genai import types

def write_file(working_directory, file_path, content):
    
    full_path = os.path.join(working_directory, file_path)
    abs_work = os.path.abspath(working_directory)
    abs_full = os.path.abspath(full_path)

   
   
    if not abs_full.startswith(abs_work + os.sep):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
   
   
   
    dirpath = os.path.dirname(full_path)
    if dirpath != "":
        os.makedirs(dirpath, exist_ok=True) 
      
        
    try:
        with open(full_path, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f"Error: {e}"


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write a file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write/overwrite",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Contents of the file"
            ),
        },
        required=["file_path", "content"],
    ),
)