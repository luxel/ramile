import os.path
import json


class ProjectInfo(object):
    """Represents all the information for a project."""
    lines_to_extract = 3000
    project_root = ''
    lines_extracted = 0
    lines_skipped_comments = 0
    lines_skipped_blank = 0
    ignore = []

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
                if "ignore" in config_data:
                    self.ignore = config_data['ignore']
        return

    def has_extracted_enough_lines(self):
        return self.lines_extracted >= self.lines_to_extract

    def get_output_file_path(self, output_filename):
        return os.path.join(self.project_root, output_filename)
