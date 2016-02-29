import PythonMagick
from pyPdf import PdfFileReader

img = PythonMagick.Image()
def pdf_to_img(input_file, density):
	img.density(density)
	my_file = PdfFileReader(file("{0}","r").format(input_file))
	numPages= myfile.getNumPages()
	for i in range(numPages):
		img.read("{0}[{1}]".format(input_file,i))
		img.write("{0}_image{1}.jpg".format(input_file,i))