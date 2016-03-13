import cv2
import numpy as np
import math
#import extract_plots
import os
import sys
from bs4 import BeautifulSoup
def axis(img) :

	#img = cv2.imread(input_file)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,80,120)
	rows, cols ,channels= img.shape
	lines = cv2.HoughLinesP(edges,1,np.pi/2,2,None,30,20)
	arrayh = []
	arrayv = []
	image1 = img
	image2 = img
	image3 = img
	xth = 0.25 * cols
	yth = 0.25 * rows
	xmax = -1
	ymax = -1
	xpt1 = ((0,0),(0,0))
	xpt2 = xpt1

	ypt1 = ((100000,100000),(100000,100000))
	ypt2 = ypt1
	xmax1 =-1 
	ymax1 = -1
	input_file = 'input.png'
	cv2.imwrite(input_file,img)
	#pixel,example,a,b = extract_plots.extract_plots(input_file,2)
	for line in lines[0]:
		pt1 = (line[0],line[1])
		pt2 = (line[2],line[3])
			
		dist = (line[0]-line[2])*(line[0]-line[2])+(line[1]-line[3])*(line[1]-line[3])
		if line[0] ==line[2] and int(line[0])>4 and int(line[0])<cols-4:#and (pixel[line[1]-5][k] == example[0] or pixel[line[3]+5][line[2]] == example[0] or pixel[(line[1]+line[3])/2][(line[0]+line[2])/2] == example[0]):
			
			temp = [dist,pt1,pt2]
			arrayv.append(temp)

		if line[1] == line[3] and int(line[1])>4 and int(line[1])<rows-4:#and (pixel[line[1]][line[0]] == example[0] or pixel[line[3]][line[2]] == example[0] or pixel[(line[1]+line[3])/2][(line[0]+line[2])/2] == example[0]):
			'''
			if dist > xmax and int(line[1])>4 and int(line[1])<rows-4:
				xmax = dist
				xpt1 = (pt1,pt2)
			'''
			temp = [dist,pt1,pt2]
			arrayh.append(temp)	
			
	
	#cv2.line(img,(135,71),(849,71),(0,0,255),2)
	
	arrayv.sort(key = lambda tup : tup[0] , reverse = True)
	arrayh.sort(key = lambda tup : tup[0] , reverse = True)
	ypt1 = (arrayv[0][1],arrayv[0][2])
	ypt2 = ypt1
	xpt1 = (arrayh[0][1],arrayh[0][2])
	xpt2 = xpt1
	ymax = arrayv[0][0]
	xmax = arrayh[0][0]
	yleft = arrayv[0][1][0]
	yright = yleft
	xtop = arrayh[0][1][1]
	xbottom = xtop
	i = 1
	while i<len(arrayv) and arrayv[i][0] > 0.8*float(ymax):
		if arrayv[i][1][0] < yleft :
			yleft = arrayv[i][1][0]
			
			ypt1 = (arrayv[i][1],arrayv[i][2])

		if arrayv[i][1][0] > yright :
			yright = arrayv[i][1][0]
			
			ypt2 = (arrayv[i][1],arrayv[i][2])
		i = i+1
	
	i = 1
	while i<len(arrayh) and arrayh[i][0] > 0.8*float(xmax):
		if arrayh[i][1][1] < xtop :
			xtop = arrayh[i][1][1]
			
			xpt1 = (arrayh[i][1],arrayh[i][2])

		if arrayh[i][1][1] > xbottom :
			xbottom = arrayv[i][1][1]
		
			xpt2 = (arrayh[i][1],arrayh[i][2])
		i = i+1
			

	# cv2.line(img,ypt2[0],ypt2[1],(0,0,255),2)	
	# cv2.line(img,ypt1[0],ypt1[1],(0,0,255),2)
	# cv2.line(img,xpt2[0],xpt2[1],(0,0,255),2)	
	# cv2.line(img,xpt1[0],xpt1[1],(0,0,255),2)
	cv2.imwrite('temp6.png',img)
	print 'the points are'
	print xpt1
	print xpt2
	print ypt1
	print ypt2
	ans1 = ypt1[0][0]
	ans3 = ypt2[0][0]
	ans2 = xpt1[0][1]
	ans = xpt2[0][1]
	
	
	os.system("tesseract "+input_file+" out5 hocr")
	f = open('out5.hocr','r')
	data=f.read()
	soup = BeautifulSoup(data)
	flag = 0
	box_l = len(soup.find_all('span',{'class':'ocr_line'}))

	for i in soup.find_all('span',{'class':'ocr_line'}) :
		h= i.get('title').split(' ')
		k= h[1:5]
		k[-1]=k[-1][:-1]
		if( (int(k[0])>int(ans1) and int(k[2])<int(ans3) and int(k[1])>int(ans2) and int(k[3])<int(ans))) :
			#cv2.rectangle(img,(int(k[0]),int(k[1])),(int(k[2]),int(k[3])),(0,255,0),3)
			flag = flag+1
			
			#cv2.rectangle(img,(int(k[0]),int(k[1])),(int(k[2]),int(k[3])),(0,255,0),3)
					
	#cv2.imwrite('temp6.png',img)
	
	if flag == box_l-1 :
		image3 = image3[ans2+2:ans-2,ans1+2:ans3-3]
		a,b,c,d = axis(image3)
		cv2.rectangle(img,(ans1+a+2,ans2+d+2),(ans1+b+2,ans2+c+2),(0,255,0),3)
		print ans1
		print ans3
		print ans2
		print ans
		print a
		print b
		print c
		print d
		cv2.imwrite('temp7.png',img)
		return ans1+a+2,ans1+b+2,ans2+c+2,ans2+d+2
	else :
		print 'no'
	

	return ans1,ans3,ans2,ans	
	
	

if __name__ == '__main__':
	print 'hi'	
	x = sys.argv[1]
	print x
	
	#a = ['1.png','2.png','3.png','4.png','5.png','6.png','7.png']
	
	img = cv2.imread(x)
	#axis(img)
	
	a = axis(img)
	print a
	#print b
	#print c
	#print d

	