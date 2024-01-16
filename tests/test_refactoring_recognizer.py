# test_refactoring_recognizer.py
import os
import subprocess
from approvaltests import verify

from src.refactoring_recognizer import RefactoringRecognizer


def canonical_json_string(non_canonical_string):
    # Convert the Python dictionary to a canonical JSON string with sorted keys
    # and an indentation of 4 spaces.
    # data = json.loads(non_canonical_string)
    # canonical_string = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
    return non_canonical_string


# refactoring_task_description = """
# # Task: infer_refactoring
#
# Analyze the following output provided in 'unified diff' format
# Determine if any standard software code refactorings can be identified.
# If a refactoring is detected, provide output including
#   - preferred refactoring name
#   - attributes specific to this refactoring
#
# Assume that the user will understand common refactorings, so do not provide explanations for them.
#
# # Preferred refactoring name(s)
# Many similar names are commonly used for a refactoring.
# When you report a refactoring, use 'preferred name' below instead of one of the 'alternate names'.
#
# Describe the refactoring by providing the attributes listed for each refactoring.
#
# Provide additional attributes if you think they are necessary.
#
# - preferred_name: Rename Variable
#   alternate_names:
#     - Rename Identifier
#   attributes:
#     - original_name
#     - new_name
#
# - preferred_name: Rename Function
#   alternate_names:
#     - Rename Method
#   attributes:
#     - original_name
#     - new_name
#
# - preferred_name: Extract Method
#   alternate_names:
#     - Extract Function
#     - Extract Procedure
#   attributes:
#     - new_name
#
# - preferred_name: Move Method
#   alternate_names:
#     - Move Function
#     - Move Procedure
#
# - preferred_name: Extract Class
#   alternate_names:
#     - Extract Module
#
# - preferred_name: Change Signature
#   alternate_names:
#     - Modify Function Signature
#
# - preferred_name: Replace Conditional with Polymorphism
#   alternate_names:
#     - Replace Conditional with Inheritance
#
# # Format
# Generate YAML output for refactoring actions.
# Output the YAML directly.
#  - Do not preface the YAML with the string literal "yaml".
#  - Do not display it in a text box.
#  - Do not surround it with multi-line quotes.
# Ensure that string values are enclosed in double quotes only when necessary.
# Quotes are optional around values that contain only letters, numbers, and underscores.
# Avoid adding optional quotes.
# Do not add quotes around values that contain only letters, numbers, and underscores.
# Ensure that there are no optional blank lines between elements in the YAML output.
#
# In the following example, notice that these values are not surrounded by quotes
#  - c
#  - city
#  - s
#  - state
#  - z
#  - zip_code
#
#
# Also notice that there is not a blank line separating the items with new name: city, state, zip_code.
# These items are adjacent with no separation.
#
# Example:
# - refactoring_name: Rename Variable
#   original_name: c
#   new_name: city
# - refactoring_name: Rename Variable
#   original_name: s
#   new_name: state
# - refactoring_name: Rename Variable
#   original_name: z
#   new_name: zip_code
#
#
# For each refactoring, output these fields.
#  - refactoring_name - Use the preferred name, not alternate names
#  - [attributes] - See below for suggested attributes based on 'refactoring-name'.
#      Do not output 'attributes' as a collection for attributes.
#      Simply place the attributes at the same level as 'refactoring_name'.
#  - [other] - if you feel that other information would be necessary to categorize the refactoring
#
# If you notice changes that are not refactorings,
# please describe the changes in the output structure with key 'other changes'.
#
# Do NOT return YAML in a code block.
# """
# 1
# pattern = r'\s+(?=\n)'

# 2 Define a regular expression pattern to match trailing whitespace before a newline
# on lines with non-whitespace characters
# pattern = r'(?<=\S)\s+(?=\n)'

# 3 Define a regular expression pattern to match trailing whitespace before a newline
# on lines with non-whitespace characters
pattern = r'(?<=\S)([ \t]+)(?=\n)'


# refactoring_task_description = re.sub(pattern, '', refactoring_task_description)


