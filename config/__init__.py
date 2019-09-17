import sys
import re
import os
from .cluster import *
from .file_organization import *
from .operation import *

# Create a configured environment
env = os.environ.copy()

# If the python package directory is not specified as an absolute path, prepend the current working directory to make it an absolute path
fixed_python_path = python_package_directory + ":" + os.getcwd()
if re.match("^/", fixed_python_path) is None:
    fixed_python_path = os.getcwd() + "/" + fixed_python_path

# If there is no PYTHONPATH environment variable, add ours
if "PYTHONPATH" not in env:
    env["PYTHONPATH"] = fixed_python_path

# Otherwise, prepend this custom python path to the list of python paths
else:
    env["PYTHONPATH"] = fixed_python_path + ":" + env["PYTHONPATH"]

# Create an environment variable pointing to the current project directory
env["PROJECT_DIRECTORY"] = os.getcwd()

from .steps import *
