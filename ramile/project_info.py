import os.path
import json


class ProjectInfo(object):
    """Represents all the information for a project.

    Attributes:
        source_root     Root directory of the source code folder for parsing.
    """
    lines_to_extract = 3000
    project_root = ''
    source_root = ''
    lines_extracted = 0
    lines_skipped_comments = 0
    lines_skipped_blank = 0
    ignore = []
    filters = []

    def __init__(self, project_root):
        self.project_root = project_root
        self.parse_config()
        return

    def parse_config(self):
        """ Try to parse .ramileconfig.json file from the project root.
        """
        config_file = os.path.join(self.project_root, '.ramileconfig.json')
        if os.path.exists(config_file):
            with open(config_file, 'r') as file:
                config_data = json.load(file)
                print(config_data)
                self.__set_config_ignore(config_data)
                self.__set_config_root(config_data)
                self.__set_config_filters(config_data)
        if self.source_root == '':
            self.source_root = self.project_root
        return

    def __set_config_filters(self, config_data):
        if 'filters' in config_data:
            self.filters = config_data['filters']

    def __set_config_root(self, config_data):
        if 'source_root' in config_data:
            self.source_root = os.path.join(
                self.project_root, config_data['source_root'])

    def __set_config_ignore(self, config_data):
        if "ignore" in config_data:
            ignores = config_data['ignore']
            for ignore in ignores:
                self.ignore.append(os.path.join(self.source_root, ignore))
            print(self.ignore)

    def has_extracted_enough_lines(self):
        return self.lines_extracted >= self.lines_to_extract

    def get_output_file_path(self, output_filename):
        return os.path.join(self.project_root, output_filename)
