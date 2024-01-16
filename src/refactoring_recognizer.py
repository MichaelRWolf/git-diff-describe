#!/usr/bin/env python3
import os
import subprocess
import sys

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
 
If you notice changes that are not refactorings, please describe the changes in the output structure with key 'other changes'.

Do NOT return YAML in a code block.

If you notice changes that are not refactorings, please describe the changes in the output structure with key 'other changes'.

Do NOT return YAML in a code block.
"""


class RefactoringRecognizer:
    def __init__(self):
        self.task = refactoring_task_description
        self.gpt_result = None
        self.diff_output = None

    def __str__(self):
        s = ''
        s += "# Diff output\n"
        s += self.diff_output + "\n"
        s += "\n\n"
        s += "# Task\n"
        s += self.task + "\n"
        return s

    def add_diff(self, diff_output):
        if not diff_output:
            raise ValueError("diff_output string should not be empty")
        self.diff_output = diff_output

    def subprocess_info(self):
        info = ""

        info += "stdout\n" + self.gpt_result.stdout
        info += "\n\n"

        info += "stderr\n" + self.gpt_result.stderr
        info += "\n\n"

        info += "returncode\n" + str(self.gpt_result.returncode)
        info += "\n"

        return info

    @staticmethod
    def create_custom_env():
        custom_env = os.environ.copy()
        secret = fetch_openai_api_key()
        custom_env['OPENAI_API_KEY'] = secret
        return custom_env

    def chatgpt_prompt_and_return(self):
        prompt = self.assemble_prompt()

        command = ["chatGPT-CLI", prompt]
        self.gpt_result = subprocess.run(command,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE,
                                         text=True,
                                         env=self.create_custom_env())
        # stdout = result.stdout
        # stderr = result.stderr
        # returncode = result.returncode
        # return self.gpt_result.stdout

    # # Now you can print them out or process them further
    # print("stdout:", stdout)
    # print("stderr:", stderr)
    # print("return code:", return_code)

    def add_task(self, task):
        self.task = task

    def analysis(self):
        return self.gpt_result.stdout

    def assemble_prompt(self):
        return self.__str__()


def fetch_openai_api_key():
    try:
        result = subprocess.run(
            [
                'security', 'find-generic-password',
                '-a', os.environ.get('USER'),
                '-s', 'OPENAI_API_KEY',
                '-w'
            ],
            capture_output=True,
            text=True,
            check=True
        )
        # Returning the stdout
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        # Handle errors if the subprocess fails
        print(f"Error occurred: {e}")
        return None


def main():
    git_diff_u_r_string = sys.stdin.read()
    print(git_diff_u_r_string)
    print("Goodbye")

    recognizer = RefactoringRecognizer()
    recognizer.add_task(refactoring_task_description)
    recognizer.add_diff(git_diff_u_r_string)

    recognizer.chatgpt_prompt_and_return()

    print(recognizer.subprocess_info())
    print(recognizer.analysis())


if __name__ == "__main__":
    main()
