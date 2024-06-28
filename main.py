import sys

from PySide6.QtWidgets import QApplication
from PySide6.QtQml import QQmlApplicationEngine

import resources_rc


if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load("qrc:/Views/app.qml")

    if not engine.rootObjects():
        sys.exit(-1)

    sys.exit(app.exec())

