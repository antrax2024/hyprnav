import sys
from PyQt6 import QtWidgets, uic, QtCore
import importlib.resources
from PyQt6.QtGui import QGuiApplication
from .config import AppConfig

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
        # appConfig
        self.appConfig = AppConfig()
        # set window object name for css styling
        self.setObjectName("MainWindow")
        # Adjust window size
        self.setMinimumSize(
            self.appConfig.main_window.width, self.appConfig.main_window.height
        )

        # set fixedLabel object name for css styling
        self.fixedLabel.setObjectName("fixedLabel")  # type: ignore

        # widget access
        self.workspaceLabel.setText(f":: {workspace} ::")  # type: ignore
        # set workspaceLabel object name for css styling
        self.workspaceLabel.setObjectName("workspaceLabel")  # type: ignore

        self.show()

    def applyStyles(self) -> None:
        """
        Applies CSS-like stylesheets from external CSS file.
        Dynamically replaces variables with configuration values.
        """
        # Path to CSS file (relative to the module)
        cssPath = self.style_file

        try:
            # Read CSS file content
            with open(cssPath, "r") as cssFile:
                cssContent = cssFile.read()

            # Apply the stylesheet
            self.setStyleSheet(cssContent)

        except FileNotFoundError:
            print(f"Warning: CSS file not found at {cssPath}")
            # Fallback to inline styles


def showWorkspaceWindow(workspace: str, delay: int) -> None:
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(workspace)
    window.show()
    QtCore.QTimer.singleShot(delay, window.close)
    app.exec()


if __name__ == "__main__":
    pass
