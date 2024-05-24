class Refactoring:
    def __init__(self, name, attributes):
        self.attributes = attributes
        self.name = name

    def __str__(self):
        name = self.name

        match name:
            case "Rename Variable" | "Rename Method" | "Rename Function" | "Rename Class":
                original_name = self.attributes["original_name"]
                new_name = self.attributes["new_name"]
                description = f"{name}: {new_name} (from {original_name})"

            case "Extract Variable" | "Extract Function" | "Extract Method":
                new_name = self.attributes.get("new_name")
                description = f"{name}: {new_name}"

            case "Extract Class" | "Replace Conditional with Polymorphism":
                # Required attributes
                refactoring_name = self.attributes.get("refactoring_name")
                original_class = self.attributes.get("original_class")

                # Optional attributes
                new_class = self.attributes.get("new_class", "<NewClass>")
                classes_in_hierarcy = self.attributes.get("classes_in_hierarchy", [])

                description = (
                    f"{refactoring_name}: {new_class}"
                    + (f" (from {original_class})" if original_class else "")
                    + (f" classes_in_hierarchy: {classes_in_hierarcy})" if classes_in_hierarcy else "")
                    + ("\n" + f"    {self.attributes}") if self.attributes else "")

            case _:
                description = (f"{name} - Unhandled Refactoring\n"
                               f"    {self.attributes}")

        return description
