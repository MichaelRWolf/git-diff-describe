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
                original_name = self_attributes_copy.pop("original_name", None)
                new_name = self_attributes_copy.pop("new_name", None)
                child_classes = self_attributes_copy.pop("child_classes", [])
                parent_class = self_attributes_copy.pop("parent_class", None)

                description = (
                        f"{refactoring_name}:"
                        + (f" {new_name}" if new_name else "")
                        + (f" (from {original_name})" if original_name else "")
                        + (f" {child_classes})" if child_classes else "")
                        + (" replaces " if (child_classes and parent_class) else "")
                        + (f" {parent_class}" if parent_class else "")
                        + (
                            ("\n" + f"    {self_attributes_copy}") if self_attributes_copy else ""
                        )  # Extra parens needed.  Don't know why.
                )

            case _:
                description = (f"{name} - Unhandled Refactoring\n"
                               f"    {self_attributes}")

        return description
