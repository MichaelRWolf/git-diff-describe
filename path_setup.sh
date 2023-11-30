#! /bin/bash

GIT_REPO_BASE=$(git rev-parse --show-toplevel)

# Check if the command succeeded before proceeding
if [ $? -eq 0 ]; then
    export PATH="${PATH}:${GIT_REPO_BASE}/utils"
else
    echo "Error: Not inside a Git repository." >&2
    exit 2
fi
