from unittest import TestCase

from approvaltests import verify

from GitDiff import GitDiff
from Refactoring import Refactoring


class TestRefactoring(TestCase):
    def test_harnesses_are_installed(self):
        obj = Refactoring("xx")
        assert True

    def test_implicit_stringify_displays_name(self):
        obj = Refactoring("Rename Variable")
        verify(obj)
