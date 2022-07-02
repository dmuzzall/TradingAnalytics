import sys
from PyQt5.QtWidgets import *
import ClockWidget


class GenericWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.layout = QVBoxLayout()
        self.layout.setSpacing(5)
        self.layout.setContentsMargins(1, 1, 1, 1)
        self.setLayout(self.layout)
        self.Setup_ClockWidget()

    def Setup_ClockWidget(self):
        self.clockWidget = ClockWidget.ClockWidget()
        self.layout.addWidget(self.clockWidget)
        self.clockWidget.secSignal.connect(self.OnSecSignal)

    def OnSecSignal(self):
        print("OnSecSignal")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GenericWidget()
    w.show()
    sys.exit(app.exec_())
