from hyprpy import Hyprland
from .window import showWorkspaceWindow

instance = Hyprland()


def on_workspace_changed(sender, **kwargs) -> None:
    workspace_name = kwargs.get("workspace_name")
    print(kwargs)
    print(f"Workspace changed: {workspace_name}")
    showWorkspaceWindow(workspace=workspace_name, delay=500)  # type: ignore


def listen() -> None:
    """Listen for workspace changes and show a window."""
    # Connect to the Hyprland signals
    instance.signals.workspacev2.connect(on_workspace_changed)
    instance.watch()
