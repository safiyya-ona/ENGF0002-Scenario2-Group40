# # class CreateTable(QTableWidget): #QTableWidget
# #     dataSignal = pyqtSignal(list, np.ndarray)
# #     def __init__(self, Data, row, col, colHeaders, rowHeaders): #Index, ColumnHeaders
# #         super(CreateTable, self).__init__()
# #
# #
# #         self.setSelectionBehavior(self.SelectRows)
# #
# #         print("Start initialization")
# #         self.ColHeader = colHeaders
# #         self.setRowCount(row)
# #         self.setColumnCount(col)
# #         self.data = Data
# #         self.setHorizontalHeaderLabels(colHeaders)
# #
# #         print("Right before for loop")
# #
# #         n = len(Data)
# #         m = len(colHeaders)
# #
# #         for i in range(n):
# #             DataValues = self.data.iloc[i,:]
# #             print("values are {}".format(DataValues))
# #             #m = len(values)
# #             ConvertedVals = pd.to_numeric(DataValues)
# #
# #             ValList = DataValues.values.tolist()
# #             print(ValList)
# #
# #             for j in range(0,m):
# #                 self.item = QTableWidgetItem(str(round(ValList[j],5)))
# #                 #print("{}, {}".format(i, j))
# #                 self.setItem(i,j, self.item)
# #
# #     def contextMenuEvent(self, event):
# #
# #         menu = QMenu(self)
# #         graphAction = menu.addAction("Graph")
# #         compareAction = menu.addAction("Compare")
# #         scatterAction = menu.addAction("Plot types")
# #         aboutAction = menu.addAction("about")
# #         quitAction = menu.addAction("quit")
# #         printAction = menu.addAction("Print Row")
# #         action = menu.exec_(self.mapToGlobal(event.pos()))
# #         if action == quitAction:
# #             qApp.quit()
# #         elif action == printAction:
# #             self.selected = self.selectedItems()
# #             n = len(self.selected)
# #             print("n is {}".format(n))
# #             for i in range(n):
# #                 self.selected[i] = str(self.selected[i].text())
# #             for i in range(n):
# #                 self.selected[i] = float(self.selected[i])
# #             print(self.selected)
# #         elif action == graphAction:
# #             self.selected = self.selectedItems()
# #             n = len(self.selected)
# #             for i in range(n):
# #                 self.selected[i] = str(self.selected[i].text())
# #             for i in range(n):
# #                 self.selected[i] = float(self.selected[i])
# #             print("right before plotter called")
# #
# #             print(type(self.selected), type(self.ColHeader))
# #             self.dataSignal.emit(self.selected, self.ColHeader)
# #
# #         else:
# #             print("u clicked something other than quit")
# # import sys
# # from PyQt5 import QtGui, QtCore, QtWidgets
# # from PyQt5.QtCore import *
# # from PyQt5.QtGui import *
# #
# # # données à représenter
# # my_array = [['00','01','02'],
# #             ['10','11','12'],
# #             ['20','21','22']]
# #
# # def main():
# #     app = QApplication(sys.argv)
# #     w = MyWindow()
# #     w.show()
# #     sys.exit(app.exec_())
# #
# # # création de la vue et du conteneur
# # class MyWindow(QWidgets.QMainWindow):
# #     def __init__(self, *args):
# #         QWidget.__init__(self, *args)
# #
# #         tablemodel = MyTableModel(my_array, self)
# #         tableview = QTableView()
# #         tableview.setModel(tablemodel)
# #
# #         layout = QVBoxLayout(self)
# #         layout.addWidget(tableview)
# #         self.setLayout(layout)
# #
# # # création du modèle
# # class MyTableModel(QAbstractTableModel):
# #     def __init__(self, datain, parent = None, *args):
# #         QAbstractTableModel.__init__(self, parent, *args)
# #         self.arraydata = datain
# #
# #     def rowCount(self, parent):
# #         return len(self.arraydata)
# #
# #     def columnCount(self, parent):
# #         return len(self.arraydata[0])
# #
# #     def data(self, index, role):
# #         if not index.isValid():
# #             return None
# #         elif role != Qt.DisplayRole:
# #             return None
# #         return (self.arraydata[index.row()][index.column()])
# #
# #     """
# #     def setData(self, index, value):
# #         self.arraydata[index.row()][index.column()] = value
# #         return True
# #     def flags(self, index):
# #         return Qt.ItemIsEditable
# #     """
# #
# # if __name__ == "__main__":
# #     main()
#
# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import *
#
# app = QtWidgets.QApplication([])
# window = QtWidgets.QWidget()
#
# # standard item model
# model = QtGui.QStandardItemModel(4, 3)
# model.setHorizontalHeaderLabels(['A', 'B', 'A V B'])
# for row, text in enumerate([0, 0, 0, 1]):
#     item = QtGui.QStandardItem(text)
#     model.setItem(row, 1, item)
# for row, text in enumerate(['Cell', 'Fish', 'Apple', 'Ananas']):
#     item = QtGui.QStandardItem(text)
#     model.setItem(row, 2, item)
#
# # filter proxy model
# filter_proxy_model = QtCore.QSortFilterProxyModel()
# filter_proxy_model.setSourceModel(model)
# filter_proxy_model.setFilterKeyColumn(2) # third column
#
# # # line edit for filtering
# layout = QVBoxLayout(window)
# # line_edit = QLineEdit()
# # line_edit.textChanged.connect(filter_proxy_model.setFilterRegExp)
# # layout.addWidget(line_edit)
#
# # table view
# table = QTableView()
# table.setModel(filter_proxy_model)
# layout.addWidget(table)
#
# enter = QtWidgets.QPushButton()
# enter.clicked.connect(QtCore.QCoreApplication.instance().quit)
# enter.resize(100, 50)
# enter.move(500, 500)
# enter.setToolTip("<h3>Submit</h3>")
# enter.setStyleSheet("background: white; border:none;")
#
# def run():
#     app = QtWidgets.QApplication(sys.argv)
#     window.show()
#     sys.exit(app.exec_())
#
# run()
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Revision Cards'
        self.setGeometry(50, 50, 1000, 600)
        backGround = self.palette()
        backGround.setColor(self.backgroundRole(), QColor(15,102,102))
        self.setPalette(backGround)

        self.table_widget = MyTableWidget(self)
        # self.setCentralWidget(self.table_widget)

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
        self.pushButton1 = QPushButton("PyQt5 button")
        self.tab1.layout.addWidget(self.pushButton1)
        self.tab1.setLayout(self.tab1.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        #self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
