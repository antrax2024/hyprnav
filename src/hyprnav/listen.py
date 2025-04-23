import os
import pygame
from hyprpy import Hyprland
from .window import showWorkspaceWindow
from rich.console import Console
from .config import AppConfig


# initialize console with custom log‐time format
cl: Console = Console(log_time=True, log_time_format="%Y-%m-%d %H:%M:%S")
instance = Hyprland()
# Inicializar o mixer do pygame
appConfig = AppConfig()
# --- sound setup ---
if appConfig.sound.enabled:
    # Expand the path in case it contains ~ to ensure proper file access
    wavFile = appConfig.sound.file
    # Start pygame mixer
    try:
        pygame.mixer.init()
        # Load the sound file
        transitionSound = pygame.mixer.Sound(wavFile)
    except pygame.error as e:
        cl.print(
            f"[red]Error loading sound file: {wavFile}. Make sure the file exists and is a valid sound file.[/red]"
        )
        cl.print(f"[red]{e}[/red]")
        exit(1)


def onWorkspaceChanged(sender, **kwargs) -> None:
    workspace_id = kwargs.get("workspace_id")
    workspace_name = kwargs.get("workspace_name")
    cl.log(
        f"[bold yellow]Workspace[/bold yellow]: id: {workspace_id} name: {workspace_name}"
    )
    # Parar qualquer som em reprodução e iniciar novo
    if appConfig.sound.enabled:
        try:
            pygame.mixer.stop()
            transitionSound.play()  # type: ignore
        except pygame.error as e:
            cl.print(
                f"[red]Error playing sound: {wavFile}. Make sure the file exists and is a valid sound file.[/red]"
            )
            cl.print(f"[red]{e}[/red]")
            exit(1)

    showWorkspaceWindow(workspace=workspace_name, delay=appConfig.main_window.duration)  # type: ignore


def listen() -> None:
    """Listen for workspace changes and show a window."""
    try:
        # Connect to the Hyprland signals
        instance.signals.workspacev2.connect(onWorkspaceChanged)
        instance.watch()
    except KeyboardInterrupt:
        cl.print("[green]Interrupt by user. Exiting...[/green]")
        return
    finally:
        pygame.mixer.quit()
