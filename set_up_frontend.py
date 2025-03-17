import os
from constants import names
from utils import SetUpRootDir, SetUpFrontendDir


class SetUpFrontend:

    def __init__(self):
        self.project_root = os.getcwd()

    def set_up_frontend_project(self):
        root_dir = SetUpRootDir(self.project_root)
        root_dir.set_up_root_dir()
        frontend_dir = SetUpFrontendDir(self.project_root)
        frontend_dir.set_up_frontend_dir()


frontend = SetUpFrontend()
frontend.set_up_frontend_project()
