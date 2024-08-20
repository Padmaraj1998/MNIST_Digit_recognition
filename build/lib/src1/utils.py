import sys
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Calculate the project root directory (one level up from src1)
project_root = os.path.abspath(os.path.join(script_dir, '..'))

# Add the project root directory to PYTHONPATH
sys.path.append(project_root)

# Change the working directory to the project root
os.chdir(project_root)

# Print the current working directory and PYTHONPATH for verification
print(f"Current working directory: {os.getcwd()}")
print(f"PYTHONPATH: {sys.path}")

# Import modules
try:
    from src1 import exception
    from src1.exception import CustomException
    print("Imports successful.")
except ModuleNotFoundError as e:
    print(f"Import failed: {e}")
