import os
from rich.console import Console
from .config import ensureConfigFiles, AppConfig

# Initialize console
cl = Console()


def main() -> None:
    try:
        del os.environ["QT_STYLE_OVERRIDE"]
    except KeyError:
        pass

    # Ensure config files exist before importing modules that use them
    ensureConfigFiles()

    # Import modules that require configuration only after configs are initialized
    from .config import cli
    from .listen import listen

    # Run the application
    cli()
    listen()
