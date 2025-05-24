# - This is a Python 3.13 application
# - Enforce static typing (type hints) in all functions
# - Enable rich terminal output using `rich`
# - Manage Python dependencies and builds with `uv`
# - Adhere to PEP8 code style standards
# - Maintain English-only documentation and code comments
# - Apply camelCase convention for variables, methods and functions
# **Note**: While camelCase conflicts with PEP8's snake_case recommendation
# for Python, this requirement takes precedence per project specifications
import threading


def main() -> None:
    # Import modules that require configuration only after configs are initialized
    from hyprnav.config import ensureConfigFiles
    from hyprnav.config import cli
    from hyprnav.listen import listen
    from hyprnav.window import startGtkLoop

    # Ensure config files exist before importing modules that use them
    ensureConfigFiles()

    # Run the application
    cli()
    threading.Thread(target=listen, daemon=True).start()
    startGtkLoop()
