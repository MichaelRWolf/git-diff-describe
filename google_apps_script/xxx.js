function myFunction() {
    return "goodness" + ", everlasting";
}


function __unused_fetchCommitsToSheet(repoUrl, branchName) {
  var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
  
  var apiUrl = repoUrl.replace("github.com", "api.github.com/repos") + "/commits?sha=" + branchName;
  var response = UrlFetchApp.fetch(apiUrl);
  var commits = JSON.parse(response.getContentText());
  
  var shaColumn = [];
  for (var i = 0; i < commits.length; i++) {
    shaColumn.push([commits[i].sha]);
  }
  
  sheet.getRange(1, 1, shaColumn.length, 1).setValues(shaColumn);
}


// PropertiesService.getScriptProperties().setProperty("GITHUB_PAT", process.env.GITHUB_PAT);

//   "Authorization": "Bearer " + PropertiesService.getScriptProperties().getProperty("GITHUB_PAT")
//   PropertiesService.getScriptProperties().setProperty(key, value);


PropertiesService.getScriptProperties().setProperty("S_PAT", "42");
PropertiesService.getUserProperties().setProperty("U_PAT", "43");

function gup(){
    return PropertiesService.getUserProperties().getProperty("U_PAT"); 
}


function gsp(){
    return      PropertiesService.getScriptProperties().getProperty("S_PAT"); 
}

var gitHubPat = "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";

function getGitHubPat() {
    return PropertiesService.getScriptProperties().getProperty("GITHUB_PAT");
}

function fooUser() {
    return PropertiesService.getUserProperties().getProperty("GITHUB_PAT");
}


var commonHeaders = {
    "User-Agent": "Google Apps Script",
    "Authorization": "Bearer " + getGitHubPat()
};


function getApiUrlFromRepoUrl(repoUrl) {
  apiUrl = repoUrl.replace("github.com", "api.github.com/repos");
  return apiUrl;
}

// Looking for format like this
//     https://api.github.com/repos/MichaelRWolf/pythonic-sound-off-machine/commits/b17c47c16a05fe34da4bd063fbe1bb14f756175d
function getCommitUrl(repoUrl, sha) {
  var apiUrl = getApiUrlFromRepoUrl(repoUrl);
  var commitUrl = apiUrl + "/commits/" + sha;
  return commitUrl;
}


function getCommitHtmlUrl(repoUrl, sha) {
  var apiUrl = getCommitUrl(repoUrl, sha)
  var response = UrlFetchApp.fetch(apiUrl, {  headers: commonHeaders });
  var commitData = JSON.parse(response.getContentText());
  var htmlUrl = commitData.html_url;
  return htmlUrl
}


// BROKEN!!!
// TODO - See why GET endpoint works differently
function getCommitDiffDirectly(repoUrl, sha) {
  var apiUrl = getCommitUrl(repoUrl, sha);
  var diffUrl = apiUrl + "/diff";  
  var response = UrlFetchApp.fetch(diffUrl, { headers: commonHeaders });
  return response.getContentText();
}


function getCommitDiff(repoUrl, sha) {
  var apiUrl = getCommitUrl(repoUrl, sha)
  var response = UrlFetchApp.fetch(apiUrl, {  headers: commonHeaders });
  var commitData = JSON.parse(response.getContentText());
  
  // Initialize an empty string to store the diff
  var diffText = "";
  
  // Iterate through the files array and concatenate the patch strings
  commitData.files.forEach(function(file) {
    diffText += file.patch + "\n"; // Add newline after each patch
  });
  
  return diffText;
}


function getCommitDiffBetter(repoUrl, sha) {
  var apiUrl = getCommitUrl(repoUrl, sha)
  var response = UrlFetchApp.fetch(apiUrl, {  headers: commonHeaders });
  var commitData = JSON.parse(response.getContentText());

  var diffText = "";

  // Iterate through files and construct diff
  commitData.files.forEach(function(file) {
    diffText += `diff --git a/${file.filename} b/${file.filename}\n`;
    diffText += `index ${file.previous_filename ? file.previous_filename : '0000000'}..${file.filename}\n`;

    if (file.status === 'added') {
      diffText += `--- /dev/null\n`;
      diffText += `+++ b/${file.filename}\n`;
    } else if (file.status === 'deleted') {
      diffText += `--- a/${file.filename}\n`;
      diffText += `+++ /dev/null\n`;
    } else {
      diffText += `--- a/${file.filename}\n`;
      diffText += `+++ b/${file.filename}\n`;
    }

    diffText += `@@ -${file.additions > 0 ? '+' : ''}${file.additions},${file.deletions > 0 ? '-' : ''}${file.deletions} @@\n`;

    diffText += file.patch + "\n";
  });

  return diffText;
}


function getCommitComment(repoUrl, sha) {
  var apiUrl = repoUrl.replace("github.com", "api.github.com/repos") + "/commits/" + sha;
  
  // Fetch commit information
  var response = UrlFetchApp.fetch(apiUrl, { headers: commonHeaders });
  var data = JSON.parse(response.getContentText());
  
  // Return commit message
  return data.commit.message;
}

