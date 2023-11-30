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
    task = """
    You are a code analysis tool.  You will analyze code changes to determine if standeard refactorings have been performed.
    """

    recognizer.add_task(task)
    recognizer.add_diff(diff_output)

    output = ""

    output += "# Result\n"
    output += recognizer.analysis()

    output += "\n\n"

    output += "# __str__\n"
    output += str(recognizer)

    verify(output)
