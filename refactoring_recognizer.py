class RefactoringRecognizer:
    def __str__(self):
        str = "Can not (yet) stringify"
        return str

    def add_diff(self, diff_output):
        self.diff_output = diff_output

    def analysis(self):
        return "No refactorings"
