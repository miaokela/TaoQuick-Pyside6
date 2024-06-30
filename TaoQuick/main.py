import os
import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

import TaoQuick


if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.addImportPath("..")
    engine.load("qrc:/TaoQuick/App.qml")
 
    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())
