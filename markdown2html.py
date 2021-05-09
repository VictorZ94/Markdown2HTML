#!/usr/bin/python3
""" Convert Markdown to HTML file
"""
from sys import argv
from sys import stderr


if __name__ == "__main__":
    """ Convert Markdown to HTML file
    """
    def heading_func(list_of_heading):
        """Function to arrange all heading
        """
        list_final = []
        for i in list_of_heading:
            heading = i.split(' ')[0]
            content = " ".join(i.split()[1:])
            mark = markdown.get(heading)
            list_final.append(mark.format(content))
        return ('\n'.join(list_final) + '\n')

    markdown = {'#': '<h1>{}</h1>',
                '##': '<h2>{}</h2>',
                '###': '<h3>{}</h3>',
                '####': '<h4>{}</h4>',
                '#####': '<h5>{}</h5>',
                '######': '<h6>{}</h6>'}

    large = len(argv[1:])
    if large < 2:
        print("Usage: ./markdown2html.py README.md README.html",
              file=stderr)
        exit(1)
    try:
        with open(f'{argv[1]}') as reader, open(f'{argv[2]}', 'w') as writer:
            list_of_heading = []
            for line in reader:
                list_of_heading.append(line.split('\n')[0])
            writer.write(heading_func(list_of_heading))
    except IOError:
        print("Missing {}".format(argv[1]), file=stderr)
        exit(1)
