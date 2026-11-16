import tomlkit
import os

def init_pyproject(name: str, version: str, pyproject_toml_path: str, description: str = ""):
    document = tomlkit.document()
    document.add(tomlkit.comment("Этот файл pyproject.toml сгенерирован python-утилитой GenPLib"))
    document.add(tomlkit.comment("Ссылка на репозиторий GenPLib: https://github.com/Kirill1943/GenPLib"))
    document.add(tomlkit.nl())
    build_system = tomlkit.table()
    build_system['requires'] = ['setuptools>=61.0.0']
    build_system['build-backend'] = "setuptools.build_meta"
    project = tomlkit.table()
    project["name"] = name
    project["version"] = version
    project["description"] = description
    project["dependencies"] = []
    project["authors"] = []
    document["build-system"] = build_system
    document["project"] = project

    path = os.path.abspath(pyproject_toml_path)

    with open(path, "w", encoding="utf-8") as f:
        tomlkit.dump(document, f)

def init_workspace(lib_dir: str, lib_name: str, create_readme: bool):
    lib_code_pth = os.path.join(lib_dir, lib_name)
    os.makedirs(lib_code_pth, exist_ok=True)
    with open(os.path.join(lib_code_pth, "__init__.py"), "w", encoding="utf-8"): pass
    if create_readme: 
        with open(os.path.join(lib_dir, 'README.md'), "w", encoding="utf-8") as f: f.write(f"# {lib_name}\n<введите сюда свой README>")