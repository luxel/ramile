class FileInfo(object):
    file_name = ''
    file_extension = ''
    file_path = ''
    is_in_comment_block = False
    blank_lines = 0
    comment_lines = 0
    extracted_lines = 0

    def __init__(self, file_path, file_name, file_extension):
        self.file_path = file_path
        self.file_extension = file_extension
        self.file_name = file_name
        return

    def has_extracted_lines(self):
        return self.extracted_lines > 0

    def extracted_line(self):
        self.extracted_lines += 1
        return

    def found_blank_line(self):
        self.blank_lines += 1
        return

    def found_comment_line(self):
        self.comment_lines += 1
        return

    def mark_comment_block_start(self):
        self.is_in_comment_block = True
        return

    def mark_comment_block_end(self):
        self.is_in_comment_block = False
        return
