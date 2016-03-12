import PythonMagick
from pyPdf import PdfFileReader
import sys
import os
from threading import Thread

img = PythonMagick.Image()

def pdf_to_img1(input_file, density): #give density in string format("200")
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
	return numPages


if __name__ == '__main__':
	pdf_to_img1(sys.argv[1], "200")