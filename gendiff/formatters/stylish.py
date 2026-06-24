def format_value(value, depth=0):
    if not isinstance(value, dict):
        if isinstance(value, bool):
            return str(value).lower()
        elif value is None:
            return 'null'
        return str(value)

    indent = '  ' * (depth + 1)
    lines = ['{']
    for key in sorted(value.keys()):
        val = value[key]
        if isinstance(val, dict):
            nested = format_value(val, depth + 1).split('\n')
            lines.append(f"{indent}{key}: {nested[0]}")
            for line in nested[1:-1]:
                lines.append(f"{indent}  {line}")
            lines.append(f"{indent}{nested[-1]}")
        else:
            formatted_val = 'null' if val is None else str(val).lower()
            lines.append(f"{indent}{key}: {formatted_val}")
    lines.append('  ' * depth + '}')
    return '\n'.join(lines)


def _format_node_value(value, depth):
    if isinstance(value, dict):
        return format_value(value, depth)
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return str(value)


def _format_leaf_node(key, node, depth):
    node_type = node['type']
    value = node['value']

    if node_type == 'added':
        prefix = '+ '
        indent = '  ' + '  ' * depth
    elif node_type == 'removed':
        prefix = '- '
        indent = '  ' + '  ' * depth
    else:  # unchanged
        prefix = ''
        indent = '    ' + '  ' * depth

    formatted_value = _format_node_value(value, depth + 1)
    return f"{indent}{prefix}{key}: {formatted_value}"


def _format_changed_node(key, node, depth):
    indent = '  ' + '  ' * depth
    old_value = node['old']
    new_value = node['new']

    old_formatted = _format_node_value(old_value, depth + 1)
    new_formatted = _format_node_value(new_value, depth + 1)

    return [
        f"{indent}- {key}: {old_formatted}",
        f"{indent}+ {key}: {new_formatted}"
    ]


def _format_nested_node(key, node, depth):
    indent = '  ' + '  ' * depth
    children = node['children']
    nested_lines = format(children, depth + 1).split('\n')

    lines = [f"{indent}  {key}: {nested_lines[0]}"]
    for line in nested_lines[1:-1]:
        lines.append(f"{indent}{line}")
    lines.append(f"{indent}{nested_lines[-1]}")
    return lines


def format(diff_tree, depth=0):
    lines = ['{']

    for key in sorted(diff_tree.keys()):
        node = diff_tree[key]
        node_type = node['type']

        if node_type == 'nested':
            lines.extend(_format_nested_node(key, node, depth))
        elif node_type == 'changed':
            lines.extend(_format_changed_node(key, node, depth))
        else:
            lines.append(_format_leaf_node(key, node, depth))

    lines.append('}')
    return '\n'.join(lines)