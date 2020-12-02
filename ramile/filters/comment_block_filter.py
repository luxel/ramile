from ramile.processors import LineFilterBase


class CommentBlockFilterBase(LineFilterBase):
    """ Filtering out comment block """
    block_signs = {}

    def filter(self, file, line):
        if file.is_in_comment_block:
            file.found_comment_line()
            if self.close_comment_block(file, line):
                file.mark_comment_block_end()
            return line, True
        else:
            is_comment_block, comment_block_start_sign, comment_block_end_sign = self.is_comment_block(line)
            if is_comment_block:
                file.mark_comment_block_start(comment_block_end_sign)
                file.found_comment_line()
                line_tail = line[len(comment_block_start_sign):]
                if self.close_comment_block(file, line_tail):
                    file.mark_comment_block_end()
                return line, True
        return line, False

    def is_comment_block(self, line):
        """ determine whether current line starts a comment block

        :param line: current line
        :return is_comment_block: whether current line starts a comment block
        :return comment_block_end_sign: sign to close the comment block
        """
        for sign_start in self.block_signs.keys():
            if line.startswith(sign_start):
                return True, sign_start, self.block_signs[sign_start]
        return False, None, None

    def close_comment_block(self, file, line):
        return line.endswith(file.comment_block_end_sign)


class PythonCommentBlockFilter(CommentBlockFilterBase):
    """ Filtering out Python multi-line docstrings with \"\"\" and '''
    """
    block_signs = {
        '"""': '"""',
        "'''": "'''"
    }


class CStyleCommentBlockFilter(CommentBlockFilterBase):
    """ Filters out C-style comment blocks with '/*' and '*/'
    """
    block_signs = {
        '/*': '*/'
    }


class HtmlCommentBlockFilter(CommentBlockFilterBase):
    """ Filters out html comment blocks with '<!--' and '-->'
    """
    block_signs = {
        '<!--': '-->'
    }
