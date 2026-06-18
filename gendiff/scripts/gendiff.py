import argparse

from .diff import generate_diff
from .parser_for_file import parser_file


def arg_parse():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', type=format,
                        default='stylish', choices=['stylish', 'plain', 'json'],
                        help='set format of output')

    args = parser.parse_args()

    first_file = parser_file(args.first_file)
    second_file = parser_file(args.second_file)

    diff = generate_diff(first_file, second_file, args.format)

    print(diff)


def main():
    arg_parse()


if __name__ == "__main__":
    main()