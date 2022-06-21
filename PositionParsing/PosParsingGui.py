
import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
import PosParsing as pp
import PandasModelView

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.dfPos = None
        self.dfPosMV = None
        self.dfMV = None

        self.ppp = pp.PosParsing()

        pos = [1, -2, 1, -3, 2]
        self.dfPos = pd.DataFrame([pos])
        print(pos)
        self.setup_Position()
        self.setup_StartButton()

        self.show()

    def setup_StartButton(self):
        self.runButton = QPushButton("Run")
        self.runButton.setMinimumWidth(300)
        self.layout.addWidget(self.runButton)
        self.runButton.clicked.connect(self.startButton_clicked)

    def startButton_clicked(self): 
        print("Start")

        pos = self.dfPos.iloc[0].tolist()
        pos = [int(p) for p in pos]
        print("Pos: ", pos)
        tradeList = self.ppp.ParsePosition(pos)
        print(tradeList)
        self.update_TradeList(tradeList)

    def setup_Position(self):
        self.dfPosMV = PandasModelView.PandasModelView(self.dfPos)
        self.dfPosMV.setFixedHeight(50)
        self.layout.addWidget(self.dfPosMV)

    def update_TradeList(self, tradeList):
        if self.dfMV != None:
            self.layout.removeWidget(self.dfMV)
        df = pd.DataFrame(tradeList)
        self.dfMV = PandasModelView.PandasModelView(df)
        self.layout.addWidget(self.dfMV)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