def run_recognizer(diff_output):
    recognizer = RefactoringRecognizer()
    # recognizer.add_task(refactoring_task_description)
    recognizer.add_diff(diff_output)
    output = ""

    recognizer.chatgpt_prompt_and_return()

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
    for filename in [filename1, filename2]:
        if not os.path.isfile(filename) or not os.access(filename, os.R_OK):
            raise FileNotFoundError(f"File not found or not readable: {filename}")

    command = ['diff', '-u', '-r', filename1, filename2]
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            text=True,
                            check=False)
    return result.stdout


# def load_openai_env():
#     openai_api_key = os.environ.get('OPENAI_API_KEY')
#     print(f"OPENAI_API_KEY: {openai_api_key}")
#
#     custom_env_path = os.path.expanduser('~/.openairc')
#     load_dotenv(dotenv_path=custom_env_path)
#
#     openai_api_key = os.environ.get('OPENAI_API_KEY')
#     print(f"OPENAI_API_KEY: {openai_api_key}")


# def datetime_scrubber(text):
#     # Regular expression pattern for date and time (customize as needed)
#     date_pattern = r'\d{4}-\d{2}-\d{2}'  # Example: '2022-01-01'
#     time_pattern = r'\d{2}:\d{2}:\d{2}'  # Example: '14:30:59'
#
#     # Replace dates and times with placeholders
#     text = re.sub(date_pattern, 'YYYY-MM-DD', text)
#     text = re.sub(time_pattern, 'HH:MM:SS', text)
#     return text


def whitespace_scrubber(text):
    lines = text.splitlines()
    stripped_lines = []
    for line in lines:
        stripped_line = line.rstrip()
        stripped_lines.append(stripped_line)
    return_string = "\n".join(stripped_lines)
    return return_string


# def test_with_scrubber():
#     output = generate_output_with_datetime()  # Function generating the output
#     verify(output)


# def xxxx_scrubber(text):
#     # Regular expression pattern for date and time (customize as needed)
#     trailing_whitespace_pattern = r'\d{4}-\d{2}-\d{2}'  # Example: '2022-01-01'
#     blank_whitespace_pattern = r'\d{2}:\d{2}:\d{2}'  # Example: '14:30:59'
#
#     # Replace dates and times with placeholders
#     text = re.sub(date_pattern, 'YYYY-MM-DD', text)
#     text = re.sub(time_pattern, 'HH:MM:SS', text)
#     return text

def verify_with_scrubber(text):
    text = whitespace_scrubber(text)
    verify(text)


import unittest


class TestRefactoringRecognizer(unittest.TestCase):
    def test_whitespace_scrubber(self):
        text = "top\n \nbottom\n"
        scrubbed_text = whitespace_scrubber(text)
        expected_text = "top\n\nbottom"
        self.assertEqual(scrubbed_text, expected_text)

    def test_hello(self):
        # verify("Hello", options=Options().with_reporter(report_with_beyond_compare()))
        # verify("Hello", reporter=DiffReporter())
        verify_with_scrubber("Hello")

    def test_recognizer_throws_value_error_on_empty_diff(self):
        with self.assertRaises(ValueError):
            RefactoringRecognizer().add_diff("")

    def test_recognize_rename_one_variable(self):
        diff_output = return_diff_u_r("diffs/lwh_original.py",
                                      "diffs/lwh_rename_one_variable.py")
        output = run_recognizer(diff_output)
        verify_with_scrubber(output)

    def test_recognize_rename_three_variables(self):
        diff_output = return_diff_u_r("diffs/lwh_original.py",
                                      "diffs/lwh_rename_three_variables.py")
        output = run_recognizer(diff_output)
        verify_with_scrubber(output)

    def test_extract_function(self):
        diff_output = return_diff_u_r("diffs/lwh_pre_extract_function.py",
                                      "diffs/lwh_original.py")
        output = run_recognizer(diff_output)
        verify_with_scrubber(output)


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
    verify_with_scrubber(output)


def test_file_differ_for_rename_one_variable():
    diff_output = return_diff_u_r("diffs/lwh_original.py",
                                  "diffs/lwh_rename_one_variable.py")
    verify_with_scrubber(diff_output)
