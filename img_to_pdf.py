from PIL import Image as IM
from pyPdf import PdfFileMerger, PdfFileReader
import os

def file_merge(filenames):
"""Takes pdf filenames in the form of list. 
Creating merger using PdfFileMerger and using this creating a single pdf file. 
merger.write writes the created pdf file"""
	merger = PdfFileMerger()
	for filename in filenames:
	    merger.append(PdfFileReader(file(filename, 'rb')))

	merger.write("{0}".format(filenames[0]))

def img_to_pdf(input_file):
""" Takes input_file of images in the form of a list. Creating an 
empty files list to store the converted pdf spages. 
And input the files list into the file_merge function """
	files = []
	for i in input_file:
		outfile_name = ''.join(i.split(".")[:-1]) + ".pdf"
		im = IM.open("{0}".format(i))
		im.save(outfile_name, "PDF", resolution = 100.0)
		files.append(outfile_name)
	file_merge(files)
	for i in files[1:]:
		os.remove(i)
