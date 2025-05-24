# - This is a Python 3.13 application
# - Enforce static typing (type hints) in all functions
# - Enable rich terminal output using `rich`
# - Manage Python dependencies and builds with `uv`
# - Adhere to PEP8 code style standards
# - Maintain English-only documentation and code comments
# - Apply camelCase convention for variables, methods and functions
# **Note**: While camelCase conflicts with PEP8's snake_case recommendation
# for Python, this requirement takes precedence per project specifications
import os
from rich.console import Console
from .config import ensureConfigFiles

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
    from hyprnav.config import cli
    from hyprnav.listen import listen

    # Run the application
    cli()
    listen()
