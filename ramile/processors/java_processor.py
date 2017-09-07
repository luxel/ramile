from ramile.processors import FileProcessorBase
from ramile.processors import BlankLineFilter
from ramile.processors.c_style_comment_block_filter import CStyleCommentBlockFilter
from ramile.processors.double_slash_comment_filter import DoubleSlashCommentFilter


class JavaProcessor(FileProcessorBase):
    expected_extensions = ['.java']

    def __init__(self):
        self.filters.append(BlankLineFilter())
        self.filters.append(CStyleCommentBlockFilter())
        self.filters.append(DoubleSlashCommentFilter())
        return
