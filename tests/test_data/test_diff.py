import json
import pytest
import os
from files.file_path import dir_file_path
from gendiff.scripts.parser_for_file import parser_file


class TestParserForFile:
    @pytest.mark.parametrize('file_name', ['file2.json', 'file2.yaml'])
    def test_successful_parsing_format_file(self, file_name):
        assert parser_file(file_name) == {'timeout': 20, 'verbose': True, 'host': 'hexlet.io'}


    def test_unsupported_format(self):
        file_name = 'file_unsupport_format.txt'

        with pytest.raises(ValueError) as exc_info:
            parser_file(file_name)

        error_message = str(exc_info.value)
        assert f'Неподдерживаемый формат файла: {file_name}. Используйте .json, .yml или .yaml' in error_message


    @pytest.mark.parametrize('file_name', ['file_not_found.yml', 'file_not_found.json'])
    def test_file_not_found(self, file_name):
        with pytest.raises(FileNotFoundError) as exc_info:
            parser_file(file_name)

        error_message = str(exc_info.value)
        assert f"Ошибка: Файл '{file_name}' не существует" in error_message


    def test_file_incorrect_json(self):
        file_name = 'file_incorrect.json'

        with pytest.raises(ValueError) as exc_info:
            parser_file(file_name)

        error_message = str(exc_info.value)
        assert f"Ошибка при парсинге JSON файла '{file_name}': Expecting value: line 1 column 1 (char 0)" in error_message


    def test_file_incorrect_yaml(self):
        file_name = 'file_incorrect.yml'

        with pytest.raises(ValueError) as exc_info:
            parser_file(file_name)

        error_message = str(exc_info.value)
        assert f"Ошибка при парсинге YAML файла '{file_name}': mapping values are not allowed here" in error_message