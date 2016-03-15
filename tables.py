import numpy as np
import cv2
import os
import sys
import copy
import math
import hough
import extract_plots
import hsv
import matplotlib.pyplot as plt

def findValue(img,jo,start_x,start_y):
	a=[]
	for i in range(len(img)):
		if img[i,jo]>=240:
			a.append(i)
	if len(a)==0:
		return -(sys.maxint)
	else:
		sum=0;
		for k in range(len(a)):
			sum+=len(img)-a[k]
		return (sum/len(a))


def lineInterpolation_y(img):
	count=0
	prevcount=0
	x=[]
	y=[]
	img1=copy.copy(img)
	for i in range(len(img)):
		count=0
		for j in range(len(img[0])):
			if img[i,j]==255:
				count+=1
				io=i
				jo=j
		if (count==0)and(prevcount>0):
			x.append(jo)
			y.append(io)
		elif (count>0)and(prevcount==0):
			x.append(jo)
			y.append(io)
				
		else:
			pass
		prevcount=count
	
	for p in range(len(x)-1):
		flag=0
		for q in range(p+1,len(x)-1):
			sq=math.pow(x[p]-x[q],2)+math.pow(y[p]-y[q],2)
			dist=math.sqrt(sq)
			if(dist<=20):
				cv2.line(img1,(x[p],y[p]),(x[q],y[q]),255,1,0)
				p=q
	return img1


def lineInterpolation_x(img):
	count=0
	prevcount=0
	x=[]
	y=[]
	img1=copy.copy(img)
	for j in range(len(img[0])):
		count=0
		for i in range(len(img)):
			if img[i,j]==255:
				count+=1
				io=i
				jo=j
		if (count==0)and(prevcount>0):
			x.append(jo)
			y.append(io)
		elif (count>0)and(prevcount==0):
			x.append(jo)
			y.append(io)
				
		else:
			pass
		prevcount=count
	
	for p in range(len(x)-1):
		flag=0
		for q in range(p+1,len(x)-1):
			sq=math.pow(x[p]-x[q],2)+math.pow(y[p]-y[q],2)
			dist=math.sqrt(sq)
			if(dist<=20):
				cv2.line(img1,(x[p],y[p]),(x[q],y[q]),255,1,0)
				p=q
	return img1
		



def approxTable(img,ppdiv_x,ppdiv_y,rectsize_x,rectsize_y,start_x,start_y,scale_x,scale_y):
	fx=[]
	x_=[]
	xdiv=float(rectsize_x)/ppdiv_x
	ydiv=float(rectsize_y)/ppdiv_y
	unit=float(scale_x)/10
	readings=int(xdiv*10)
	print "No of readings : "+str(readings)
	pixeldiff=float(rectsize_x)/readings
	r=0
	while r<readings:
		expected=pixeldiff*r
		prevpixel=int(math.floor(expected))
		nextpixel=int(math.ceil(expected))
		prevval=findValue(img,prevpixel,start_x,start_y)
		nextval=findValue(img,nextpixel,start_x,start_y)
		x=(r*unit)+start_x
		if (prevval==(-(sys.maxint)))and(nextval!=(-(sys.maxint))):
			val=nextval
			trueval=(float(val)/rectsize_y)*(ydiv*scale_y)+start_y
			fx.append(str(trueval))
			x_.append(str(x))
		elif (prevval!=(-(sys.maxint)))and(nextval==(-(sys.maxint))):
			val=prevval
			trueval=(float(val)/rectsize_y)*(ydiv*scale_y)+start_y
			fx.append(str(trueval))
			x_.append(x)
		elif(prevval==(-(sys.maxint)))and(nextval==(-(sys.maxint))):
			fx.append("--")
			x_.append(str(x))
		else:
			val=float(prevval+nextval)/2
			trueval=(float(val)/rectsize_y)*(ydiv*scale_y)+start_y
			fx.append(str(trueval))
			x_.append(str(x))
		r+=1
	#print x_
	#print fx	
	return (x_,fx)


def findParameters(x1,p_x1,y1,p_y1,x2,p_x2,y2,p_y2,scale_x,scale_y,bottom_left,top_right):
	print "X1 = "+str(x1)
	print "P_X1 = "+str(p_x1)
	print "X2 = "+str(x2)
	print "P_X2 = "+str(p_x2)
	rectsize_x=top_right[0]-bottom_left[0]
	rectsize_y=top_right[1]-bottom_left[0]
	x_div=math.fabs(x2-x1)/scale_x
	y_div=math.fabs(y2-y1)/scale_y
	ppdiv_x=math.fabs(p_x2-p_x1)/x_div
	ppdiv_y=math.fabs(p_y2-p_y1)/y_div
	diff_x1=math.fabs(p_x1-bottom_left[0])
	diff_x2=math.fabs(p_x2-bottom_left[0])
	diff_y1=math.fabs(p_y1-bottom_left[1])
	diff_y2=math.fabs(p_y2-bottom_left[1])
	no_div_x1=float(diff_x1)/ppdiv_x
	no_div_x2=float(diff_x2)/ppdiv_x
	no_div_y1=float(diff_y1)/ppdiv_y
	no_div_y2=float(diff_y2)/ppdiv_y
	startx_x1=x1-(no_div_x1*scale_x)
	startx_x2=x2-(no_div_x2*scale_x)
	starty_y1=y1-(no_div_y1*scale_y)
	starty_y2=y2-(no_div_y2*scale_y)
	start_x=float(startx_x1+startx_x2)/2
	start_y=float(starty_y1+starty_y2)/2
	print "ppdiv_x = "+str(ppdiv_x)+" ppdiv_y = "+str(ppdiv_y)
	print "Origin X = "+str(start_x)+" Y = "+str(start_y)
	return (ppdiv_x,ppdiv_y,rectsize_x,rectsize_y,start_x,start_y,scale_x,scale_y)

