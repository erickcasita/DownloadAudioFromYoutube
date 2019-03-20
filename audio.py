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
        MainWindow.resize(618, 448)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lbl_titulo = QtWidgets.QLabel(self.centralwidget)
        self.lbl_titulo.setGeometry(QtCore.QRect(90, 0, 441, 71))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(18)
        self.lbl_titulo.setFont(font)
        self.lbl_titulo.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_titulo.setObjectName("lbl_titulo")
        self.lbl_version = QtWidgets.QLabel(self.centralwidget)
        self.lbl_version.setGeometry(QtCore.QRect(260, 60, 91, 21))
        self.lbl_version.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_version.setObjectName("lbl_version")
        self.lbl_url = QtWidgets.QLabel(self.centralwidget)
        self.lbl_url.setGeometry(QtCore.QRect(190, 100, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lbl_url.setFont(font)
        self.lbl_url.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_url.setObjectName("lbl_url")
        self.txt_url = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_url.setGeometry(QtCore.QRect(180, 130, 271, 31))
        self.txt_url.setObjectName("txt_url")
        self.btn_descargar = QtWidgets.QPushButton(self.centralwidget)
        self.btn_descargar.setGeometry(QtCore.QRect(280, 270, 91, 31))
        self.btn_descargar.setObjectName("btn_descargar")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(170, 310, 311, 31))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.lbl_status = QtWidgets.QLabel(self.centralwidget)
        self.lbl_status.setGeometry(QtCore.QRect(240, 360, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lbl_status.setFont(font)
        self.lbl_status.setText("")
        self.lbl_status.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_status.setObjectName("lbl_status")
        self.btn_destino = QtWidgets.QPushButton(self.centralwidget)
        self.btn_destino.setGeometry(QtCore.QRect(70, 210, 91, 31))
        self.btn_destino.setObjectName("btn_destino")
        self.txt_ruta = QtWidgets.QLineEdit(self.centralwidget)
        self.txt_ruta.setGeometry(QtCore.QRect(180, 210, 271, 33))
        self.txt_ruta.setObjectName("txt_ruta")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 618, 25))
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
        self.lbl_titulo.setText(_translate("MainWindow", "DOWNLOAD AUDIO FROM YOUTUBE"))
        self.lbl_version.setText(_translate("MainWindow", "Versión 0.1"))
        self.lbl_url.setText(_translate("MainWindow", "Ingrese URL de Youtube:"))
        self.btn_descargar.setText(_translate("MainWindow", "Descargar"))
        self.btn_destino.setText(_translate("MainWindow", "Destino:"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
