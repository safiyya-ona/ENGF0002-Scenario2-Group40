# https://www.learnpyqt.com/tutorials/qtableview-modelviews-numpy-pandas/
# https://www.youtube.com/watch?v=dRRpbDFnMHI&ab_channel=Ssj6
# https://stackoverflow.com/questions/56989216/switching-frames-in-pyqt
# https://www.tutorialspoint.com/pyqt/pyqt_qfiledialog_widget.htm
import sys
from PyQt5 import QtWidgets
from PyQt5.QtGui import QColor, QFont
from PyQt5.QtWidgets import QFileDialog, QLabel
import TruthTableGenerator
import revisionCards

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 1200, 700)
        self.setWindowTitle("Welcome to Truth Tables don't lie")
        backGround = self.palette()
        backGround.setColor(self.backgroundRole(), QColor(15, 102, 102))
        self.setPalette(backGround)
        self.widgets()

    def widgets(self):
        title = QLabel("Welcome to Truth Tables don't lie", self)
        title.move(300, 30)
        title.setFont(QFont('Times', 20))
        title.setStyleSheet("color: white;")
        title.adjustSize()

        self.TTOButton = QtWidgets.QPushButton(self)
        self.TTOButton.clicked.connect(self.showTTF)
        self.TTOButton.resize(300, 300)
        self.TTOButton.move(450, 180)
        self.TTOButton.setToolTip("<h3>Truth Table Filler</h3>")
        self.TTOButton.setStyleSheet("background-image: url('TTFButton.png'); border:none;")

        revCards = QtWidgets.QPushButton(self)
        revCards.clicked.connect(self.showRevCardsFrame)
        revCards.resize(300, 300)
        revCards.move(100, 180)
        revCards.setToolTip("<h3>Revise Truth Tables</h3>")
        revCards.setStyleSheet("background-image: url('Revision.png'); border:none;")

        fileChooser = QtWidgets.QPushButton(self)
        fileChooser.clicked.connect(self.getfile)
        fileChooser.resize(300, 300)
        fileChooser.move(800, 180)
        fileChooser.setToolTip("<h3>Create Exercise</h3>")
        fileChooser.setStyleSheet("background-image: url('ExerciseButton.png'); border: none;")

        self.show()

    def getfile(self):
        fileName = QFileDialog.getOpenFileName(self, 'Open file', 'c:\\', "Text files (*.txt)")
        print(fileName)

    def showTTF(self):
        self.TTF = TruthTableGenerator.TTFWindow()
        self.TTF.show()

    def showRevCardsFrame(self):
        self.RevCards = revisionCards.RevCards()
        self.RevCards.show()

    # def getfiles(self):
    #     dialogue = QFileDialog()
    #     dialogue.setFileMode(QFileDialog.AnyFile)
    #     dialogue.setFilter("Text files (*.txt)")
    #     filenames = QtCore.QStringList()
    #
    #     if dialogue.exec_():
    #         filenames = dialogue.selectedFiles()
    #         f = open(filenames[0], 'r')
    #
    #         with f:
    #             data = f.read()
    #             self.contents.setText(data)

def run():
    app = QtWidgets.QApplication(sys.argv)
    GUI = Window()
    GUI.show()
    sys.exit(app.exec_())

run()
