import os

import requests
from dotenv import load_dotenv
from typing import Dict

load_dotenv()

OWNER = os.getenv("OWNER")
GIT_API_KEY = os.getenv("GIT_API_KEY")


BASE_URI = "https://api.github.com/"

HEADERS = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {GIT_API_KEY}",
        "X-GitHub-Api-Version": "2022-11-28",
    }

def list_open_pr(repo_name: str) -> Dict:
    headers = HEADERS.update( {
        "state": "open",
        "direction": "desc"
    })
    response = requests.get(BASE_URI + f"repos/{OWNER}/{repo_name}/pulls", headers=headers)
    return response.json()

def get_diff(diff_repo_link: str) -> bytes:
    response = requests.get(diff_repo_link, headers=HEADERS)
    return response._content


def add_comment(repo_name: str, pull_number: int, ai_response: str) -> Dict:
    url = f"{BASE_URI}repos/{OWNER}/{repo_name}/issues/{pull_number}/comments"
    data = {
        "body": ai_response
    }

    response = requests.post(url, headers=HEADERS, json=data)
    return response.json()