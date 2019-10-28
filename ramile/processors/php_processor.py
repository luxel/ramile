from ramile.filters.comment_filter import DoubleSlashCommentFilter

from ramile.filters.comment_block_filter import CStyleCommentBlockFilter, HtmlCommentBlockFilter
from ramile.processors import FileProcessorBase


class PhpProcessor(FileProcessorBase):
    expected_extensions = ['.php']

    def __init__(self):
        super().__init__()
        self.filters.append(CStyleCommentBlockFilter())
        self.filters.append(DoubleSlashCommentFilter())
        self.filters.append(HtmlCommentBlockFilter())
        return
