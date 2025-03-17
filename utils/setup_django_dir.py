import os
import content
from constants import names


class SetUpDjangoUrlsFile:
    def __init__(self, project_root: str):
        self.PROJECT_ROOT = project_root
        self.URLS_FILE = self._find_urls_file()

    def _find_urls_file(self):
        django_project_files = [names.DJANGO_ASGI_FILE, names.DJANGO_WSGI_FILE]
        for root, dirs, files in os.walk(self.PROJECT_ROOT):
            if any(file in files for file in django_project_files):
                return os.path.join(root, names.DJANGO_URLS_FILE)
        print(
            "❌ Django urls.py file not found, please create django project and try again"
        )
        return None

    def setup_django_urls_file(self):
        if self.URLS_FILE:
            print("📦 Setting up Django urls.py file ...")
            with open(self.URLS_FILE, "w") as urls_file:
                urls_file.write(content.DJANGO_URLS_CONTENT)
            print("✅ Django urls.py file created successfully")
