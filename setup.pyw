from audio import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog,QFileDialog, QPushButton,QMessageBox,QTableWidget,QTableWidgetItem
from pydub import AudioSegment
import os,pyprind, getpass, glob, pafy, youtube_dl,tqdm
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.setFixedSize(920,700)
		self.txt_ruta.setText("/home/"+getpass.getuser()+"/Música")
		self.tableWidget.setColumnWidth(0, 350)
		self.tableWidget.setColumnWidth(1, 350) 
		self.btn_descargar.clicked.connect(self.download_audio)
		self.btn_destino.clicked.connect(self.ruta)

	def download_audio(self):
		ruta = self.txt_ruta.text()
		self.progressBar.setValue(0)
		url = self.txt_url.text()
		video = pafy.new(url)
		title = video.title
		duration = video.duration
		self.tableWidget.setItem(0,0, QTableWidgetItem(title))
		self.tableWidget.setItem(0,1, QTableWidgetItem(duration))
		s = video.getbestaudio()
		s.download(filepath=ruta,callback=self.mycb,meta=True)
		self.lbl_status.setText("Convirtiendo a MP3 espere....")
		self.progressBar.setValue(100)
		if (self.radioButton.isChecked()):
			song = AudioSegment.from_file(ruta+"/"+title+".webm",format="webm")
			song.export(ruta+"/"+title+".mp3", format="mp3",bitrate="128k")
			os.remove(ruta+"/"+title+".webm")
			QMessageBox.about(self,"Completado","La conversión se ha completado.")
		self.lbl_status.setText("Descarga y conversión finalizada")
		if (self.radioButton_2.isChecked()):
			song = AudioSegment.from_file(ruta+"/"+title+".webm",format="webm")
			song.export(ruta+"/"+title+".ogg", format="ogg",bitrate="128k")
			os.remove(ruta+"/"+title+".webm")
			QMessageBox.about(self,"Completado","La conversión se ha completado.")

			
	def mycb(self,total, recvd, ratio, rate,eta):
		self.lbl_status.setText("Descargando...")
		self.progressBar.setMaximum(total)
		self.progressBar.setValue(recvd)
	def ruta(self):
		path = os.path.normpath(QFileDialog.getExistingDirectory(self))
		self.txt_ruta.setText(path) 
if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()