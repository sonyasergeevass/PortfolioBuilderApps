__plugin_name__ = "Pull GitHub Repositories"
__version__ = "1.0"
__author__ = "Sonya Sergeeva BPI21-01"

import requests

def get_github_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
