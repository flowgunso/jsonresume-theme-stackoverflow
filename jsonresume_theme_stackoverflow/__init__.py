from pathlib import Path

base_dir = Path(__file__).parent.parent
templates_path = base_dir.joinpath('jsonresume_theme_stackoverflow', 'templates')
resume_path = base_dir.joinpath('resume.json')
render_path = base_dir.joinpath('resume.html')
