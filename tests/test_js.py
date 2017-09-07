import pytest
from ramile import *


def test_react_native_app():
    """ Test with react-native app project. cloc results:
    -------------------------------------------------------------------------------
Language                     files          blank        comment           code
-------------------------------------------------------------------------------
JavaScript                       1              6              6             21
-------------------------------------------------------------------------------
    """
    project = Project('data/js-react-native-app', 'test-output.txt')
    project.run()
    assert project.info.lines_extracted == 21
    assert project.info.lines_skipped_blank == 6
    assert project.info.lines_skipped_comments == 6
    return
