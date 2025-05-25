"""
GTK4 LayerShell Window Module for HyprNav

This module creates and manages a GTK4 window using LayerShell for displaying
workspace information as an overlay on Wayland compositors like Hyprland.
The window appears temporarily when workspace changes occur.
"""

from ctypes import CDLL

from hyprnav.config import AppConfig

# Load the GTK4 LayerShell library before importing gi
CDLL("libgtk4-layer-shell.so")
import gi  # noqa

# Require specific versions of GTK and LayerShell
gi.require_version("Gtk", "4.0")
gi.require_version("Gtk4LayerShell", "1.0")

from gi.repository import Gtk  # pyright: ignore #noqa
from gi.repository import Gtk4LayerShell as LayerShell  # pyright: ignore #noqa
from gi.repository import GLib  # pyright: ignore # noqa
from hyprnav.constants import APP_NAME, APP_VERSION, STYLE_FILE  # pyright: ignore # noqa
from hyprnav.util import printLog  # pyright: ignore # noqa

# Global variables to hold the main window and workspace label references
window: Gtk.Window
workspace_label: Gtk.Label


def onActivate(app: Gtk.Application) -> None:
    """
    Callback function executed when the GTK application is activated.

    Creates and configures the main overlay window with LayerShell integration.
    The window is initially hidden and will be shown when workspace changes occur.

    Args:
        app: The GTK Application instance that triggered the activation
    """
    global window
    global workspace_label

    printLog("Creating workspace window instance...")
    window = Gtk.Window(application=app)
    # Initialize LayerShell for the window to create an overlay
    printLog("Initialize LayerShell for the window...")
    LayerShell.init_for_window(window)

    # Center the window on screen by disabling all edge anchors
    printLog("set window position to center...")
    LayerShell.set_anchor(window, LayerShell.Edge.LEFT, False)
    LayerShell.set_anchor(window, LayerShell.Edge.RIGHT, False)
    LayerShell.set_anchor(window, LayerShell.Edge.TOP, False)
    LayerShell.set_anchor(window, LayerShell.Edge.BOTTOM, False)

    # Load application configuration
    appConfig = AppConfig()

    # Set window title with application name and version
    window.set_title(f"{APP_NAME} - v{APP_VERSION}")
    printLog(
        f"set default size to {appConfig.main_window.width}x{appConfig.main_window.height} as config.yaml file"
    )
    window.set_default_size(appConfig.main_window.width, appConfig.main_window.height)

    # Set CSS identifier for styling
    printLog(f"set css id to{APP_NAME.lower()}...")
    window.set_name("main-window")

    # Load and apply CSS styling
    printLog("Setting up style with CSS path: " + STYLE_FILE)
    css_provider = Gtk.CssProvider()
    css_provider.load_from_path(f"{STYLE_FILE}")
    display = window.get_display()
    Gtk.StyleContext.add_provider_for_display(
        display, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )
    printLog("CSS provider loaded")

    LayerShell.set_layer(window, LayerShell.Layer.OVERLAY)

    # Create vertical layout container
    printLog("orientation to vertical...")
    box = Gtk.Box(
        orientation=Gtk.Orientation.VERTICAL,
        spacing=appConfig.main_window.spacing,
    )

    # Center the box vertically within the window
    printLog("Set box to vertical alignment to center")
    box.set_valign(Gtk.Align.CENTER)

    # Create fixed label (static text from config)
    fixed_label = Gtk.Label(label=appConfig.main_window.label)
    fixed_label.set_name("fixed-label")

    # Add fixed label to the layout
    printLog("Append fixed-label to box...")
    box.append(fixed_label)

    # Create workspace label (dynamic text showing current workspace)
    workspace_label = Gtk.Label()
    workspace_label.set_name("workspace-label")

    # Add workspace label to the layout
    printLog("Append workspace_label to box...")
    box.append(workspace_label)

    # Set the box as the window's child widget
    printLog("Append box to window...")
    window.set_child(box)

    # Present the window (make it ready) but keep it hidden initially
    window.present()
    window.set_visible(False)


def showWorkspace(workspaceID: str) -> None:
    """
    Display the workspace overlay with the given workspace ID.

    Shows the window with the workspace information and automatically
    hides it after 300ms using a GLib timeout.

    Args:
        workspaceID: The identifier of the current workspace to display
    """
    global workspace_label
    global window

    # Update the workspace label text
    workspace_label.set_label(f"{workspaceID}")

    # Show the window
    window.set_visible(True)

    # Schedule automatic window hiding after 300ms
    GLib.timeout_add(300, lambda: window.set_visible(False))


def startGtkLoop() -> None:
    """
    Initialize and start the GTK main event loop.

    Creates a GTK Application, connects the activation signal to onActivate,
    and runs the main loop. Handles KeyboardInterrupt gracefully for clean shutdown.
    """
    printLog("Instantiate the config Class ")

    # Create the GTK application with unique application ID
    printLog("Create a new Application instance with 'com.antrax.hyprnav' as an id")
    app = Gtk.Application(application_id="com.antrax.hyprnav")

    # Connect the activate signal to our window creation function
    printLog("Connect to the activate signal of the application")
    app.connect("activate", onActivate)

    # Start the main event loop
    printLog("Start the GTK main loop with 'app.run()'")
    try:
        app.run(None)
    except KeyboardInterrupt:
        printLog("KeyboardInterrupt detected. Exiting...")


if __name__ == "__main__":
    """
    Entry point when the module is run directly.
    Starts the GTK main loop for testing purposes.
    """
    printLog("Starting the GTK main loop...")
    startGtkLoop()
