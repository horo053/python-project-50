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


def format(diff_tree, depth=0):
    lines = ['{']
    indent = '  ' * depth

    for key in sorted(diff_tree.keys()):
        node = diff_tree[key]
        node_type = node['type']

        if node_type == 'nested':
            children = node['children']
            nested_lines = format(children, depth + 1).split('\n')
            lines.append(f"{indent}    {key}: {nested_lines[0]}")
            for line in nested_lines[1:-1]:
                lines.append(f"{indent}  {line}")
            lines.append(f"{indent}  {nested_lines[-1]}")

        elif node_type == 'changed':
            old_value = node['old']
            new_value = node['new']

            # Старое значение
            if isinstance(old_value, dict):
                old_formatted = format_value(old_value, depth)
                lines.append(f"{indent}  - {key}: {old_formatted}")
            else:
                old_formatted = 'null' if old_value is None else str(old_value).lower()
                lines.append(f"{indent}  - {key}: {old_formatted}")

            if isinstance(new_value, dict):
                new_formatted = format_value(new_value, depth)
                lines.append(f"{indent}  + {key}: {new_formatted}")
            else:
                new_formatted = 'null' if new_value is None else str(new_value).lower()
                lines.append(f"{indent}  + {key}: {new_formatted}")

        else:
            value = node['value']

            if node_type == 'added':
                prefix = '+ '
                value_indent = f"{indent}  "
            elif node_type == 'removed':
                prefix = '- '
                value_indent = f"{indent}  "
            else:
                prefix = ''
                value_indent = f"{indent}    "

            if isinstance(value, dict):
                formatted_value = format_value(value, depth)
                lines.append(f"{value_indent}{prefix}{key}: {formatted_value}")
            else:
                formatted_value = 'null' if value is None else str(value).lower()
                lines.append(f"{value_indent}{prefix}{key}: {formatted_value}")

    lines.append(indent + '}')
    return '\n'.join(lines)