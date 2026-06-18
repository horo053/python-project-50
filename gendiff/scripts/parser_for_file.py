import json
import os

import yaml
from yaml.loader import SafeLoader

from files.file_path import dir_file_path


def parser_file(file_json):
    file_path = os.path.join(dir_file_path(), file_json)

    if file_json[-4:] == 'json':
        with open(file_path, 'r', encoding='utf-8') as file:
            parsed_file = json.load(file)

    if file_json[-3:] == 'yml' or file_json[-4:] == 'yaml':
        with open(file_path, 'r', encoding='utf-8') as file:
            parsed_file = yaml.load(file, Loader=SafeLoader)

    return parsed_file