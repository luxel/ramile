from ramile.filters.comment_block_filter import CStyleCommentBlockFilter
from ramile.filters.comment_line_filter import DoubleSlashCommentFilter
from ramile.processors import FileProcessorBase


class CppProcessor(FileProcessorBase):
    expected_extensions = ['.cpp', '.c', 'h']

    def __init__(self):
        super().__init__()
        self.filters.append(DoubleSlashCommentFilter())
        self.filters.append(CStyleCommentBlockFilter())
