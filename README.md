# commit-message-generator

To make it useful to the Thursday group


To make it work as a developer
- in environment
  - OPENAI_API_KEY into environment
    - . ~/.openairc
- Executables on `PATH`
  - `refactoring_recognizer.py`
  - `ChatGPT-CLI`



What's needed to run
  recognizer....py is on path and executable
  chatGPT-CLI is be used by recognizer



# How To Run


Make sure 'chatGPT-CLI' is on path.

Assure that key is in environment.


# Work Plan

## WIP

## TODO
- pass OPENAI_API_KEY to... (PyCharm, pytest, PyCharm/pytest, other?)
- tests run from PyCharm, not just command line (after)
- new create_diff_string(original_text, current_text)
- output ALL info in YAML (so that it can be passed directly to generate-commit-message)

## DONE
- refactor to run_recognizer(diff_string)
- add stdout to validation string
- add a .gitignore for .idea, `__pycache__`, etc.
