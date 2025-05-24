import os
import sys
from hyprpy import Hyprland
from rich.console import Console
from typing import Any
from nava import play
from hyprnav.config import AppConfig
from hyprnav.window import WorkspaceWindow


# initialize console with custom log‐time format
cl: Console = Console(log_time=True, log_time_format="%Y-%m-%d %H:%M:%S")
try:
    instance = Hyprland()
except Exception as e:
    cl.print(f"[red]Error connecting to Hyprland: {e}[/red]")
    sys.exit(1)

appConfig = AppConfig()
workspaceWindow = WorkspaceWindow(config=appConfig)
audioFileOK = False  # by default we assume the audio file is not ok
iterations: int = 0  # number of iterations to wait for the workspace to be ready

if appConfig.sound.enabled:
    # check if appConfig.sound.file exists
    if not os.path.exists(appConfig.sound.file):
        cl.print(f"[red]Audio file not found: {appConfig.sound.file}[/red]")
        sys.exit(1)
    else:
        # now the audio is ok
        audioFileOK = True


def playSound() -> None:
    if audioFileOK:
        play(appConfig.sound.file, async_mode=True, loop=False)


def onWorkspaceChanged(sender: Any, **kwargs) -> None:
    """Handle workspace change events"""
    workspaceId = kwargs.get("workspace_id")
    workspaceName = kwargs.get("workspace_name")

    # Increment iterations counter before printing
    global iterations
    iterations += 1

    cl.print(
        f"{iterations}\t: [bold yellow]Workspace[/bold yellow]: id: {workspaceId} name: {workspaceName}"
    )

    if audioFileOK:
        playSound()

    workspaceWindow.showWorkspace(workspaceID=str(workspaceName))


def listen() -> None:
    """Listen for workspace changes and show a window."""
    try:
        # Connect to the Hyprland signals
        instance.signals.workspacev2.connect(onWorkspaceChanged)
        instance.watch()
    except KeyboardInterrupt:
        cl.print("[green]Interrupt by user. Exiting...[/green]")
        return
