import os
import sys
import subprocess

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(project_root, 'engine_control'))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "engine_control.settings")

manage_py_dir = os.path.join(project_root, 'engine-control', 'engine_control')

log_file_path = os.path.join(project_root, 'engine-control', 'engine_log.txt')

activate_script = os.path.join(project_root, 'env', 'Scripts', 'activate')
activate_command = f'"{activate_script}" && python "{manage_py_dir}\\manage.py" runserver > "{log_file_path}" 2>&1'

print("Server should be available at http://127.0.0.1:8000. If not, check engine_control/engine_log.txt. Press Ctrl+C to quit")

try:
    subprocess.run(activate_command, shell=True)
except KeyboardInterrupt:
    print("Django development server has been stopped.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    pass
