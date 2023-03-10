from ramile.processors import LineFilterBase


class CommentFilterBase(LineFilterBase):
    """ Filters out single line comments which start with '//'
    """
    comment_sign = None
    strip_endings = False

    def filter(self, file, line):
        if line.startswith(self.comment_sign):
            file.found_comment_line()
            return line, True
        if not line:
            return line, False
        if self.strip_endings:
            if self.comment_sign in line:
                return line[:line.index(self.comment_sign)], False
        return line, False


class DoubleSlashCommentFilter(CommentFilterBase):
    """ Filters out single line comments which start with '//'
    """
    comment_sign = '//'
    strip_endings = True


class SharpCommentFilter(CommentFilterBase):
    """ Filters out single line comments which start with '#'
    """
    comment_sign = '#'


class ColonCommentFilter(CommentFilterBase):
    """ Filters out single line comments which start with ':'
    """
    comment_sign = ':'
