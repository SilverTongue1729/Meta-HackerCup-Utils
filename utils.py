import os
import shutil
import subprocess

def setup_problem_directory(downloads_path, year, round_name, problem_name):
    if not isinstance(year, str):
        year = str(year)
    if not year or not round_name:
        raise ValueError("Year and Round name must be provided.")

    cwd = os.getcwd()
    problem_dir = os.path.join(cwd, year, round_name, problem_name)
    os.makedirs(problem_dir, exist_ok=True)

    code_file_path = os.path.join(problem_dir, f"{problem_name}.cpp")
    if not os.path.exists(code_file_path):
        with open(code_file_path, 'w') as f:
            f.write("")

    return problem_dir

def setup_code_file(problem_dir, code_file):
    code_file_path = os.path.join(problem_dir, code_file)
    if not os.path.exists(code_file_path):
        raise FileNotFoundError(f"Code file {code_file_path} does not exist.")

    return code_file_path

def compile_code(code_file_path, compile_args):
    # Compile the code
    executable = os.path.splitext(code_file_path)[0]
    compile_command = ["g++"] + compile_args + [code_file_path, "-o", executable]
    subprocess.run(compile_command, check=True)

def execute_code(problem_dir, input_file, code_file_path, compile_args):
  executable = os.path.splitext(code_file_path)[0]
  if not os.path.exists(executable):
    compile(code_file_path, compile_args)
  
  input_file_path = os.path.join(problem_dir, input_file)
  output_file_name = input_file.replace("input", "output")
  output_file_path = os.path.join(problem_dir, output_file_name)

  with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
      subprocess.run([executable], stdin=infile, stdout=outfile)

def handle_validation_input(problem_dir, downloads_path, code_file_path, compile_args):
    # Define validation input file pattern
    validation_input_file = None
    for filename in os.listdir(problem_dir):
        if filename.endswith("_validation_input.txt"):
            validation_input_file = filename
            break

    # If not found, search and move from downloads path
    if not validation_input_file:
        for filename in os.listdir(downloads_path):
            if filename.endswith("_validation_input.txt"):
                shutil.move(os.path.join(downloads_path, filename), problem_dir)
                validation_input_file = filename
                break

    if not validation_input_file:
        print("Validation input file not found.")
        return

    execute_code(problem_dir, validation_input_file, code_file_path, compile_args)

def handle_final_input(problem_dir, downloads_path, code_file_path, password, compile_args):
    # Define final input file pattern
    final_input_file = None
    for filename in os.listdir(problem_dir):
        if filename.endswith("_input.txt") and not filename.endswith("_validation_input.txt"):
            final_input_file = filename
            break

    # If not found, search and move from downloads path and unzip
    if not final_input_file:
        zip_file_name = None
        for filename in os.listdir(downloads_path):
            if filename.endswith("_input.zip"):
                zip_file_name = filename
                break

        if zip_file_name:
            shutil.move(os.path.join(downloads_path, zip_file_name), problem_dir)
            zip_file_path = os.path.join(problem_dir, zip_file_name)

            # Unzip using 7zip
            unzip_command = ["7z", "x", f"-p{password}", zip_file_path, f"-o{problem_dir}"]
            subprocess.run(unzip_command, check=True)

            # Search for the final input file after unzipping
            for filename in os.listdir(problem_dir):
                if filename.endswith("_input.txt") and not filename.endswith("_validation_input.txt"):
                    final_input_file = filename
                    break

            if not final_input_file:
                print("Final input file not found after unzipping.")
                return
        else:
            print("Final input zip file not found in downloads path.")
            return

    execute_code(problem_dir, final_input_file, code_file_path, compile_args)