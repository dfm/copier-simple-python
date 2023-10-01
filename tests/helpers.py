import warnings
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory

from copier import run_copy
from copier.errors import DirtyLocalWarning
from plumbum import local

git = local["git"]


@contextmanager
def generate_project(**data):
    data["project_name"] = data.get("project_name", "example project")
    data["project_description"] = data.get("project_name", "An example project")
    data["author_fullname"] = data.get("author_fullname", "A Python Coder")
    data["author_email"] = data.get("author_email", "coder@python.codes")
    with TemporaryDirectory() as project:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore", DirtyLocalWarning)
            run_copy(".", project, data=data, defaults=True, vcs_ref="HEAD")
        with local.cwd(project):
            git("init", ".")
            git("add", ".")
            git(
                "commit",
                "--message=test",
                "--author=Test<test@test>",
                "--no-verify",
            )
            git("tag", "0.1.0")
            yield Path(project)
