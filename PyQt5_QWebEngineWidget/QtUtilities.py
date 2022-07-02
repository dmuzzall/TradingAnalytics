
from PyQt5.QtWidgets import QLabel, QFrame, QTableWidgetItem
from PyQt5.QtCore import Qt, QDateTime
from PyQt5.QtGui import QPalette, QColor


class QLabelSunken(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.setAlignment(Qt.AlignCenter)

class QLabelSunkenW(QLabelSunken):
    def __init__(self, name, minWidth, parent=None):
        super().__init__(parent)
        self.setFrameStyle(QFrame.Panel | QFrame.Raised)
        self.setAlignment(Qt.AlignCenter)
        self.setText(name)
        self.setFixedWidth(minWidth)

def SetQLabelColor(qLabel, textColor, backColor):
    qLabel.setStyleSheet("color: {0}; background-color: {1};".format(textColor, backColor))

def SetQLabelTextColorWeight(qLabel, textColor, fontWeight):
    qLabel.setStyleSheet("color: {0}; font-weight: {1};".format(textColor, fontWeight))

def SetButtonColorsWeight(qPushButton, textColor, backColor, fontWeight):
    qPushButton.setStyleSheet("color: {0}; background-color: {1}; font-weight: {2};".format(textColor, backColor, fontWeight))
    #qPushButton.setStyleSheet("QPushButton { background-color: yellow }")

def SetButtonTextColorWeight(qPushButton, textColor, fontWeight):
    qPushButton.setStyleSheet("color: {0}; font-weight: {1};".format(textColor, fontWeight))

def QDateTimeToString(qDateTime):
    return qDateTime.toString('yyyy-MM-dd hh:mm:ss')

def StringToQDateTime(dateTimeStr):
    return QDateTime.fromString('yyyy-MM-dd hh:mm:ss')

def Fill_TableWidgetWithItems(tw):
    for r in range(tw.rowCount()):
        for c in range(tw.columnCount()):
            item = QTableWidgetItem()
            item.setTextAlignment(Qt.AlignCenter)
            tw.setItem(r, c, item)

def Get_DarkThemePalette():
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(53, 53, 53))
    palette.setColor(QPalette.WindowText, Qt.white)
    palette.setColor(QPalette.Base, QColor(25, 25, 25))
    palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    palette.setColor(QPalette.ToolTipBase, Qt.black)
    palette.setColor(QPalette.ToolTipText, Qt.white)
    palette.setColor(QPalette.Text, Qt.white)
    palette.setColor(QPalette.Button, QColor(53, 53, 53))
    palette.setColor(QPalette.ButtonText, Qt.white)
    palette.setColor(QPalette.BrightText, Qt.red)
    palette.setColor(QPalette.Link, QColor(42, 130, 218))
    palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    palette.setColor(QPalette.HighlightedText, Qt.black)
    return palette
