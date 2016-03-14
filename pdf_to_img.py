import PythonMagick
from pyPdf import PdfFileReader
import sys
import os
import threading 
from PyQt4 import QtCore



class ResultObj(QtCore.QObject):
    def __init__(self, val, numPages):
        self.val = val
        self.numPages=numPages

class ImageThread(QtCore.QThread):
    finished = QtCore.pyqtSignal(object)
    progress = QtCore.pyqtSignal(object)

    def __init__(self, input_file,density, callback,callback2, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.input_file = input_file
        self.density = density
        self.finished.connect(callback)
        self.progress.connect(callback2)

    def pdf_to_img1(self,input_file, density): #give density in string format("200")
		img = PythonMagick.Image()	
		img.density(density)
		my_file = PdfFileReader(file("{0}".format(input_file),"r"))
		numPages= my_file.getNumPages()
		for i in range(numPages):
			img.read("{0}[{1}]".format(input_file,i))
			img.alpha=False
			filename="{0}{1}.png".format(input_file,i)
			filename1="{0}{1}new.png".format(input_file,i)
			img.write(filename)
			os.system("convert -flatten "+filename+" "+filename1)
			self.progress.emit(ResultObj(i, numPages))
		self.finished.emit(ResultObj(numPages, numPages))

    
    def run(self):
        #call your function here
        self.pdf_to_img1(self.input_file, self.density)    

	



'''class imageThread (threading.Thread):
    def __init__(self, threadID, name, array,filename, density):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.array = array
        self.filename = filename
        self.density = density
    def run(self):
        print "Starting " + self.name
        #print_time(self.name, self.counter, 5)
        pdf_to_img1(self.filename, self.density, self.array)
        print "Exiting " + self.name'''






if __name__ == '__main__':
	pdf_to_img1(sys.argv[1], "200")