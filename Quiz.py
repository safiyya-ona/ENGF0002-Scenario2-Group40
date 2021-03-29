from PyQt5 import QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import main

class QuizWindow(QDialog):
    def __init__(self):
        super(QuizWindow, self).__init__()
        self.setGeometry(50, 50, 1200, 700)
        self.setWindowTitle("Quiz")
        background = self.palette()
        background.setColor(self.backgroundRole(), QColor(15, 102, 102))
        self.vbox = QGridLayout()
        self.setPalette(background)
        self.table = QTableWidget()
        self.equation = "NOT A"  # function(random)
        self.widgets()
        self.show()

    def widgets(self):

        self.vbox.setSpacing(20)

        space = QLabel("     ", self)
        space.setFont(QFont('Times', 20))
        space.setStyleSheet("color: white;")
        space.adjustSize()
        self.vbox.addWidget(space, 1, 0)
        title = QLabel("Quiz Mode", self)
        title.move(400, 30)
        title.setFont(QFont('Times', 20))
        title.setStyleSheet("color: white;")
        title.adjustSize()

        self.questionLabel = QLabel(self)
        equation = "QUESTION: " # function(random)
        self.questionLabel.setText(equation)
        self.questionLabel.move(245, 132)
        self.questionLabel.setFont(QFont('Times', 12))
        self.questionLabel.setStyleSheet("color: white;")
        self.vbox.addWidget(self.questionLabel, 2, 0)

        self.equationLabel = QLabel(self)

        self.equationLabel.setText(self.equation)
        self.equationLabel.move(245, 132)
        self.equationLabel.setFont(QFont('Times', 15))
        self.equationLabel.setStyleSheet("color: white;")
        self.vbox.addWidget(self.equationLabel, 2, 1)

        check = QPushButton(' ', self)
        check.clicked.connect(self.checkTable)
        check.resize(100, 100)
        check.move(1080, 580)
        check.setToolTip("<h3>Show Answer</h3>")
        check.setStyleSheet(""
                           "QPushButton { background-image: url('CHECK.png'); border: none; }"
                           "QToolTip { color: #000000; background-color:#ffffff ; border: 0px; }")

        returnButton = QPushButton('', self)
        returnButton.clicked.connect(self.returnMainMenu)
        returnButton.resize(100, 100)
        returnButton.move(20, 580)
        returnButton.setToolTip("<h3>Return to Main Menu</h3>")
        returnButton.setStyleSheet(""
                                   "QPushButton { background-image: url('return.png'); border: none; }"
                                   "QToolTip { color: #000000; background-color:#ffffff ; border: 0px; }")

        gap = QLabel("           ", self)
        gap.setFont(QFont('Times', 20))
        gap.setStyleSheet("color: white;")
        gap.adjustSize()
        self.vbox.addWidget(gap, 5, 2)

        rows = self.returnRows(self.equation)
        columns = self.returnColumns(self.equation)
        # firstRow =  self.headings(equation)
        # table = []
        # table.append(firstRow)
        self.table = self.setupTable([], rows, columns)
        self.table = self.headings(self.equation)
        self.vbox.addWidget(self.table, 3, 1)
        self.setLayout(self.vbox)

    def returnRows(self, equation):
        table = main.createTruthTable(equation)
        newTable = table.run()
        return len(newTable)

    def returnColumns(self, equation):
        table = main.createTruthTable(equation)
        newTable = table.run()
        return len(newTable[0])

    def headings(self, equation):
        table = main.createTruthTable(equation)
        newTable = table.run()
        for row in range(0, 1):
            for colVal in range(0, len(newTable[row])):
                self.table.setItem(row, colVal, QTableWidgetItem(str(newTable[row][colVal])))
        return self.table

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
                    # print(tableVals[row][colVal])
                    # print((table.item(row, colVal)).text())
        return self.table

    def adjustTable(self):
        # https://stackoverflow.com/questions/21945044/wait-for-last-character-typed-in-qlineeditontextchanged
        rows = main.createTruthTable(str(self.textEditor.text())).numberOfRows
        print(rows)
        columns = main.createTruthTable(self.textEditor.text()).numberOfColumns
        print(columns)
        self.setupTable([], rows, columns)

    def checkTable(self):
        # self.setupTable()
        userEntry = []
        tableValues = main.createTruthTable(self.equation)
        CorrectTable = tableValues.run()
        for row in range(0, len(CorrectTable)):
            rowVal = []
            for colVal in range(0, len(CorrectTable[row])):
                # table.setItem(row, colVal, QTableWidgetItem(str(tableVals[row][colVal])))
                # print((self.table.item(row, colVal)))
                value = (self.table.item(row, colVal)).text()
                print(value)
                rowVal.append(value)
                # userEntry.append(value)
            userEntry.append(rowVal)
        print(sorted(userEntry))
        print(sorted(CorrectTable))
        # correct = False
        # for row in (0, len(CorrectTable):
        #     if CorrectTable[row] in userEntry:
        #
        #
        if sorted(userEntry) == sorted(CorrectTable):
            print("correct")
            self._createStatusBar("CORRECT!")
        else:
            print("INCORRECT")
            self._createStatusBar("INCORRECT. Try Again.")

    def _createStatusBar(self, message):
        self.statusbar = QStatusBar()
        # self.setStatusBar(self.statusbar)
        self.statusbar.move(100, 580)
        self.statusbar.showMessage(message, 4000)
        self.vbox.addWidget(self.statusbar, 5, 1)
        # self.show()

    def returnMainMenu(self):
        print("return")
        self.hide()