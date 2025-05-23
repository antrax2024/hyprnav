from ctypes import CDLL

from hyprnav.config import AppConfig

CDLL("libgtk4-layer-shell.so")
import gi  # noqa

gi.require_version("Gtk", "4.0")
gi.require_version("Gtk4LayerShell", "1.0")

from gi.repository import Gtk  # pyright: ignore #noqa
from gi.repository import Gtk4LayerShell as LayerShell  # pyright: ignore #noqa
from gi.repository import GLib  # pyright: ignore # noqa
from hyprnav.constants import APP_NAME, APP_VERSION  # pyright: ignore # noqa
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

        # self.set_decorated(False)
        #
        printLog(f"set css id to{APP_NAME.lower()}...")
        self.set_name(f"{APP_NAME.lower()}")

        LayerShell.init_for_window(self)
        LayerShell.set_layer(self, LayerShell.Layer.OVERLAY)

        # Centraliza a janela na tela
        LayerShell.set_anchor(self, LayerShell.Edge.LEFT, False)
        LayerShell.set_anchor(self, LayerShell.Edge.RIGHT, False)
        LayerShell.set_anchor(self, LayerShell.Edge.TOP, False)
        LayerShell.set_anchor(self, LayerShell.Edge.BOTTOM, False)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        label = Gtk.Label(label="Workspace")
        label.set_margin_top(10)
        label.set_margin_bottom(5)
        box.append(label)
        self.workspace_label = Gtk.Label()
        box.append(self.workspace_label)

        self.set_child(box)

    def showWorkspace(self, workspaceID: str):
        self.workspace_label.set_label(f"{workspaceID}")
        self.present()
        loop = GLib.MainLoop()
        GLib.timeout_add(
            self.config.main_window.duration, lambda: (loop.quit(), False)[1]
        )
        loop.run()


def show_workspace_window(workspace, delay_ms):
    win = WorkspaceWindow(workspace)
    win.present()

    GLib.timeout_add(delay_ms, win.close)


if __name__ == "__main__":
    appConfig = AppConfig()
    WorkspaceWindow(appConfig).showWorkspace("8")
    # delay = 15000  # ms
    # win = WorkspaceWindow(workspace)
    # win.present()
    # loop = GLib.MainLoop()
    # GLib.timeout_add(delay, lambda: (loop.quit(), False)[1])
    # loop.run()
