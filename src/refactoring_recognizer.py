# !/usr/bin/env python3
import os
import re
import subprocess
import sys

import yaml


def read_task_description():
    current_dir = os.path.dirname(__file__)
    task_description_file_path = os.path.join(current_dir,
                                              '..',
                                              'resources',
                                              'refactoring_task_description.md')

    with open(task_description_file_path, 'r') as file:
        task_description = file.read()
        return task_description


refactoring_task_description = read_task_description()


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
            raise ValueError("diff_output is empty")
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

    def create_custom_env(self):
        custom_env = os.environ.copy()
        secret = self.fetch_openai_api_key()
        custom_env['OPENAI_API_KEY'] = secret
        return custom_env

    def chatgpt_prompt_and_return(self):
        prompt = self.assemble_prompt()

        current_dir = os.path.dirname(__file__)
        chat_command_path = os.path.join(current_dir,
                                         '..',
                                         'utils',
                                         'chatGPT-CLI')

        command = [chat_command_path, prompt]
        custom_env = self.create_custom_env()

        self.gpt_result = subprocess.run(command,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE,
                                         text=True,
                                         env=custom_env)
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

    def analysis_pretty_print(self):
        yaml_string = self.analysis()

        pattern = r'^```yaml\s*|```$'
        # pattern = r'^.*?```yaml\s*|```$'

        cleaned_yaml_string = re.sub(pattern, '', yaml_string, flags=re.MULTILINE)
        if cleaned_yaml_string != yaml_string:
            print("Code block indicators were removed from the YAML string.", file=sys.stderr)

        try:
            analysis_data = yaml.safe_load(cleaned_yaml_string)
        except yaml.YAMLError as e:
            print(f"Could not parse as YAML\n{cleaned_yaml_string}\n", file=sys.stderr)
            # raise ValueError(f"Could not parse as YAML:\n{cleaned_yaml_string}\n"
            #                  f"Which was cleaned from:\n{yaml_string}\n") from e
            return (yaml_string)

        big_stringy = ""
        for refactoring_attributes in analysis_data:
            if 'refactoring_name' in refactoring_attributes:
                stringy = (refactoring_attributes['refactoring_name']) + ":  " + str(refactoring_attributes)
            else:
                stringy = "Non-refactoring:  " + str(refactoring_attributes)
            big_stringy += stringy + "\n"

        # return str(analysis_data)
        return big_stringy

    def assemble_prompt(self):
        return self.__str__()

    @staticmethod
    def fetch_openai_api_key():
        result = os.environ.get('OPENAI_API_KEY', "")
        if not result:
            raise ValueError("Environment variable 'OPENAI_API_KEY' is not set or empty.")
        return result


def main():
    git_diff_u_r_string = sys.stdin.read()

    recognizer = RefactoringRecognizer()
    recognizer.add_task(refactoring_task_description)
    recognizer.add_diff(git_diff_u_r_string)

    recognizer.chatgpt_prompt_and_return()

    pretty_data_unless_dirty_yaml = recognizer.analysis_pretty_print()
    yaml_maybe_encrusted = str(recognizer.analysis())

    print("**Pretty Analysis (if clean YAML)L**\n")
    if pretty_data_unless_dirty_yaml == yaml_maybe_encrusted:
        print("Dirty YAML -- No Pretty Analysis\n")
    else:
        print(pretty_data_unless_dirty_yaml + "\n")
    print("\n\n")
    print("**YAML (probably)**\n")
    print(yaml_maybe_encrusted + "\n")


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

    output += "# Result - Pretty\n"
    output += str(recognizer.analysis_pretty_print())
    output += "\n\n"

    output += "# __str__\n"
    output += str(recognizer)
    return output


if __name__ == "__main__":
    main()
