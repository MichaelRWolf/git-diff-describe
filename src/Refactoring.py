class Refactoring:
    def __init__(self, name, attributes):
        self.attributes = attributes
        self.name = name

    def __str__(self):
        name = self.name

        self_attributes = self.attributes
        match name:
            case "Rename Variable" | "Rename Method" | "Rename Function" | "Rename Class":
                original_name = self_attributes["original_name"]
                new_name = self_attributes["new_name"]
                description = f"{name}: {new_name} (from {original_name})"

            case "Extract Variable" | "Extract Function" | "Extract Method":
                new_name = self_attributes.get("new_name")
                description = f"{name}: {new_name}"

            case "Extract Class" | "Replace Conditional with Polymorphism":
                self_attributes_copy = self_attributes.copy()
                refactoring_name = self_attributes_copy.pop("refactoring_name")
                original_class = self_attributes_copy.pop("original_class", "<NoOriginalClass>")
                new_class = self_attributes_copy.pop("new_class", "<NewClass>")
                classes_in_hierarcy = self_attributes_copy.pop("classes_in_hierarchy", [])

                description = (
                        f"{refactoring_name}: {new_class}"
                        + (f" (from {original_class})" if original_class else "")
                        + (f" classes_in_hierarchy: {classes_in_hierarcy})" if classes_in_hierarcy else "")
                        + (
                            ("\n" + f"    {self_attributes_copy}") if self_attributes_copy else ""
                        ) # Extra parens needed.  Don't know why.
                )

            case _:
                description = (f"{name} - Unhandled Refactoring\n"
                               f"    {self_attributes}")

        return description
