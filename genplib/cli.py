import typer
import tomlkit
from genplib.modules import init as lib_init, set_parameters as set_params
import os

app = typer.Typer()
app_set = typer.Typer()
app_set_dependencies = typer.Typer()

app.add_typer(app_set, name="set")
app_set.add_typer(app_set_dependencies, name="dependencies")

@app.callback(invoke_without_command=True)
def callback_main(): pass
@app_set.callback(invoke_without_command=True)
def callback_set(): pass
@app_set_dependencies.callback(invoke_without_command=True)
def callback_set_dependencies(): pass

@app.command()
def init() -> None:
    name = input("Введите имя вашей новой библиотеки: ")
    if name.strip():
        pass
    else:
        print("ERROR: Название библиотеки не может быть пустым")
        return
    version = input("Введите версию вашей новой библиотеки (например: 0.1.0): ")
    description = input("Введите описание вашей библиотеки (необязательно): ")
    readme = input("Добавлять README.md? [Y/n] ").strip().lower()
    if readme in ['y', 'д'] or not readme:
        readme = True
    else:
        readme = False
    print("\nСоздание файла pyproject.toml... [1 / 2]")
    pyproject_pth = os.path.join('.', 'pyproject.toml')
    if os.path.exists(pyproject_pth):
        answer = input("Внимание! В директории уже имеется файл pyproject.toml, перезаписать? [y/N] ").strip().lower()
        if not answer:
            answer = "n"
        if answer in ["y", "д"]:
            lib_init.init_pyproject(name=name, version=version, description=description, pyproject_toml_path=pyproject_pth)
        else:
            print("Перезапись отменена")
            return
    else:
        lib_init.init_pyproject(name=name, version=version, description=description, pyproject_toml_path=pyproject_pth)
    print("\nСоздание рабочей области [2 / 2]")
    if os.listdir('.') != ['pyproject.toml']:
        answer = input("В директории есть другие файлы, точно записать? [y/N] ").strip().lower()
        if not answer:
            answer = "n"
        if answer in ["y", "д"]:
            lib_init.init_workspace('.', name, readme)
    else:
        lib_init.init_workspace('.', name, readme)

@app_set.command()
def name(
    name_: str
):
    pyproject_pth = os.path.join('.', 'pyproject.toml')
    if os.path.exists(pyproject_pth):
        with open(pyproject_pth, "r+", encoding="utf-8") as f:
            document = tomlkit.load(f)
            old_name = document.get("project", {}).get("name")
            set_params.set(document, "project", "name", name_)
            f.seek(0)
            tomlkit.dump(document, f)
            f.truncate()
        if old_name and os.path.exists(os.path.join(".", old_name)):
            os.rename(os.path.join(".", old_name), os.path.join(".", name_))
@app_set.command()
def version(
    version_: str
):
    pyproject_pth = os.path.join('.', 'pyproject.toml')
    if os.path.exists(pyproject_pth):
        with open(pyproject_pth, "r+", encoding="utf-8") as f:
            document = tomlkit.load(f)
            set_params.set(document, 'project', 'version', version_)
            f.seek(0)
            tomlkit.dump(document, f)
            f.truncate()

@app_set.command()
def description(
    description_: str
):
    pyproject_pth = os.path.join('.', 'pyproject.toml')
    if os.path.exists(pyproject_pth):
        with open(pyproject_pth, "r+", encoding="utf-8") as f:
            document = tomlkit.load(f)
            set_params.set(document, 'project', 'description', description_)
            f.seek(0)
            tomlkit.dump(document, f)
            f.truncate()

@app_set_dependencies.command()
def add(
    lib: str
):
    pyproject_pth = os.path.join('.', 'pyproject.toml')
    if os.path.exists(pyproject_pth):
        with open(pyproject_pth, "r+", encoding="utf-8") as f:
            document = tomlkit.load(f)
            lib_list = document.get('project', {}).get('dependencies', [])
            if lib in lib_list:
                return
            else:
                lib_list.append(lib)
                set_params.set(document, 'project', 'dependencies', lib_list)
                f.seek(0)
                tomlkit.dump(document, f)
                f.truncate()

@app_set_dependencies.command()
def pop(
    lib: str
):
    pyproject_pth = os.path.join('.', 'pyproject.toml')
    if os.path.exists(pyproject_pth):
        with open(pyproject_pth, "r+", encoding="utf-8") as f:
            document = tomlkit.load(f)
            lib_list = document.get('project', {}).get('dependencies', [])
            if lib not in lib_list:
                return
            else:
                lib_list.remove(lib)
                set_params.set(document, 'project', 'dependencies', lib_list)
                f.seek(0)
                tomlkit.dump(document, f)
                f.truncate()

def fallback():
    print("ERROR: Вы ввели несуществующую команду")


def run():
    try:
        app(standalone_mode=False)
    except Exception as e:
        if "No such command" in str(e):
            fallback()
        else:
            raise