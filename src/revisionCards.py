from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class RevCards(QMainWindow):
    def __init__(self):
        super(RevCards, self).__init__()
        self.title = 'Revision Cards'
        self.setGeometry(50, 50, 1200, 700)
        backGround = self.palette()
        backGround.setColor(self.backgroundRole(), QColor(15, 102, 102))
        self.setPalette(backGround)
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        self.returnButton()
        self.show()

    def returnButton(self):
        returnButton = QPushButton('', self)
        returnButton.clicked.connect(self.returnMainMenu)
        returnButton.resize(100, 100)
        returnButton.move(20, 580)
        returnButton.setToolTip("<h3>Return to Main Menu</h3>")
        returnButton.setStyleSheet(""
                                   "QPushButton { background-image: url('./images/return.png'); border: none; }"
                                   "QToolTip { color: #000000; background-color:#ffffff ; border: 0px; }")

    def returnMainMenu(self):
        print("return")
        self.hide()

class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tabs.resize(0, 0)

        self.tabs.addTab(self.tab1, "A OR B")
        self.tabs.addTab(self.tab2, "A AND B")
        self.tabs.addTab(self.tab3, "A -> B")
        self.tabs.addTab(self.tab4, "A <-> B")
        self.tabs.addTab(self.tab5, "NOT A")

        self.tab1.layout = QVBoxLayout(self)
        self.label = QLabel(self)
        pixmap = QPixmap('./images/AORB.png')
        self.resized = pixmap.scaled(800, 400, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.resized)
        self.label.setAlignment(Qt.AlignCenter)
        self.tab1.layout.addWidget(self.label)
        self.tab1.setLayout(self.tab1.layout)

        self.tab2.layout = QVBoxLayout(self)
        self.label = QLabel(self)
        pixmap = QPixmap('./images/AANDB.png')
        self.resized = pixmap.scaled(800, 400, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.resized)
        self.label.setAlignment(Qt.AlignCenter)
        self.tab2.layout.addWidget(self.label)
        self.tab2.setLayout(self.tab2.layout)

        self.tab3.layout = QVBoxLayout(self)
        self.label = QLabel(self)
        pixmap = QPixmap('./images/AIMPLYB.png')
        self.resized = pixmap.scaled(800, 400, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.resized)
        self.label.setAlignment(Qt.AlignCenter)
        self.tab3.layout.addWidget(self.label)
        self.tab3.setLayout(self.tab3.layout)

        self.tab4.layout = QVBoxLayout(self)
        self.label = QLabel(self)
        pixmap = QPixmap('./images/AARROWSB.png')
        self.resized = pixmap.scaled(800, 400, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.resized)
        self.label.setAlignment(Qt.AlignCenter)
        self.tab4.layout.addWidget(self.label)
        self.tab4.setLayout(self.tab4.layout)

        self.tab5.layout = QVBoxLayout(self)
        self.label = QLabel(self)
        pixmap = QPixmap('./images/notA.png')
        self.resized = pixmap.scaled(800, 400, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.resized)
        self.label.setAlignment(Qt.AlignCenter)
        self.tab5.layout.addWidget(self.label)
        self.tab5.setLayout(self.tab5.layout)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
