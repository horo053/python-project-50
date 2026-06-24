def format_value(value, depth, indent_size=4):
    if isinstance(value, dict):
        if not value:
            return '{}'
        indent = ' ' * (depth * indent_size)
        lines = []
        for key, val in value.items():
            if isinstance(val, dict):
                lines.append(f"{indent}    {key}: "
                             f"{format_value(val, depth + 1)}")
            else:
                lines.append(f"{indent}    {key}: "
                             f"{format_value(val, depth + 1)}")
        return '{\n' + '\n'.join(lines) + f'\n{indent}}}'
    elif isinstance(value, bool):
        return 'true' if value else 'false'
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return value
    else:
        return str(value)


def format_stylish(diff_tree, depth=0, indent_size=4):
    indent = ' ' * (depth * indent_size)
    lines = []

    for key, node in diff_tree.items():
        node_type = node['type']

        if node_type == 'nested':
            lines.append(f"{indent}    {key}: "
                         f"{format_stylish(node['children'], depth + 1)}")
        elif node_type == 'added':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}  + {key}: {value}")
        elif node_type == 'removed':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}  - {key}: {value}")
        elif node_type == 'changed':
            old_value = format_value(node['old'], depth + 1)
            new_value = format_value(node['new'], depth + 1)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")
        elif node_type == 'unchanged':
            value = format_value(node['value'], depth + 1)
            lines.append(f"{indent}    {key}: {value}")

    if depth == 0:
        return '{\n' + '\n'.join(lines) + '\n}'
    else:
        return '{\n' + '\n'.join(lines) + f'\n{indent}}}'


def format(diff_tree):
    return format_stylish(diff_tree)