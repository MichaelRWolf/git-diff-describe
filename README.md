# commit-message-generator

# Work Plan

## WIP

## TODO
- scrubber removes trailing whitespace so that compare is immune to variations
- OPENAI_API_KEY is fetched before ChatGPT prompt/response
- custom comparison function ignores 'other_changes'
- move class from tests/ to src/
- collect test_* into a test class

## DONE
- output ALL info in YAML (so that it can be passed directly to generate-commit-message)
- new create_diff_string(original_text, current_text)
- tests run from PyCharm, not just command line (after)
- refactor to run_recognizer(diff_string)
- add stdout to validation string
- add a .gitignore for .idea, `__pycache__`, etc.
