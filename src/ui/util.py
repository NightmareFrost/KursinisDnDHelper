import os

current_dir = os.path.dirname(os.path.abspath(__file__))
base_dir = os.path.join(current_dir, "..", "..", "ui")


def ui_file_path(name: str) -> str:
    return os.path.join(base_dir, name)
