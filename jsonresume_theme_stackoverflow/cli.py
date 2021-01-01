from pprint import pprint
import json

from jinja2 import Environment, FileSystemLoader, select_autoescape

from . import templates_path, resume_path, render_path
from .filters import format_date


def entrypoint():
    # Load the template from the local environment with the format_date filter.
    env = Environment(loader=FileSystemLoader(templates_path), autoescape=select_autoescape(['html']))
    env.filters["format_date"] = format_date
    template = env.get_template('stackoverflow.html.j2')

    # Get the resume payload the render the resume with it.
    with open(resume_path, 'rt') as f:
        payload = json.load(f)
    with open(render_path, 'wt') as f:
        f.write(template.render(payload))
