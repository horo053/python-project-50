def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def format(diff_tree, path=''):
    lines = []

    for key in sorted(diff_tree.keys()):
        node = diff_tree[key]
        current_path = f"{path}.{key}" if path else key
        node_type = node['type']
        if node_type == 'added':
            value = format_value(node['value'])
            lines.append(f"Property '{current_path}' "
                         f"was added with value: {value}")
        elif node_type == 'removed':
            lines.append(f"Property '{current_path}' was removed")
        elif node_type == 'changed':
            old_value = format_value(node['old'])
            new_value = format_value(node['new'])
            lines.append(f"Property '{current_path}' "
                         f"was updated. From {old_value} to {new_value}")
        elif node_type == 'nested':
            nested_lines = format(node['children'], current_path)
            if nested_lines:
                lines.append(nested_lines)

    return '\n'.join(lines)