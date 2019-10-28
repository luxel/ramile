from ramile.filters.comment_filter import DoubleSlashCommentFilter

from ramile.filters.comment_block_filter import CStyleCommentBlockFilter, HtmlCommentBlockFilter
from ramile.processors import FileProcessorBase


class HtmlProcessor(FileProcessorBase):
    expected_extensions = ['.html', '.htm']

    def __init__(self):
        super().__init__()
        self.filters.append(CStyleCommentBlockFilter())
        self.filters.append(DoubleSlashCommentFilter())
        self.filters.append(HtmlCommentBlockFilter())
        return
