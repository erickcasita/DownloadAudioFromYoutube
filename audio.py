# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'audio.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(915, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_version = QtWidgets.QLabel(self.centralwidget)
        self.lbl_version.setGeometry(QtCore.QRect(410, 300, 91, 21))
        self.lbl_version.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_version.setObjectName("lbl_version")
        self.lbl_url = QtWidgets.QLabel(self.centralwidget)
        self.lbl_url.setGeometry(QtCore.QRect(40, 290, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_url.setFont(font)
        self.lbl_url.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_url.setObjectName("lbl_url")
        self.txt_url = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_url.setGeometry(QtCore.QRect(220, 330, 531, 31))
        self.txt_url.setObjectName("txt_url")
        self.btn_descargar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_descargar.setGeometry(QtCore.QRect(410, 420, 91, 31))
        self.btn_descargar.setObjectName("btn_descargar")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(280, 470, 371, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.lbl_status = QtWidgets.QLabel(self.centralwidget)
        self.lbl_status.setGeometry(QtCore.QRect(370, 570, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_status.setFont(font)
        self.lbl_status.setText("")
        self.lbl_status.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_status.setObjectName("lbl_status")
        self.btn_destino = QtWidgets.QPushButton(self.centralwidget)
        self.btn_destino.setGeometry(QtCore.QRect(110, 370, 91, 31))
        self.btn_destino.setObjectName("btn_destino")
        self.txt_ruta = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_ruta.setGeometry(QtCore.QRect(220, 370, 281, 33))
        self.txt_ruta.setObjectName("txt_ruta")
        self.lbl_titulo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_titulo.setGeometry(QtCore.QRect(40, 0, 831, 311))
        self.lbl_titulo.setText("")
        self.lbl_titulo.setPixmap(QtGui.QPixmap(":/logo_cabeza/logosoftware.png"))
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(280, 510, 371, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setAutoScroll(True)
        self.tableWidget.setHorizontalScrollMode(QtWidgets.QAbstractItemView.ScrollPerItem)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.lbl_titulo.raise_()
        self.lbl_version.raise_()
        self.lbl_url.raise_()
        self.txt_url.raise_()
        self.btn_descargar.raise_()
        self.lbl_status.raise_()
        self.btn_destino.raise_()
        self.txt_ruta.raise_()
        self.progressBar.raise_()
        self.tableWidget.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 915, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Download Audio From Youtube"))
        self.lbl_version.setText(_translate("MainWindow", "Versión 0.3"))
        self.lbl_url.setText(_translate("MainWindow", "Ingrese URL de Youtube:"))
        self.btn_descargar.setText(_translate("MainWindow", "Descargar"))
        self.btn_destino.setText(_translate("MainWindow", "Destino:"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("MainWindow", "1"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nombre "))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Duración"))


import logo_cabeza_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
