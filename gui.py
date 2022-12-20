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
                    self.shif_head_open()
                if role == 2:
                    self.admin_open()
                if role == 1:
                    self.seller_open()

    def error(self):
        self.mesbox = QMessageBox(self)
        self.mesbox.setWindowTitle("Ошибка")
        self.mesbox.setText("Ошибка входа")
        self.mesbox.setStandardButtons(QMessageBox.Ok)
        self.mesbox.show()

    def shif_head_open(self):
        self.ui.close()
        self.ui = ShiftHeadMenu()
        self.ui.show()

    def admin_open(self):
        self.ui.close()
        self.ui = AdminMenu()
        self.ui.show()

    def seller_open(self):
        self.ui.close()
        self.ui = SellerMenu()
        self.ui.show()

class ShiftHeadMenu(QMainWindow):
    def __init__(self):
        super(ShiftHeadMenu, self).__init__()
        self.ui = uic.loadUi("forms/shift_head.ui", self)
        self.window().setWindowTitle("ShiftHead")
        self.ui.back_btn.clicked.connect(self.exit)
        self.table = self.ui.tableWidget
        self.db = Database()
        self.ui.add_order_btn.clicked.connect(self.add_order)
        self.orders()

    def add_order(self):
        dialog = DialogAdd()
        dialog.setWindowTitle("Добавить заказ")
        dialog.show()
        dialog.exec_()

    def orders(self):
        self.table.clear()
        out = self.db.get_ord()
        self.table.setColumnCount(9)  # кол-во столбцов
        self.table.setRowCount(len(out))  # кол-во строк
        self.table.setHorizontalHeaderLabels(['ID', 'код заказа', 'дата создания','Время заказа','Код клиента','Код услуги','статус', 'дата закрытия','время аренды'])
        for i, order in enumerate(out):
            for x, field in enumerate(order):  # i, x - координаты ячейки, в которую будем записывать текст
                item = QTableWidgetItem()
                item.setText(str(field))  # записываем текст в ячейку
                item.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(i, x, item)


    def exit(self):
        dialog = DialogAutorization(self.window)
        self.ui.close()
        dialog.setWindowTitle("Авторизация")
        dialog.show()
        dialog.exec_()

class AdminMenu(QMainWindow):
    def __init__(self):
        super(AdminMenu, self).__init__()
        self.ui = uic.loadUi("forms/admin.ui", self)
        self.window().setWindowTitle("Admin")
        self.db = Database()
        self.ui.orders_btn.clicked.connect(self.orders)
        self.ui.history_btn.clicked.connect(self.history)
        self.ui.back_btn.clicked.connect(self.exit)
        self.table = self.ui.tableWidget

    def orders(self):
        self.table.clear()
        out = self.db.get_ord()
        self.table.setColumnCount(9)  # кол-во столбцов
        self.table.setRowCount(len(out))  # кол-во строк
        self.table.setHorizontalHeaderLabels(['ID', 'код заказа', 'дата создания','Время заказа','Код клиента','Код услуги','статус', 'дата закрытия','время аренды'])
        for i, order in enumerate(out):
            for x, field in enumerate(order):  # i, x - координаты ячейки, в которую будем записывать текст
                item = QTableWidgetItem()
                item.setText(str(field))  # записываем текст в ячейку
                if x == 0:  # для id делаем некликабельные ячейки
                    item.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(i, x, item)

    def history(self):
        self.table.clear()
        out = self.db.get_his()
        self.table.setColumnCount(4)  # кол-во столбцов
        self.table.setRowCount(len(out))  # кол-во строк
        self.table.setHorizontalHeaderLabels(
            ['ID', 'Дата входа', 'Дата выхода', 'Id сотрудника'])
        for i, order in enumerate(out):
            for x, field in enumerate(order):  # i, x - координаты ячейки, в которую будем записывать текст
                item = QTableWidgetItem()
                item.setText(str(field))  # записываем текст в ячейку
                item.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(i, x, item)

    def exit(self):
        dialog = DialogAutorization(self.window)
        self.ui.close()
        dialog.setWindowTitle("Авторизация")
        dialog.show()
        dialog.exec_()


class SellerMenu(QMainWindow):
    def __init__(self):
        super(SellerMenu, self).__init__()
        self.ui = uic.loadUi("forms/seller.ui", self)
        self.window().setWindowTitle("Seller")
        self.table = self.ui.order_table
        self.db = Database()
        self.ui.order_add_btn.clicked.connect(self.add_order)
        self.table = self.ui.order_table
        self.ui.back_btn.clicked.connect(self.exit)
        self.orders()

    def exit(self):
        dialog = DialogAutorization(self.window)
        self.ui.close()
        dialog.setWindowTitle("Авторизация")
        dialog.show()
        dialog.exec_()

    def orders(self):
        self.table.clear()
        out = self.db.get_ord()
        self.table.setColumnCount(9)  # кол-во столбцов
        self.table.setRowCount(len(out))  # кол-во строк
        self.table.setHorizontalHeaderLabels(['ID', 'код заказа', 'дата создания','Время заказа','Код клиента','Код услуги','статус', 'дата закрытия','время аренды'])
        for i, order in enumerate(out):
            for x, field in enumerate(order):  # i, x - координаты ячейки, в которую будем записывать текст
                item = QTableWidgetItem()
                item.setText(str(field))  # записываем текст в ячейку
                item.setFlags(Qt.ItemIsEnabled)
                self.table.setItem(i, x, item)

    def add_order(self):
        dialog = DialogAdd()
        dialog.setWindowTitle("Добавить заказ")
        dialog.show()
        dialog.exec_()

class DialogAdd(QDialog):
    def __init__(self):
        super(DialogAdd, self).__init__()
        self.ui = uic.loadUi("forms/add_order.ui", self)
        self.setWindowTitle("Добавить")
        self.db = Database()
        self.ui.add_btn_2.clicked.connect(self.add)
'''
    def add(self):
        create_date = self.ui.create_date.text()
        order_code = self.ui.order_code.text()
        order_time = self.ui.order_time.text()
        client_code = self.ui.client_code.text()
        services = self.ui.services.text()
        order_status = self.ui.order_status.text()
        use_time = self.ui.use_time.text()
        self.db.insertRequests(order_code, create_date,order_time, client_code,services, order_status,use_time)
        self.ui.close()
'''
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