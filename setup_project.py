import setup.virtualenv_utils as venv
import setup.generate_config as config
import setup.git_utils as git

if __name__ == "__main__":
    venv.create_virtual_environment()
    venv.install_requirements()
    config.generate_config_xml("setup/config.xml")
    git.clone_repositories()