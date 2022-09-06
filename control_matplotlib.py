import sys

from PyQt6 import QtCore, QtWidgets, QtGui
from PyQt6.QtWidgets import QApplication, QMainWindow
from mpl_squares import square as sq
from scatter_squares import scatter_squares as sc_sq
from rw_visual import print_randow_walk as r_w

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.main = MainWindow
        MainWindow.resize(self, 653, 326)
        self.main.setWindowTitle(self, 'matplotlib')
        self.widget = QtWidgets.QWidget(self)
        self.widget.setObjectName("widget")

        self.btn_1 = QtWidgets.QPushButton(self.widget)
        self.btn_1.setGeometry(QtCore.QRect(120, 110, 131, 71))
        self.btn_1.setStyleSheet("background-color: rgb(181, 255, 120);")
        self.btn_1.setObjectName("btn_1")

        self.btn_2 = QtWidgets.QPushButton(self.widget)
        self.btn_2.setGeometry(QtCore.QRect(260, 110, 131, 71))
        self.btn_2.setStyleSheet("background-color: rgb(107, 255, 218);")
        self.btn_2.setObjectName("btn_2")

        self.btn_3 = QtWidgets.QPushButton(self.widget)
        self.btn_3.setGeometry(QtCore.QRect(400, 110, 131, 71))
        self.btn_3.setStyleSheet("background-color: rgb(255, 128, 37);")
        self.btn_3.setObjectName("btn_3")

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(False)

        self.btn_2.setFont(font)
        self.btn_3.setFont(font)
        self.btn_1.setFont(font)

        MainWindow.setCentralWidget(self, self.widget)


        self.retranslate()

    def retranslate(self):
        _translate = QtCore.QCoreApplication.translate
        self.btn_1.setText(_translate("MainWindow", "Squares"))
        self.btn_2.setText(_translate("MainWindow", "Scatter squares"))
        self.btn_3.setText(_translate("MainWindow", "Randow walk"))

        self.btn_1.clicked.connect(self.show_window_1)
        self.btn_2.clicked.connect(self.show_window_2)
        self.btn_3.clicked.connect(self.show_window_3)

    def show_window_1(self):
        a1 = sq()

    def show_window_2(self):
        a2 = sc_sq()

    def show_window_3(self):
        a3 = r_w()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())