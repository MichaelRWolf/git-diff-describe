class RefactoringRecognizer:
    def __str__(self):
        s = ''
        s += "# Diff output\n"
        s += self.diff_output + "\n"
        return s

    def add_diff(self, diff_output):
        self.diff_output = diff_output

    def analysis(self):
        return "No refactorings"
