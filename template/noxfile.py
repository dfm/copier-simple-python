import nox


@nox.session(python=["3.9", "3.10", "3.11", "3.12"])
def tests(session):
    session.install(".[test]")
    session.run("pytest", *session.posargs)


@nox.session
def docs(session: nox.Session):
    session.install(".[docs]")
    with session.chdir("docs"):
        session.run(
            "python",
            "-m",
            "sphinx",
            "-T",
            "-E",
            "-W",
            "--keep-going",
            "-b",
            "dirhtml",
            "-d",
            "_build/doctrees",
            "-D",
            "language=en",
            ".",
            "_build/dirhtml",
        )
