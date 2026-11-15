import tomlkit
import os

def init_pyproject(name: str, version: str, pyproject_toml_path: str, description: str = ""):
    document = tomlkit.document()
    project = tomlkit.table()
    project["name"] = name
    project["version"] = version
    project["description"] = description
    document["project"] = project

    path = os.path.abspath(pyproject_toml_path)

    with open(path, "w", encoding="utf-8") as f:
        tomlkit.dump(document, f)

def init_workspace(lib_dir: str, lib_name: str):
    lib_code_pth = os.path.join(lib_dir, lib_name)
    os.makedirs(lib_code_pth, exist_ok=True)
    with open(os.path.join(lib_code_pth, "__init__.py"), "w", encoding="utf-8"): pass