from ramile.filters.comment_block_filter import CStyleCommentBlockFilter
from ramile.filters.comment_line_filter import DoubleSlashCommentFilter
from ramile.processors import FileProcessorBase


class CssProcessor(FileProcessorBase):
    expected_extensions = ['.css', '.less', '.sass']

    def __init__(self):
        super().__init__()
        self.filters.append(CStyleCommentBlockFilter())
        self.filters.append(DoubleSlashCommentFilter())
        return
