import os


def dir_file_path():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return script_dir