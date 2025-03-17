import os
import subprocess
from constants import names
import content
from utils import SetUpRootDir


class SetUpFrontend:
    PROJECT_ROOT = os.getcwd()
    FRONTEND_DIR = os.path.join(os.getcwd(), names.FRONTEND_DIR)
    FRONTEND_DIR = os.path.join(PROJECT_ROOT, names.FRONTEND_DIR)

    def __init__(self):
        """Nothing to do here for now"""
        pass

    def set_up_frontend_project(self):
        root_dir = SetUpRootDir(self.PROJECT_ROOT)
        root_dir.set_up_root_dir()


frontend = SetUpFrontend()
frontend.set_up_frontend_project()
