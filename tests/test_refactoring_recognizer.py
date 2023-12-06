# test_refactoring_recognizer.py
import re
import subprocess

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

# Format
Generate YAML output for refactoring actions.
Output the YAML directly.
 - Do not preface the YAML with the string literal "yaml".
 - Do not display it in a text box.
 - Do not surround it with multi-line quotes.
Ensure that string values are enclosed in double quotes only when necessary.
Quotes are optional around values that contain only letters, numbers, and underscores.
Avoid adding optional quotes.
Do not add quotes around values that contain only letters, numbers, and underscores.
Ensure that there are no optional blank lines between elements in the YAML output.

In the following example, notice that these values are not surrounded by quotes
 - c
 - city
 - s
 - state
 - z
 - zip_code


Also notice that there is not a blank line separating the items with new name: city, state, zip_code.
These items are adjacent with no separation.

Example:
- refactoring_name: Rename Variable
  original_name: c
  new_name: city
- refactoring_name: Rename Variable
  original_name: s
  new_name: state
- refactoring_name: Rename Variable
  original_name: z
  new_name: zip_code


For each refactoring, output these fields.
 - refactoring_name - Use the preferred name, not alternate names
 - [attributes] - See below for suggested attributes based on 'refactoring-name'.
     Do not output 'attributes' as a collection for attributes.
     Simply place the attributes at the same level as 'refactoring_name'.
 - [other] - if you feel that other information would be necessary to categorize the refactoring
"""
# 1
# pattern = r'\s+(?=\n)'

# 2 Define a regular expression pattern to match trailing whitespace before a newline
# on lines with non-whitespace characters
# pattern = r'(?<=\S)\s+(?=\n)'

# 3 Define a regular expression pattern to match trailing whitespace before a newline
# on lines with non-whitespace characters
pattern = r'(?<=\S)([ \t]+)(?=\n)'
refactoring_task_description = re.sub(pattern, '', refactoring_task_description)


def run_recognizer(diff_output):
    recognizer = RefactoringRecognizer()
    recognizer.add_task(refactoring_task_description)
    recognizer.add_diff(diff_output)
    output = ""
    recognizer.chatGPT_prompt_and_return()
    output += "# subprocess\n"
    output += recognizer.subprocess_info()
    output += "\n\n"
    output += "# Result\n"
    output += str(recognizer.analysis())
    output += "\n\n"
    output += "# __str__\n"
    output += str(recognizer)
    return output


def return_diff_u_r(filename1, filename2):
    command = ['diff', '-u', '-r', filename1, filename2]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True,
                            check=False)
    return result.stdout


def test_recognize_rename_one_variable():
    diff_output = return_diff_u_r("tests/diffs/lwh_original.py",
                                  "tests/diffs/lwh_rename_one_variable.py")
    output = run_recognizer(diff_output)
    verify(output)


def test_recognize_rename_three_variables():
    diff_output = return_diff_u_r("tests/diffs/lwh_original.py",
                                  "tests/diffs/lwh_rename_three_variables.py")
    output = run_recognizer(diff_output)
    verify(output)


def test_extract_function():
    diff_output = return_diff_u_r("tests/diffs/lwh_pre_extract_function.py",
                                  "tests/diffs/lwh_original.py")
    output = run_recognizer(diff_output)
    verify(output)


def test_recognize_rename_method():
    diff_output = """
    --- a/original_file.py
    +++ b/updated_file.py
    @@ -1,4 +1,4 @@
    -def some_function():
    +def some_renamed_function():
         pass
    """
    output = run_recognizer(diff_output)
    verify(output)


def test_hello():
    # verify("Hello", options=Options().with_reporter(report_with_beyond_compare()))
    # verify("Hello", reporter=DiffReporter())
    verify("Hello")


def test_file_differ_for_rename_one_variable():
    diff_output = return_diff_u_r("tests/diffs/lwh_original.py",
                                  "tests/diffs/lwh_rename_one_variable.py")
    verify(diff_output)
