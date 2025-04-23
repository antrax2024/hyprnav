import os
import pygame
from hyprpy import Hyprland
from .window import showWorkspaceWindow
from rich.console import Console
from .config import AppConfig


# initialize console with custom log‐time format
cl: Console = Console(log_time=True, log_time_format="%Y-%m-%d %H:%M:%S")
instance = Hyprland()

# Initialize sound variables
transitionSound = None


def initializeSound() -> None:
    """Initialize pygame mixer and load sound if enabled in config."""
    appConfig = AppConfig()

    if appConfig.sound.enabled:
        # Expand the path in case it contains ~ to ensure proper file access
        wavFile = os.path.expanduser(appConfig.sound.file)

        # Start pygame mixer
        try:
            pygame.mixer.init()
            # Load the sound file
            global transitionSound
            transitionSound = pygame.mixer.Sound(wavFile)
        except (pygame.error, FileNotFoundError) as e:
            cl.print(
                f"[red]Warning: Sound file not found at '{wavFile}'. Application will continue without sound effects.[/red]"
            )
            # Set transitionSound to None to indicate sound is not available
            transitionSound = None


def onWorkspaceChanged(sender, **kwargs) -> None:
    appConfig = AppConfig()
    workspace_id = kwargs.get("workspace_id")
    workspace_name = kwargs.get("workspace_name")
    cl.log(
        f"[bold yellow]Workspace[/bold yellow]: id: {workspace_id} name: {workspace_name}"
    )
    # Parar qualquer som em reprodução e iniciar novo
    if appConfig.sound.enabled and transitionSound:
        try:
            pygame.mixer.stop()
            transitionSound.play()
        except Exception as e:
            cl.print(f"[red]Error. Sound file not found!.[/red]")
            cl.print(f"[red]{e}[/red]")

    showWorkspaceWindow(workspace=workspace_name, delay=appConfig.main_window.duration)  # type: ignore


def listen() -> None:
    """Listen for workspace changes and show a window."""
    # Initialize sound system
    initializeSound()

    try:
        # Connect to the Hyprland signals
        instance.signals.workspacev2.connect(onWorkspaceChanged)
        instance.watch()
    except KeyboardInterrupt:
        cl.print("[green]Interrupt by user. Exiting...[/green]")
        return
    finally:
        if pygame.mixer.get_init():
            pygame.mixer.quit()
