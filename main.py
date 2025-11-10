"""The main file of the robot which will install all requirements in
a virtual environment and then start the actual process.
"""

import subprocess
import os
import sys

script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

subprocess.run("pip install --upgrade uv", check=True)
command_args = ["uv", "run", "python", "-m", "robot_framework"] + sys.argv[1:]
subprocess.run(command_args, check=True)
