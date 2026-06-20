
from gendiff.scripts.diff import build_diff, generate_diff


class TestBuildDiff:
    def test_identical_dict(self):
        dictionaries = {"timeout": 20, "verbose": True, "host": "hexlet.io"}
        result = build_diff(dictionaries, dictionaries)
        for key, value in result.items():
            assert value['type'] == 'unchanged'

    def test_only_in_second_dict(self):
        dictionaries_one = {"timeout": 20}
        dictionaries_two = {"timeout": 20, "verbose": True}
        result = build_diff(dictionaries_one, dictionaries_two)
        assert result['verbose']['type'] == 'added'

    def test_only_in_first_dict(self):
        dictionaries_one = {"timeout": 20, "host": "hexlet.io"}
        dictionaries_two = {"host": "hexlet.io"}
        result = build_diff(dictionaries_one, dictionaries_two)
        assert result['timeout']['type'] == 'removed'

    def test_different_meanings(self):
        dictionaries_one = {"timeout": 20, "host": "hexlet.io"}
        dictionaries_two = {"timeout": 50, "host": "hexlet.io"}
        result = build_diff(dictionaries_one, dictionaries_two)
        key_result = result['timeout']
        assert key_result['type'] == 'changed'
        assert key_result['old'] == 20
        assert key_result['new'] == 50

    def test_dict_in_dict(self):
        dictionaries = {"host": {"timeout": 50}}
        result = build_diff(dictionaries, dictionaries)
        assert result['host']['type'] == 'nested'


class TestGenerateDiff:
    def test_stylish_format(self):
        format_name = 'stylish'
        dictionaries_one = {"timeout": 20, "verbose": True}
        dictionaries_two = {"timeout": 20, "verbose": False,
                            "host": "hexlet.io"}
        result = generate_diff(dictionaries_one, dictionaries_two, format_name)
        assert result == ('{\n..+ host: hexlet.io\n....timeout: 20\n..'
                          '- verbose: true\n..+ verbose: false\n}')

    def test_default_stylish_format(self):
        dictionaries_one = {"timeout": 20, "verbose": True}
        dictionaries_two = {"timeout": 20, "verbose": False,
                            "host": "hexlet.io"}
        result = generate_diff(dictionaries_one, dictionaries_two)
        assert result == ('{\n..+ host: hexlet.io\n....timeout: 20\n..'
                          '- verbose: true\n..+ verbose: false\n}')

    def test_plain_format(self):
        format_name = 'plain'
        dictionaries_one = {"timeout": 20, "verbose": True}
        dictionaries_two = {"timeout": 20, "verbose": False,
                            "host": "hexlet.io"}
        result = generate_diff(dictionaries_one, dictionaries_two, format_name)
        print(result)
        assert result == ("Property 'host' was added with value: 'hexlet.io'"
                          "\nProperty 'verbose' was updated. "
                          "From true to false")

    def test_json_format(self):
        format_name = 'json'
        dictionaries_one = {"timeout": 20, "verbose": True}
        dictionaries_two = {"timeout": 20, "verbose": False,
                            "host": "hexlet.io"}
        correct_jason = '''{
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
}'''
        result = generate_diff(dictionaries_one, dictionaries_two, format_name)
        assert result == correct_jason
