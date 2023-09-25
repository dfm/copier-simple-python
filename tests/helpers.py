from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory

from copier import run_copy
from plumbum import local

git = local["git"]


@contextmanager
def generate_project(**data):
    data["project_name"] = data.get("project_name", "test project")
    data["project_description"] = data.get("project_name", "A test project")
    data["author_fullname"] = data.get("author_fullname", "A Python Coder")
    data["author_email"] = data.get("author_email", "coder@python.codes")
    with TemporaryDirectory() as project:
        run_copy(".", project, data=data, defaults=True)
        with local.cwd(project):
            git("init", ".")
            git("add", ".")
            git(
                "commit",
                "--message=test",
                "--author=Test<test@test>",
                "--no-verify",
            )
            yield Path(project)
