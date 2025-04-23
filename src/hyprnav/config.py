import os
import shutil
from confz import BaseConfig, FileSource
from .constants import APP_NAME
import importlib.resources
from rich.console import Console

cl = Console()


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


# Main configuration class
class AppConfig(BaseConfig):
    CONFIG_SOURCES = FileSource(
        file=os.path.join(
            os.path.expanduser(path="~"), ".config", f"{APP_NAME}", "config.yaml"
        )
    )
    main_window: MainWindow  # Main Window
    sound: Sound  # Sound configuration
