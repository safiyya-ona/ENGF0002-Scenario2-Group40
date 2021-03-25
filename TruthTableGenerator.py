# https://www.youtube.com/watch?v=ECIZgWeyFFk&ab_channel=ParwizForogh

from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# class TableModel(QtCore.QAbstractTableModel):
#     def __init__(self, data):
#         super(TableModel, self).__init__()
#         self._data = data
#
#     def data(self, index, role):
#         if role == QtCore.DisplayRole:
#             # See below for the nested-list data structure.
#             # .row() indexes into the outer list,
#             # .column() indexes into the sub-list
#             return self._data[index.row()][index.column()]
#
#     def rowCount(self, index):
#         # The length of the outer list.
#         return len(self._data)
#
#     def columnCount(self, index):
#         # The following takes the first sub-list, and returns
#         # the length (only works if all rows are an equal length)
#         return len(self._data[0])

# class MyTable(QWidget):
#
#     def __init__(self):
#         super(MyTable, self).__init__()
#         self.Table()
#
#     def Table(self):
#         self.mytable()
#         self.layout = QVBoxLayout()
#         self.layout.addWidget(self.tableWidget)
#         self.setLayout(self.layout)
#         self.show()
#
#     def mytable(self):
#         self.tableWidget = QTableWidget()
#         self.tableWidget.setRowCount(1)
#         self.tableWidget.setColumnCount(1)
#         self.tableWidget.setItem(0, 0 , QTableWidgetItem("Hello"))
#         self.tableWidget.move(300, 300)
class TTFWindow(QDialog):
    def __init__(self):
        super(TTFWindow, self).__init__()
        self.setGeometry(50, 50, 1200, 700)
        self.setWindowTitle("Truth Table Filler")
        backGround = self.palette()
        backGround.setColor(self.backgroundRole(), QColor(15, 102, 102))
        self.setPalette(backGround)

        # self.table_widget = MyTableWidget(self)
        # self.setCentralWidget(self.truthTable())
        self.widgets()
        self.show()

    def widgets(self):
        vbox = QGridLayout()
        vbox.setSpacing(20)
        title = QLabel("Truth Table Filler", self)
        title.move(400, 30)
        title.setFont(QFont('Times', 25))
        title.setStyleSheet("color: white;")
        title.adjustSize()
        vbox.addWidget(title, 1, 1)

        self.equationLabel = QLabel('Equation:', self)
        self.equationLabel.move(245, 132)
        self.equationLabel.setFont(QFont('Times', 12))
        self.equationLabel.setStyleSheet("color: white;")
        vbox.addWidget(self.equationLabel, 2, 0)
        self.textEditor = QLineEdit(self)
        self.textEditor.move(350, 130)
        self.textEditor.resize(400, 40)
        vbox.addWidget(self.textEditor, 2, 1)

        enter = QPushButton('SUBMIT', self)
        enter.clicked.connect(self.sendEquation)
        enter.resize(80, 40)
        enter.move(820, 130)
        enter.setToolTip("<h3>Enter Equation</h3>")
        enter.setStyleSheet("background: green;")
        vbox.addWidget(enter, 4, 2)

        returnButton = QPushButton('', self)
        returnButton.clicked.connect(self.returnMainMenu)
        returnButton.resize(100, 100)
        returnButton.move(20, 580)
        returnButton.setToolTip("<h3>Return to Main Menu</h3>")
        returnButton.setStyleSheet(""
                                   "QPushButton { background-image: url('return.png'); border: none; }"
                                   "QToolTip { color: #000000; background-color:#ffffff ; border: 0px; }")
        vbox.addWidget(returnButton, 4, 0)

        table = self.setupTable(4, 3)
        vbox.addWidget(table, 3, 1)

        self.setLayout(vbox)

    def sendEquation(self):
        print(self.textEditor.text())

    def getTableData(self):
        table = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
        return table

    def setupTable(self, rows, columns):
        table = QTableWidget()
        table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        table.setHorizontalHeaderLabels(["A", "B", "A OR B"])
        table.setRowCount(rows)
        table.setColumnCount(columns)
        tableValues = self.getTableData()
        for row in range(0, len(tableValues)):
            for colVal in range(0, len(tableValues[row])):
                table.setItem(row, colVal, QTableWidgetItem(str(tableValues[row][colVal])))
        return table

    def returnMainMenu(self):
        print("return")
        # self.MainMenu = pyQt.Window()
        # self.MainMenu.show()
        self.hide()

# class MyTableWidget(QWidget):
#     def __init__(self, parent):
#         super(QWidget, self).__init__(parent)
#         self.layout = QGridLayout(self)
#
#         # standard item model
#         model = QtGui.QStandardItemModel(4, 3)
#         model.setHorizontalHeaderLabels(['A', 'B', 'A V B'])
#         for row, text in enumerate([0, 0, 0, 1]):
#             item = QtGui.QStandardItem(text)
#             model.setItem(0, row, item)
#         for row, text in enumerate(['Cell', 'Fish', 'Apple', 'Ananas']):
#             item = QtGui.QStandardItem(text)
#             model.setItem(row, 2, item)
#
#         # filter proxy model
#         filter_proxy_model = QtCore.QSortFilterProxyModel()
#         filter_proxy_model.setSourceModel(model)
#         #filter_proxy_model.setFilterKeyColumn(2)  # third column
#         #layout = QVBoxLayout(window)
#         # line_edit = QLineEdit()
#         # line_edit.textChanged.connect(filter_proxy_model.setFilterRegExp)
#         # layout.addWidget(line_edit)
#
#         # table view
#         table = QTableView()
#         table.setModel(filter_proxy_model)
#         #layout.addWidget(table)
#
#         # Add tabs to widget
#         self.layout.addWidget(table, 50, 2, 3, 4)
#         self.setLayout(self.layout)

# def run():
#     app = QtWidgets.QApplication(sys.argv)
#     GUI = TTFWindow()
#     GUI.show()
#     sys.exit(app.exec_())
#
# run()
