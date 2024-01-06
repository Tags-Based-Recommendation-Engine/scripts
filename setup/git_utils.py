import sys
from pathlib import Path
from git import Repo
import requests
import json
import xml.etree.ElementTree as ET

ROOT_FOLDER = Path(__file__).resolve().parent.parent.parent

def get_config_value(element_name):
    config_file = Path(__file__).resolve().parent / 'config.xml'
    tree = ET.parse(config_file)
    root = tree.getroot()
    element = root.find(element_name)
    return element.text if element is not None else None

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
