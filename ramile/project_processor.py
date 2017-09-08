import os

from ramile.file_info import FileInfo
from ramile.processors import FileProcessor


class ProjectProcessor(object):

    def __init__(self, project):
        self.project = project
        self.files = []
        self.file_processor = FileProcessor()
        return

    def process(self):
        self.find_files()
        self.sort_files()
        return self.files

    def find_files(self):
        for root, dirs, files in os.walk(self.project.project_root):
            if self.is_ignored(root):
                continue
            for file_name in files:
                file_path = os.path.join(root, file_name)
                if self.is_ignored(file_path):
                    continue
                name, extension = os.path.splitext(file_name)
                if self.is_interested_file(name, extension):
                    info = FileInfo(file_path, file_name, extension)
                    self.files.append(info)
        return

    def walk(self):
        return

    def is_ignored(self, path):
        """ Checks whether the specified path is ignored.
        """
        for ignore in self.project.ignore:
            if path.startswith(ignore):
                return True
        return False

    def is_interested_file(self, filename, extension):
        return self.file_processor.has_interest(extension)

    def sort_files(self):
        return
