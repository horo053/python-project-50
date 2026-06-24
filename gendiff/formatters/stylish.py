import itertools


map_type_to_sign = {
    'unchanged': ' ',
    'nested': ' ',
    'removed': '-',
    'added': '+',
}


def get_indent(depth, indent_type=' ', indent_size=4, offset=0):
    current_indent_size = depth * indent_size
    return indent_type * current_indent_size + (indent_type * offset)


def stringify(tree, depth):

    if isinstance(tree, dict):
        brace_indent = get_indent(depth + 1)
        deep_indent = get_indent(depth + 1, offset=2)
        formatted_values = []
        for key, value in tree.items():
            formatted_values.append(
                '{}  {}: {}'.format(
                    deep_indent,
                    key,
                    stringify(value, depth + 1),
                )
            )
        return '{{{}}}'.format(
            '\n' + '\n'.join(formatted_values) + '\n' + brace_indent
        )
    if tree is None:
        return 'null'
    if isinstance(tree, str):
        return tree
    return str(tree).lower()


def walk(tree, depth):
    brace_indent = get_indent(depth)
    deep_indent = get_indent(depth, offset=2)
    lines = []
    if not isinstance(tree, list) and not isinstance(tree, dict):
        return str(tree)
    for node in tree:
        if node['type'] == 'nested':
            lines.append('{}{} {}: {}'.format(
                deep_indent, map_type_to_sign['nested'],
                node['key'],
                walk(node['children'], depth + 1)
            ))
            continue
        if node['type'] == 'changed':
            lines.append('{}{} {}: {}'.format(
                deep_indent,
                map_type_to_sign['removed'],
                node['key'],

                stringify(
                    node['old_value'],
                    depth,
                )
            ))
            lines.append('{}{} {}: {}'.format(
                deep_indent,
                map_type_to_sign['added'],
                node['key'],
                stringify(
                    node['new_value'],
                    depth,
                )
            ))
            continue

        lines.append('{}{} {}: {}'.format(
            deep_indent,
            map_type_to_sign[node['type']],
            node['key'],
            stringify(
                node['value'],
                depth,
            )
        ))

    formatted_diff = itertools.chain("{", lines, [brace_indent + "}"])
    return '\n'.join(formatted_diff)


def format(nodes):
    return walk(nodes, 0)