import typer
from genplib.modules import toml_init
import os

app = typer.Typer()

@app.callback(invoke_without_command=True)
def main():
    pass

@app.command()
def init() -> None:
    name = input("Введите имя вашей новой библиотеки: ")
    version = input("Введите версию вашей новой библиотеки (например: 0.1.0): ")
    description = input("Введите описание вашей библиотеки (необязательно): ")
    pyproject_pth = os.path.join('.', 'pyproject.toml')
    if os.path.exists(pyproject_pth):
        answer = input("Похоже, что в текущей директории уже создан файл pyproject.toml, перезаписать? [y/N] ").replace('', 'n')
        if answer.strip().lower() in ["y", "д"]:
            toml_init.init(name=name, version=version, description=description, pyproject_toml_path=pyproject_pth)
        else:
            print("Перезапись отменена")
            return
    else:
        toml_init.init(name=name, version=version, description=description, pyproject_toml_path=pyproject_pth)

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