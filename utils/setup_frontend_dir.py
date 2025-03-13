import os 
import subprocess 
from constants import names 
import content

class SetUpFrontendDir:
    PROJECT_ROOT = os.getcwd()
    FRONTEND_DIR = os.path.join(PROJECT_ROOT, names.FRONTEND_DIR)

    def __init__(self):
        """Nothing to do here for now"""
        pass 

    def set_up_frontend_dir(self):
        self._setup_frontend_dir()

    def _setup_frontend_dir(self):
        print("📦 Creating frontend folder and initializing React ...")
        os.makedirs(self.FRONTEND_DIR, exist_ok=True)
        os.chdir(self.FRONTEND_DIR)
        print("✅ Folder frontend created successfully")