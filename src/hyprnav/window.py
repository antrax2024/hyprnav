import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QGuiApplication
from .config import AppConfig


app = None  # Global QApplication instance


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, workspace: str) -> None:
        super().__init__()
        # Set application name and class before creating QWidget
        QGuiApplication.setApplicationName("hyprnav")
        QGuiApplication.setDesktopFileName("hyprnav")
        QGuiApplication.setApplicationDisplayName("hyprnav")

        # setup main window
        self.setObjectName("MainWindow")

        # Create a central widget and set layout
        centralWidget = QtWidgets.QWidget(self)
        self.verticalLayout = QtWidgets.QVBoxLayout(centralWidget)

        # set up fixedLabel
        self.fixedLabel = QtWidgets.QLabel("Workspace")
        self.fixedLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fixedLabel.setObjectName("fixedLabel")
        self.verticalLayout.addWidget(self.fixedLabel)
        # set up workspaceLabel
        self.workspaceLabel = QtWidgets.QLabel(f"{workspace}")
        self.workspaceLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.workspaceLabel.setObjectName("workspaceLabel")
        self.verticalLayout.addWidget(self.workspaceLabel)

        # appConfig
        self.appConfig = AppConfig()
        # set window object name for css styling
        self.setObjectName("MainWindow")
        # apply styles
        self.applyStyles()

        self.setCentralWidget(centralWidget)
        self.show()

    def applyStyles(self) -> None:
        """
        Applies CSS-like stylesheets from external CSS file.
        Dynamically replaces variables with configuration values.
        """
        # Path to CSS file (relative to the module)
        from .click import styleFile

        cssPath = styleFile

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
