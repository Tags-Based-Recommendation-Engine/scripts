import sys
from pathlib import Path
from git import Repo
import requests
import json
from .config_utils import get_config_value

ROOT_FOLDER = Path(__file__).resolve().parent.parent.parent

def clone_repositories():
    root_folder = ROOT_FOLDER
    repositories_url = get_config_value('repositories_url')
    branch_name = get_config_value('branch')

    try:
        response = requests.get(repositories_url)
        response.raise_for_status()
        repo_data = response.json()

        for entry in repo_data:
            print(entry)
            repo_url = entry['link']
            repo_path = entry['path']

            repo_name = repo_url.split('/')[-1]
            repo_destination = root_folder / repo_path

            if repo_destination.exists():
                print(f"Repository '{repo_name}' already cloned in {repo_destination}")
            else:
                Repo.clone_from(repo_url, str(repo_destination), branch=branch_name)
                print(f"Repository '{repo_name}' cloned successfully to {repo_destination}")

    except Exception as e:
        print(f"Error cloning repositories: {e}")
        sys.exit(1)

if __name__ == "__main__":
    sys.exit(1)
