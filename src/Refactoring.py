class Refactoring:
    def __init__(self, name, attributes):
        self.attributes = attributes
        self.name = name

    def __str__(self):
        name = self.name

        match name:
            case "Rename Variable" | "Rename Method" | "Rename Class":
                original_name = self.attributes["original_name"]
                new_name = self.attributes["new_name"]
                description = f"{name}: {new_name} (from {original_name})"

            case "Extract Variable" | "Extract Function" | "Extract Method":
                new_name = self.attributes.get("new_name")
                description = f"{name}: {new_name}"

            case "Extract Class" | "Replace Conditional with Polymorphism":
                new_name = self.attributes.get("new_class", "<NewClass>")
                original_name = self.attributes.get("original_class")
                description = (
                        f"{name}: {new_name}"
                        + (f" (from {original_name})" if original_name else "")
                        + "\n"
                        + f"    {self.attributes}")

            case _:
                description = (f"{name} - Unhandled Refactoring\n"
                               f"    {self.attributes}")

        return description
