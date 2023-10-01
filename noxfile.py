import nox


@nox.session
def tests(session):
    session.install("copier", "plumbum", "pytest", "nox")
    session.run("pytest", "-v", *session.posargs)
