import os
from audio import *
from PyQt5 import QtCore, QtWidgets
import os.path as path
import pafy,time
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
        video = pafy.new(url)
        title = video.title
        duration = video.duration
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
        self.setFixedSize(920,700)
        music_path = QtCore.QStandardPaths.writableLocation(
            QtCore.QStandardPaths.MusicLocation
        )
        self.txt_ruta.setText(os.path.normpath(music_path))
        self.tableWidget.setColumnWidth(0, 350)
        self.tableWidget.setColumnWidth(1, 350)
        self.btn_descargar.clicked.connect(self.download_audio)
        self.btn_destino.clicked.connect(self.ruta)
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
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()