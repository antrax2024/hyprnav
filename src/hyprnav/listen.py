import os
import sys
from hyprpy import Hyprland
from .window import showWorkspaceWindow
from playsound3 import playsound
from rich.console import Console
from .config import AppConfig
from typing import Any

# initialize console with custom log‐time format
cl: Console = Console(log_time=True, log_time_format="%Y-%m-%d %H:%M:%S")
instance = Hyprland()
appConfig = AppConfig()
audioFileOK = False  # by default we assume the audio file is not ok
iterations: int = 0  # number of iterations to wait for the workspace to be ready

if appConfig.sound.enabled:
    # check if appConfig.sound.file exists
    if not os.path.exists(appConfig.sound.file):
        cl.print(f"[red]Audio file not found: {appConfig.sound.file}[/red]")
        sys.exit(1)

    # now the audio is ok
    audioFileOK = True


def playSound() -> None:
    if audioFileOK:
        playsound(sound=f"{appConfig.sound.file}", block=False)


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

    showWorkspaceWindow(workspace=workspaceName, delay=appConfig.main_window.duration)  # type: ignore


def listen() -> None:
    """Listen for workspace changes and show a window."""
    try:
        # Connect to the Hyprland signals
        instance.signals.workspacev2.connect(onWorkspaceChanged)
        instance.watch()
    except KeyboardInterrupt:
        cl.print("[green]Interrupt by user. Exiting...[/green]")
        return
