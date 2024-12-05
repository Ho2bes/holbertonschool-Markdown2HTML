#!/usr/bin/env python3
import sys
import os
import re
import hashlib

def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r') as md_file:
        lines = md_file.readlines()

    html_output = []
    in_list = False

    for line in lines:
        line = line.strip()

        # Headings
        if line.startswith('#'):
            heading_level = len(line.split(' ')[0])
            content = line[heading_level + 1:]
            html_output.append(f"<h{heading_level}>{content}</h{heading_level}>")

        # Unordered lists
        elif line.startswith('- '):
            if not in_list:
                html_output.append("<ul>")
                in_list = True
            html_output.append(f"<li>{line[2:]}</li>")

        # Ordered lists
        elif line.startswith('* '):
            if not in_list:
                html_output.append("<ol>")
                in_list = True
            html_output.append(f"<li>{line[2:]}</li>")

        # Closing lists
        else:
            if in_list:
                html_output.append("</ul>" if line.startswith('- ') else "</ol>")
                in_list = False

            # Bold and emphasis
            line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
            line = re.sub(r'__(.*?)__', r'<em>\1</em>', line)

            # MD5 conversion
            line = re.sub(r'\[\[(.*?)\]\]', lambda m: hashlib.md5(m.group(1).encode()).hexdigest(), line)

            # Remove all 'c' or 'C'
            line = re.sub(r'\(\((.*?)\)\)', lambda m: m.group(1).replace('c', '').replace('C', ''), line)

            # Paragraphs and line breaks
            if line:
                html_output.append(f"<p>{line}</p>")

    with open(output_file, 'w') as html_file:
        html_file.write('\n'.join(html_output))

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: ./markdown2html.py README.md README.html", file=sys.stderr)
        sys.exit(1)

    input_file, output_file = sys.argv[1], sys.argv[2]

    if not os.path.exists(input_file):
        print(f"Missing {input_file}", file=sys.stderr)
        sys.exit(1)

    convert_markdown_to_html(input_file, output_file)
    sys.exit(0)
