import os
import threading
from hyprpy import Hyprland
import shutil
import importlib.resources


def copyFile(destination) -> None:
    # Extract only the filename from destination variable
    filename = os.path.basename(destination)
    # if directory does not exist, create it
    os.makedirs(os.path.dirname(destination), exist_ok=True)

    source = importlib.resources.files(anchor="hyprnav").joinpath(f"assets/{filename}")
    # Convert Traversable to string path and copy the file
    shutil.copy2(
        src=str(object=source),
        dst=destination,
    )


def main() -> None:
    # certify if hyprland is running
    try:
        Hyprland()
    except Exception as e:
        print(f"[red]Error connecting to Hyprland: {e}[/red]")
        return
    from rich.console import Console
    from rich.table import Table
    from hyprnav.constants import APP_NAME, APP_VERSION, CONFIG_FILE, STYLE_FILE
    from hyprnav.util import fileExists, showError

    cl = Console()

    # Run the application
    cl.print(
        f"[bold green]{APP_NAME}[/bold green] [bold blue]{APP_VERSION}[/bold blue]"
    )

    cl.print("Configuration Status...")

    table = Table(show_header=True, header_style="bold cyan")
    table.add_column("Item", justify="right")
    table.add_column("Path")
    table.add_column("Status", justify="center")

    configFileOk = fileExists(file=CONFIG_FILE)
    styleFileOk = fileExists(file=STYLE_FILE)

    if not configFileOk:
        showError(f"{CONFIG_FILE} does not exist. Creating...")
        copyFile(destination=CONFIG_FILE)

    if not styleFileOk:
        showError(f"{STYLE_FILE} does not exists. Creating...")
        copyFile(destination=STYLE_FILE)

    table.add_row(
        "Config",
        f"[yellow]{CONFIG_FILE}[/yellow]",
        f"{'[bold green]Passed[/bold green]' if configFileOk else '[bold red]Fail[/bold red]'}",
    )
    table.add_row(
        "Style",
        f"[yellow]{STYLE_FILE}[/yellow]",
        f"{'[bold green]Passed[/bold green]' if styleFileOk else '[bold red]Fail[/bold red]'}",
    )

    table.add_row(
        "Style",
        f"[yellow]{STYLE_FILE}[/yellow]",
        f"{'[bold green]Passed[/bold green]' if styleFileOk else '[bold red]Fail[/bold red]'}",
    )

    cl.print(table)

    from hyprnav.listen import listen
    from hyprnav.window import startGtkLoop

    threading.Thread(target=listen, daemon=True).start()
    startGtkLoop()
