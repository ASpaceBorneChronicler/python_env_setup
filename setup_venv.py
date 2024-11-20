import os
import shutil
import subprocess
import argparse

def setup_venv(file_name):
    # Step 0: Make dir
    base_path = os.getcwd()
    new_path = os.path.join(base_path, file_name)
    print(new_path)
    if not os.path.exists(file_name):
        print(f"Creating directory: {file_name}")
        os.makedirs(file_name)
    else:
        print(f"Directory already exists: {file_name}")
    os.chdir(new_path)
    if not os.path.exists(file_name):
        print(f"Creating main.py in {new_path}")
        subprocess.run(["powershell", "-Command", "New-Item", "main.py"])
    
    # Step 1: Create the virtual environment
    venv_dir = ".venv"
    if not os.path.exists(venv_dir):
        print("Creating virtual environment...")
        subprocess.run(["python3", "-m", "venv", venv_dir], check=True)
    else:
        print("Virtual environment already exists.")

    # Step 2: Activate the virtual environment (platform-specific)
    activate_script = os.path.join(venv_dir, "Scripts", "activate") if os.name == "nt" else os.path.join(venv_dir, "bin", "activate")
    
    # Step 3: Open VS Code
    print(f"Opening {file_name} in VS Code...")

    try:
        subprocess.run(["powershell", "-Command" ,"code", f'"{new_path}"'], check=True)
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Subprocess error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")


    # Step 4: Notify user of activation command
    print("\nVirtual environment setup complete.")
    print(f"To activate the virtual environment, run:\nsource {activate_script}" if os.name != "nt" else f"{activate_script}")

def main():
    parser = argparse.ArgumentParser(description="Setup a virtual environment, open VS Code, and provide activation instructions.")
    parser.add_argument("fileName", help="The name of the file or folder to open in VS Code.")
    args = parser.parse_args()

    setup_venv(args.fileName)

if __name__ == "__main__":
    main()
