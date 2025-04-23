from hyprpy import Hyprland
from .window import showWorkspaceWindow
from rich.console import Console

cl = Console()
instance = Hyprland()


def onWorkspaceChanged(sender, **kwargs) -> None:
    workspace_id = kwargs.get("workspace_id")
    workspace_name = kwargs.get("workspace_name")
    cl.print(
        f"[bold yellow]Workspace[/bold yellow]:\tid: {workspace_id}\tname: {workspace_name}"
    )
    showWorkspaceWindow(workspace=workspace_name, delay=500)  # type: ignore


def listen() -> None:
    """Listen for workspace changes and show a window."""
    try:
        # Connect to the Hyprland signals
        instance.signals.workspacev2.connect(onWorkspaceChanged)
        instance.watch()
    except KeyboardInterrupt:
        cl.print("[green]Interrupt by user. Exiting...[/green]")
        return
