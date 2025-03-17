from os import getenv
from pathlib import Path

def get_gh_variable(env_var: str) -> str:

    local_env_vars = {
        "GITHUB_OUTPUT":"./github_output",
        "GITHUB_ENV":"./github_env"
    }

    CI = getenv("CI")
    if(CI):
        value = getenv(env_var)
    else:
        value = local_env_vars[env_var]
        file_path = Path(value)
        if not file_path.exists():
                file_path.write_text("##### LOCAL TEST FILE #####\n")

    return value

def write_gha_file(line: str, file: str) -> None:
    file_path = Path(file).open("a")
    file_path.write(f"{line}\n")

def set_gha_output(entry: str, value: str) -> None:
    output = get_gh_variable("GITHUB_OUTPUT")
    write_gha_file(f"{entry}={value}", output)

def set_gha_env(entry, value) -> None:
    output = get_gh_variable("GITHUB_ENV")
    write_gha_file(f"{entry}={value}", output)