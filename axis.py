import cv2
import numpy as np
import math
import extract_plots
import sys
def axis(img) :

	#img = cv2.imread(input_file)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,80,120)
	rows, cols ,channels= img.shape
	print 'eomedme'
	print rows,cols
	lines = cv2.HoughLinesP(edges,1,np.pi/2,2,None,30,10)
	arrayh = []
	arrayv = []
	image1 = img
	image2 = img
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
	pixel,example,a,b = extract_plots.extract_plots(input_file,2)
	for line in lines[0]:
		#print line
		pt1 = (line[0],line[1])
		pt2 = (line[2],line[3])
		#print pt1
		#if pt1 == (133,523) :
			#print 'hi111111111111'
		k = line[0]-2
		h=0
		while h<5:
			if pixel[line[1]-5][k] == example[0] :
				break
			h=h+1
			k=k+1
				
		dist = (line[0]-line[2])*(line[0]-line[2])+(line[1]-line[3])*(line[1]-line[3])
		if line[0] ==line[2] and (pixel[line[1]-5][k] == example[0] or pixel[line[3]+5][line[2]] == example[0] or pixel[(line[1]+line[3])/2][(line[0]+line[2])/2] == example[0]):
			
			if dist > ymax :
			#	print 'hi333333333333'
				ymax = dist
				ypt1 = (pt1,pt2)
		if line[1] == line[3] and (pixel[line[1]][line[0]] == example[0] or pixel[line[3]][line[2]] == example[0] or pixel[(line[1]+line[3])/2][(line[0]+line[2])/2] == example[0]):
			if dist > xmax :
				xmax = dist
				xpt1 = (pt1,pt2)
			
			
	#cv2.line(img,(135,71),(849,71),(0,0,255),2)
	for line in lines[0]:
		#print line
		pt1 = (line[0],line[1])
		pt2 = (line[2],line[3])
		dist = (line[0]-line[2])*(line[0]-line[2])+(line[1]-line[3])*(line[1]-line[3])
		k = line[0]-2
		h=0
		while h<5:
			if pixel[line[1]-5][k] == example[0] :
				break
			h=h+1
			k=k+1

		if line[0] == line[2] and (pixel[line[1]-5][k] == example[0] or pixel[line[3]+5][line[2]] == example[0] or pixel[(line[1]+line[3])/2][(line[0]+line[2])/2] == example[0]):
			
			if dist > ymax1  and not (pt1,pt2) == ypt1 and abs(ypt1[0][0]-line[0]) > xth and dist > 0.7*yth :
				ymax1 = dist
				ypt2 = (pt1,pt2)

			#cv2.line(img,pt1,pt2,(0,0,255),2)
		if line[1] == line[3] and (pixel[line[1]-5][line[0]] == example[0] or pixel[line[3]+5][line[2]] == example[0] or pixel[(line[1]+line[3])/2][(line[0]+line[2])/2] == example[0]):
			#if dist > xmax1 and not (pt1,pt2) == xpt1 and abs(pt1[1]-xpt1[0][1]) > yth:
			if dist > xmax1  and not (pt1,pt2) == xpt1 and abs(xpt1[0][1]-line[1]) > yth and dist > 0.7*xth :
				xmax1 = dist
				xpt2 = (pt1,pt2)

	cv2.line(img,xpt1[0],xpt1[1],(0,0,255),2)	
	cv2.line(img,ypt1[0],ypt1[1],(0,0,255),2)
	if not xmax1 == -1 :
		print 'inside'
		cv2.line(img,xpt2[0],xpt2[1],(0,0,255),2)	
	if not ymax1 == 1 :
		print 'inside input'	
		cv2.line(img,ypt2[0],ypt2[1],(0,0,255),2)
	#cv2.line(img,(300,rows),(300,0),(0,0,255),2)	
	print xpt1,xpt2,ypt1,ypt2	
	#cv2.imwrite('temp6.png',img)
	#cv2.waitKey(0)
	ans2 = xpt1[0][1]
	ans = xpt2[0][1]
	if xpt1[0][1] > xpt2[0][1] :
		ans = xpt1[0][1]	
		ans2 = xpt2[0][1]

	ans1 = ypt2[0][0]
	ans3 = ypt1[0][0]
	if ypt1[0][0] < ans1 :
		ans1 = ypt1[0][0]
		ans3 = ypt2[0][0]
	
	return ans1,ans3,ans2,ans	
	

if __name__ == '__main__':
	print 'hi'
	x = sys.argv[1]
	print x
	img = cv2.imread(x)
	a,b,c,d = axis(img)
	print a
	print b
	print c
	print d