import rotation
import cv2
import numpy as np
import math
import os
import sys
import y_scale_length
#import ocr_parse
from bs4 import BeautifulSoup

def extract_y_scale(input_file,coordinate,output_file,output_array,xcoordinate,y_pos) :
	img = cv2.imread(input_file,cv2.IMREAD_GRAYSCALE)
	rows,cols = img.shape
	img = img[0:rows,0:coordinate]
	temp_file = 'temp.png'
	temp1_file = 'temp1.png'
	cv2.imwrite(temp_file,img)
	cv2.imwrite(temp1_file,img)
	rotation.rotate(temp_file,output_file,1)
	img = cv2.imread(output_file,cv2.IMREAD_GRAYSCALE)
	cv2.imwrite(temp1_file,img)
	rows,cols = img.shape
	os.system("tesseract "+output_file+" out1 hocr")
	#os.rename('out.hocr','out.xml')
	
	f = open('out1.hocr','r')
	data=f.read()
	soup = BeautifulSoup(data)
	'''
	i = soup.find('span',{'class':'ocr_line'})
	h= i.get('title').split(' ')
	k= h[1:5]
	k[-1]=k[-1][:-1]
	print k
	'''
	mini = 1000000000
	
	for i in soup.find_all('span',{'class':'ocr_line'}) :
		h= i.get('title').split(' ')
		k= h[1:5]
		k[-1]=k[-1][:-1]
		print k
		if int(k[3])<mini :
			mini = int(k[3])
	#cv2.rectangle(img,(int(k[0]),int(k[1])),(int(k[2]),int(k[3])),(0,255,0),3)
	#print min
	#cv2.rectangle(img,(294,60),(394,75),(0,255,0),3)
	#cv2.imwrite(temp1_file,img)	
	#cv2.rectangle(img,(int(k[0]),int(k[1])),(int(k[2]),int(k[3])),(0,255,0),3)
	#cv2.imwrite(output_file,img)
	
	img = img[mini:rows,0:cols]
	cv2.imwrite(temp_file,img)
	rotation.rotate(temp_file,output_file,0)
	os.system("tesseract "+output_file+" out hocr")
	f = open('out.hocr','r')
	data=f.read()
	a = []
	soup = BeautifulSoup(data)
	for i in soup.find_all('span',{'class':'ocrx_word'}) :
		
		print 'ndns'
		print i.text
		h= i.get('title').split(' ')
		k= h[1:5]
		k[-1]=k[-1][:-1]
		x = ''
		for char in i.text :
			if char == 'O' or char =='o':
				x+='0'
			else :
				x+=char	
		print x
				
		y_pos.append((int(k[1])+int(k[3]))/2)
		output_array.append(float(x))
		a.append(float(x))
		
	h= i.get('title').split(' ')
	k= h[1:5]
	k[-1]=k[-1][:-1]
	t = (int(k[1])+int(k[3]))/2
	x = a[0] - a[1]

	leng = len(output_array)	
	y = a[leng-1]

	z = a[leng-2] - 2*a[leng-1]
	print z
	yl = y_scale_length.y_scale_length(output_file)
	if abs(xcoordinate - t>= 0.1*yl) :
		#print output_array[leng-1] - x
		output_array.append(z)
	



if __name__ == '__main__':
	array = []
	extract_y_scale('pic1.png',133,'test3.png',array)
	for i in array :
		print i,


