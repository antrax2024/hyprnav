import os
from rich.console import Console
from .listen import listen

from .config import cli

cl = Console()


def main() -> None:
    try:
        del os.environ["QT_STYLE_OVERRIDE"]
    except KeyError as e:
        cl.print(f"KeyError: {e}")

    cli()
    listen()
