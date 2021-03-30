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
        self.questionLabel = QLabel(self)
        self.equationLabel = QLabel(self)
        self.equation = str(main.GenerateQuestions("test.txt").run())
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
        title.move(470, 30)
        title.setFont(QFont('Times', 20))
        title.setStyleSheet("color: white;")
        title.adjustSize()

        equation = "QUESTION: "
        self.questionLabel.setText(equation)
        self.questionLabel.move(245, 132)
        self.questionLabel.setFont(QFont('Times', 12))
        self.questionLabel.setStyleSheet("color: white;")
        self.vbox.addWidget(self.questionLabel, 2, 0)

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

        nextQ = QPushButton(self)
        nextQ.clicked.connect(self.nextQuestion)
        nextQ.resize(100, 100)
        nextQ.move(1080, 100)
        nextQ.setToolTip("<h3>New Question</h3>")
        nextQ.setStyleSheet(""
                            "QPushButton { background-image: url('newq.png'); border: none; }"
                            "QToolTip { color: #000000; background-color:#ffffff ; border: 0px; }")

        gap = QLabel("           ", self)
        gap.setFont(QFont('Times', 20))
        gap.setStyleSheet("color: white;")
        gap.adjustSize()
        self.vbox.addWidget(gap, 5, 2)

        rows = self.returnRows(self.equation)
        columns = self.returnColumns(self.equation)
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
            for row in range(0, len(tableVals)):
                for colVal in range(0, len(tableVals[row])):
                    self.table.setItem(row, colVal, QTableWidgetItem(str(tableVals[row][colVal])))
        return self.table

    def checkTable(self):
        userEntry = []
        tableValues = main.createTruthTable(self.equation)
        CorrectTable = tableValues.run()
        for row in range(0, len(CorrectTable)):
            rowVal = []
            for colVal in range(0, len(CorrectTable[row])):
                if self.table.item(row, colVal) is None:
                    value = " "
                else:
                    value = (self.table.item(row, colVal)).text()
                rowVal.append(value)
            userEntry.append(rowVal)
        print(userEntry)
        print(CorrectTable)
        if sorted(userEntry) == sorted(CorrectTable):
            self._createStatusBar("CORRECT!")
        else:
            self._createStatusBar("INCORRECT. Try Again.")
            self.showAnswerPopUp()

    def _createStatusBar(self, message):
        self.statusbar = QStatusBar()
        self.statusbar.move(100, 580)
        self.statusbar.setFont(QFont('Times', 20))
        self.statusbar.setStyleSheet('color: white')
        self.statusbar.showMessage(message, 4000)
        self.vbox.addWidget(self.statusbar, 5, 1)

    def nextQuestion(self):
        self.equation = str(main.GenerateQuestions("test.txt").run())
        self.hide()
        quiz = QuizWindow()
        quiz.show()
        print("pressed")

    def showAnswerPopUp(self):
        choice = QMessageBox.question(self, 'Show Answer',
                                      "Would you like to show the correct answer?",
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            tableValues = main.createTruthTable(self.equation)
            correctTable = tableValues.run()
            self.setupTable(correctTable, len(correctTable), len(correctTable[0]))
        else:
            pass

    def returnMainMenu(self):
        print("return")
        self.hide()
