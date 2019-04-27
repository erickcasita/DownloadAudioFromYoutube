import os
from audio import *
from PyQt5 import QtCore, QtWidgets
import os.path as path
import pafy,time,sys,csv
from functools import partial
from pydub import AudioSegment
class ConvertAudio(QtCore.QObject):
    signal_conv_total = QtCore.pyqtSignal(int)
    signal_conv_value = QtCore.pyqtSignal(int)
    @QtCore.pyqtSlot(bool)
    def progress_infinito(self,ruta, title,value):
        self.signal_conv_total.emit(100)
        cont = 0
        while value:
            time.sleep(1)
            self.signal_conv_value.emit(cont)
            if not (path.exists(ruta+"/"+title+".webm")):
                break
            else:
                if(cont == 100):
                    cont = 0
                else:
                    cont+=1
        self.signal_conv_value.emit(100)
class MetaDatos(QtCore.QObject):
    signal_meta = QtCore.pyqtSignal(str, str,int,str,str)
    @QtCore.pyqtSlot(str, str,int,str,str)
    def information(self, url):
        video = pafy.new(url)
        title = video.title
        duration = video.duration
        views = video.viewcount
        autor = video.author
        imagen = video.thumb
        self.signal_meta.emit(title,duration,views,autor,imagen)
