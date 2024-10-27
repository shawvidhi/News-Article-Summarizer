import os
from pathlib import Path
import logging

# Configure logging to provide timestamps and custom formatting for messages
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# Name of the project root directory
project_name = "textSummarizer"

# List of files and directories to create for the project
list_of_files = [
    ".github/workflows/.gitkeep",                          # For GitHub actions CI/CD pipeline
    f"src/{project_name}/__init__.py",                     # Initialize main package
    f"src/{project_name}/components/__init__.py",          # Sub-package for project components (e.g., models, pipelines)
    f"src/{project_name}/utils/__init__.py",               # Utilities module
    f"src/{project_name}/utils/common.py",                 # Common utility functions
    f"src/{project_name}/logging/__init__.py",             # Custom logging module
    f"src/{project_name}/config/__init__.py",              # Configurations package
    f"src/{project_name}/config/configuration.py",         # Configuration settings and loaders
    f"src/{project_name}/pipeline/__init__.py",            # Data processing and pipeline management
    f"src/{project_name}/entity/__init__.py",              # Entity definitions (e.g., data classes, schemas)
    f"src/{project_name}/constants/__init__.py",           # Project constants
    "config/config.yaml",                                  # Global configuration file
    "params.yaml",                                         # Parameters for training, hyperparameters, etc.
    "app.py",                                              # Application script
    "main.py",                                             # Entry point for execution
    "Dockerfile",                                          # Docker setup file for containerization
    "requirements.txt",                                    # Dependencies
    "setup.py",                                            # Project setup and installation
    "research/trials.ipynb",                               # Research and experimentation notebook
]

# Loop through each file path, creating directories and files as needed
for filepath in list_of_files:
    # Convert the filepath to a Path object for better path manipulation
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)  # Extract directory and file name

    # Create directories if they do not exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Created directory: {filedir} for the file {filename}")

    # Create a new file if it does not exist or if it's empty
    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, 'w') as f:
            pass  # Create an empty file
        logging.info(f"Created empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
