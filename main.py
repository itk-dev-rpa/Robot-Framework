"""The main file of the robot which will install all requirements in
a virtual environment and then start the actual process.
"""

import subprocess
import os
import sys

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

# Install uv
subprocess.run([sys.executable, "-m", "pip", "install", "uv"], check=True)

# Create virtual environment
subprocess.run(["uv", "venv"], check=True)

# Install packages in the virtual environment
subprocess.run(["uv", "pip", "install", "."], check=True)

command_args = [r".venv\Scripts\python", "-m", "robot_framework"] + sys.argv[1:]

subprocess.run(command_args, check=True)
