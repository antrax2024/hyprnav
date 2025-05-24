from ctypes import CDLL

from hyprnav.config import AppConfig

CDLL("libgtk4-layer-shell.so")
import gi  # noqa

gi.require_version("Gtk", "4.0")
gi.require_version("Gtk4LayerShell", "1.0")

from gi.repository import Gtk  # pyright: ignore #noqa
from gi.repository import Gtk4LayerShell as LayerShell  # pyright: ignore #noqa
from gi.repository import GLib  # pyright: ignore # noqa
import sys  # pyright: ignore # noqa
from hyprnav.constants import APP_NAME, APP_VERSION, STYLE_FILE  # pyright: ignore # noqa
from hyprnav.util import printLog  # pyright: ignore # noqa


class WorkspaceWindow(Gtk.Window):
    def __init__(self, config: AppConfig):
        super().__init__()

        printLog("Creating workspace window instance...")
        printLog("Atribute appConfig to self.config...")
        self.config = config
        printLog(f"set title to {APP_NAME} - v{APP_VERSION}")
        self.set_title(f"{APP_NAME} - v{APP_VERSION}")
        printLog(
            f"set default size to {self.config.main_window.width}x{self.config.main_window.height} as config.yaml file"
        )
        self.set_default_size(
            self.config.main_window.width, self.config.main_window.height
        )

        printLog(f"set css id to{APP_NAME.lower()}...")
        self.set_name("main-window")

        # Carregar CSS
        printLog("Setting up style with CSS path: " + STYLE_FILE)
        css_provider = Gtk.CssProvider()
        css_provider.load_from_path(f"{STYLE_FILE}")
        display = self.get_display()
        Gtk.StyleContext.add_provider_for_display(
            display, css_provider, Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
        )
        printLog("CSS provider loaded")

        printLog("set resizable to False...")
        LayerShell.init_for_window(self)
        LayerShell.set_layer(self, LayerShell.Layer.OVERLAY)

        # Centraliza a janela na tela
        printLog("set window position to center...")
        LayerShell.set_anchor(self, LayerShell.Edge.LEFT, False)
        LayerShell.set_anchor(self, LayerShell.Edge.RIGHT, False)
        LayerShell.set_anchor(self, LayerShell.Edge.TOP, False)
        LayerShell.set_anchor(self, LayerShell.Edge.BOTTOM, False)

        printLog("orientation to vertical...")
        box = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL,
            spacing=self.config.main_window.spacing,
        )
        # set box to vertical alignment to center
        printLog("Set box to vertical alignment to center")
        box.set_valign(Gtk.Align.CENTER)
        fixed_label = Gtk.Label(label=self.config.main_window.label)
        fixed_label.set_name("fixed-label")

        printLog("Append fixed-label to box...")
        box.append(fixed_label)
        self.workspace_label = Gtk.Label()
        self.workspace_label.set_name("workspace-label")

        printLog("Append workspace_label to box...")
        box.append(self.workspace_label)

        printLog("Append box to window...")
        self.set_child(box)

    def showWorkspace(self, workspaceID: str):
        self.workspace_label.set_label(f"{workspaceID}")
        self.present()
        # Schedule automatic window closing after 300ms
        GLib.timeout_add(300, lambda: self.hide() or False)


# window: WorkspaceWindow
#
#
# def onActivate(app):
#     global window
#     appConfig = AppConfig()
#     window = WorkspaceWindow(appConfig)
#     app.add_window(window)
#
#     window.showWorkspace("Gonha")
#
#
# if __name__ == "__main__":
#     config = AppConfig()
#     app = Gtk.Application()
#     app.connect("activate", onActivate)
#     app.run(sys.argv)
