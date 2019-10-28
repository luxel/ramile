from ramile.filters.comment_block_filter import CStyleCommentBlockFilter
from ramile.filters.double_slash_comment_filter import DoubleSlashCommentFilter
from ramile.processors import FileProcessorBase


class OCProcessor(FileProcessorBase):
    expected_extensions = ['.m']

    def __init__(self):
        super().__init__()
        self.filters.append(CStyleCommentBlockFilter())
        self.filters.append(DoubleSlashCommentFilter())
        return
