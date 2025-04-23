import sys
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtGui import QGuiApplication
from .config import AppConfig
import os


app = None  # Global QApplication instance


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, workspace: str) -> None:
        super().__init__()
        # Set application name and class before creating QWidget
        QGuiApplication.setApplicationName("hyprnav")
        QGuiApplication.setDesktopFileName("hyprnav")
        QGuiApplication.setApplicationDisplayName("hyprnav")

        # setup main window
        # appConfig
        self.appConfig = AppConfig()
        self.setObjectName("MainWindow")
        self.setMinimumWidth(self.appConfig.main_window.width)
        self.setMinimumHeight(self.appConfig.main_window.height)

        # Create a central widget and set layout
        centralWidget = QtWidgets.QWidget(self)
        centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(centralWidget)

        # set up fixedLabel
        self.fixedLabel = QtWidgets.QLabel("Workspace")
        self.fixedLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.fixedLabel.setObjectName("fixedLabel")
        self.verticalLayout.addWidget(self.fixedLabel)

        # set up workspaceLabel
        self.workspaceLabel = QtWidgets.QLabel(f"{workspace} ::")

        self.workspaceLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.workspaceLabel.setObjectName("workspaceLabel")
        self.verticalLayout.addWidget(self.workspaceLabel)

        # set window object name for css styling
        self.setObjectName("MainWindow")

        # Set the central widget before applying styles
        self.setCentralWidget(centralWidget)

        # apply styles
        self.applyStyles()

        self.show()

    def applyStyles(self) -> None:
        """
        Applies CSS-like stylesheets from external CSS file.
        Dynamically replaces variables with configuration values.
        """
        # Get the directory of the current module
        currentDir = os.path.dirname(os.path.abspath(__file__))
        cssPath = os.path.join(currentDir, "assets", "style.css")

        try:
            # Read CSS file content
            with open(cssPath, "r") as cssFile:
                cssContent = cssFile.read()

            # Apply the stylesheet
            self.setStyleSheet(cssContent)
        except Exception as e:
            print(f"Error loading CSS file: {e}")
            # Fallback to inline styles
            self.setStyleSheet(
                """
            #centralWidget {
                background-color: #23272e;
            }
            
            #fixedLabel {
                color: #13d81d;
                font-size: 36px;
                font-weight: bold;
            }
            
            #workspaceLabel {
                color: #8be9fd;
                font-size: 26px;
            }
            """
            )


def showWorkspaceWindow(workspace: str, delay: int) -> None:
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(workspace)
    window.show()
    QtCore.QTimer.singleShot(delay, window.close)
    app.exec()


if __name__ == "__main__":
    pass
