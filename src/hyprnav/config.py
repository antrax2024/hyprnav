import os
from confz import BaseConfig, FileSource
from .constants import APP_NAME


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
    spacing: int = 10  # vertical spacing between widgets
    label: str = "Workspace"  # Label for the window


# Main configuration class
class AppConfig(BaseConfig):
    CONFIG_SOURCES = FileSource(
        file=os.path.join(
            os.path.expanduser(path="~"), ".config", f"{APP_NAME}", "config.yaml"
        )
    )
    main_window: MainWindow  # Main Window
    sound: Sound  # Sound configuration
