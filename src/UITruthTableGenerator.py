from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
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
        self.equationLabel = QLabel('Equation:', self)
        self.Label = QLabel('            ', self)
        self.vbox = QGridLayout()
        self.widgets()
        self.show()

    def widgets(self):

        self.vbox.setSpacing(20)
        space = QLabel("     ", self)
        space.setFont(QFont('Times', 20))
        space.setStyleSheet("color: white;")
        space.adjustSize()
        self.vbox.addWidget(space, 1, 0)

        title = QLabel("Truth Table Filler", self)
        title.move(400, 30)
        title.setFont(QFont('Times', 20))
        title.setStyleSheet("color: white;")
        title.adjustSize()

        self.equationLabel.move(245, 132)
        self.equationLabel.setFont(QFont('Times', 12))
        self.equationLabel.setStyleSheet("color: white;")
        self.vbox.addWidget(self.equationLabel, 2, 0)

        self.Label.setFont(QFont('Times', 12))
        self.Label.setStyleSheet("color: white;")
        self.vbox.addWidget(self.Label, 2, 2)

        self.textEditor.move(350, 130)
        self.textEditor.resize(400, 70)
        self.vbox.addWidget(self.textEditor, 2, 1)

        gap = QLabel("     ", self)
        gap.setFont(QFont('Times', 20))
        gap.setStyleSheet("color: white;")
        gap.adjustSize()
        self.vbox.addWidget(gap, 5, 2)

        show = QPushButton(' ', self)
        show.clicked.connect(self.showTTF)
        show.resize(100, 100)
        show.move(1080, 580)
        show.setToolTip("<h3>Show Answer</h3>")
        show.setStyleSheet(""
                           "QPushButton { background-image: url('./images/SHOW.png'); border: none; }"
                           "QToolTip { color: #000000; background-color:#ffffff ; border: 0px; }")

        returnButton = QPushButton('', self)
        returnButton.clicked.connect(self.returnMainMenu)
        returnButton.resize(100, 100)
        returnButton.move(20, 580)
        returnButton.setToolTip("<h3>Return to Main Menu</h3>")
        returnButton.setStyleSheet(""
                                   "QPushButton { background-image: url('./images/return.png'); border: none; }"
                                   "QToolTip { color: #000000; background-color:#ffffff ; border: 0px; }")
        self.table = self.setupTable([], 5, 3)
        self.vbox.addWidget(self.table, 3, 1)
        self.setLayout(self.vbox)

    def showTTF(self):
        try:
            table = main.createTruthTable(str(self.textEditor.text()))
            newTable = table.run()
            self.setupTable(newTable, 0, 0)
        except:
            self._createStatusBar("Please enter an equation")

    def _createStatusBar(self, message):
        self.statusbar = QStatusBar()
        self.statusbar.move(100, 580)
        self.statusbar.setFont(QFont('Times', 15))
        self.statusbar.setStyleSheet('color: white')
        self.statusbar.showMessage(message, 4000)
        self.vbox.addWidget(self.statusbar, 5, 1)

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
            for row in range(0, len(tableVals)):
                for colVal in range(0, len(tableVals[row])):
                    self.table.setItem(row, colVal, QTableWidgetItem(str(tableVals[row][colVal])))
        return self.table

    def returnMainMenu(self):
        print("return")
        self.hide()
