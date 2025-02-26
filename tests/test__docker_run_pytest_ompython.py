import os
import subprocess
from typing import List

import pytest


def docker_run(cmd:List[str]) -> subprocess.CompletedProcess:
    return subprocess.run(
        [
            "docker", "run", "--rm",
            "--volume", f"{os.environ['HOME']}:{os.environ['GITHUB_WORKSPACE']}",
            "--env", f"HOME={os.environ['GITHUB_WORKSPACE']}",
            "--workdir", f"{os.environ['PWD']}",
            "--user", f"{os.getuid()}",
            "openmodelica/openmodelica:v1.24.4-ompython",
        ] + cmd,
        capture_output=True,
        text=True,
    )


def test__docker_run_pytest_ompython():
    # docker run --rm --volume "$HOME:${{ github.workspace }}" --env "HOME=${{ github.workspace }}" --workdir "$PWD" --user $UID openmodelica/openmodelica:v1.24.4-ompython python -m pytest tests/test__check_ompython.py
    p = docker_run(["python", "-m", "pytest", "--version",],)

    assert p.returncode == 0, (
        '\n'
        f"Return code: {p.returncode}\n"
        f"stdout:\n{p.stdout}\n"
        f"stderr:\n{p.stderr}"
    )


def test__docker_run_pytest_omc():
    # docker run --rm --volume "$HOME:${{ github.workspace }}" --env "HOME=${{ github.workspace }}" --workdir "$PWD" --user $UID openmodelica/openmodelica:v1.24.4-ompython python -m pytest tests/test__check_ompython.py
    p = docker_run(["omc", "--version"])
    # could successfully run the command
    assert p.returncode == 0, (
        '\n'
        f"Return code: {p.returncode}\n"
        f"stdout:\n{p.stdout}\n"
        f"stderr:\n{p.stderr}"
    )


def test__docker_run_pytest_omc_compile_export_fmu():
    p_ls = docker_run(["ls"])
    p_ls__home = docker_run(["ls", f"{os.environ['HOME']}"])

    p_pwd = docker_run(["pwd"])

    p = docker_run(["omc", "exportFMU.mos",])
    # could successfully run the command
    assert p.returncode == 0, (
        '\n'
        f"Return code: {p.returncode}\n"
        f"stdout:\n{p.stdout}\n"
        f"stderr:\n{p.stderr}\n"
        f"pwd stdout:\n{p_pwd.stdout}\n"
        f"pwd stderr:\n{p_pwd.stderr}\n"
        f"ls stdout:\n{p_ls.stdout}\n"
        f"ls stderr:\n{p_ls.stderr}\n"
        f"ls__home stdout:\n{p_ls__home.stdout}\n"
        f"ls__home stderr:\n{p_ls__home.stderr}\n"
    )


if "__main__" == __name__:
    pytest.main([__file__])
