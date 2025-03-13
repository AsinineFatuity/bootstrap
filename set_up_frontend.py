import os 
import subprocess 
from constants import names
from content import PACKAGE_JSON_CONTENT

class SetUpFrontend:
    PROJECT_ROOT = os.getcwd()
    FRONTEND_DIR = os.path.join(os.getcwd(), names.FRONTEND_DIR)
    FRONTEND_DIR = os.path.join(PROJECT_ROOT, names.FRONTEND_DIR)
    def __init__(self):
        """Nothing to do here for now"""
        pass 

    def set_up_frontend(self):
        print("📦 Creating frontend folder and initializing React ...")
        os.makedirs(self.FRONTEND_DIR, exist_ok=True)
        os.chdir(self.FRONTEND_DIR)
        print("✅ Folder frontend created successfully")
    
    def _setup_webpack_config_files(self):
        os.makedirs(names.WEBPACK_DIR, exist_ok=True)
        os.chdir(names.WEBPACK_DIR)
    
    def _setup_package_json_file(self):
        print("📦 Setting up package.json file and installing dependencies ...")
        with open(names.PACKAGE_JSON_FILE, "w") as package_json_file:
            package_json_file.write(PACKAGE_JSON_CONTENT)
        print("✅ package.json file created successfully")
        print("📦 Installing dependencies ...")
        subprocess.run(["npm", "install"])
        print("✅ Dependencies installed successfully")


frontend = SetUpFrontend()
frontend._setup_package_json_file()
