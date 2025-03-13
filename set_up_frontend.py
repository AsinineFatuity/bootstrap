import os 
import subprocess 
from constants import names
import content 

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
        print("📦 Setting up webpack configuration files ...")
        os.makedirs(names.WEBPACK_DIR, exist_ok=True)
        os.chdir(names.WEBPACK_DIR)
        with open(names.WEBPACK_COMMON_CONFIG_FILE, "w") as webpack_common_file:
            webpack_common_file.write(content.WEBPACK_COMMON_CONTENT)
        print("✅ webpack.common.js file created successfully")
        with open(names.WEBPACK_DEV_CONFIG_FILE, "w") as webpack_dev_file:
            webpack_dev_file.write(content.WEBPACK_DEV_CONTENT)
        print("✅ webpack.dev.js file created successfully")
        with open(names.WEBPACK_PROD_CONFIG_FILE, "w") as webpack_prod_file:
            webpack_prod_file.write(content.WEBPACK_PROD_CONTENT)
        print("✅ webpack.prod.js file created successfully")
        print("✅ Webpack configuration files created successfully")
    
    def _setup_package_json_file(self):
        print("📦 Setting up package.json file and installing dependencies ...")
        with open(names.PACKAGE_JSON_FILE, "w") as package_json_file:
            package_json_file.write(content.PACKAGE_JSON_CONTENT)
        print("✅ package.json file created successfully")
        print("📦 Installing dependencies ...")
        subprocess.run(["npm", "install"])
        print("✅ Dependencies installed successfully")

frontend = SetUpFrontend()
frontend._setup_webpack_config_files()