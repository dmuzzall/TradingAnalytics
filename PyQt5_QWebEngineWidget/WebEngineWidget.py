#!/usr/bin/env python

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
import QtUtilities


class WebEngineWidget(QWidget):
    finishedSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.status = 0
        self.pageText = ""
        self.Setup_Layout()
        self.Setup_WebEngineView()

    def Setup_Layout(self):
        self.layout = QHBoxLayout()
        self.statusLabel = QtUtilities.QLabelSunken()
        self.layout.setSpacing(2)
        self.layout.setContentsMargins(2, 2, 2, 2)
        self.layout.addWidget(self.statusLabel)
        self.setLayout(self.layout)

    def Setup_WebEngineView(self):
        self.webEngineView = QWebEngineView()
        self.webEngineView.loadStarted.connect(self.OnLoadStarted)
        self.webEngineView.loadFinished.connect(self.OnLoadFinished)
        self.Update_StatusLabelColor()

    def Open_Url(self, urlStr):
        url = QUrl(urlStr)
        self.webEngineView.setUrl(url)

    def OnLoadStarted(self):
        self.status = 1
        self.pageText = ""
        self.Update_StatusLabelColor()

    def OnLoadFinished(self):
        page = self.webEngineView.page()
        page.toPlainText(self.OnPageToPlainText)

    def OnPageToPlainText(self, pageText):
        self.pageText = pageText
        self.status = 2
        self.Update_StatusLabelColor()
        self.finishedSignal.emit()

    def Update_StatusLabelColor(self):
        if self.status == 0: self.statusLabel.setStyleSheet("background-color: grey")
        elif self.status == 1: self.statusLabel.setStyleSheet("background-color: yellow")
        elif self.status == 2: self.statusLabel.setStyleSheet("background-color: green")
        else: self.statusLabel.setStyleSheet("background-color: red")

    def Get_PageText(self):
        return self.pageText
