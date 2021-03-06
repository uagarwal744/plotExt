import cv2
import numpy as np
import math
#from wand.image import Image
import PythonMagick
from pyPdf import PdfFileReader
import os,sys

class PlotExtractor:
    def __init__(self,pdfFile,minLineLength=100,maxLineGap=50,threshArea=1500,percent=70,ang_prec=180,det_prec=0.25,density="300"):
        """Initializes the class
        Keyword arguments:
        filename -- actual image of the entire pdf
        maxLineLength -- parameter of HpughLinesP function of opencv
        minLineGap -- parameter of HoughLinesP function of opencv
        threshArea -- threshold area to select the required contours
        percent -- percentage of area by which the the entire graph with labels is more than than the bounding box
        ang_prec -- angular precision of HoughLinesP function
        det_prec -- detail precision of HoughLinesP function
        density -- parameter for the quality of image. TO BE ENTERED IN STRING FORMAT
        """
        self.pagelist =[]# pagelist

        print self.pagelist
        
        self.pdfFile = pdfFile
        self.minLineLength = minLineLength
        self.maxLineGap = maxLineGap
        self.threshArea = threshArea
        self.percent = percent  
        self.ang_prec = ang_prec
        self.det_prec = det_prec  
        self.density = density  
        self.pdfImage = []  
        #self.graphArray = []
        self.graphName = []
        self.graphList = []

    
    def houghp(self):
        """Does a Hough Transform (probabilistic) on the image given"""
        global img
        img = cv2.imread(self.pageImage)
        #print self.pdfImage
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        h,w,channel = img.shape
        gray = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,7)
        kernel = np.zeros((5,5),np.uint8)
        gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
        #gray = cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel)
        #gray = cv2.filter2D(gray,-1,kernel)
        #gray = cv2.blur(gray,(5,5))
        #gray = cv2.medianBlur(gray,5)
        #gray = cv2.bilateralFilter(gray,9,75,75)
        gray = cv2.GaussianBlur(gray,(3,3),0)
        #edges = cv2.Canny(gray,50,150,apertureSize = 3)
        lines = cv2.HoughLinesP(gray,self.det_prec,np.pi/self.ang_prec,100,self.minLineLength,self.maxLineGap)
        im2 = np.zeros((h,w,channel),np.uint8)
        for x1,y1,x2,y2 in lines[0]:
            cv2.line(im2,(x1,y1),(x2,y2),(0,255,0),2)
        cv2.imwrite(self.graphfolder+"/houghp.png",im2)
        return im2

    
    def polydp(self,image):
        """Does a polydp (shape) approximation on the contours detected
        Keyword arguments:
        image -- image returned by the houghp()
        """
        #img = cv2.imread(self.pageImage)
        gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        cv2.imwrite(self.graphfolder+"/gray.png",gray)
        (cnts, _) = cv2.findContours(gray, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        h,w,channel = image.shape
        hi,wi = h,w
        count_graph = 1
        #f = open("contours.txt","wb")
        
        list1 = []
        list2 = []

        self.x = []
        self.y = []
        self.w = []
        self.h = []
        self.cont = []
        self.cflag = []

        for c in cnts:
            if cv2.contourArea(c) >self.threshArea:
            #if 1:
                approx = cv2.approxPolyDP(c,0.01*cv2.arcLength(c,True),True)
                if len(approx)<10 and len(approx)>2:
                    x_,y_,w_,h_  = cv2.boundingRect(c)
                    cv2.rectangle(img,(x_,y_),(x_+w_,y_+h_),(255,0,0))
                    #specify = [x,y,w,h]
                    #a =  int(((-2)*(w+h) + math.sqrt((4*(w+h)*(w+h)+4*4*self.percent*w*h/100)))/8)
                    #graph = img[y-a:y+h+a,x-2*a:x+w+a]
                    
                    if(self.aspectRatio(w_,h_) == True and h_ < 0.95*hi and w_ < 0.95*wi):
                        
                        self.cont.append([c])
                        self.x.append(x_)
                        self.y.append(y_)
                        self.h.append(h_)
                        self.w.append(w_)
                        self.cflag.append("1")
                   # else:
                  #      self.cflag.append("0")

                        #a =  int(((-2)*(w+h) + math.sqrt((4*(w+h)*(w+h)+4*4*self.percent*w*h/100)))/8)
                        #graph = img[y-a:y+h+a,x-2*a:x+w+a]
                        #scv2.drawContours(img, [c], -1, (0, 0, 255), 2)
                        
                        ##percentin = 0.2
                        ##xstart = max(0,x-percentin*w)
                        ##xend = min(wi,x+w+percentin*w)
                        ##ystart = max(0,y-percentin*h)
                        ##yend = min(hi,y+h+percentin*h)
                        ##graph = img[int(ystart):int(yend),int(xstart):int(xend)]
                        
                        #self.graphArray.append(graph)
                        
                        ##list.append(graph)
                        ##filename = self.graphfolder+"/"+str(count_graph)+".png"
                        
                        #self.graphName.append(filename)
                        
                        ##list2.append(filename)
                        
                        #print graph.shape
                        # cv2.imshow("window",graph)
                        # cv2.waitKey(0)
                        # cv2.destroyAllWindows()
                        
                        ##cv2.imwrite(filename,graph)
                        
                        #os.system("convert -resize 25% "+filename+" "+filename)
                        
                        ##if(graph.shape[1]>900):
                        ##    os.system("convert -resize 900 "+filename+" "+filename)

                        #specify = ""#str(tuple((2*a,a,w,h)))
                        #f.write(specify)
                        #f.write('\n')
                        #self.count_graph = self.count_graph + 1
                        
                        ##count_graph = count_graph + 1

        for i in range(len(self.x)):
            if(self.w[i]*self.h[i]<self.threshArea):
                self.cflag[i]=0
        '''
        for i in range(len(cflag)):
            xstart = max(0,self.x[i])
            xend = min(wi,self.x[i]+self.w[i])
            ystart = max(0,self.y[i])
            yend = min(hi,self.y[i]+self.h[i])
            graph = img[ystart:yend,xstart:xend]
            gray1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            (cnts1, _) = cv2.findContours(gray1, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            if len(cnts1) >=5 :
                cflag[i]=0
        '''

        for i in range(len(self.x)):
            if(self.cflag[i]==0):
                continue
            x_,y_,w_,h_ = self.x[i],self.y[i],self.w[i],self.h[i]
            for j in range(len(self.x)):
                if j==i:
                    continue
                if self.cflag[j] == 0:
                    continue
                if x_>=self.x[j] and y_>=self.y[j] and (x_+w_)<=(self.x[j]+self.w[j]) and (y_+h_)<=(self.y[j]+self.h[j]):
                    self.cflag[i]="0"
        
        for i in range(len(self.cflag)): 
            if(self.cflag[i]=="0"):
                continue

            cv2.drawContours(img, self.cont[i], -1, (0, 0, 255), 2)
            percentin = 0.2
            xstart = max(0,self.x[i]-percentin*self.w[i])
            #xend = min(wi,self.x[i]+self.w[i]+percentin*self.w[i])
            xend = min(wi,self.x[i]+self.w[i]+0.05*self.w[i])
            ystart = max(0,self.y[i]-percentin*self.h[i])
            yend = min(hi,self.y[i]+self.h[i]+percentin*self.h[i])
            
            graph = img[ystart:yend,xstart:xend]

            list1.append(graph)
            filename = self.graphfolder+"/"+str(count_graph)+".png"
            list2.append(filename)
            cv2.imwrite(filename,graph)
            if(graph.shape[1]>900):
                os.system("convert -resize 900 "+filename+" "+filename)

            count_graph = count_graph + 1
        cv2.imwrite(self.graphfolder+"/contour_next.png",img)
        return list1,list2

    def pdf_to_img(self): 
        """Convert pdf to png image
        """
        self.folder_name = "output_"+self.pdfFile
        if(not os.path.exists(self.folder_name)):
            os.makedirs(self.folder_name)
        img = PythonMagick.Image()
        img.density(self.density)
        my_file = PdfFileReader(file("{0}".format(self.pdfFile),"r"))
        self.numPages= my_file.getNumPages()
        for i in range(self.numPages):
            img.read("{0}[{1}]".format(self.pdfFile,i))
            #img.write("self.folder_name/{0}_image{1}.png".format(self.pdfFile,i))
            #img.write("{0}_image{1}.jpg".format(self.pdfFile,i))
            img.write(self.folder_name+"/page_"+str(i)+".png".format(self.pdfFile,i))
            
            #self.pdfImage = self.folder_name+"/page_"+str(i)+".png"
            self.pagelist.append(self.folder_name+"/page_"+str(i)+".png")
            #return img
 
    def aspectRatio(self,w,h):
        #print w,h
        if(h*1.0/w >= 4 or w*1.0/h >= 4):
            return False
        return True

    def graphextract(self):
        """Wrapper function for extracting the images"""
        self.pdf_to_img()
        #self.count_graph=1
        
        pagelist = self.pagelist
        self.numPages = len(pagelist)
        

        for i in range(len(pagelist)):
            self.graphfolder = "output_page_"+str(i)
            if(not os.path.exists(self.graphfolder)):
                os.makedirs(self.graphfolder)
            self.pageImage = pagelist[i]
            #self.pagecount = i
            list1,list2 = self.polydp(self.houghp())
            self.graphList.append(list1)
            self.graphName.append(list2)
            #self.polydp(self.houghp())

        return self.graphList,self.graphName

def main():
    """Main function to execute. Put name of image in the first parameter of constructor"""
    pdfName  = raw_input()
    name = ["output_ps/test.pdf0.png","output_ps/test.pdf1.png","output_ps/test.pdf2.png","output_ps/test.pdf3.png","output_ps/test.pdf4.png"]
    #page = []
    #for n in name:
    #    page.append(cv2.imread(n))
    #G = PlotExtractor(name)
    G = PlotExtractor(pdfName)
    
    ga,na = G.graphextract()
    print ga,na

if __name__=='__main__':
    main()








#pdf_to_img('OpenSoft_Problem_February_23_2016.4.pdf',"200")
