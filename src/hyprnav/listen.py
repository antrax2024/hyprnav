from hyprpy import Hyprland
from .window import showWorkspaceWindow
from rich.console import Console
import pygame
from .config import AppConfig
import importlib.resources


cl = Console()
instance = Hyprland()
# Inicializar o mixer do pygame
appConfig = AppConfig()
# --- sound setup ---
if appConfig.sound.enabled:
    wavFile = importlib.resources.files().joinpath(appConfig.sound.sound_file)
    # Inicializar o mixer do pygame
    pygame.mixer.init()
    # Carregar o som antecipadamente
    transition_sound = pygame.mixer.Sound(str(wavFile))


def onWorkspaceChanged(sender, **kwargs) -> None:
    workspace_id = kwargs.get("workspace_id")
    workspace_name = kwargs.get("workspace_name")
    cl.print(
        f"[bold yellow]Workspace[/bold yellow]: id: {workspace_id} name: {workspace_name}"
    )
    # Parar qualquer som em reprodução e iniciar novo
    if appConfig.sound.enabled:
        pygame.mixer.stop()
        transitionSound.play()  # type: ignore

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
    finally:
        pygame.mixer.quit()