class DownloadAudio(QtCore.QObject):
    signal_recvd = QtCore.pyqtSignal(int)
    signal_total = QtCore.pyqtSignal(int)
    signal_info = QtCore.pyqtSignal(str, str)
    signal_btn_status = QtCore.pyqtSignal(bool)
    signal_dwn_file = QtCore.pyqtSignal(str, bool)
    @QtCore.pyqtSlot(str, str)
    def download(self, ruta, url,formato):
        self.signal_btn_status.emit(False)
        video = pafy.new(url)
        title = video.title
        duration = video.duration
        self.signal_info.emit(title, duration)
        """
        video = pafy.new(url)
        title = video.title
        duration = video.duration
        """
        dwn = video.getbestaudio()
        dwn.download(filepath=ruta, callback=self.mycb, meta=True)
        if (formato == "mp3"):
            self.signal_dwn_file.emit(title,True)
            song = AudioSegment.from_file(ruta+"/"+title+".webm",format="webm")
            song.export(ruta+"/"+title+".mp3", format="mp3",bitrate="128k")
            os.remove(ruta+"/"+title+".webm")
        elif (formato == "ogg"):
            self.signal_dwn_file.emit(title,True)
            song = AudioSegment.from_file(ruta+"/"+title+".webm",format="webm")
            song.export(ruta+"/"+title+".ogg", format="mp3",bitrate="128k")
            os.remove(ruta+"/"+title+".webm")
        else:
            pass
        self.signal_btn_status.emit(True)
    #Enviar una señal que determina si el archivo ya esta descargado
    # Método de la librería Pafy para saber los kbs recibidos y
    # los totales (con este me apoyo para establecer la barra de progreso)
    def mycb(self, total, recvd, ratio, rate, eta):
        self.signal_total.emit(total)
        self.signal_recvd.emit(recvd)
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)
        self.setFixedSize(920,670)
        music_path = QtCore.QStandardPaths.writableLocation(
            QtCore.QStandardPaths.MusicLocation
        )
        self.txt_ruta.setText(os.path.normpath(music_path))
        self.tableWidget.setColumnWidth(0, 350)
        self.tableWidget.setColumnWidth(1, 350)
        self.tabla_datos.setAlternatingRowColors(True)
        for indice, ancho in enumerate((200, 120, 120, 110, 280), start=0):
            self.tabla_datos.setColumnWidth(indice, ancho)
        self.btn_descargar.clicked.connect(self.download_audio)
        self.btn_destino.clicked.connect(self.ruta)
        self.btn_datos.clicked.connect(self.metadatos)
        self.btn_exportar.clicked.connect(self.exportar)
        self.btn_nuevo.clicked.connect(self.limpiar_tabla)
        self.progressBar.setValue(0)

        thread = QtCore.QThread(self)
        thread.start()
        self.calc = DownloadAudio()
        self.calc.moveToThread(thread)
        self.calc.signal_recvd.connect(self.progressBar.setValue)
        self.calc.signal_total.connect(self.progressBar.setMaximum)
        self.calc.signal_info.connect(self.append_row)
        self.calc.signal_btn_status.connect(self.btn_descargar.setEnabled)
        self.calc.signal_dwn_file.connect(self.barra_infinita)
        self.tableWidget.setRowCount(0)
        #Declarando un hilo para ejecutar la barra infinita
        bthread = QtCore.QThread(self)
        bthread.start()
        self.bcvn = ConvertAudio()
        self.bcvn.moveToThread(bthread)
        self.bcvn.signal_conv_value.connect(self.progressBar.setValue)
        self.bcvn.signal_conv_total.connect(self.progressBar.setMaximum)
        #Declarando un hilo para los metadatos
        methread = QtCore.QThread(self)
        methread.start()
        self.hinfo = MetaDatos()
        self.hinfo.moveToThread(methread)
        self.hinfo.signal_meta.connect(self.agrega_info)
    def download_audio(self):
        ruta = self.txt_ruta.text()
        if (self.radioButton.isChecked()):
            formato = "mp3"
        if (self.radioButton_2.isChecked()):
            formato = "ogg"
        self.progressBar.setValue(0)
        self.lbl_status.setText("Descargando audio...")
        url = self.txt_url.text()
        if url:
            
            wrapper = partial(self.calc.download, ruta, url,formato)
            QtCore.QTimer.singleShot(0, wrapper)
    @QtCore.pyqtSlot(str, str)
    def append_row(self, title, duration):
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(duration))
    def barra_infinita(self,title, value):
        ruta = self.txt_ruta.text()
        self.progressBar.setValue(0)
        self.lbl_status.setText("Convirtiendo audio")
        value = True
        wrapper2 = partial(self.bcvn.progress_infinito,ruta,title,value)
        QtCore.QTimer.singleShot(0, wrapper2)
    def ruta(self):
        path = QtWidgets.QFileDialog.getExistingDirectory(self)
        if path:
            self.txt_ruta.setText(os.path.normpath(path))
    def metadatos(self):
        url = self.txt_url_2.text()
        if url:
            wrapper3 = partial(self.hinfo.information, url)
            QtCore.QTimer.singleShot(0, wrapper3)
    @QtCore.pyqtSlot(str, str, int, str, str)
    def agrega_info(self, title, duration, views, autor, imagen):
        row = self.tabla_datos.rowCount()
        self.tabla_datos.insertRow(row)
        self.tabla_datos.setItem(row, 0, QtWidgets.QTableWidgetItem(title))
        self.tabla_datos.setItem(row, 1, QtWidgets.QTableWidgetItem(duration))
        self.tabla_datos.setItem(row, 2, QtWidgets.QTableWidgetItem(str(views)))
        self.tabla_datos.setItem(row, 3, QtWidgets.QTableWidgetItem(autor))
        self.tabla_datos.setItem(row, 4, QtWidgets.QTableWidgetItem(imagen))
    def exportar(self):
        name, _ = QtWidgets.QFileDialog.getSaveFileName(self,"Exportar","","CSV(*.csv)")
        if (name):
            with open(str(name), "w") as fileOutput:
                writer = csv.writer(fileOutput)
                for row in range(self.tabla_datos.rowCount()):
                    rowdata = []
                    for column in range(self.tabla_datos.columnCount()):
                        item = self.tabla_datos.item(row, column)
                        if item is not None:
                            rowdata.append(item.text())
                        else:
                            rowdata.append('')
                    writer.writerow(rowdata)
    def limpiar_tabla(self):
        self.tabla_datos.clearContents()
        self.tabla_datos.setRowCount(0)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()