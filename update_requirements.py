import subprocess
import setup.virtualenv_utils as venv

def update_requirements():
    requirements_path = "setup/requirements.txt"

    venv.activate_virtual_environment()

    try:
        requirements = subprocess.check_output(["pip", "freeze"]).decode("utf-8").strip()

        with open(requirements_path, "w") as requirements_file:
            requirements_file.write(requirements)

        print("Requirements updated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to update requirements. Error: {e}")


if __name__ == "__main__":
    update_requirements()