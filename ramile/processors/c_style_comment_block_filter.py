from ramile.processors import LineFilterBase


class CStyleCommentBlockFilter(LineFilterBase):
    """ Filters out C-style comment blocks with '/*' and '*/'
    """

    def filter(self, file, line):
        if file.is_in_comment_block:
            file.found_comment_line()
            if line.endswith('*/'):
                file.mark_comment_block_end()
            return line, True
        else:
            if line.startswith('/*'):
                file.found_comment_line()
                file.mark_comment_block_start()
                if line.endswith('*/'):
                    file.mark_comment_block_end()
                return line, True
        return line, False
