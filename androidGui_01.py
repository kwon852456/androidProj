import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
import PyQt5

form_class = uic.loadUiType("main_window.ui")[0]
LandingPageUI, LandingPageBase = uic.loadUiType("recording_dialog.ui")



#유저 목록
users = ["kim", "park", "lee", "han"]


class Recording_dialog(PyQt5.QtWidgets.QDialog, LandingPageUI):
    def __init__(self, parent=None):
        LandingPageBase.__init__(self, parent)
        self.setupUi(self)

        self.btn_stop.clicked.connect(self.btn_stop_clicked)

    def btn_stop_clicked(self):
        self.close()


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self.currentItem = 0;
        self.users = ["kim", "park", "lee", "han"]

        self.view = self.lv_names
        self.model = QStandardItemModel()

        for f in self.users:
            self.model.appendRow(QStandardItem(f))

        self.view.setModel(self.model)

        self.btn_add.clicked.connect(self.btn_add_clicked)
        self.btn_delete.clicked.connect(self.btn_delete_clicked)
        self.view.clicked.connect(self.lv_clicked)

    def btn_add_clicked(self):

        text, ok = QInputDialog.getText(self, '추가할 사용자', '추가할 사용자 이름을 입력하세요')
        if ok:
            self.dlg = Recording_dialog()
            self.dlg.exec_()

            users.append(str(text))
            self.update_view()

    def btn_delete_clicked(self):
        users.pop(self.currentItem)
        self.update_view()

    def lv_clicked(self, index):
        self.currentItem = index.row()

    def update_view(self):
            self.model.clear()

            for f in users:
                self.model.appendRow(QStandardItem(f))
            self.view.setModel(self.model)

            print(self.users)




if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec_()
