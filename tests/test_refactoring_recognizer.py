# test_refactoring_recognizer.py
import json

from approvaltests import verify
# Import your RefactoringRecognizer class. Update the path as appropriate
from refactoring_recognizer import RefactoringRecognizer


def canonical_json_string(non_canonical_string):
    # Convert the Python dictionary to a canonical JSON string with sorted keys
    # and an indentation of 4 spaces.
    # data = json.loads(non_canonical_string)
    # canonical_string = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
    return non_canonical_string


refactoring_task_description = """
# Task: infer_refactoring

Analyze the following output provided in 'unified diff' format
Determine if any standard software code refactorings can be identified. 
If a refactoring is detected, provide output including
  - preferred refactoring name
  - attributes specific to this refactoring
  
Assume that the user will understand common refactorings, so do not provide explanations for them.

# Preferred refactoring name(s)
Many similar names are commonly used for a refactoring.  
When you report a refactoring, use 'preferred name' below instead of one of the 'alternate names'.

Further describe the refactoring by providing the attributes listed for each refactoring.

Provide additional attributes if you think they are necessary.

- preferred_name: Rename Variable
  alternate_names:
    - Rename Identifier
  attributes:
    - original_name
    - new_name

- preferred_name: Rename Function
  alternate_names:
    - Rename Method
  attributes:
    - original_name
    - new_name

- preferred_name: Extract Method
  alternate_names:
    - Extract Function
    - Extract Procedure
  attributes:
    - new_name

- preferred_name: Move Method
  alternate_names:
    - Move Function
    - Move Procedure

- preferred_name: Extract Class
  alternate_names:
    - Extract Module

- preferred_name: Change Signature
  alternate_names:
    - Modify Function Signature

- preferred_name: Replace Conditional with Polymorphism
  alternate_names:
    - Replace Conditional with Inheritance

# Formt
Output YAML format.  
  - Do output quotes around values when they are not necessary.
  - Do not put blank lines between items in an array (or list)
  - Even if there is only one refacoring, output it as a list (with one element)

For each refactoring, output these fields.
 - refactoring_name - Use the preferred name, not alternate names
 - [attributes] - See below for suggested attributes based on 'refactoring-name'.
     Do not output 'attributes' as a collection for attributes.  
     Simply place the attributes at the same level as 'refactoring_name'.
 - [other] - if you feel that other information would be necessary to categorize the refactoring
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
    output += str(recognizer.analysis())

    output += "\n\n"

    output += "# __str__\n"
    output += str(recognizer)

    verify(output)


def test_recognize_rename_three_variables():
    recognizer = RefactoringRecognizer()
    diff_output = """
--- tests/diffs/lwh_original.py	2023-12-03 18:36:26
+++ tests/diffs/lwh_rename_three_variables.py	2023-12-03 19:09:18
@@ -3,8 +3,8 @@
     return value
 
 def main():
-    l = 3
-    w = 4
-    h = 5
-    vol = fn(l, w, h)
+    length = 3
+    width = 4
+    height = 5
+    vol = fn(length, width, height)
     print vol
"""
    recognizer.add_task(refactoring_task_description)
    recognizer.add_diff(diff_output)

    output = ""

    recognizer.chatGPT_prompt_and_return()

    output += "# Result\n"
    output += canonical_json_string(recognizer.analysis())

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
    output += canonical_json_string(recognizer.analysis())

    output += "\n\n"

    output += "# __str__\n"
    output += str(recognizer)

    verify(output)
