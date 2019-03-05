import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic

form_class = uic.loadUiType("main_window.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.currentIndex = 0;

        self.btn_add.clicked.connect(self.btn_add_clicked)

        self.fruits = ["banana", "apple", "melon", "pear"]

        self.view = self.lv_names
        model = QStandardItemModel()
        for f in self.fruits:
            model.appendRow(QStandardItem(f))
        self.view.setModel(model)

        self.view.doubleClicked.connect(self.lv_double_clicked)

        self.view.clicked.connect(self.lv_double_clicked)

    def btn_add_clicked(self):
#        QMessageBox.about(self,"Message", "clicked...!")
        print(self.fruits[self.currentIndex])

    def lv_double_clicked(self, index):
        print(self.fruits[index.row()])

    def lv_double_clicked(self,index):
        self.currentIndex = index.row()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
