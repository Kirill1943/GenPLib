import tomlkit
import os

def init(name: str, version: str, pyproject_toml_path: str, description: str = ""):
    document = tomlkit.document()
    project = tomlkit.table()
    project["name"] = name
    project["version"] = version
    project["description"] = description
    document["project"] = project

    path = os.path.abspath(pyproject_toml_path)

    with open(path, "w", encoding="utf-8") as f:
        tomlkit.dump(document, f)