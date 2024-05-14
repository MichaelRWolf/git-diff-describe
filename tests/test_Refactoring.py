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

    def test_extract_refactorings(self):
        refactoring_list = [
            Refactoring("Extract Variable", {"new_name" : "new_var"}),
            Refactoring("Extract Function", {"new_name": "new_fun"}),
            Refactoring("Extract Method", {"new_name": "new_meth"}),

            Refactoring("Extract Variable", {}),
        ]
        value = ''.join(map(lambda obj: str(obj) + '\n', refactoring_list))
        verify(value)

    def test_unknown_refactorings(self):
        verify(Refactoring("FindAndFixAllBugs", {"cost": 0, "value": 1000}))