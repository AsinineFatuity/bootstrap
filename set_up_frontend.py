import os 
import subprocess 
from constants import names
# Get current working directory
PROJECT_ROOT = os.getcwd() 

# Define Frontend Paths
FRONTEND_DIR = os.path.join(PROJECT_ROOT, names.FRONTEND_DIR)

def set_up_frontend():
    # Create directory if it doesn't exist
    os.makedirs(FRONTEND_DIR, exist_ok=True)
    # Change directory to frontend
    os.chdir(FRONTEND_DIR)
