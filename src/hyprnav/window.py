import sys
from PyQt6 import QtWidgets, uic, QtCore
import importlib.resources
from PyQt6.QtGui import QGuiApplication

app = None  # Global QApplication instance


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, workspace: str) -> None:
        super().__init__()
        # Load ui
        uiFile = importlib.resources.files("hyprnav").joinpath("assets/window.ui")
        uic.loadUi(uiFile, self)  # type: ignore
        # Set application name and class before creating QWidget
        QGuiApplication.setApplicationName("hyprnav")
        QGuiApplication.setDesktopFileName("hyprnav")
        QGuiApplication.setApplicationDisplayName("hyprnav")
        # widget access
        self.workspaceLabel.setText(f":: {workspace} ::")  # type: ignore
        self.show()


def showWorkspaceWindow(workspace: str, delay: int) -> None:
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(workspace)
    window.show()
    QtCore.QTimer.singleShot(delay, window.close)
    app.exec()


if __name__ == "__main__":
    pass
