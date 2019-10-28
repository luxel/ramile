from ramile.filters.c_style_comment_block_filter import CStyleCommentBlockFilter
from ramile.filters.double_slash_comment_filter import DoubleSlashCommentFilter
from ramile.filters.html_comment_block_filter import HtmlCommentBlockFilter
from ramile.processors import FileProcessorBase


class PhpProcessor(FileProcessorBase):
    expected_extensions = ['.php']

    def __init__(self):
        super().__init__()
        self.filters.append(CStyleCommentBlockFilter())
        self.filters.append(DoubleSlashCommentFilter())
        self.filters.append(HtmlCommentBlockFilter())
        return
