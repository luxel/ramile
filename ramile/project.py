from docx import Document
from ramile.project_info import ProjectInfo
from ramile.project_processor import ProjectProcessor
from ramile.processors import FileProcessor
import os


class Project(object):
    info = None
    output = True
    files = []

    def __init__(self, project_root, lines_to_extract=3000, output_file='extracted_code.docx', output=True):
        self.info = ProjectInfo(project_root, lines_to_extract)
        self.output = output
        if output:
            self.output_path = self.info.get_output_file_path(output_file)
            # self.output_file = open(
            # self.info.get_output_file_path(output_file), 'w+')
            self.output_file = Document(os.path.join(
                os.path.dirname(__file__), 'data/template.docx'))
            self.paragraph = None
        return

    def run(self, output=True, echo=True):
        if echo:
            print("I'm going to extract %s lines from %s." %
                  (self.info.lines_to_extract, self.info.project_root))
        self.info.lines_extracted = 0
        project_processor = ProjectProcessor(self.info)
        file_processor = FileProcessor()
        # 1. Process and collect the files
        self.files = project_processor.process()
        # 2. Process each file
        for file in self.files:
            for output in file_processor.process(file):
                self.export(output)
                file.extracted_line()
                if self.info.has_extracted_enough_lines():
                    break
            # collect file summary
            self.info.lines_skipped_blank += file.blank_lines
            self.info.lines_skipped_comments += file.comment_lines
            if self.info.has_extracted_enough_lines():
                break
        # self.output_file.close()
        print('current file = ', __file__)
        self.output_file.save(self.output_path)
        if echo:
            self.print_summary()

        if not self.info.has_extracted_enough_lines():
            print("Warning!! Not enough source code to extract %s lines!" %
                  self.info.lines_to_extract)
        return

    def print_summary(self):
        print("The extraction is done. Here's the summary:")
        print("%d files that contributed to the output:" % (len(self.files)))
        for file in self.files:
            if file.has_extracted_lines():
                print("%s : %s lines" % (file.file_path, file.extracted_lines))
        print("Code was extracted in: %s" % self.output_path)
        print("Total extracted: %s lines" % self.info.lines_extracted)
        print("Total skipped comments: %s lines" %
              self.info.lines_skipped_comments)
        print("Total skipped blank lines: %s lines" %
              self.info.lines_skipped_blank)

    def export(self, line):
        if self.output:
            # self.output_file.write(line)
            # if not line.endswith('\n'):
            #     self.output_file.write('\n')
            if self.paragraph is None:
                self.paragraph = self.output_file.paragraphs[0]
            self.paragraph.add_run(line)
        self.info.lines_extracted += 1
        return
