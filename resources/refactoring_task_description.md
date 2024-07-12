# refactoring_task_description = """
# # Task: infer_refactoring
# 
# Analyze the following output provided in 'unified diff' format
# Determine if any standard software code refactorings can be identified.
# If a refactoring is detected, provide output including
#   - preferred refactoring name
#   - attributes specific to this refactoring
# 
# Assume that the user will understand common refactorings, so do not provide explanations for them.
# 
# # Preferred refactoring name(s)
# Many similar names are commonly used for a refactoring.
# When you report a refactoring, use 'preferred name' below instead of one of the 'alternate names'.
# 
# Further describe the refactoring by providing the attributes listed for each refactoring.
# 
# For these attributes, provide both if they are different, otherwise suppress both.
# - original_class
# - new_class
# 
# For these attributes, provide both if they are different, otherwise suppress both.
# - original_filename
# - new_filename
# 
# Provide additional attributes if you think they are necessary.
# 
# - preferred_name: Rename Variable
#   alternate_names:
#     - Rename Identifier
#   attributes:
#     - original_name
#     - new_name
# 
# - preferred_name: Rename Function
#   alternate_names:
#     - Rename Method
#   attributes:
#     - original_name
#     - new_name
# 
# - preferred_name: Extract Method
#   alternate_names:
#     - Extract Function
#     - Extract Procedure
#   attributes:
#     - new_name
# 
# - preferred_name: Move Method
#   alternate_names:
#     - Move Function
#     - Move Procedure
# 
# - preferred_name: Extract Class
#   alternate_names:
#     - Extract Module
#   attributes:
#     - new_name (NOT new_class)
#     - original_name (NOT original_class)
# 
# - preferred_name: Change Signature
#   alternate_names:
#     - Modify Function Signature
#   attributes:
#     - new_signature
#     - original_signature
# 
# - preferred_name: Replace Conditional with Polymorphism
#   alternate_names:
#     - Replace Conditional with Inheritance
#   attributes:
#     - parent_class
#     - child_classes[]
# 
# # Format
# Generate YAML output for refactoring actions.
# Output the YAML directly.
#  - Do not preface the YAML with the string literal "yaml".
#  - Do not display it in a text box.
#  - Do not surround it with multi-line quotes.
# Ensure that string values are enclosed in double quotes only when necessary.
# Quotes are optional around values that contain only letters, numbers, and underscores.
# Avoid adding optional quotes.
# Do not add quotes around values that contain only letters, numbers, and underscores.
# Ensure that there are no optional blank lines between elements in the YAML output.
# 
# In the following example, notice that these values are not surrounded by quotes
#  - c
#  - city
#  - s
#  - state
#  - z
#  - zip_code
# 
# 
# Also notice that there is not a blank line separating the items with new name: city, state, zip_code.
# These items are adjacent with no separation.
# 
# For each refactoring, output these fields.
#  - refactoring_name - Use the preferred name, not alternate names
#  - [attributes] - See below for suggested attributes based on 'refactoring-name'.
#      Do not output 'attributes' as a collection for attributes.
#      Simply place the attributes at the same level as 'refactoring_name'.
#  - [other sttributes] - if you feel that other information would be necessary to categorize the refactoring
#  
# If you notice changes that are not refactorings, add thm as list elements with a 'key' of 'change', 
# and its value being your description.
# Put double-quotes around each value
# Assure that values are encoded to prvent YAML parse errors (especially when using punctuation 
# like `-` `:` `[` and `]` that are special to YAML)
#
# Example:
# - refactoring_name: Rename Variable
#   original_name: c
#   new_name: city
# - refactoring_name: Rename Variable
#   original_name: s
#   new_name: state
# - refactoring_name: Rename Variable
#   original_name: z
#   new_name: zip_code
# - change: "Add safety precautions to TODO.md file"
# - change: "reformat file"
# - change: "remove whitespace"
# - change: "Assure that 4 - 1 is equal to 3"
# - change: "too extensive for me to understand"
# 
# Do NOT return YAML in a code block.
# Do NOT put code block indicators around the YAML that is returned
#
# Example -- NOT Acceptable
# ``` yaml
# - refactoring_name: Extract Method
#   new_name: express_pizza_delivery
# ```
#
# Example -- MUCH preferred
# - refactoring_name: Extract Method
#   new_name: express_pizza_delivery
