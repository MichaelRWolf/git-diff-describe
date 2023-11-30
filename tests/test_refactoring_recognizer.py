# test_refactoring_recognizer.py
from approvaltests import verify
# Import your RefactoringRecognizer class. Update the path as appropriate
from refactoring_recognizer import RefactoringRecognizer


def test_recognize_diff_output():
    recognizer = RefactoringRecognizer()
    diff_output = """
    --- a/original_file.py
    +++ b/updated_file.py
    @@ -1,4 +1,4 @@
    -def some_function():
    +def some_renamed_function():
         pass
    """
    output = ""

    output += "# Diff output\n"
    output += diff_output

    output += "\n\n"

    output += "# Result\n"
    output += recognizer.recognize(diff_output)

    verify(output)
