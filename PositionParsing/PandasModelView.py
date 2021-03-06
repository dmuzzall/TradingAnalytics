import sys
import pandas as pd
from PyQt5.QtWidgets import QTableView, QHeaderView
from PyQt5.QtCore import Qt, QAbstractTableModel, QSortFilterProxyModel


class PandasModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, parent=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole or role == Qt.EditRole:
                value = self._data.iloc[index.row(), index.column()]
                return str(value)

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            self._data.iloc[index.row(), index.column()] = value
            return True
        return False

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]

    def flags(self, index):
        return Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable


class PandasModelView(QTableView):

    def __init__(self, dataFrame):
        QTableView.__init__(self)
        self.pandasModel = PandasModel(dataFrame)
        self.setModel(self.pandasModel)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

