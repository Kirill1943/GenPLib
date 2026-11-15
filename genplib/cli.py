import typer
import tomlkit
from genplib.modules import init as lib_init, set_parameters as set
import os

app = typer.Typer()
app_set = typer.Typer()
app.add_typer(app_set, name="set")

@app.callback(invoke_without_command=True)
def main():
    pass

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
    print("\nСоздание папки с кодом... [2 / 2]")
    if os.listdir('.') != ['pyproject.toml']:
        answer = input("В директории есть другие файлы, точно записать? [y/N] ").strip().lower()
        if not answer:
            answer = "n"
        if answer in ["y", "д"]:
            lib_init.init_workspace('.', name)
    else:
        lib_init.init_workspace('.', name)

@app_set.command()
def name(
    name_: str
):
    pyproject_pth = os.path.join('.', 'pyproject.toml')
    if os.path.exists(pyproject_pth):
        with open(pyproject_pth, "r+", encoding="utf-8") as f:
            document = tomlkit.load(f)
            old_name = document.get("project", {})["name"]
            set.set(document, 'project', 'name', name_)
            f.seek(0)
            f.write("")
            tomlkit.dump(document, f)
    if os.path.exists(os.path.join('.', old_name)):
        os.rename(os.path.join('.', old_name), os.path.join('.', name_))

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