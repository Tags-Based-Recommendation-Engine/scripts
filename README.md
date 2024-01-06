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
├──  .gitignore
├──  README.md
└── setup.py
```

# A brief description of what each file does

## /setup
### config_default.xml:
```
Used by generate_config.py to fetch defaults
```
### config.xml:
```
Configuration file used by scripts related to setup
```
### generate_config.py:
```
Used for regenerating config.xml
```
### git_utils:
```
Used by setup.py for cloning all project repositories
```
### requirements.txt
```
Used by virtualenv_utils.py while setting up the python virtual environment
```

## setup.py

Used for setting up various repositories required for project as well as the virtual environment automatically
