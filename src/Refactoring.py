class Refactoring:
    def __init__(self, name, attributes):
        self.attributes = attributes
        self.name = name

    def __str__(self):
        name = self.name

        original_name = self.attributes["original_name"]
        new_name = self.attributes["new_name"]
        description = f"{name} to {new_name} from {original_name}"

        return description
