from ramile.filters.comment_block_filter import CStyleCommentBlockFilter
from ramile.filters.comment_filter import DoubleSlashCommentFilter
from ramile.processors import FileProcessorBase


class JavaProcessor(FileProcessorBase):
    expected_extensions = ['.java']

    def __init__(self):
        super().__init__()
        self.filters.append(CStyleCommentBlockFilter())
        self.filters.append(DoubleSlashCommentFilter())
        return
