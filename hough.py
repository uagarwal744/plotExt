import cv2
import numpy as np
import math
import extract_plots
import testing
import x_scale
import sys
def final_scale(img,clusters=2) :

	#img = cv2.imread(input_file)
	xarr=[]
	yarr=[]
	output_file = 'houghlines3.png'
	input_file ='input.png'
	cv2.imwrite(input_file,img)
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,80,120)
	rows, cols ,channels= img.shape
	lines = cv2.HoughLinesP(edges,1,np.pi/2,2,None,30,10)
	arrayh = []
	arrayv = []
	image1 = img
	image2 = img
	tempimg = img
	xth = 0.25 * cols
	yth = 0.25 * rows
	xmax = -1
	ymax = -1
	xpt1 = ((0,0),(0,0))
	xpt2 = xpt1

	ypt1 = ((1000,1000),(1000,1000))
	ypt2 = ypt1
	xmax1 =-1 
	ymax1 = -1
	pixel,example,a,b = extract_plots.extract_plots(input_file,clusters)
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
			#print 'hi22'
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
	'''
	cv2.line(img,xpt1[0],xpt1[1],(0,0,255),2)	
	cv2.line(img,ypt1[0],ypt1[1],(0,0,255),2)
	
	if not xmax1 == -1 :
		cv2.line(img,xpt2[0],xpt2[1],(0,0,255),2)	
	if not ymax1 == 1 :	
		cv2.line(img,ypt2[0],ypt2[1],(0,0,255),2)
	'''	
	#cv2.line(img,(549,397),(549,24),(0,0,255),2)
	'''
	i= 24
	print 'hi'
	print example[0]
	while i < 397 :
		print pixel[i,548,0]
		if pixel[i,548] == example[0] :
			
			print i
		i=i+1
	print ypt1
	print ypt2
	print xpt1
	print xpt2
	'''
	'''
	ans = xpt2[0][0]
	if xpt1[0][0] < xpt2[0][0] :
		ans = xpt1[0][0]	

	ans1 = ypt2[0][1]
	if ypt1[0][1] < ans1 :
		ans1 = ypt1[0][1]
	'''
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
		
			
	#print 'y coordinate is ' + str(ans)
	#print 'x coordinate is ' + str(ans1)
	#print ypt1[0][0]
	#print ypt2[0][0]
	#print ans1
	
	
	#cv2.line(image2,(ypt1[0][0],ypt1[0][1]),(ypt1[1][0],ypt1[1][1]),(0,0,255),2)
	bot_left = (ans1,ans)
	top_right = (ans3,ans2)
	#cv2.line(image1,(bot_left),(top_right),(0,0,255),2)
	y_pos = []
	x_pos = []
	cv2.rectangle(tempimg,(bot_left),(top_right),(0,255,0),3)
	#cv2.imwrite('temp6.jpg',tempimg)
	testing.extract_y_scale(input_file,int(ans1),'test3.png',yarr,int(ans),y_pos)

	x_scale.extract_x_scale(input_file,int(ans),'test2.png',xarr,x_pos)
	
	cv2.imwrite('line4.jpg',image1)
	#cv2.imwrite('line5.jpg',image2)
	
	scale_y = abs(float(yarr[2])-float(yarr[1]))
	scale_x = abs(float(xarr[2])-float(xarr[1]))
	'''
	print 'x scale'
	print scale_x
	print bot_left
	print x_pos[len(xarr)-1]
	print 'y scale'
	print scale_y
	print top_right
	print y_pos[0]
	'''
	cv2.imwrite('houghlines3.jpg',img)
	[x,y,z ] = image2.shape
	print (x,y)
	print (ans1,ans3)
	print (ans2,ans)
	image2 = image2[ans2+2:ans-2,ans1+2:ans3-2]
	cv2.imwrite('line5.jpg',image2)
	x_len = len(xarr)
	print xarr[x_len-1]
	print xarr[x_len-2]
	print bot_left,top_right
	print 'x scales are '
	diff = float(yarr[3]) - float(yarr[2])
	for i in xarr :
			print i,

	print '\nyscales are'
	for i in yarr :
			print i,
	return 'line5.jpg',bot_left,top_right,scale_x,scale_y,xarr[x_len-1],xarr[x_len-2],yarr[0],yarr[1],x_pos[x_len-1],x_pos[x_len-2],y_pos[0],y_pos[1]

	#cv2.imwrite(output_file,img)

if __name__ == '__main__':
	print 'hi'
	x = sys.argv[1]
	xarr = []
	yarr = []
	print x
	img = cv2.imread(x)
	final_scale(img)
	
	
	