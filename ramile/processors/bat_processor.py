#! /usr/bin/env python
#
# Copyright 2021 eVision.ai Inc. All Rights Reserved.
#
# @author: Chen Shijiang(chenshijiang@evision.ai)
# @date: 2021-01-04 19:53
# @version: 1.0
#
from ramile.filters.comment_line_filter import ColonCommentFilter, SharpCommentFilter
from ramile.processors import FileProcessorBase


class BatchProcessor(FileProcessorBase):
    expected_extensions = ['.bat', '.cmd']

    def __init__(self):
        super().__init__()
        self.filters.append(SharpCommentFilter())
        self.filters.append(ColonCommentFilter())
        return
