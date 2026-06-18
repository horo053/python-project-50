import json


def format(diff_tree):
    return json.dumps(diff_tree, indent=2, default=str)