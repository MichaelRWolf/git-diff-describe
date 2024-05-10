
# Dockerfile

Q - Why does removing this line still build the script and let it run,
but have it produce no output?
> `RUN apt-get update && apt-get install -y jq`

# README.md

- Create it


# LICENSE.txt

- Create it


# OPENAI_API_KEY
- Describe in `README.md`


# GitHub PAT (Personal Access Token)
- Describe in `README.md`
- Allow users to provide their own GitHub token
- Later - Allow users to authorize via OAuth.


# Class GitDiffAnalyzer
- Q? - Why does 'rewrite expression' get interpreted as 'rename variable'


# Class GitDiffDescription
- Add member `RecommendationsToImproveGitDiffAnalyzer`
  - More `diff` context?
  - Supply complete file?


# Class GitDiffDescriptionFormatter
- `formatAsPlainText()`
  - Use `case` statement for each kind in GAS spreadsheet
  - Do not (yet) subclass anything
- NOT YET
  - `formatAsCommitMessage()`
  - `_commitMessageHeader()`
  - `_commitMessageBody()`


# Class ApprovalTestComparer
- Add  method`function equalEnoughForApprovalTest() : Boolean`









