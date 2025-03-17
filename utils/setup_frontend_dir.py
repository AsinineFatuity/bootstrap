import os 
import content
from constants import names 

class SetUpFrontendDir:

    def __init__(self, project_root:str):
        self.PROJECT_ROOT = project_root 
        self.FRONTEND_DIR = os.path.join(project_root, names.FRONTEND_DIR)


    def set_up_frontend_dir(self):
        self._setup_frontend_dir()
    
    def _setup_src_dir(self):
        print("📦 Setting up src folder ...")
        os.makedirs(names.SRC_DIR, exist_ok=True)
        os.chdir(names.SRC_DIR)
        with open(names.INDEX_TS_FILE, "w") as index_ts_file:
            index_ts_file.write(content.INDEX_TSX_CONTENT)
        with open(names.APP_TSX_FILE, "w") as app_tsx_file:
            app_tsx_file.write(content.APP_TSX_CONTENT)
        print("✅ Folder src created successfully")

    def _setup_frontend_dir(self):
        print("📦 Creating frontend folder and initializing React ...")
        os.makedirs(self.FRONTEND_DIR, exist_ok=True)
        os.chdir(self.FRONTEND_DIR)
        print("✅ Folder frontend created successfully")