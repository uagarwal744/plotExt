import PythonMagick
from pyPdf import PdfFileReader

def pdf_to_img(input_file, density): #give density in string format("200")
""" Creating an image file using PythonMagick and assigning density to it.
	img.read reads the input_file in the specified density(say 200) and 
	img.write writes the pdf file in image format."""
    img = PythonMagick.Image()
	img.density(density)
	my_file = PdfFileReader(file("{0}".format(input_file),"r"))
	numPages= my_file.getNumPages()
	for i in range(numPages):
		img.read("{0}[{1}]".format(input_file,i))
		img.write("{0}_image{1}.jpg".format(input_file,i))