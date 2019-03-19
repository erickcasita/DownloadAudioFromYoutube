from audio import *
import pafy
import youtube_dl
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.btn_descargar.clicked.connect(self.download_audio)

	def download_audio(self):
		self.progressBar.setValue(0)
		url = self.txt_url.text()
		video = pafy.new(url)
		s = video.getbestaudio()
		filename = s.download(callback=self.mycb)
		self.lbl_status.setText("Descarga finalizada")
	def mycb(self,total, recvd, ratio, rate,eta):
		self.lbl_status.setText("Descargando....")
		self.progressBar.setMaximum(total)
		self.progressBar.setValue(recvd)
if __name__ == '__main__':
	app = QtWidgets.QApplication([])
	window = MainWindow()
	window.show()
	app.exec_()
    
    
    