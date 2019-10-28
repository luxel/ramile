from ramile.processors import LineFilterBase


class DoubleSlashCommentFilter(LineFilterBase):
    """ Filters out single line comments which start with '//'
    """

    def filter(self, file, line):
        if line.startswith('//'):
            file.found_comment_line()
            return line, True
        return line, False
