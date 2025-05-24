from ctypes import CDLL

from hyprnav.config import AppConfig

CDLL("libgtk4-layer-shell.so")
import gi  # noqa

gi.require_version("Gtk", "4.0")
gi.require_version("Gtk4LayerShell", "1.0")

from gi.repository import Gtk  # pyright: ignore #noqa
from gi.repository import Gtk4LayerShell as LayerShell  # pyright: ignore #noqa
from gi.repository import GLib  # pyright: ignore # noqa
from hyprnav.constants import APP_NAME, APP_VERSION, STYLE_FILE  # pyright: ignore # noqa
from hyprnav.util import printLog  # pyright: ignore # noqa


window: Gtk.Window
workspace_label: Gtk.Label


def onActivate(app):
    global window
    global workspace_label
    printLog("Creating workspace window instance...")
    window = Gtk.Window(application=app)

    appConfig = AppConfig()

    window.set_title(f"{APP_NAME} - v{APP_VERSION}")
    printLog(
        f"set default size to {appConfig.main_window.width}x{appConfig.main_window.height} as config.yaml file"
    )
    window.set_default_size(appConfig.main_window.width, appConfig.main_window.height)

    printLog(f"set css id to{APP_NAME.lower()}...")
    window.set_name("main-window")

    printLog("Setting up style with CSS path: " + STYLE_FILE)
    css_provider = Gtk.CssProvider()
    css_provider.load_from_path(f"{STYLE_FILE}")
    display = window.get_display()
    Gtk.StyleContext.add_provider_for_display(
        display, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )
    printLog("CSS provider loaded")

    printLog("set resizable to False...")
    LayerShell.init_for_window(window)
    LayerShell.set_layer(window, LayerShell.Layer.OVERLAY)

    # Centraliza a janela na tela
    printLog("set window position to center...")
    LayerShell.set_anchor(window, LayerShell.Edge.LEFT, False)
    LayerShell.set_anchor(window, LayerShell.Edge.RIGHT, False)
    LayerShell.set_anchor(window, LayerShell.Edge.TOP, False)
    LayerShell.set_anchor(window, LayerShell.Edge.BOTTOM, False)

    printLog("orientation to vertical...")
    box = Gtk.Box(
        orientation=Gtk.Orientation.VERTICAL,
        spacing=appConfig.main_window.spacing,
    )
    # set box to vertical alignment to center
    printLog("Set box to vertical alignment to center")
    box.set_valign(Gtk.Align.CENTER)
    fixed_label = Gtk.Label(label=appConfig.main_window.label)
    fixed_label.set_name("fixed-label")

    printLog("Append fixed-label to box...")
    box.append(fixed_label)
    workspace_label = Gtk.Label()
    workspace_label.set_name("workspace-label")

    printLog("Append workspace_label to box...")
    box.append(workspace_label)

    printLog("Append box to window...")
    window.set_child(box)

    window.present()  # show the window
    window.set_visible(False)


def showWorkspace(workspaceID: str):
    global workspace_label
    global window
    workspace_label.set_label(f"{workspaceID}")
    window.set_visible(True)
    # Schedule automatic window closing after 300ms
    GLib.timeout_add(300, lambda: window.set_visible(False))


def startGtkLoop() -> None:
    printLog("Instantiate the config Class ")

    # Create the application
    printLog("Create a new Application instance with 'com.antrax.HyprBar' as an id")
    app = Gtk.Application(application_id="com.antrax.hyprnav")
    printLog("Connect to the activate signal of the application")
    app.connect("activate", onActivate)
    printLog("Start the GTK main loop with 'app.run()'")
    try:
        app.run(None)
    except KeyboardInterrupt:
        printLog("KeyboardInterrupt detected. Exiting...")


if __name__ == "__main__":
    printLog("Starting the GTK main loop...")
    startGtkLoop()
