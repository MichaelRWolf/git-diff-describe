from unittest import TestCase

from approvaltests import verify

from GitDiff import GitDiff
from Refactoring import Refactoring


class TestRefactoring(TestCase):
    def test_harnesses_are_installed(self):
        obj = Refactoring("xx", attributes)
        assert True

    def test_implicit_stringify_displays_name(self):
        attributes = {'original_name': 'fn',
                      'new_name'     : 'file_name'}
        obj = Refactoring("Rename Variable", attributes)
        # value = f"{obj}\n    {attributes}"
        value = str(obj)
        verify(value)
