from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import * # QLabel, QLineEdit, QPushButton, QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem


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

class TTFWindow(QtWidgets.QMainWindow):
    # def setupUI(self, TTOFrame):
    #     TTOFrame.setObjectName("Truth Table Filler")
    def __init__(self):
        super(TTFWindow, self).__init__()
        self.setGeometry(50, 50, 1200, 700)
        self.setWindowTitle("Truth Table Filler")
        backGround = self.palette()
        backGround.setColor(self.backgroundRole(), QColor(15, 102, 102))
        self.setPalette(backGround)
        # self.table_widget = MyTable()
        #
        # self.widget = QWidget(self)
        # layout = QGridLayout()
        # self.widget.setLayout(layout)
        # layout.addWidget(self.table_widget)
        # self.setCentralWidget(self.widget)
        self.widgets()

    def widgets(self):
        title = QLabel("Truth Table Filler", self)
        title.move(400, 30)
        title.setFont(QFont('Times', 25))
        title.setStyleSheet("color: white;")
        title.adjustSize()

        self.equationLabel = QLabel('Equation:', self)
        self.equationLabel.move(245, 132)
        self.equationLabel.setFont(QFont('Times', 12))
        self.equationLabel.setStyleSheet("color: white;")
        self.textEditor = QLineEdit(self)

        self.textEditor.move(350, 130)
        self.textEditor.resize(450, 40)

        enter = QPushButton('ENTER', self)
        enter.clicked.connect(self.sendEquation)
        enter.resize(80, 40)
        enter.move(820, 130)
        enter.setToolTip("<h3>Enter Equation</h3>")
        enter.setStyleSheet("background: white;")

        returnButton = QPushButton('', self)
        returnButton.clicked.connect(self.returnMainMenu)
        returnButton.resize(100, 100)
        returnButton.move(20, 20)
        returnButton.setToolTip("<h3>Return to Main Menu</h3>")
        returnButton.setStyleSheet(""
                                   "QPushButton { background-image: url('return.png'); border: none; }"
                                   "QToolTip { color: #000000; background-color:#ffffff ; border: 0px; }")

        model = QtGui.QStandardItemModel(5, 3)
        model.setHorizontalHeaderLabels(['ID', 'DATE', 'VALUE'])
        for row, text in enumerate(['Cell', 'Fish', 'Apple', 'Ananas', 'Mango']):
            item = QtGui.QStandardItem(text)
            model.setItem(row, 2, item)

        # table view
        # table = QtGui.QTableView()
        # table.setModel(model)
        # layout.addWidget(table)

        # self.table = QtWidgets.QTableView()
        #
        # data = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1]] # ["A", "B", "A V B"],
        #
        # self.model = TableModel(data)
        # self.table.setModel(self.model)
        #
        # self.setCentralWidget(self.table)

        self.show()

    def sendEquation(self):
        print(self.textEditor.text())

    def returnMainMenu(self):
        print("return")
        # self.MainMenu = pyQt.Window()
        # self.MainMenu.show()
        self.hide()
