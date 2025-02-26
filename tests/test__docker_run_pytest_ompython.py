import os
import subprocess

import pytest


def test__docker_run_pytest_ompython():
    # docker run --rm --volume "$HOME:${{ github.workspace }}" --env "HOME=${{ github.workspace }}" --workdir "$PWD" --user $UID openmodelica/openmodelica:v1.24.4-ompython python -m pytest tests/test__check_ompython.py
    p = subprocess.run(
        (
            "docker", "run", "--rm",
            "--volume", f"{os.environ['HOME']}:{os.environ['GITHUB_WORKSPACE']}",
            "--env", f"HOME={os.environ['GITHUB_WORKSPACE']}",
            "--workdir", f"{os.environ['PWD']}",
            "--user", f"{os.getuid()}",
            "openmodelica/openmodelica:v1.24.4-ompython",
            "python", "-m",
                "pytest", "--version",
        ),
        capture_output=True,
        text=True,
    )
    # could successfully run the command
    assert p.returncode == 0, (
        '\n'
        f"Return code: {p.returncode}\n"
        f"stdout:\n{p.stdout}\n"
        f"stderr:\n{p.stderr}"
    )


def test__docker_run_pytest_omc():
    # docker run --rm --volume "$HOME:${{ github.workspace }}" --env "HOME=${{ github.workspace }}" --workdir "$PWD" --user $UID openmodelica/openmodelica:v1.24.4-ompython python -m pytest tests/test__check_ompython.py
    p = subprocess.run(
        (
            "docker", "run", "--rm",
            "--volume", f"{os.environ['HOME']}:{os.environ['GITHUB_WORKSPACE']}",
            "--env", f"HOME={os.environ['GITHUB_WORKSPACE']}",
            "--workdir", f"{os.environ['PWD']}",
            "--user", f"{os.getuid()}",
            "openmodelica/openmodelica:v1.24.4-ompython",
            "omc", "--version",
        ),
        capture_output=True,
        text=True,
    )
    # could successfully run the command
    assert p.returncode == 0, (
        '\n'
        f"Return code: {p.returncode}\n"
        f"stdout:\n{p.stdout}\n"
        f"stderr:\n{p.stderr}"
    )


def test__docker_run_pytest_omc_compile_export_fmu():
    # docker run --rm --volume "$HOME:${{ github.workspace }}" --env "HOME=${{ github.workspace }}" --workdir "$PWD" --user $UID openmodelica/openmodelica:v1.24.4-ompython python -m pytest tests/test__check_ompython.py
    p = subprocess.run(
        (
            "docker", "run", "--rm",
            "--volume", f"{os.environ['HOME']}:{os.environ['GITHUB_WORKSPACE']}",
            "--env", f"HOME={os.environ['GITHUB_WORKSPACE']}",
            "--workdir", f"{os.environ['PWD']}",
            "--user", f"{os.getuid()}",
            "openmodelica/openmodelica:v1.24.4-ompython",
            "omc", "exportFMU.mos",
        ),
        capture_output=True,
        text=True,
    )
    # could successfully run the command
    assert p.returncode == 0, (
        '\n'
        f"Return code: {p.returncode}\n"
        f"stdout:\n{p.stdout}\n"
        f"stderr:\n{p.stderr}"
    )


if "__main__" == __name__:
    pytest.main([__file__])
