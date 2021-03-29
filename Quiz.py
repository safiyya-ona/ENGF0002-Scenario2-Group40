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
        self.setPalette(background)
        self.table = QTableWidget()
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
        vbox.addWidget(self.questionLabel, 2, 0)

        self.equationLabel = QLabel(self)
        equation = "A OR B AND C AND D" # function(random)
        self.equationLabel.setText(equation)
        self.equationLabel.move(245, 132)
        self.equationLabel.setFont(QFont('Times', 12))
        self.equationLabel.setStyleSheet("color: white;")
        vbox.addWidget(self.equationLabel, 2, 1)

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
        vbox.addWidget(gap, 5, 2)

        rows = self.returnRows(equation)
        columns = self.returnColumns(equation)
        # firstRow =  self.headings(equation)
        # table = []
        # table.append(firstRow)
        self.table = self.setupTable([], rows, columns)
        self.table = self.headings(equation)
        vbox.addWidget(self.table, 3, 1)
        self.setLayout(vbox)

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
        userEntry = [[]]
        # tableValues = main.createTruthTable(s)
        for row in range(0, len(self.table)):
            for colVal in range(0, len(self.table[row])):
                # table.setItem(row, colVal, QTableWidgetItem(str(tableVals[row][colVal])))
                value = (self.table.item(row, colVal)).text()
                print(value)
                userEntry[row].append(value)

    def returnMainMenu(self):
        print("return")
        # self.MainMenu = pyQt.Window()
        # self.MainMenu.show()
        self.hide()