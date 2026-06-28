### Hexlet tests and linter status:
[![Actions Status](https://github.com/horo053/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/horo053/python-project-50/actions)


### Линтер Ruff и Тесты Pytest:
[![Python CI](https://github.com/horo053/python-project-50/actions/workflows/python-ci.yml/badge.svg)](https://github.com/horo053/python-project-50/actions/workflows/python-ci.yml)


### Coverage из SonarQube:
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=horo053_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=horo053_python-project-50)


# Проект: Вычислитель отличий
## Программа сравнивает два конфигурационных файла
Возможные форматы файлов: json, yaml, yml

Вывод сравнения может быть в трех вариантах:
- json - Словарь из сравниваемых элементов
- stylish - Строка с отметками различия строк в файлах. Является форматом по умолчанию
- plain - Список строк, в котором различия описаны в текстовом виде


## Помимо основного функционала в программе реализованы:
- Тесты на написанный код в директории tests/test_data
- Интеграция с SonarQube для вывода процента покрытия тестами
- GitHub CI
- Линтер Ruff



## Примеры команд и вывода данных:
### Есть два файла со словарями:
1. file1.json: {"timeout": 20, "verbose": true}
2. file2.json: {"timeout": 20, "verbose": false, "host": "hexlet.io"}

### Для вывода различий данных файлов с отметками различия строк нужно выполнить команду:
- gendiff --format stylish filepath1.json filepath2.yml

ИЛИ
- gendiff filepath1.json filepath2.yml

В ответ выводятся различия в виде:
```json
{
  + host: hexlet.io
    timeout: 20
  - verbose: true
  + verbose: false
}
```

### Для вывода различий данных файлов в виде cписка строк, в котором различия описаны в текстовом виде, нужно выполнить команду:
- gendiff --format plain filepath1.json filepath2.yml

В ответ выводятся различия в виде:
```json
Property 'host' was added with value: 'hexlet.io'
Property 'verbose' was updated. From true to false
```

### Для вывода различий данных файлов в виде json нужно выполнить команду:
- gendiff --format json filepath1.json filepath2.yml

В ответ выводятся различия в виде:
```json
{
  "host": {
    "type": "added",
    "value": "hexlet.io"
  },
  "timeout": {
    "type": "unchanged",
    "value": 20
  },
  "verbose": {
    "type": "changed",
    "old": true,
    "new": false
  }
}
```


(Аскинемы нет, так как работаю под windows 🌺)