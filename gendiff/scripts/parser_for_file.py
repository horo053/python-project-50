import collections.abc
import json

import yaml
from yaml.loader import SafeLoader

# не проходили тесты на парсинг yaml, править парсинг yaml файлов
if not hasattr(collections, 'Hashable'):
    collections.Hashable = collections.abc.Hashable


def parser_file(file_json):
    file_path = file_json

    try:
        if file_json[-4:] == 'json':
            with open(file_path, 'r', encoding='utf-8') as file:
                parsed_file = json.load(file)
                return parsed_file

        elif file_json[-3:] == 'yml' or file_json[-4:] == 'yaml':
            with open(file_path, 'r', encoding='utf-8') as file:
                parsed_file = yaml.load(file, Loader=SafeLoader)
                return parsed_file

        else:
            raise ValueError(f'Неподдерживаемый формат файла: {file_json}. '
                             f'Используйте .json, .yml или .yaml')

    except FileNotFoundError:
        raise FileNotFoundError(f"Ошибка: Файл '{file_json}' не существует")
    except json.JSONDecodeError as f:
        raise ValueError(f"Ошибка при парсинге JSON файла '{file_json}': {f}")
    except yaml.YAMLError as f:
        raise ValueError(f"Ошибка при парсинге YAML файла '{file_json}': {f}")