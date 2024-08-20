from jinja2 import Environment, FileSystemLoader
import subprocess

file_loader = FileSystemLoader('.')
env = Environment(loader=file_loader)
template = env.get_template('README.template.md')

version = subprocess.check_output(['git', 'describe', '--tags']).decode('utf-8').strip()

# Сгенерируйте README
output = template.render(version=version)

with open('README.md', 'w') as f:
    f.write(output)
