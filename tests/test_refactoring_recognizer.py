# test_refactoring_recognizer.py
from approvaltests import verify
# Import your RefactoringRecognizer class. Update the path as appropriate
from refactoring_recognizer import RefactoringRecognizer


def test_recognize_rename_method():
    recognizer = RefactoringRecognizer()
    diff_output = """
    --- a/original_file.py
    +++ b/updated_file.py
    @@ -1,4 +1,4 @@
    -def some_function():
    +def some_renamed_function():
         pass
    """
    refactoring_task_description = """
Task: infer_refactoring
Please analyze the following unified diff output to determine if any standard refactorings can be identified. 
If a refactoring is detected, name the refactoring and provide the relevant details, such as the functions or variables involved.

Do not provide explanations for refactoring names (e.g. rename variable, extract method).  
Assume theat the user will understand the names.  
But _do_ provide details about the refactoring like original identifier and new identifier.

Provide analysis in JSON format with fields like 'refactoring name', 'variable mame - original', 'variable name - new'.
    """

    recognizer.add_task(refactoring_task_description)
    recognizer.add_diff(diff_output)

    output = ""

    recognizer.chatGPT_prompt_and_return()

    output += "# Result\n"
    output += recognizer.analysis()\

    output += "\n\n"

    output += "# __str__\n"
    output += str(recognizer)

    verify(output)
