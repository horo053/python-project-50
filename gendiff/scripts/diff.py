from ..formatters import json_formatter, plain, stylish


def build_diff(d1, d2):
    keys = sorted(set(d1) | set(d2))
    diff = {}
    for key in keys:
        if key not in d1:
            diff[key] = {'type': 'added', 'value': d2[key]}
        elif key not in d2:
            diff[key] = {'type': 'removed', 'value': d1[key]}
        else:
            val1 = d1[key]
            val2 = d2[key]
            if isinstance(val1, dict) and isinstance(val2, dict):
                diff[key] = {'type': 'nested',
                             'children': build_diff(val1, val2)}
            elif val1 != val2:
                diff[key] = {'type': 'changed', 'old': val1, 'new': val2}
            else:
                diff[key] = {'type': 'unchanged', 'value': val1}
    return diff


def generate_diff(dict1, dict2, format_name='stylish'):
    diff_tree = build_diff(dict1, dict2)

    if format_name == 'stylish':
        return stylish.format(diff_tree)
    elif format_name == 'plain':
        return plain.format(diff_tree)
    elif format_name == 'json':
        return json_formatter.format(diff_tree)

    return None
