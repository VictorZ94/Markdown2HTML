#!/usr/bin/python3
""" Convert Markdown to HTML file
"""
import sys


if __name__ == "__main__":
    """ Convert Markdown to HTML file
    """
    large = len(sys.argv[1:])
    if large < 2:
        print("Usage: ./markdown2html.py README.md README.html",
              file=sys.stderr)
        exit(1)
    try:
        with open('README.md') as my_file:
            pass
    except IOError:
        print("Missing {}".format(sys.argv[1]), file=sys.stderr)
        exit(1)
