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
import main

class TTFWindow(QDialog):
    def __init__(self):
        super(TTFWindow, self).__init__()
        self.setGeometry(50, 50, 1200, 700)
        self.setWindowTitle("Truth Table Filler")
        backGround = self.palette()
        backGround.setColor(self.backgroundRole(), QColor(15, 102, 102))
        self.setPalette(backGround)
        self.table = QTableWidget()
        self.textEditor = QLineEdit(self)
        self.widgets()
        self.show()

    def widgets(self):
        vbox = QGridLayout()
        vbox.setSpacing(20)
        space = QLabel("     ", self)
        space.setFont(QFont('Times', 20))
        space.setStyleSheet("color: white;")
        space.adjustSize()
        vbox.addWidget(space, 1, 0)

        title = QLabel("Truth Table Filler", self)
        title.move(400, 30)
        title.setFont(QFont('Times', 20))
        title.setStyleSheet("color: white;")
        title.adjustSize()

        self.equationLabel = QLabel('Equation:', self)
        self.equationLabel.move(245, 132)
        self.equationLabel.setFont(QFont('Times', 12))
        self.equationLabel.setStyleSheet("color: white;")
        vbox.addWidget(self.equationLabel, 2, 0)

        self.Label = QLabel('            ', self)
        self.Label.setFont(QFont('Times', 12))
        self.Label.setStyleSheet("color: white;")
        vbox.addWidget(self.Label, 2, 2)

        self.textEditor.move(350, 130)
        self.textEditor.resize(400, 40)
        vbox.addWidget(self.textEditor, 2, 1)

        gap = QLabel("     ", self)
        gap.setFont(QFont('Times', 20))
        gap.setStyleSheet("color: white;")
        gap.adjustSize()
        vbox.addWidget(gap, 5, 2)

        enter = QPushButton(' ', self)
        enter.clicked.connect(self.checkTable)
        enter.resize(100, 100)
        enter.move(1080, 450)
        enter.setToolTip("<h3>Check Answer</h3>")
        enter.setStyleSheet(""
                            "QPushButton { background-image: url('CHECK.png'); border: none; }"
                            "QToolTip { color: #000000; background-color:#ffffff ; border: 0px; }")
        #vbox.addWidget(enter, 4, 2)

        show = QPushButton(' ', self)
        show.clicked.connect(self.showTTF)
        show.resize(100, 100)
        show.move(1080, 580)
        show.setToolTip("<h3>Show Answer</h3>")
        show.setStyleSheet(""
                           "QPushButton { background-image: url('SHOW.png'); border: none; }"
                           "QToolTip { color: #000000; background-color:#ffffff ; border: 0px; }")

        plus = QPushButton('PLUS', self)
        plus.clicked.connect(self.adjustTable)
        plus.resize(100, 100)
        plus.move(1110, 130)
        plus.setToolTip("<h3>Show Answer</h3>")
        plus.setStyleSheet(""
                           "QPushButton { background-color: white; border: none; }"
                           "QToolTip { color: #000000; background-color:#ffffff ; border: 0px; }")
        vbox.addWidget(plus, 3, 2)

        returnButton = QPushButton('', self)
        returnButton.clicked.connect(self.returnMainMenu)
        returnButton.resize(100, 100)
        returnButton.move(20, 580)
        returnButton.setToolTip("<h3>Return to Main Menu</h3>")
        returnButton.setStyleSheet(""
                                   "QPushButton { background-image: url('return.png'); border: none; }"
                                   "QToolTip { color: #000000; background-color:#ffffff ; border: 0px; }")
        # if not self.getTableData():
        #     tableCol = 3
        #     tableRows = 4
        # else:
        #     tableCol = len(self.getTableData()[1])
        #     tableRows = len(self.getTableData())
        self.table = self.setupTable([], 5, 3)
        vbox.addWidget(self.table, 3, 1)
        self.setLayout(vbox)

    def showTTF(self):
        print(self.textEditor.text())
        table = main.createTruthTable(str(self.textEditor.text()))
        newTable = table.run()
        print(newTable)

        self.setupTable(newTable, 0, 0)

    # def _createStatusBar(self):
    #     self.statusbar = QStatusBar()
    #     self.setStatusBar(self.statusbar)
    #     self.statusbar.move(100, 580)
    #     self.statusbar.showMessage("Invalid Entry", 3000)

    def adjustTable(self):
        # https://stackoverflow.com/questions/21945044/wait-for-last-character-typed-in-qlineeditontextchanged
        rows = main.createTruthTable(str(self.textEditor.text())).numberOfRows()
        print(rows)
        columns = main.createTruthTable(self.textEditor.text()).numberOfColumns()
        print(columns)
        self.setupTable([], rows, columns)

    # def getTableData(self):
    #     # table = main.createTruthTable('A OR B')
    #     # print(table)
    #     table = [] # [['A', 'B', 'A OR B'], [0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]]
    #     return table

    def checkTable(self):
        # self.setupTable()
        userEntry = [[]]
        # tableValues = main.createTruthTable(s)
        for row in range(1, len(self.table)):
            for colVal in range(1, len(self.table[row])):
                # table.setItem(row, colVal, QTableWidgetItem(str(tableVals[row][colVal])))
                value = (table.item(row, colVal)).text()
                print(value)
                userEntry[row].append(value)

    def setupTable(self, tableVals, rows, columns):
        self.table.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.table.horizontalHeader().setVisible(False)
        self.table.verticalHeader().setVisible(False)
        if not tableVals:
            self.table.setRowCount(rows)
            self.table.setColumnCount(columns)
        else:
            self.table.setRowCount(len(tableVals))
            self.table.setColumnCount(len(tableVals[0]))
            # tableValues = self.getTableData()
            for row in range(0, len(tableVals)):
                for colVal in range(0, len(tableVals[row])):
                    self.table.setItem(row, colVal, QTableWidgetItem(str(tableVals[row][colVal])))
                    print(tableVals[row][colVal])
                    # print((table.item(row, colVal)).text())
        return self.table

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
