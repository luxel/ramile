from ramile.filters.comment_block_filter import CStyleCommentBlockFilter
from ramile.filters.comment_line_filter import DoubleSlashCommentFilter
from ramile.processors import FileProcessorBase


class SwiftProcessor(FileProcessorBase):
    expected_extensions = ['.swift']

    def __init__(self):
        super().__init__()
        self.filters.append(CStyleCommentBlockFilter())
        self.filters.append(DoubleSlashCommentFilter())
        return
