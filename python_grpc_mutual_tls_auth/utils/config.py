import os


def invoke_config():
    from invoke.config import Config
    cfg = Config()
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cfg.set_project_location(root_dir)
    cfg.load_project()
    return cfg
