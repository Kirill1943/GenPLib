from rich import print

def show_help():
    print("[#00aaff]Использование:[/] [#8800ff]genplib[/] [[#00aa00]option[/]] [#ffffff]...")
    print("[#ffff00]genplib help[/] - Показывает это меню")
    print("[#ffff00]genplib set name <new-name>[/] - Изменение имени библиотеки")
    print("[#ffff00]genplib set version <new-version>[/] - Изменение версии библиотеки")
    print("[#ffff00]genplib set description <new-description>[/] - Изменение описания библиотеки")
    print("[#ffff00]genplib set dependencies add[/] - Добавление зависимости в проект")
    print("[#ffff00]genplib set dependencies pop[/] - Удаление зависимости из проекта")