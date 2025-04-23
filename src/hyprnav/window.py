import sys
from PyQt6 import QtWidgets, uic
import importlib.resources
from PyQt6.QtGui import QGuiApplication


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        # Load ui
        uiFile = importlib.resources.files("hyprnav").joinpath("assets/window.ui")
        uic.loadUi(uiFile, self)  # type: ignore

        # Set application name and class before creating QWidget
        QGuiApplication.setApplicationName("hyprnav")
        QGuiApplication.setDesktopFileName("hyprnav")
        QGuiApplication.setApplicationDisplayName("hyprnav")

        # widget access
        # self.workspaceLabel.setText(":: Gonha ::")  # type: ignore

        self.show()

    # def buttonClicked(self):
    #     print("Button clicked!")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
