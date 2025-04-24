import os
import shutil
from typing import Any
from confz import BaseConfig, FileSource
from .constants import APP_NAME, APP_VERSION, DEFAULT_CONFIG_FILE, DEFAULT_STYLE_FILE
import importlib.resources
from rich.console import Console


cl = Console()


def printMessage(preamble: str, variable: Any) -> None:
    """
    Print a message to the console with fixed width preamble.
    """
    cl.print(f"[bold yellow]{preamble:<15}[/bold yellow]: {variable}")


def ensureConfigFiles() -> None:
    """
    Ensure that all required configuration files exist.
    This function must be called before any AppConfig instances are created.
    """
    # Check if the config file exists
    checkFile(file=DEFAULT_CONFIG_FILE)
    # Check if the style file exists
    checkFile(file=DEFAULT_STYLE_FILE)


def cli() -> None:
    cl.print(f"[bold yellow]{APP_NAME} v{APP_VERSION}[/bold yellow]\n")
    cl.print("[cyan]=[/cyan]" * 80)
    # Display configuration information
    printMessage(preamble="Config", variable=DEFAULT_CONFIG_FILE)
    printMessage(preamble="Style", variable=DEFAULT_STYLE_FILE)
    # Check if sound if Enabled
    appConfig = AppConfig()
    printMessage(
        preamble="Audio File",
        variable=(f"{appConfig.sound.file}"),
    )
    printMessage(
        preamble="Enabled",
        variable=("[green]Yes[/green]" if appConfig.sound.enabled else "[red]No[/red]"),
    )

    cl.print("[cyan]=[/cyan]" * 80)


def checkFile(file: str) -> None:
    if not os.path.exists(path=file):
        os.makedirs(name=os.path.dirname(p=file), exist_ok=True)
        copyFile(destination=file)


def copyFile(destination) -> None:
    destinationDir = os.path.dirname(destination)

    # Extract only the filename from destination variable
    filename = os.path.basename(destination)

    source = importlib.resources.files(anchor="hyprnav").joinpath(f"assets/{filename}")
    # Convert Traversable to string path and copy the file
    shutil.copy2(
        src=str(object=source),
        dst=destination,
    )


class Sound(BaseConfig):
    """
    Sound configuration class.
    """

    enabled: bool  # Whether sound is enabled
    file: str  # Path to the sound file


# Main Window
class MainWindow(BaseConfig):
    width: int  # Width of the window
    height: int  # Height of the window
    duration: int  # Duration of the transition in milliseconds


# Main configuration class
class AppConfig(BaseConfig):
    CONFIG_SOURCES = FileSource(
        file=os.path.join(
            os.path.expanduser(path="~"), ".config", f"{APP_NAME}", "config.yaml"
        )
    )
    main_window: MainWindow  # Main Window
    sound: Sound  # Sound configuration
