import os
from typing import Any
from rich.console import Console
from .config import checkFile
from .constants import (
    APP_NAME,
    APP_VERSION,
    DEFAULT_CONFIG_FILE,
    DEFAULT_STYLE_FILE,
)
from .config import AppConfig

cl = Console()


def printMessage(preamble: str, variable: Any) -> None:
    """
    Print a message to the console.
    """
    cl.print(f"[bold yellow]" + preamble + f"[/bold yellow]:\t\t{variable}")


def main() -> None:
    try:
        del os.environ["QT_STYLE_OVERRIDE"]
    except KeyError as e:
        cl.print(f"KeyError: {e}")

    cl.print(f"[bold yellow]{APP_NAME} v{APP_VERSION}[/bold yellow]")
    # Check if the config file exists
    checkFile(file=DEFAULT_CONFIG_FILE)
    printMessage("Config", DEFAULT_CONFIG_FILE)
    # Check if the style file exists
    checkFile(file=DEFAULT_STYLE_FILE)
    printMessage("Style", DEFAULT_STYLE_FILE)
    # Check if sound if Enabled
    appConfig = AppConfig()
    printMessage(
        "Sound",
        "[green]enabled[/green]" if appConfig.sound.enabled else "[red]disabled[/red]",
    )
