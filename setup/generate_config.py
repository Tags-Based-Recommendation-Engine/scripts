import xml.etree.ElementTree as ET
import os
import sys

def fetch_defaults_from_config(config_path):
    config_file = config_path
    
    if not os.path.exists(config_file):
        config_file = "setup/"+config_path

    if os.path.exists(config_file):
        tree = ET.parse(config_file)
        root = tree.getroot()

        default_branch = root.findtext("branch")
        default_autoupdates = root.findtext("autoupdates")
        default_repositories_url = root.findtext("repositories_url")
        default_migration = root.findtext("migration")

        return {
            'default_branch': default_branch,
            'default_autoupdates': default_autoupdates,
            'default_repositories_url': default_repositories_url,
            'default_migration' : default_migration
        }

    else:
        print("Cannot find config_default.xml! Quitting...")
        sys.exit(1)

def generate_config_xml(config_path):
    config_file = config_path

    if os.path.exists(config_file):
        overwrite = input(f"The {config_file} file already exists. Do you want to regenerate it? (yes/no): ").lower() == 'yes'
        if not overwrite:
            print(f"Skipping generation of {config_file}.")
            return

    defaults = fetch_defaults_from_config("config_default.xml")

    branch_name = input(f"Enter the branch name to be cloned by clone_repositories.py (default: {defaults['default_branch']}): ") or defaults['default_branch']
    autoupdates = input(f"Enable autoupdates? (true/false, default: {defaults['default_autoupdates']}): ").lower() in ['true', 't'] or defaults['default_autoupdates']
    repositories_url = input(f"Enter the path for repositories.json used by clone_repositories.py (default: {defaults['default_repositories_url']}): ") or defaults['default_repositories_url']
    migration_input = input(f"Mode of automatic migration to run before running server (auto/interactive/disabled, default: {defaults['default_migration']}): ") or defaults['default_migration']

    config = ET.Element("config")
    
    branch_element = ET.SubElement(config, "branch")
    branch_element.text = branch_name
    
    autoupdates_element = ET.SubElement(config, "autoupdates")
    autoupdates_element.text = str(autoupdates)
    
    repositories_url_element = ET.SubElement(config, "repositories_url")
    repositories_url_element.text = repositories_url

    migration_element = ET.SubElement(config, "migration")
    migration_element.text = migration_input
    
    xml_string = ET.tostring(config, encoding='utf-8').decode()
    
    with open(config_file, "w") as file:
        file.write(xml_string)

    print(f"{config_file} generated successfully!")

if __name__ == "__main__":
    generate_config_xml("config.xml")
