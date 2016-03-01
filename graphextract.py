import cv2
import numpy as np
import math
from wand.image import Image

class pdfwithgraph:
    def __init__(self,filename,minLineLength,maxLineGap,threshArea,percent):
        """Initializes the class
        Keyword arguments:
        filename -- actual image of the entire pdf
        maxLineLength -- parameter of HpughLinesP function of opencv
        minLineGap -- parameter of HoughLinesP function of opencv
        threshArea -- threshold area to select the required contours
        percent -- percentage of area by which the the entire graph with labels is more than than the bounding box
        """
        self.file = filename
        self.minLineLength = minLineLength
        self.maxLineGap = maxLineGap
        self.threshArea = threshArea
        self.percent = percent        

    
    def houghp(self):
        """Does a Hough Transform (probabilistic) on the image given"""
        img = cv2.imread(self.file)
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        h,w,channel = img.shape
        gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,7)
        kernel = np.zeros((5,5),np.uint8)
        gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
        gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
        gray = cv2.GaussianBlur(gray,(5,5),0)
        #edges = cv2.Canny(gray,50,150,apertureSize = 3)
        lines = cv2.HoughLinesP(gray,0.25,np.pi/360,100,self.minLineLength,self.maxLineGap)
        im2 = np.zeros((h,w,channel),np.uint8)
        for x1,y1,x2,y2 in lines[0]:
            cv2.line(im2,(x1,y1),(x2,y2),(0,255,0),2)
        return im2

    
    def polydp(self,image):
        """Does a polydp (shape) approximation on the contours detected
        Keyword arguments:
        image -- image returned by the houghp()
        """
        img = cv2.imread(self.file)
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        (cnts, _) = cv2.findContours(gray, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        h,w,channel = image.shape
        count_graph = 1
        f = open("contours.txt","wb")
        for c in cnts:
            if cv2.contourArea(c) >self.threshArea:
                approx = cv2.approxPolyDP(c,0.01*cv2.arcLength(c,True),True)
                if len(approx)<10 and len(approx)>2:
                    x,y,w,h = cv2.boundingRect(c)
                    #specify = [x,y,w,h]
                    a =  int(((-2)*(w+h) + math.sqrt((4*(w+h)*(w+h)+4*4*self.percent*w*h/100)))/8)
                    graph = img[y-a:y+h+a,x-2*a:x+w+a]
                    cv2.imwrite("graph_"+str(count_graph)+".jpg",graph)
                    specify = str(tuple((2*a,a,w,h)))
                    f.write(specify)
                    f.write('\n')
                    count_graph = count_graph + 1

 
    def graphextract(self):
        """Wrapper function for extracting the images"""
        self.polydp(self.houghp())
def main():
    """Main function to execute. Put name of image in the first parameter of constructor"""
    G = pdfwithgraph('0001.jpg',200,50,1500,70)
    G.graphextract()

if __name__=='__main__':
    main()