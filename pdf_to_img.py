import PythonMagick
from pyPdf import PdfFileReader

img = PythonMagick.Image()
def pdf_to_img(input_file, density): #give density in string format("200")
	img.density(density)
	my_file = PdfFileReader(file("{0}".format(input_file),"r"))
	numPages= my_file.getNumPages()
	for i in range(numPages):
		img.read("{0}[{1}]".format(input_file,i))
		img.write("{0}_image{1}.jpg".format(input_file,i))