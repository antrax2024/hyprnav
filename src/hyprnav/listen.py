import os
import sys
from hyprpy import Hyprland
from typing import Any
from hyprnav.config import AppConfig
from hyprnav.window import showWorkspace
from hyprnav.util import printLog
from playsound3 import playsound

try:
    instance = Hyprland()
except Exception as e:
    printLog(f"[red]Error connecting to Hyprland: {e}[/red]")
    sys.exit(1)

appConfig = AppConfig()


audioFileOK = False  # by default we assume the audio file is not ok
iterations: int = 0  # number of iterations to wait for the workspace to be ready

if appConfig.sound.enabled:
    # check if appConfig.sound.file exists
    if not os.path.exists(appConfig.sound.file):
        printLog(f"[red]Audio file not found: {appConfig.sound.file}[/red]")
        sys.exit(1)
    else:
        # now the audio is ok
        audioFileOK = True


def playSound() -> None:
    if audioFileOK:
        playsound(appConfig.sound.file, block=False)


def onWorkspaceChanged(sender: Any, **kwargs) -> None:
    """Handle workspace change events"""
    workspaceId = kwargs.get("workspace_id")
    workspaceName: str = str(kwargs.get("workspace_name"))

    # Increment iterations counter before printing
    global iterations
    iterations += 1

    printLog(
        f"{iterations}\t: [bold yellow]Workspace[/bold yellow]: id: {workspaceId} name: {workspaceName}"
    )

    if audioFileOK:
        playSound()

    showWorkspace(workspaceID=workspaceName)


def listen() -> None:
    """Listen for workspace changes and show a window."""
    try:
        # Connect to the Hyprland signals
        instance.signals.workspacev2.connect(onWorkspaceChanged)
        instance.watch()
    except KeyboardInterrupt:
        printLog("[green]Interrupt by user. Exiting...[/green]")
        return
