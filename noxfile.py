import nox


@nox.session
def lint(session):
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files", "--show-diff-on-failure")


@nox.session
@nox.parametrize(
    "python,runner",
    [("2.7", "unittest2")]
    + [
        (python, runner)
        for python in ["2.7", "3.7", "3.8", "3.9", "3.10"]
        for runner in ["nose", "nose2", "unittest", "pytest"]
        if (python, runner) != ("3.10", "nose")
    ],
)
def test(session, runner):
    if runner != "unittest":
        session.install(runner)
    session.install("-e", ".")

    if runner == "nose":
        session.run("nosetests")
    elif runner == "nose2":
        session.run("nose2")
    elif runner == "unittest":
        session.run("python", "-m", "unittest")
    elif runner == "unittest2":
        session.run("unit2")
    elif runner == "pytest":
        session.run("pytest")
