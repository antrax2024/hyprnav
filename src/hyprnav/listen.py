from hyprpy import Hyprland
from .window import showWorkspaceWindow
from rich.console import Console
from playsound3 import playsound
import importlib.resources

cl = Console()
instance = Hyprland()
mp3File = importlib.resources.files("hyprnav").joinpath("assets/transition.wav")


def onWorkspaceChanged(sender, **kwargs) -> None:
    workspace_id = kwargs.get("workspace_id")
    workspace_name = kwargs.get("workspace_name")
    cl.print(
        f"[bold yellow]Workspace[/bold yellow]: id: {workspace_id} name: {workspace_name}"
    )
    playsound(sound=str(mp3File), block=False)
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
