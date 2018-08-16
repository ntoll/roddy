# -*- coding: utf-8 -*-
"""
Tests for the module __init__ file.
"""
from unittest import mock
import roddy


def test_version():
    """
    There should be a version associated with roddy.
    """
    assert roddy.__version__


def test_run():
    """
    There should be a place holder message when the command is run.
    """
    with mock.patch('builtins.print') as mock_p:
        roddy.run()
    mock_p.assert_called_once_with('TBD ;-)')
