from unittest import TestCase

from approvaltests import verify

from GitDiff import GitDiff
from Refactoring import Refactoring


class TestRefactoring(TestCase):
    def test_harnesses_are_installed(self):
        obj = Refactoring()
        assert True
