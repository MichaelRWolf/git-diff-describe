from setuptools import setup, find_packages

setup(
    name="refactoring-recognizer",
    version="1.0",
    packages=find_packages(),

    # Metadata for PyPI
    # url="...",
    # author="...",
    description="Generate a git-commit(1) message from git-diff(1) output",

    # Add executable scripts
    entry_points={
        'console_scripts': [
            'refactoring_recognizer = src.refactoring_recognizer:main',
            'chatgpt = utils.chatgpt:main'
        ],
    },
)
