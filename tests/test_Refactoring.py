from shlex import join
from unittest import TestCase

from approvaltests import verify

from GitDiff import GitDiff
from Refactoring import Refactoring


class TestRefactoring(TestCase):
    def test_harnesses_are_installed(self):
        obj = Refactoring("xx", attributes)
        assert True

    def test_implicit_stringify_displays_name_and_attributes(self):
        attributes = {'original_name': 'fn',
                      'new_name': 'file_name'}
        obj = Refactoring("Rename Variable", attributes)
        value = str(obj)
        verify(value)

    def test_rename_refactorings(self):
        rename_variable = Refactoring("Rename Variable",
                                      {"original_name": "maxSpeed",
                                       "new_name": "speedMax"});

        rename_method = Refactoring("Rename Method",
                                      {"original_name": "m1",
                                       "new_name": "mach1"});
        rename_class = Refactoring("Rename Class",
                                      {"original_name": "FastCar",
                                       "new_name": "WayOutOfHere"});


        value = ''.join( [str(rename_variable)+"\n", str(rename_method)+"\n", str(rename_class)+"\n"])
        verify(value)
