import nox


@nox.session
def tests(session):
    session.install("copier", "plumbum", "pytest", "nox", "pre-commit")
    session.run("pytest", "-v", *session.posargs)
