# Scripts
### This is a collection of useful scripts used throughout the project

## Folder structure:
```
├── setup
│   ├── __init__.py
│   ├── config_default.xml
│   ├── config.xml
│   ├── generate_config.py
│   ├── git_utils.py
│   ├── requirements.txt
│   ├── virtualenv_utils.py
├── .gitignore
├── engine_operations.py
├── README.md
├── runserver.py
├── setup_project.py
└── update_requirements.py
```

# A brief description of what each file does

### config_default.xml:
Used by ```generate_config.py``` to fetch defaults

### config.xml:
Configuration file used by scripts related to setup

### generate_config.py:
Used for regenerating ```config.xml```

### git_utils:
Used by ```setup_project.py``` for cloning all project repositories

### requirements.txt
Used by ```virtualenv_utils.py``` while setting up the python virtual environment

## setup_project.py
Used for setting up various repositories required for project as well as the virtual environment automatically

## update_requirements.py
Automatically updates ```setup/requirements.txt``` using ```pip freeze```

## engine_operations.py
Set of methods for engine django server. Used by run_server.py

## run_server.py
Automigrate and run engine development server.