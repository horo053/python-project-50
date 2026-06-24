def format_value(value, depth=0):
    if not isinstance(value, dict):
        if isinstance(value, bool):
            return str(value).lower()
        elif value is None:
            return 'null'
        return str(value)

    indent = '  ' * depth
    lines = ['{']
    for key in sorted(value.keys()):
        val = value[key]
        if isinstance(val, dict):
            nested = format_value(val, depth + 1).split('\n')
            lines.append(f"{indent}  {key}: {nested[0]}")
            for line in nested[1:-1]:
                lines.append(f"{indent}    {line}")
            lines.append(f"{indent}  {nested[-1]}")
        else:
            formatted_val = 'null' if val is None else str(val).lower()
            lines.append(f"{indent}  {key}: {formatted_val}")
    lines.append(indent + '}')
    return '\n'.join(lines)


def _format_simple_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    return str(value)


def _format_node_value(value, depth):
    if isinstance(value, dict):
        return format_value(value, depth)
    return _format_simple_value(value)


def _get_indent_and_prefix(node_type, depth):
    if node_type == 'added':
        return '  ' * depth + '  ', '+ '
    elif node_type == 'removed':
        return '  ' * depth + '  ', '- '
    else:
        return '  ' * depth + '    ', ''


def _format_changed_node(key, old_value, new_value, depth):
    indent = '  ' * depth
    old_formatted = _format_node_value(old_value, depth + 1)
    new_formatted = _format_node_value(new_value, depth + 1)
    return [
        f"{indent}  - {key}: {old_formatted}",
        f"{indent}  + {key}: {new_formatted}"
    ]


def _format_nested_node(key, children, depth):
    indent = '  ' * depth
    nested_lines = format(children, depth + 1).split('\n')
    lines = [f"{indent}    {key}: {nested_lines[0]}"]
    for line in nested_lines[1:-1]:
        lines.append(f"{indent}  {line}")
    lines.append(f"{indent}  {nested_lines[-1]}")
    return lines


def _format_leaf_node(key, node, depth):
    node_type = node['type']
    indent, prefix = _get_indent_and_prefix(node_type, depth)
    value = node['value']
    formatted_value = _format_node_value(value, depth + 1)
    return f"{indent}{prefix}{key}: {formatted_value}"


def format(diff_tree, depth=0):
    lines = ['{']

    for key in sorted(diff_tree.keys()):
        node = diff_tree[key]
        node_type = node['type']

        if node_type == 'nested':
            lines.extend(_format_nested_node(key, node['children'], depth))
        elif node_type == 'changed':
            lines.extend(_format_changed_node(key, node['old'], node['new'], depth))
        else:
            lines.append(_format_leaf_node(key, node, depth))

    lines.append('  ' * depth + '}')
    return '\n'.join(lines)