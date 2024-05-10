function __unused_fetchCommitsToSheet(repoUrl, branchName) {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();

    const apiUrl = repoUrl.replace("github.com", "api.github.com/repos") + "/commits?sha=" + branchName;
    const response = UrlFetchApp.fetch(apiUrl);
    const commits = JSON.parse(response.getContentText());

    let shaColumn = [];
    for (let i = 0; i < commits.length; i++) {
        shaColumn.push([commits[i].sha]);
    }

    sheet.getRange(1, 1, shaColumn.length, 1).setValues(shaColumn);
}


// PropertiesService.getScriptProperties().setProperty("GITHUB_PAT", process.env.GITHUB_PAT);

//   "Authorization": "Bearer " + PropertiesService.getScriptProperties().getProperty("GITHUB_PAT")
//   PropertiesService.getScriptProperties().setProperty(key, value);


PropertiesService.getScriptProperties().setProperty("S_PAT", "42");
PropertiesService.getUserProperties().setProperty("U_PAT", "43");

function getGitHubPat() {
    return PropertiesService.getScriptProperties().getProperty("GITHUB_PAT");
}

const commonHeaders = {
    "User-Agent": "Google Apps Script",
    "Authorization": "Bearer " + getGitHubPat()
};


function getApiUrlFromRepoUrl(repoUrl) {
    let apiUrl;
    apiUrl = repoUrl.replace("github.com", "api.github.com/repos");
    return apiUrl;
}

// Looking for format like this
//     https://api.github.com/repos/MichaelRWolf/pythonic-sound-off-machine/commits/b17c47c16a05fe34da4bd063fbe1bb14f756175d
function getCommitUrl(repoUrl, sha) {
    const apiUrl = getApiUrlFromRepoUrl(repoUrl);
    return `${apiUrl}/commits/${sha}`;
}


function getCommitHtmlUrl(repoUrl, sha) {
    const apiUrl = getCommitUrl(repoUrl, sha);
    const response = UrlFetchApp.fetch(apiUrl, {headers: commonHeaders});
    const commitData = JSON.parse(response.getContentText());
    return commitData.html_url
}


// BROKEN!!!
// TODO - See why GET endpoint works differently
function getCommitDiffDirectly(repoUrl, sha) {
    const apiUrl = getCommitUrl(repoUrl, sha);
    const diffUrl = apiUrl + "/diff";
    const response = UrlFetchApp.fetch(diffUrl, {headers: commonHeaders});
    return response.getContentText();
}


function getCommitDiff(repoUrl, sha) {
    const apiUrl = getCommitUrl(repoUrl, sha);
    const response = UrlFetchApp.fetch(apiUrl, {headers: commonHeaders});
    const commitData = JSON.parse(response.getContentText());

    // Initialize an empty string to store the diff
    let diffText = "";

    // Iterate through the files array and concatenate the patch strings
    commitData.files.forEach(function (file) {
        diffText += file.patch + "\n"; // Add newline after each patch
    });

    return diffText;
}


function getCommitDiffBetter(repoUrl, sha) {
    const apiUrl = getCommitUrl(repoUrl, sha);
    const response = UrlFetchApp.fetch(apiUrl, {headers: commonHeaders});
    const commitData = JSON.parse(response.getContentText());

    let diffText = "";

    // Iterate through files and construct diff
    commitData.files.forEach(function (file) {
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
    const apiUrl = repoUrl.replace("github.com", "api.github.com/repos") + "/commits/" + sha;

    // Fetch commit information
    const response = UrlFetchApp.fetch(apiUrl, {headers: commonHeaders});
    const data = JSON.parse(response.getContentText());

    // Return commit message
    return data.commit.message;
}

