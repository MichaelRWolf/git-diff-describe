#! /bin/bash

# This file must be 'dotted', not run as a sub-shell (the normal command line way)
(return 0 2>/dev/null) && sourced=1 || sourced=0

if ! (($sourced)); then
    echo >&2 "File was not sourced. It should be."
    kill -s KILL $$
fi

# Add to PATH using this git repo's toplevel as a starting place
GIT_REPO_BASE=$(git rev-parse --show-toplevel)

if [ $? -eq 0 ]; then
    export PATH="${GIT_REPO_BASE}/utils:${PATH}"
else
    echo "Error: Not inside a Git repository." >&2
    exit 2
fi
