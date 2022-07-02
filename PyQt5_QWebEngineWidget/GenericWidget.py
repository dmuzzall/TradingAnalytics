import sys
from PyQt5.QtWidgets import *
import ClockWidget
import WebEngineWidget
import QtUtilities
from PyQt5.QtWebEngineWidgets import *


class GenericWidget(QWidget):

    def __init__(self):
        QWidget.__init__(self)
        self.layout = QVBoxLayout()
        self.layout.setSpacing(1)
        self.layout.setContentsMargins(1, 1, 1, 1)
        self.setLayout(self.layout)
        self.Setup_ClockWidget()
        self.Setup_WebEngineWidgets()
        self.Setup_Contols()

    def Setup_ClockWidget(self):
        self.clockWidget = ClockWidget.ClockWidget()
        self.layout.addWidget(self.clockWidget)
        self.clockWidget.secSignal.connect(self.OnSecSignal)

    def Setup_WebEngineWidgets(self):
        self.webEngineWidget = WebEngineWidget.WebEngineWidget()
        self.layout.addWidget(self.webEngineWidget)
        self.webEngineWidget.finishedSignal.connect(self.OnFinishedSignal)

    def Setup_Contols(self):
        self.button = QPushButton("Run")
        self.layout.addWidget(self.button)
        self.button.clicked.connect(self.OnButtonClicked)

    def OnSecSignal(self):
        return

    def OnButtonClicked(self):
        url = "http://news.google.com"
        w.webEngineWidget.Open_Url(url)

    def OnFinishedSignal(self):
        print("OnFinishedSignal")
        pageText = w.webEngineWidget.Get_PageText()
        print(pageText)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = GenericWidget()
    w.setPalette(QtUtilities.Get_DarkThemePalette())
    w.show()
    sys.exit(app.exec_())
