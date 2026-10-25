import tomllib
from pathlib import Path

ROOT = Path(__file__).parents[2]


def test_pyproject_lists_the_runtime_dependencies_in_requirements_txt() -> None:
    # Vercel installs from pyproject.toml whenever it exists and ignores requirements.txt,
    # so a pyproject without dependencies deploys a function with nothing installed.
    project = tomllib.loads((ROOT / "pyproject.toml").read_text()).get("project", {})
    pinned = [
        line.strip()
        for line in (ROOT / "requirements.txt").read_text().splitlines()
        if line.strip() and not line.startswith("#")
    ]

    assert sorted(project.get("dependencies", [])) == sorted(pinned)