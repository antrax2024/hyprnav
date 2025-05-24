# - This is a Python 3.13 application
# - Enforce static typing (type hints) in all functions
# - Enable rich terminal output using `rich`
# - Manage Python dependencies and builds with `uv`
# - Adhere to PEP8 code style standards
# - Maintain English-only documentation and code comments
# - Apply camelCase convention for variables, methods and functions
# **Note**: While camelCase conflicts with PEP8's snake_case recommendation
# for Python, this requirement takes precedence per project specifications
from hyprnav.config import ensureConfigFiles
import gi

gi.require_version("Gtk", "4.0")
from gi.repository import Gtk  # pyright: ignore # noqa


def main() -> None:
    # Ensure config files exist before importing modules that use them
    ensureConfigFiles()

    # Import modules that require configuration only after configs are initialized
    from hyprnav.config import cli
    from hyprnav.listen import listen

    # Run the application
    cli()
    listen()
