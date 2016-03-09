import cv2
import numpy as np
import math
from wand.image import Image
import PythonMagick
from pyPdf import PdfFileReader
import os,sys
from graphextract_returnArray import pdfwithgraph

class Graph:
	def __init__(self,image):
		self.graph = image
    	

def main():
    """Main function to execute. Put name of image in the first parameter of constructor"""
    pdfName  = raw_input()
    G = pdfwithgraph(pdfName,200,50,1500,70)
    ga = G.graphextract()
    graphImages = []
    for g in ga:
    	graphImages.append(Graph(g))


if __name__=='__main__':
    main()