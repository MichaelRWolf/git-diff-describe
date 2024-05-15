FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .



# 1 - Run script and die
# 2 - 
# 3 - Start.  Sit.  Do nothing.  Wait for `docker exec` command
#     Mike's preference....
CMD [ "python", "src/refactoring_recognizer.py" ]

# Mike said this...
# Cannot copy ../....
# The container is rooted at project directory.  There is nothing above it.
# I am coming in as src/.., but there is no src/../..


RUN apt-get update && apt-get install -y jq
# RUN apt-get update && apt-get install -y bat


# How To Build

# Original
# ARG openaiapikeythingy 
# ENV OPENAI_API_KEY $openaiapikeythingy 
# docker build . -t mrw/commit-message-generator --build-arg openaiapikeythingy=$OPENAI_API_KEY
# git diff | docker run -i  mrw/commit-message-generator

# Newer/cleaner...
# docker build . -t mrw/commit-message-generator
# git diff | docker run -i  -e "OPENAI_API_KEY=$OPENAI_API_KEY" mrw/commit-message-generator
# docker run -i -t -e "OPENAI_API_KEY=$OPENAI_API_KEY" mrw/commit-message-generator /bin/bash
# -i interactive stdin<->stdin/



# TODO
# - Set up docker account mrw////....
#   Find free one. Get login.
#   `docker login user password`  pseudocode
#
# `docker tag mrw/com...:latest mrw/comm..:1`

# - I publish this
# - `docker push mrw/commit-message-generator:1`
# - `docker push mrw/commit-message-generator:latest`

# - User installs/gets this
# - `docker pull mrw:\commi:latest`
# - `git diff | docker ....`

# TODL
# Change "/" to ":" in mrw/... as naming.  Image names vs Container name.



