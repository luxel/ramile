import io


class FileProcessorBase(object):
    """ Base class for file processors. The processor for each lanuage should inherit from this class.
    """
    expected_extensions = []

    def __init__(self):
        # by default, processors of all languages will always starts with a blank line filter
        self.filters = []
        self.filters.append(BlankLineFilter())
        return

    def is_interested_in(self, extension):
        """ Checks whether the filter is interested in the provided file extension.
        """
        for expected in self.expected_extensions:
            if expected == extension:
                return True
        return False

    def process(self, file):
        """ Processes a file and extracts lines out of it.
        """
        with io.open(file.file_path, 'r', encoding='utf-8') as open_file:
            last_line = None
            for original_line in open_file:
                if self.process_line(file, original_line):
                    yield original_line
                    last_line = original_line
        return

    def process_line(self, file, line):
        """ Processes a line, returns true if the line should be extracted.
        """
        for filter in self.filters:
            line, dropped = filter.filter(file, line)
            if dropped:
                return False
        return True

    def add_filter(self, filter):
        self.filters.append(filter)
        return


class LineFilterBase(object):
    """ A filter will process each line, and determine whether each line should be dropped. A filter can also perform any neccessary process on the line and replace the original line.
    """

    def filter(self, file, line):
        """ Filters a line of code, outputs the filtered content, and a flag whether the line should be dropped.
        """
        return line, False


class FileProcessor(object):

    def __init__(self):
        self.processors = {}
        self.__build_processors()
        return

    def print_processors(self):
        return list(self.processors.keys())

    def has_interest(self, extension):
        return extension in self.processors

    def process(self, file):
        processor = self.__get_cached_processor(file.file_extension)
        for output in processor.process(file):
            yield output

    def __build_processors(self):
        """ Register and cache all supported file processors.
        """
        self.__cache_processor(JsProcessor())
        self.__cache_processor(JavaProcessor())
        self.__cache_processor(PhpProcessor())
        self.__cache_processor(HtmlProcessor())
        self.__cache_processor(CssProcessor())
        self.__cache_processor(SwiftProcessor())
        self.__cache_processor(OCProcessor())
        self.__cache_processor(PythonProcessor())
        self.__cache_processor(CppProcessor())
        self.__cache_processor(JsonProcessor())
        self.__cache_processor(BatchProcessor())
        self.__cache_processor(GoProcessor())
        return

    def __get_cached_processor(self, extension):
        return self.processors[extension]

    def __cache_processor(self, processor):
        if len(processor.expected_extensions) > 0:
            for extension in processor.expected_extensions:
                self.processors[extension] = processor
        return


from ramile.filters.blank_line_filter import BlankLineFilter
from ramile.processors.js_processor import JsProcessor
from ramile.processors.java_processor import JavaProcessor
from ramile.processors.php_processor import PhpProcessor
from ramile.processors.html_processor import HtmlProcessor
from ramile.processors.css_processor import CssProcessor
from ramile.processors.swift_processor import SwiftProcessor
from ramile.processors.oc_processor import OCProcessor
from ramile.processors.python_processor import PythonProcessor
from ramile.processors.cpp_processor import CppProcessor
from ramile.processors.json_processor import JsonProcessor
from ramile.processors.bat_processor import BatchProcessor
from ramile.processors.go_processor import GoProcessor
