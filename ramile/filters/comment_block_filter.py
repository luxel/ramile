from ramile.processors import LineFilterBase


class CommentBlockFilter(LineFilterBase):
    """ Filters out everything - when the file is currently in a comment block.
    """

    def filter(self, file, line):
        if file.is_in_comment_block:
            file.found_comment_line()
            return line, True
        return line, False
