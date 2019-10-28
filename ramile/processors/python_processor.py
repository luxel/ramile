from ramile.filters.comment_block_filter import PythonCommentBlockFilter
from ramile.filters.sharp_comment_filter import SharpCommentFilter
from ramile.processors import FileProcessorBase


class PythonProcessor(FileProcessorBase):
    expected_extensions = ['.py', ]

    def __init__(self):
        super().__init__()
        self.filters.append(PythonCommentBlockFilter())
        self.filters.append(SharpCommentFilter())
