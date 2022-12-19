import sys
from main import Database
import pyodbc
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QApplication, QDialog, QGraphicsScene, QTableWidgetItem

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = uic.loadUi("forms/admin.ui", self)
        self.setWindowTitle("ничто")

    def authoriz(self, wnd):
        dialog = DialogAutorization(wnd)
        dialog.setWindowTitle("Авторизация")
        dialog.show()
        dialog.exec_()


class DialogAutorization(QDialog):
    def __init__(self, wnd, parent=None):
        self.wnd = wnd
        super(DialogAutorization, self).__init__(parent)
        self.ui = uic.loadUi("forms/auth.ui", self)
        self.setWindowTitle("Авторизация?")
        self.scene = QGraphicsScene(0, 0, 350, 50)
        self.scene.clear()
        self.ui.autorization_btn.clicked.connect(self.autoriz)
        self.db = Database()


    def autoriz(self):
        login = self.ui.line_log.text()
        password = self.ui.line_pas.text()

        if login == '' or password == '':
            self.error()

        if login not in self.db.check_login():
            self.error()

        else:
            aut = self.db.get_log(login)
            autpas = aut[0]
            role = aut[1]

            if password != autpas:
                self.error()
            else:
                if role == 3:
                    self.HeadShift()
                if role == 2:
                    self.Admin()
                if role == 1:
                    self.Seller()

    def error(self):
        self.mesbox = QMessageBox(self)
        self.mesbox.setWindowTitle("Ошибка")
        self.mesbox.setText("Ошибка входа")
        self.mesbox.setStandardButtons(QMessageBox.Ok)
        self.mesbox.show()

    def Seller(self):
        self.mesbox = QMessageBox(self)
        self.mesbox.setWindowTitle("Продавец")
        self.mesbox.setText("Окно продавца")
        self.mesbox.setStandardButtons(QMessageBox.Ok)
        self.mesbox.show()

    def Admin(self):
        self.mesbox = QMessageBox(self)
        self.mesbox.setWindowTitle("Админ")
        self.mesbox.setText("Окно админа")
        self.mesbox.setStandardButtons(QMessageBox.Ok)
        self.mesbox.show()

    def HeadShift(self):
        self.mesbox = QMessageBox(self)
        self.mesbox.setWindowTitle("Старший смены")
        self.mesbox.setText("Окно старшего смена")
        self.mesbox.setStandardButtons(QMessageBox.Ok)
        self.mesbox.show()

class Builder:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.wnd = MainWindow()
        self.auth()

    def auth(self):
        self.wnd.authoriz(self.wnd)
        self.app.exec()

if __name__ == '__main__':
    B = Builder()