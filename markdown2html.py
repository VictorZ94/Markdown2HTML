#!/usr/bin/python3
""" Convert Markdown to HTML file
"""
from sys import argv
from sys import stderr


if __name__ == "__main__":
    """ Convert Markdown to HTML file
    """
    large = len(argv[1:])
    if large < 2:
        print("Usage: ./markdown2html.py README.md README.html",
              file=stderr)
        exit(1)
    try:
        with open('{}'.format(argv[1])) as my_file:
            pass
    except IOError:
        print("Missing {}".format(argv[1]), file=stderr)
        exit(1)
