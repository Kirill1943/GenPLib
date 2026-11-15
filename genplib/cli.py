import typer
from genplib.modules import init as lib_init
import os

app = typer.Typer()

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