import os
import re


if __name__ == '__main__':
    if os.path.exists('htmlcov/class_index.html'):
        with open('htmlcov/class_index.html', 'r') as file:
            html_content = file.read()
        table_regex = re.compile(r'<table.*?>(.*?)</table>', re.DOTALL)
        table_match = table_regex.search(html_content)

        if table_match:
            table_html = table_match.group(1)
            with open('tests/README.md', 'w+') as f:
                f.write('<table>' + table_html + '</table>')
