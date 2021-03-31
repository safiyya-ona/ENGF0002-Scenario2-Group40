import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QFileDialog, QLabel, QErrorMessage, QMessageBox
import UITruthTableGenerator
import revisionCards
import Quiz
import main

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 1200, 700)
        self.setWindowTitle("Welcome to Truth Tables don't lie")
        backGround = self.palette()
        backGround.setColor(self.backgroundRole(), QColor(15, 102, 102))
        self.TTOButton = QtWidgets.QPushButton(self)
        self.setPalette(backGround)
        self.widgets()

    def widgets(self):
        title = QLabel("Welcome to Truth Tables don't lie", self)
        title.move(300, 30)
        title.setFont(QFont('Times', 20))
        title.setStyleSheet("color: white;")
        title.adjustSize()

        self.TTOButton.clicked.connect(self.showTTF)
        self.TTOButton.resize(300, 300)
        self.TTOButton.move(450, 180)
        self.TTOButton.setToolTip("<h3>Truth Table Filler</h3>")
        self.TTOButton.setStyleSheet("background-image: url('./images/TTFButton.png'); border:none;")

        revCards = QtWidgets.QPushButton(self)
        revCards.clicked.connect(self.showRevCardsFrame)
        revCards.resize(300, 300)
        revCards.move(100, 180)
        revCards.setToolTip("<h3>Revise Truth Tables</h3>")
        revCards.setStyleSheet("background-image: url('./images/Revision.png'); border:none;")

        fileChooser = QtWidgets.QPushButton(self)
        fileChooser.clicked.connect(self.getfile)
        fileChooser.resize(300, 100)
        fileChooser.move(450, 500)
        fileChooser.setToolTip("<h3>Create Exercise</h3>")
        fileChooser.setStyleSheet("background-image: url('./images/ExerciseButton.png'); border: none;")

        quizButton = QtWidgets.QPushButton(self)
        quizButton.clicked.connect(self.showQuizFrame)
        quizButton.resize(300, 300)
        quizButton.move(800, 180)
        quizButton.setToolTip("<h3>Create Exercise</h3>")
        quizButton.setStyleSheet("background-image: url('./images/QUIZIcon.png'); border: none;")

        self.show()

    def getfile(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open file', '../', "Text files (*.txt)")
        print(fileName)
        if not fileName[0]:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('No file selected')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            try:
                file = main.addQuestions(fileName[0])
                file.run()

            except:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Formula found in incorrect format')
                msg.setWindowTitle("Error")
                msg.exec_()
                pass
        
    def showTTF(self):
        self.TTF = UITruthTableGenerator.TTFWindow()
        self.TTF.show()

    def showRevCardsFrame(self):
        self.RevCards = revisionCards.RevCards()
        self.RevCards.show()

    def showQuizFrame(self):
        self.quiz = Quiz.QuizWindow()
        self.quiz.show()

def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    GUI.show()
    sys.exit(app.exec_())

run()
