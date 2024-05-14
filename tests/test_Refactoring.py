from unittest import TestCase

from approvaltests import verify

from Refactoring import Refactoring


class TestRefactoring(TestCase):
    def test_implicit_stringify_displays_name_and_attributes(self):
        attributes = {'original_name': 'fn',
                      'new_name': 'file_name'}
        obj = Refactoring("Rename Variable", attributes)
        value = str(obj)
        verify(value)

    def test_rename_refactorings(self):
        rename_variable = Refactoring("Rename Variable",
                                      {"original_name": "maxSpd",
                                       "new_name": "speedMax"});
        rename_method = Refactoring("Rename Method",
                                      {"original_name": "m1",
                                       "new_name": "mach1"});
        rename_class = Refactoring("Rename Class",
                                      {"original_name": "FastCar",
                                       "new_name": "WayOutOfHere"});

        value = ''.join(map(lambda obj: str(obj) + '\n',
                            [rename_variable, rename_method, rename_class]))

        verify(value)
