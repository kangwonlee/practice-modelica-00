import pathlib
import sys


import pytest


sys.path.append(str(pathlib.Path(__file__).parent.parent))


import check_ompython


def test__check_ompythion():
    check_ompython.check_ompythion()
    # could successfully run a few commands
    assert False


if "__main__" == __name__:
    pytest.main([__file__])
