import os

import pytest

from gendiff.scripts.parser_for_file import parser_file

script_dir = os.path.dirname(os.path.abspath(__file__))


class TestParserForFile:
    @pytest.mark.parametrize('file_name', ['file2.json', 'file2.yaml'])
    def test_successful_parsing_format_file(self, file_name):
        file_path = os.path.join(script_dir, 'test_data', file_name)
        assert (parser_file(file_path) ==
                {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'})

    def test_unsupported_format(self):
        file_name = 'file_unsupport_format.txt'

        with pytest.raises(ValueError) as exc_info:
            parser_file(file_name)

        error_message = str(exc_info.value)
        assert (f'Неподдерживаемый формат файла: {file_name}. '
                f'Используйте .json, .yml или .yaml') in error_message

    @pytest.mark.parametrize('file_name',
                             ['file_not_found.yml', 'file_not_found.json'])
    def test_file_not_found(self, file_name):
        with pytest.raises(FileNotFoundError) as exc_info:
            parser_file(file_name)

        error_message = str(exc_info.value)
        assert f"Ошибка: Файл '{file_name}' не существует" in error_message

    def test_file_incorrect_json(self):
        file_name = 'file_incorrect.json'
        file_path = os.path.join(script_dir, 'test_data', file_name)

        with pytest.raises(ValueError) as exc_info:
            parser_file(file_path)

        error_message = str(exc_info.value)
        assert (f"Ошибка при парсинге JSON файла '{file_path}': "
                f"Expecting value: line 1 column 1 (char 0)") in error_message

    def test_file_incorrect_yaml(self):
        file_name = 'file_incorrect.yml'
        file_path = os.path.join(script_dir, 'test_data', file_name)

        with pytest.raises(ValueError) as exc_info:
            parser_file(file_path)

        error_message = str(exc_info.value)
        assert (f"Ошибка при парсинге YAML файла '{file_path}': "
                f"mapping values are not allowed here") in error_message
