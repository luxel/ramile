from ramile.processors import LineFilterBase


class CommentFilterBase(LineFilterBase):
    """ Filters out single line comments which start with '//'
    """
    comment_sign = None

    def filter(self, file, line):
        if line.startswith(self.comment_sign):
            file.found_comment_line()
            return line, True
        return line, False


class DoubleSlashCommentFilter(CommentFilterBase):
    """ Filters out single line comments which start with '//'
    """
    comment_sign = '//'


class SharpCommentFilter(CommentFilterBase):
    """ Filters out single line comments which start with '#'
    """
    comment_sign = '#'
