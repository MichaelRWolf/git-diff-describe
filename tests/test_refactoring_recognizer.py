# test_refactoring_recognizer.py
from approvaltests import verify
# Import your RefactoringRecognizer class. Update the path as appropriate
from refactoring_recognizer import RefactoringRecognizer

refactoring_task_description = """
Task: infer_refactoring
Please analyze the following unified diff output to determine if any standard refactorings can be identified. 
If a refactoring is detected, name the refactoring and provide the relevant details, such as the functions or variables involved.

Do not provide explanations for refactoring names (e.g. rename variable, extract method).  
Assume theat the user will understand the names.  
But _do_ provide details about the refactoring like original identifier and new identifier.

Provide analysis in JSON format a required field named 'refactoring-name'.
Depending on the refactoring name, also report values for attributes listed below.
 
Many similar names are commonly used for a refactoring.  
When you report a refactoring, I would like to standardize the naming according to the groupings below.  
That is, the 'refactoring-name' field should have the value from 'preferred name', not a value from 'other common names'.


preferred name: rename function
other common names: rename method
attributes:
  - function name original
  - function name new
  
preferred name: rename variable
other common names: rename constant
attributes:
  - variable name original
  - variable name new
  
"""

def test_recognize_rename_one_variable():
    recognizer = RefactoringRecognizer()
    diff_output = """
    --- tests/diffs/lwh_original.py	2023-12-03 18:36:26
+++ tests/diffs/lwh_rename_one_variable.py	2023-12-03 18:37:47
@@ -6,5 +6,5 @@
     l = 3
     w = 4
     h = 5
-    vol = fn(l, w, h)
-    print vol
+    volume = fn(l, w, h)
+    print volume
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
