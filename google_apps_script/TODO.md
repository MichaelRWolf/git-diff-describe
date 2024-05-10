* Secrets
Q - How does Google Scripts environment have access to environment variables?  
A - Google Scripts environment has access to environment variables through the PropertiesService.getScriptProperties()
  method.

Q - How to store secrets in Google Scripts?
A - Use the PropertiesService.getUserProperties() method to store secrets. This method stores secrets in the user's
  Google account. The user can access the secrets by going to File -> Project Properties -> User Properties.    

Q - How to store secrets in Google Apps Script?
A - Use the PropertiesService.getScriptProperties() method to store secrets. This method stores secrets in the script
  project. The secrets are not accessible to the user.

Q - What is the difference between the two methods?


Q - What is a good way for other users to provide OPENAI_API_KEY, GITHUB_TOKEN if I were to distribute this script as a Docker image?
A - Use the PropertiesService.getUserProperties() method to store secrets. This method stores secrets in the user's
  Google account. The user can access the secrets by going to File -> Project Properties -> User Properties.

Q - How will users store OPENAI_API_KEY, GITHUB_TOKEN, and make them available as environment variables, thus making them available to the Google Apps Script?
A - Use the PropertiesService.getUserProperties() method to store secrets.

Q - How do users run PropertyService.getUserProperties() method?
A - Users can run the PropertyService.getUserProperties() method by going to File -> Project Properties -> User Properties.

Q - Do these get backed up to the user's Google Drive?
A - No. The user's Google Drive does not back up the user properties.

Q - Where are User Properties located in IntelliJ on macOS, since they are NOT in File -> Project Properties -> User Properties?
A - User Properties are located in the IntelliJ Preferences -> Languages & Frameworks -> Google Apps Script -> User
Properties.

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









