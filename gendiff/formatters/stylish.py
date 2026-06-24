def format(diff_tree, depth=0):
    lines = ['{']

    for key in sorted(diff_tree.keys()):
        node = diff_tree[key]
        node_type = node['type']
        if node_type == 'added':
            prefix = '+ '
            value = node['value']
            indent = '  ' + '  ' * depth
        elif node_type == 'removed':
            prefix = '- '
            value = node['value']
            indent = '  ' + '  ' * depth
        elif node_type == 'unchanged':
            prefix = ''
            value = node['value']
            indent = '    ' + '  ' * depth
        elif node_type == 'changed':
            indent = '  ' + '  ' * depth
            old_value = node['old']
            new_value = node['new']
            lines.append(f"{indent}- {key}: {str(old_value)}")
            lines.append(f"{indent}+ {key}: {str(new_value)}")
            continue
        elif node_type == 'nested':
            indent = '  ' + '  ' * depth
            children = node['children']
            nested_lines = format(children, depth + 1).split('\n')
            lines.append(f"    {key}: {{")
            for line in nested_lines[1:-1]:
                lines.append('  ' + line)
            lines.append('  }')
            continue

        lines.append(f"{indent}{prefix}{key}: {str(value)}")

    lines.append('}')
    return '\n'.join(lines)