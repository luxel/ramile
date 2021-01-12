from ramile.processors import LineFilterBase


class BlankLineFilter(LineFilterBase):
    """ Filters out blank lines - lines with only spaces, tabs and line ends. It also strips the line for later processing.
    """

    def filter(self, file, line):
        stripped_line = line.strip(' \t\n')
        if stripped_line == '':
            file.found_blank_line()
            return stripped_line, True
        return stripped_line, False
