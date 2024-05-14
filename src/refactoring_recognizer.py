# !/usr/bin/env python3
import os
import subprocess
import sys

# refactoring_task_description_file_name = '../resources/refactoring_task_description.md'
# with open(refactoring_task_description_file_name, 'r') as file:
#     refactoring_task_description = file.read()

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

        current_dir = os.path.dirname(__file__)
        chat_command_path = os.path.join(current_dir,
                                                  '..',
                                                  'utils',
                                                  'chatGPT-CLI')

        command = [chat_command_path, prompt]
        custom_env = self.create_custom_env()

        for key, value in custom_env.items():
            print(f"{key}: {value}")

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

    def assemble_prompt(self):
        return self.__str__()


# def fetch_openai_api_key():
#     result = os.environ.get('OPENAI_API_KEY_git_diff_analyzer')
#     return result.strip()

def fetch_openai_api_key():
    result = os.environ.get('OPENAI_API_KEY', "")
    if not result:
        raise ValueError("Environment variable 'OPENAI_API_KEY' is not set or empty.")
    return result

#     try:
#         result = subprocess.run(
#             [
#                 'security', 'find-generic-password',
#                 '-a', os.environ.get('USER'),
#                 '-s', 'OPENAI_API_KEY_git_diff_analyzer
# ',
#                 '-w'
#             ],
#             capture_output=True,
#             text=True,
#             check=True
#         )
# # Returning the stdout
# return result.stdout.strip()
# except subprocess.CalledProcessError as e:
#     # Handle errors if the subprocess fails
#     print(f"Error occurred: {e}")
#     return None


def main():
    git_diff_u_r_string = sys.stdin.read()
    # print("Sending this git-diff to be analyzed..." +
    #       "---------------------------------------" +
    #       git_diff_u_r_string,
    #       file=sys.stdout)

    recognizer = RefactoringRecognizer()
    recognizer.add_task(refactoring_task_description)
    recognizer.add_diff(git_diff_u_r_string)

    recognizer.chatgpt_prompt_and_return()

    # print(recognizer.subprocess_info(), file=sys.stdout) 
    print(recognizer.analysis())


if __name__ == "__main__":
    main()
