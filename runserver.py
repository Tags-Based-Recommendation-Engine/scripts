import engine_operations as engine
import setup.virtualenv_utils as venv
from setup.config_utils import get_config_value

if __name__ == "__main__":
    venv.activate_virtual_environment()
    migration_mode = get_config_value("migration")
    if migration_mode == "auto":
        engine.auto_migrate()
    if migration_mode == "interactive":
        engine.interactive_migrate()
    if migration_mode == "disabled":
        print(f"Information: You have disabled automatic migration!")
    engine.run_server()