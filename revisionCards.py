import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Revision Cards'
        self.setGeometry(50, 50, 1000, 600)
        backGround = self.palette()
        backGround.setColor(self.backgroundRole(), QColor(15, 102, 102))
        self.setPalette(backGround)

        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)

        self.show()


class MyTableWidget(QWidget):
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "A OR B")
        self.tabs.addTab(self.tab2, "A AND B")
        self.tabs.addTab(self.tab3, "A -> B")
        self.tabs.addTab(self.tab4, "A <-> B")

        # Create first tab
        self.tab1.layout = QVBoxLayout(self)
        self.label = QLabel(self)
        pixmap = QPixmap('A AND B.png')
        self.resized = pixmap.scaled(800, 400, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.resized)
        self.label.setAlignment(Qt.AlignCenter)
        self.tab1.layout.addWidget(self.label)
        self.tab1.setLayout(self.tab1.layout)

        self.tab2.layout = QVBoxLayout(self)
        self.label = QLabel(self)
        pixmap = QPixmap('A AND B.png')
        self.resized = pixmap.scaled(800, 400, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.resized)
        self.label.setAlignment(Qt.AlignCenter)
        self.tab2.layout.addWidget(self.label)
        self.tab2.setLayout(self.tab2.layout)

        self.tab3.layout = QVBoxLayout(self)
        self.label = QLabel(self)
        pixmap = QPixmap('A AND B.png')
        self.resized = pixmap.scaled(800, 400, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.resized)
        self.label.setAlignment(Qt.AlignCenter)
        self.tab3.layout.addWidget(self.label)
        self.tab3.setLayout(self.tab3.layout)

        self.tab4.layout = QVBoxLayout(self)
        self.label = QLabel(self)
        pixmap = QPixmap('return.png')
        self.resized = pixmap.scaled(800, 400, QtCore.Qt.KeepAspectRatio)
        self.label.setPixmap(self.resized)
        self.label.setAlignment(Qt.AlignCenter)
        self.tab4.layout.addWidget(self.label)
        self.tab4.setLayout(self.tab4.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())