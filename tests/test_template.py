import platform

import pytest
from helpers import generate_project
from plumbum import local


@pytest.mark.parametrize("extra_data", [{}, {"c_or_cpp_support": True}])
def test_pre_commit(extra_data):
    with generate_project(**extra_data):
        local["pre-commit"]("run", "--all-files")


@pytest.mark.parametrize("extra_data", [{}, {"c_or_cpp_support": True}])
def test_template_tests(extra_data):
    python_version = platform.python_version_tuple()
    python_version = ".".join(python_version[:2])
    print(python_version)
    with generate_project(**extra_data):
        local.python(
            "-m", "nox", "--verbose", "--python", python_version, "-s", "tests"
        )
