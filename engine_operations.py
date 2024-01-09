import os
import sys
import subprocess
import setup.virtualenv_utils as venv

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(project_root, 'engine_control'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "engine_control.settings")

manage_py_dir = os.path.join(project_root, 'engine-control', 'engine_control')

log_file_path = os.path.join(project_root, 'engine-control', 'engine_log.txt')

migration_log_path = os.path.join(project_root, 'engine-control', 'migration_log.txt')

def auto_migrate():
    activate_command = f'python "{manage_py_dir}\\manage.py" makemigrations && python "{manage_py_dir}\\manage.py" migrate'
    with open(migration_log_path, 'w') as migration_log:
        subprocess.run(activate_command, shell=True, stdout=migration_log, stderr=subprocess.STDOUT)
    print("Automigration complete! Check migration_log under engine-control for details.")

def interactive_migrate():
    print("Warning! Only use interactive migration if you get errors with auto_migrate. Log will not be saved during an interactive migrate")
    makemigrations = f'python "{manage_py_dir}\\manage.py" makemigrations'
    migrate = f'python "{manage_py_dir}\\manage.py" migrate'
    subprocess.run(makemigrations, shell=True)
    subprocess.run(migrate, shell=True)

def run_server():
    activate_command = f'python "{manage_py_dir}\\manage.py" runserver > "{log_file_path}" 2>&1'

    print("Server should be available at http://127.0.0.1:8000. If not, check engine_control/engine_log.txt. Press Ctrl+C to quit")

    try:
        subprocess.run(activate_command, shell=True)
    except KeyboardInterrupt:
        print("Django development server has been stopped.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        pass

if __name__ == "__main__":
    sys.exit(1)