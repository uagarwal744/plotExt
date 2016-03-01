from PIL import Image as IM
from PyPDF2 import PdfFileMerger, PdfFileReader
import os

def file_merge(filenames):
	merger = PdfFileMerger()
	for filename in filenames:
	    merger.append(PdfFileReader(file(filename, 'rb')))

	merger.write("{0}".format(filenames[0]))

def img_to_pdf(input_file):
	files = []
	for i in input_file:
		outfile_name = ''.join(i.split(".")[:-1]) + ".pdf"
		im = IM.open("{0}".format(i))
		im.save(outfile_name, "PDF", resolution = 100.0)
		files.append(outfile_name)
	file_merge(files)
	for i in files[1:]:
		os.remove(i)
