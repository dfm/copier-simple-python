import pytest
from helpers import generate_project
from plumbum import local


@pytest.mark.parametrize("extra_data", [{}, {"c_or_cpp_support": True}])
def test_pre_commit(extra_data):
    with generate_project(**extra_data):
        local["pre-commit"]("run", "--all-files")


# @pytest.mark.parametrize("extra_data", [{}, {"c_or_cpp_support": True}])
def test_template_tests():
    with generate_project(c_or_cpp_support=True):
        local.python("-m", "nox", "-s", "tests")
