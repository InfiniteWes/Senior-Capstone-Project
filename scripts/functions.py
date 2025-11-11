from prompt_toolkit import prompt
from prompt_toolkit.completion import PathCompleter
import os


def inputFile(oldFile,oldFileName):
    completer = PathCompleter(only_directories=False, expanduser=True)  # tab-completion for files/folders

    while True:
        path = prompt("Enter path to network log file (.csv) (H for Help Menu): ",completer=completer).strip()
        path = path.replace("\\", "/")

        if path.lower() == 'h':
            print('C: Cancel')
            print('ls: Look in dir')
            print('cd: Change dir')
            print('mkdir: Make new dir')
            continue

        if path.lower() == 'c':
            return oldFile, oldFileName

        if path.lower() == 'ls':
            print("\n".join(os.listdir(".")))
            continue

        if path.lower().startswith("cd "):
            new_dir = path[3:].strip()
            try:
                os.chdir(new_dir)
                print(f"Changed directory to {os.getcwd()}")
            except FileNotFoundError:
                print(f"Directory '{new_dir}' not found.")
            continue

        if path.lower().startswith("mkdir "):
            new_dir = path[6:].strip()
            try:
                os.makedirs(new_dir, exist_ok=True)
                print(f"Directory '{new_dir}' created.")
            except Exception as e:
                print(f"Could not create directory: {e}")
            continue

        if not path.lower().endswith(".csv"):
            print("Invalid file type. Please enter a CSV file.")
            continue

        try:
            if oldFile is not None:
                confirm = input(f"'{oldFileName}' is already loaded. Overwrite? (Y/N): ").strip().lower()
                if confirm != 'y':
                    continue
            with open(path, 'r') as f:
                file = f.read()
                fileName = path.split('/')[-1]
                print(f"File '{fileName}' uploaded successfully.")
                return file, fileName
        except FileNotFoundError:
            print("File not found. Please try again.")
