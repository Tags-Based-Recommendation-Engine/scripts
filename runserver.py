import engine_operations as engine
import setup.virtualenv_utils as venv

if __name__ == "__main__":
    venv.activate_virtual_environment()
    engine.auto_migrate()
    engine.run_server()