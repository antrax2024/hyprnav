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
