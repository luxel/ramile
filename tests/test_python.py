import pytest
from ramile import *


def test_file__init__():
    """ Test with __init__.py from fire project:
    -------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                       1              4            14                6
-------------------------------------------------------------------------------
    """
    project = Project('data/fire',
                      3000, 'test-output.docx')
    project.run()
    assert project.info.lines_extracted == 6
    assert project.info.lines_skipped_blank == 4
    assert project.info.lines_skipped_comments == 14
    return

def test_comments_startswith_linebreak():
    """ Test with python_module/settings.py:
-------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
Python                           1              4              7              3
-------------------------------------------------------------------------------
    """
    project = Project('data/python_module',
                      3000, 'test-output.docx')
    project.run()
    assert project.info.lines_extracted == 3
    assert project.info.lines_skipped_blank == 4
    assert project.info.lines_skipped_comments == 7

    return
