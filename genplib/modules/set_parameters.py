import tomlkit
import tomlkit.items
from typing import Any

def set(document: tomlkit.TOMLDocument, table: tomlkit.items.Table, config: str, value: Any):
    if table not in document:
        document[table] = {}

    document[table][config] = value