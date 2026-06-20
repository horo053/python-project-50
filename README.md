### Hexlet tests and linter status:
[![Actions Status](https://github.com/horo053/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/horo053/python-project-50/actions)


### Линтер Ruff и Тесты Pytest:
[![Python CI](https://github.com/horo053/python-project-50/actions/workflows/python-ci.yml/badge.svg)](https://github.com/horo053/python-project-50/actions/workflows/python-ci.yml)


### Coverage из SonarQube:
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=horo053_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=horo053_python-project-50)


## Проект: Вычислитель отличий
### Программа сравнивает два конфигурационных файла
Возможные форматы файлов: json, yaml, yml

Вывод сравнения может быть в трех вариантах:
- json - Словарь из сравниваемых элементов
- stylish - Строка с отметками различия строк в файлах. Является форматом по умолчанию
- plain - Список строк, в котором различия описаны в текстовом виде


### Помимо основного функционала в программе реализованы:
- Тесты на написанный код в директории tests/test_data
- Интеграция с SonarQube для вывода процента покрытия тестами
- GitHub CI
- Линтер Ruff


(Аскинемы нет, так как работаю под windows 🌺)