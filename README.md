# Generation Python Library

**Generation Python Library (или коротко GenPLib)** - CLI-утилита на Python 3.14, предназначенная для помощи в создании своей Python библиотеки

## Версия и возможности

Текущая версия программы: **0.0.0.alpha6**

### Возможности

* **Команда `help`** - показывает справку
* **Команда `init`** - спрашивает у вас название, версию,  описание будущей библиотеки и создавать ли README.md. И затем **создает** папку с названием библиотеки где находится ее код, README.md (при желании) и pyproject.toml с базовыми настройками
* **Подгруппа `set`** - Предназначена для изменений настроек в pyproject.toml
    * **genplib set name <новое-имя>** - изменяет имя проекта в pyproject.toml
    * **genplib set version <новая-версия>** - изменяет версию проекта в pyproject.toml
    * **genplib set description <новое-описание>** - изменяет описание проекта в pyproject.toml
* **Подгруппа `set dependencies`** - Изменение зависимостей:
    * **genplib set dependencies add <библиотека>** - добавляет зависимость
    * **genplib set dependencies pop <библиотека>** - удаляет зависимость

## Установка

**Важное уточнение:** Библиотека GenPLib еще не выложена на PyPI поэтому ее невозможно установить через `pip install genplib`

Чтобы установить CLI-утилиту вам нужно:

1. **Склонировать** репозиторий и **Перейти** в скачанную директорию:

```bash
git clone https://github.com/Kirill1943/GenPLib
cd GenPLib
```

2. **Установить** библиотеку через pip:

```bash
python -m pip install .
```