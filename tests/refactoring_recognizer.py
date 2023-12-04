import subprocess

class RefactoringRecognizer:
    def __init__(self):
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

    def chatGPT_prompt_and_return(self):
        prompt = self.assemble_prompt()

        command = ["chatGPT-CLI", prompt]
        self.gpt_result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
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
