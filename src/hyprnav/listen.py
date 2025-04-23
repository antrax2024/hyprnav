from hyprpy import Hyprland
from .window import showWorkspaceWindow

instance = Hyprland()


def onWorkspaceChanged(sender, **kwargs) -> None:
    workspace_name = kwargs.get("workspace_name")
    print(kwargs)
    print(f"Workspace changed: {workspace_name}")
    showWorkspaceWindow(workspace=workspace_name, delay=500)  # type: ignore


def listen() -> None:
    """Listen for workspace changes and show a window."""
    try:
        # Connect to the Hyprland signals
        instance.signals.workspacev2.connect(onWorkspaceChanged)
        instance.watch()
    except KeyboardInterrupt:
        print("Interrupt by user. Exiting...")
        return
