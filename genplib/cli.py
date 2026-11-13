import typer

app = typer.Typer()


@app.callback(invoke_without_command=True)
def main():
    pass


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