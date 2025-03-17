import os
import content
from constants import names


class SetUpFrontendDir:

    def __init__(self, project_root: str):
        self.PROJECT_ROOT = project_root
        self.FRONTEND_DIR = os.path.join(project_root, names.FRONTEND_DIR)

    def set_up_frontend_dir(self):
        self._setup_frontend_dir()

    def _setup_components_dir(self):
        print("📦 Setting up components folder ...")
        os.makedirs(names.COMPONENTS_DIR, exist_ok=True)
        os.chdir(names.COMPONENTS_DIR)
        with open(names.INDEX_TS_FILE, "w") as index_ts_file:
            index_ts_file.write(content.COMPONENTS_INDEX_TSX_CONTENT)
        with open(names.LOADING_INDICATOR_TSX_FILE, "w") as loading_indicator_tsx_file:
            loading_indicator_tsx_file.write(content.LOADING_INDICATOR_TSX_CONTENT)
        with open(names.FEEDBACK_TOAST_TSX_FILE, "w") as feedback_toast_tsx_file:
            feedback_toast_tsx_file.write(content.FEEDBACK_TOAST_TSX_CONTENT)
        print("✅ Folder components created successfully")
        os.chdir(self.FRONTEND_DIR)

    def _setup_src_dir(self):
        print("📦 Setting up src folder ...")
        os.makedirs(names.SRC_DIR, exist_ok=True)
        os.chdir(names.SRC_DIR)
        with open(names.INDEX_TS_FILE, "w") as index_ts_file:
            index_ts_file.write(content.INDEX_TSX_CONTENT)
        with open(names.APP_TSX_FILE, "w") as app_tsx_file:
            app_tsx_file.write(content.APP_TSX_CONTENT)
        print("✅ Folder src created successfully")
        os.chdir(self.FRONTEND_DIR)

    def _setup_frontend_dir(self):
        print("📦 Creating frontend folder and initializing React ...")
        os.makedirs(self.FRONTEND_DIR, exist_ok=True)
        os.chdir(self.FRONTEND_DIR)
        print("✅ Folder frontend created successfully")
