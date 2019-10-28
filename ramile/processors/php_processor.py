from ramile.filters.comment_block_filter import CStyleCommentBlockFilter, HtmlCommentBlockFilter
from ramile.filters.comment_line_filter import DoubleSlashCommentFilter
from ramile.processors import FileProcessorBase


class PhpProcessor(FileProcessorBase):
    expected_extensions = ['.php']

    def __init__(self):
        super().__init__()
        self.filters.append(CStyleCommentBlockFilter())
        self.filters.append(DoubleSlashCommentFilter())
        self.filters.append(HtmlCommentBlockFilter())
        return
