# Copyright 2023 Dan Foreman-Mackey
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from contextlib import contextmanager
from pathlib import Path
from tempfile import TemporaryDirectory

import nox
from plumbum import local

cp = local["cp"]
git = local["git"]
rm = local["rm"]


def generate_in(session, target, *args, project_name="test package"):
    session.install("copier")
    all_files = git("ls-tree", "--name-only", "HEAD").splitlines()
    # First copy the template to a temporary directory and install from there
    with TemporaryDirectory() as template:
        for file in all_files:
            cp("-r", file, template)

        # Tag a 'test' release in this temporary directory
        with local.cwd(template):
            git("init", ".")
            git("add", ".")
            git(
                "commit",
                "--message=test",
                "--author=Test<test@test>",
                "--no-verify",
            )
            git("tag", "--force", "test")

        # Generate the copy from the temporary copy
        session.run(
            "copier",
            "-f",
            template,
            target,
            "-d",
            f"project_name={project_name}",
            *args,
        )

    # Set up the copy as a git repository for SCM purposes
    with local.cwd(target):
        git("init", ".")
        git("add", ".")


@nox.session
def pre_commit():
    pass
