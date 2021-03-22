# https://www.learnpyqt.com/tutorials/qtableview-modelviews-numpy-pandas/
# https://www.youtube.com/watch?v=dRRpbDFnMHI&ab_channel=Ssj6
# https://stackoverflow.com/questions/56989216/switching-frames-in-pyqt
# https://www.tutorialspoint.com/pyqt/pyqt_qfiledialog_widget.htm
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QColor, QIcon, QPixmap, QFont
from PyQt5.QtWidgets import QFileDialog, QLabel, QVBoxLayout
#from TruthTableGenerator import TruthTableFiller

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(50, 50, 1200, 700)
        self.setWindowTitle("Truth Table Filler")
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

        TTOButton = QtWidgets.QPushButton(self)
        TTOButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        # TTOButton.clicked.connect(QtCore.QCoreApplication.instance().quit)
        TTOButton.resize(300, 300)
        TTOButton.move(100, 100)
        TTOButton.setStyleSheet("background-image: url('icon.png'); border: none;")
        exButton = QtWidgets.QPushButton("Create Exercise", self)
        # button.clicked.connect(QtCore.QCoreApplication.instance().quit)
        exButton.resize(300, 300)
        exButton.move(450, 100)
        exButton.setStyleSheet("background-color: white;")

        fileChooser = QtWidgets.QPushButton("QFileDialog object", self)
        fileChooser.clicked.connect(self.getfile)
        fileChooser.resize(300, 300)
        fileChooser.move(800, 100)

        self.show()

    def openTTFFrame(self):
        window = QtWidgets.QMainWindow()
        #TTFFrame = TruthTableFiller()


    def getfile(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\')
        print(fname)

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
