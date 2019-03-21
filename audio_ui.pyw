from audio import *
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton,QMessageBox
from PyQt5.QtWidgets import QFileDialog
import pafy
import youtube_dl
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.btn_descargar.clicked.connect(self.download_audio)
		self.btn_destino.clicked.connect(self.ruta)

	def download_audio(self):
		try:
			ruta = self.txt_ruta.text()
			self.progressBar.setValue(0)
			url = self.txt_url.text()
			video = pafy.new(url)
			s = video.getbestaudio()
			filename = s.download(ruta,callback=self.mycb)
			self.lbl_status.setText("Descarga finalizada")		
		except:
			QMessageBox.about(self,"Error","Ha ocurrido algun error con la URL O Esta vacía.")


	def mycb(self,total, recvd, ratio, rate,eta):
		self.lbl_status.setText("Descargando....")
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
    
    
    