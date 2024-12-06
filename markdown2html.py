#!/usr/bin/python3
"""
Markdown2HTML
Converts a Markdown file to an HTML file based on strict syntax rules.
"""

import sys
import os
import re
import hashlib


def markdown_to_html(input_file, output_file):
    """
    Converts the content of a Markdown file into HTML.
    """
    with open(input_file, 'r') as md_file:
        lines = md_file.readlines()

    html_lines = []
    in_list = False
    list_type = None

    for line in lines:
        line = line.strip()

        # Handle Headings
        if line.startswith('#'):
            heading_level = len(line.split(' ')[0])
            content = line[heading_level + 1:].strip()
            html_lines.append(f"<h{heading_level}>{content}</h{heading_level}>")

        # Handle Unordered Lists (-)
        elif line.startswith('- '):
            if not in_list or list_type != "ul":
                if in_list:
                    html_lines.append(f"</{list_type}>")
                html_lines.append("<ul>")
                in_list = True
                list_type = "ul"
            html_lines.append(f"<li>{line[2:].strip()}</li>")

        # Handle Ordered Lists (*)
        elif line.startswith('* '):
            if not in_list or list_type != "ol":
                if in_list:
                    html_lines.append(f"</{list_type}>")
                html_lines.append("<ol>")
                in_list = True
                list_type = "ol"
            html_lines.append(f"<li>{line[2:].strip()}</li>")

        # Handle Plain Text
        else:
            if in_list:
                html_lines.append(f"</{list_type}>")
                in_list = False
            line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)  # Bold
            line = re.sub(r'__(.*?)__', r'<em>\1</em>', line)    # Italic
            line = re.sub(
                r'\[\[(.*?)\]\]',
                lambda m: hashlib.md5(m.group(1).encode()).hexdigest(),
                line
            )  # MD5
            line = re.sub(
                r'\(\((.*?)\)\)',
                lambda m: m.group(1).replace('c', '').replace('C', ''),
                line
            )  # Remove 'C'
            if line:
                html_lines.append(f"<p>{line}</p>")

    if in_list:
        html_lines.append(f"</{list_type}>")

    # Write HTML to output file
    with open(output_file, 'w') as html_file:
        html_file.write('\n'.join(html_lines))


def main():
    """
    Entry point for the script.
    """
    # Check argument count
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_file, output_file = sys.argv[1], sys.argv[2]

    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    # Convert Markdown to HTML
    markdown_to_html(input_file, output_file)
    sys.exit(0)


if __name__ == "__main__":
    main()
