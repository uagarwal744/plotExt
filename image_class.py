import cv2
import numpy as np
import math
#from wand.image import Image
import PythonMagick
from pyPdf import PdfFileReader
import os,sys
from graphextract_returnArray import PlotExtractor
import axis
import legendDetect
import hough
from PyQt4 import QtCore
import os
import uuid

import tables
import time
current_milli_time = lambda: int(round(time.time() * 1000))

class Graph:
    outer_dir = "plot_dir"
    def __init__(self,image,outer_image_file):
        self.image = image
        self.manual_axis = False
        self.manual_legend = False
        self.outer_image_file = outer_image_file
        if not os.path.exists(Graph.outer_dir):
            os.makedirs(Graph.outer_dir)
        inner_dir = str(uuid.uuid4())
        self.working_dir = os.path.join(Graph.outer_dir,inner_dir)
        if not os.path.exists(self.working_dir):
            os.makedirs(self.working_dir)

    def axis_detection(self):
        #self.resized_image=cv2.imread(self.outer_image_file)
        self.axis_x1,self.axis_x2,self.axis_y1,self.axis_y2 = axis.axis(self.image,self.working_dir)
        print self.axis_x1,self.axis_x2,self.axis_y1,self.axis_y2,'axxxxxxxis'
    
    def legend_detection(self):
        self.image_without_legend,self.legend = legendDetect.legend_detect(self.outer_image_file,self.axis_x1,self.axis_x2,self.axis_y1,self.axis_y2,self.working_dir)
        #cv2.imshow("image",self.image_without_legend)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
    def value_calculation(self):
        self.inner_image_without_legend = self.image_without_legend[self.axis_y1:self.axis_y2,self.axis_x1:self.axis_x2]
        self.inner_image_file_without_legend = os.path.join(self.working_dir,"inner_image_without_legend.png")
        cv2.imwrite(self.inner_image_file_without_legend,self.inner_image_without_legend)
        self.table = tables.run(self.inner_image_file_without_legend,self.axis_bot_left,self.axis_top_right,self.scale_x,self.scale_y,self.value_x1,self.value_x2,self.value_y1,self.value_y2,self.pixel_x1,self.pixel_x2,self.pixel_y1,self.pixel_y2,self.inner_image_without_legend,self.legend,self.working_dir)
    
    def scale_detection(self):
        self.inner_image_file,self.axis_bot_left,self.axis_top_right,self.scale_x,self.scale_y,self.value_x1,self.value_x2,self.value_y1,self.value_y2,self.pixel_x1,self.pixel_x2,self.pixel_y1,self.pixel_y2 = hough.final_scale(self.image,self.working_dir)
        #print(hough.final_scale(self.image))
    
    def run(self):
        self.axis_detection()
        graph = self.image[self.axis_y1:self.axis_y2,self.axis_x1:self.axis_x2]
        cv2.imwrite("image.png",graph)
        #cv2.namedWindow("image",cv2.CV_WINDOW_NORMAL)
        #cv2.imshow("image",graph)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        self.scale_detection()
        self.legend_detection()
        self.value_calculation()

'''class ResultObj(QtCore.QObject):
    def __init__(self, table):
        self.table=table

class TableThread(QtCore.QThread):
    finished=QtCore.pyqtSignal(object)
    def __init__(self,GraphObj, callback, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.image = GraphObj
        self.finished.connect(callback)
    
    def run(self):
        self.image.run()
        self.finished.emit(ResultObj(self.image.table))'''


def main():
    """Main function to execute. Put name of image in the first parameter of constructor"""
    pdfName  = raw_input()
    G = PlotExtractor(pdfName,200,50,1500,70)
    ga,na = G.graphextract()
    print(ga,na)
    graphImages = []
    
    for i in range(len(ga)):
        for j in range(len(ga[i])):
            graphImages.append(Graph(ga[i][j],na[i][j]))
    for G in graphImages:
        G.run()
        break;




if __name__=='__main__':
    main()
