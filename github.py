# go to github and retrieve different github issues
import os
import requests
from dotenv import load_dotenv
from langchain_core.documents import (
    Document,
)  # Class for storing a piece of text and associated metadata.

# wrap our github issues and then pass it to vector store database

# let's call this load_dotenv() to load environment variables from .env file
load_dotenv()

# grab our github token from environment variable
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")


# Function to utilize this github api
def fetch_github(owner, repo, endpoint):
    url = f"https://api.github.com/repos/{owner}/{repo}/{endpoint}"  # to load any kind of repo we want
    headers = {
        "Authorization": f"Bearer {GITHUB_TOKEN}",
        # "Accept": "application/vnd.github+json",
    }
    response = requests.get(url, headers=headers)
    # response.raise_for_status()
    # return response.json()
    if response.status_code == 200:
        data = response.json()
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return []
    # print(data)
    return data


def fetch_github_issues(owner, repo):
    data = fetch_github(owner, repo, "issues")

    return load_issues(data)


# write a function that will take the results from github_repo and then wrap them as a langchain document
def load_issues(issues):

    docs = []
    for (
        entry
    ) in issues:  # issues is a list of all diff issues that have bunch of diff keys
        metadata = {
            "author": entry["user"]["login"],
            "comments": entry["comments"],
            "body": entry["body"],
            "labels": entry["labels"],
            "created_at": entry["created_at"],
        }
        data = entry["title"]  # indexing or lookinhg up issues from the issue title
        if entry["body"]:
            data += entry["body"]
        doc = Document(
            page_content=data, metadata=metadata
        )  # when we look up in database we're lookinhg into this page_content
        docs.append(doc)

    return docs