def plot(x_axis,y_axis) :
	plt.plot(x_axis,y_axis,'ro')
	plt.axis([min(x_axis) , max(x_axis) , 40 , 100])
	#plt.show()

def findTables(masks,ppdiv_x,ppdiv_y,rectsize_x,rectsize_y,start_x,start_y,scale_x,scale_y,legend):
	table=[]
	x_=[]
	fx=[]
	for i in range(len(masks)):
		masks[i]=lineInterpolation_x(masks[i])
		masks[i]=lineInterpolation_y(masks[i])
	for i in range(len(masks)):
		(x_,fx)=approxTable(masks[i],ppdiv_x,ppdiv_y,rectsize_x,rectsize_y,start_x,start_y,scale_x,scale_y)

		if(i==0):
			table.append(x_)
		table.append(fx)
	print 'hi'
	print len(table[1])
	# for j in range(len(table[0])):
	# 	for i in range(len(table)):
	# 		print table[i][j],

	table2 = [[] for x in table]
	miny=10000
	maxy=-100
	for i in range(len(table)):
		for j in range(len(table[i])):
			if(table[i][j]=="--"):
				table2[i].append(0)
			else:
				table2[i].append(float(table[i][j]))
		if i!=0:
			miny=min(miny,min(table2[i]))
			maxy=max(maxy,max(table2[i]))

	plt.axis([min(table2[0]) , max(table2[0]) , miny ,maxy ])
	colors=[]
	for i in range(len(legend)):
		#print legend[i][0]
		b=legend[i][1][0]
		g=legend[i][1][1]
		r=legend[i][1][2]
		colors.append((r,g,b))

	# plt.set_color_cycle(colors)
	# 	print '\n'
	for i in range(1,len(table)):
		plt.plot(table2[0],table2[i])
	plt.savefig('plot_from_data.png')
		#plot(table[0] , table[2])
	return table

def run(input_file,bottom_left,top_right,scale_x,scale_y,x1,x2,y1,y2,p_x1,p_x2,p_y1,p_y2,image_without_legend,legend):
	(ppdiv_x,ppdiv_y,rectsize_x,rectsize_y,start_x,start_y,scale_x,scale_y) = findParameters(int(x1),int(p_x1),int(y1),int(p_y1),int(x2),int(p_x2),int(y2),int(p_y2),int(scale_x),int(scale_y),bottom_left,top_right)
	print 'above'
#	(x,y,z,masks) = extract_plots.extract_plots(input_file,8)
#	print z
	masks=[]
	for i in range(len(legend)):
		print legend[i][0]
		b=legend[i][1][0]
		g=legend[i][1][1]
		r=legend[i][1][2]
		plotImg = hsv.mark(image_without_legend,b,g,r)
		print r,g,b
		masks.append(plotImg)
		cv2.imwrite("mask %d.png"%(i),plotImg)
	print 'below'
	return findTables(masks,ppdiv_x,ppdiv_y,rectsize_x,rectsize_y,start_x,start_y,scale_x,scale_y,legend)
	


def main():
	xarr=[]
	yarr=[]
	(input_file,bottom_left,top_right,scale_x,scale_y,x1,x2,y1,y2,p_x1,p_x2,p_y1,p_y2) = hough.final_scale('a.jpg')
	img = cv2.imread(input_file)
	print 'hi'
	print bottom_left
	print top_right
	print scale_x
	print scale_y
	print x1
	print x2
	print y1
	print y2
	print p_x1
	print p_x2
	print p_y1
	print p_y2
	(ppdiv_x,ppdiv_y,rectsize_x,rectsize_y,start_x,start_y,scale_x,scale_y) = findParameters(int(x1),int(p_x1),int(y1),int(p_y1),int(x2),int(p_x2),int(y2),int(p_y2),int(scale_x),int(scale_y),bottom_left,top_right)
	print 'above'
	(x,y,z,masks) = extract_plots.extract_plots(input_file,8)
	print z
	print 'below'
	findTables(masks,ppdiv_x,ppdiv_y,rectsize_x,rectsize_y,start_x,start_y,scale_x,scale_y)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
	return

if __name__=='__main__':
	main()







