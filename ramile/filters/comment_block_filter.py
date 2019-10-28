from ramile.processors import LineFilterBase


class CommentBlockFilter(LineFilterBase):
    """ Filters out everything - when the file is currently in a comment block.
    """

    def filter(self, file, line):
        if file.is_in_comment_block:
            file.found_comment_line()
            return line, True
        return line, False


class CommentBlockFilterBase(LineFilterBase):
    """ Filtering out comment block """

    def filter(self, file, line):
        if file.is_in_comment_block:
            file.found_comment_line()
            if self.close_comment_block(file, line):
                file.mark_comment_block_end()
            return line, True
        else:
            is_comment_block, comment_block_sign_end = self.is_comment_block(line)
            if is_comment_block:
                file.comment_block_sign_end = comment_block_sign_end
                file.mark_comment_block_start()
                file.found_comment_line()

                if self.close_comment_block(file, line):
                    file.mark_comment_block_end()
                return line, True
        return line, False

    def is_comment_block(self, line):
        """ determine whether current line starts a comment block

        :param line: current line
        :return is_comment_block: whether current line starts a comment block
        :return comment_block_sign_end: sign to close the comment block
        :raise NotImplementedError: every subclass should implement this method
        """
        raise NotImplementedError

    def close_comment_block(self, file, line):
        return line.endswith(file.comment_block_sign_end)


class PythonCommentBlockFilter(CommentBlockFilterBase):
    """ Filtering out Python multi-line docstrings with \"\"\" and '''
    """

    def is_comment_block(self, line):
        if line.startswith('"""'):
            return True, '"""'
        if line.startswith("'''"):
            return True, "'''"
        return False, None
