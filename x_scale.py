import rotation
import cv2
import numpy as np
import math
import os
import sys
#import ocr_parse
from bs4 import BeautifulSoup

def extract_x_scale(input_file,coordinate,output_file,output_array,xpos) :
	img = cv2.imread(input_file,cv2.IMREAD_GRAYSCALE)
	rows,cols = img.shape
	img = img[coordinate:rows,0:cols]
	#temp_file = 'temp.png'
	#temp1_file = 'temp1.png'
	cv2.imwrite(output_file,img)
	'''
	cv2.imwrite(temp1_file,img)
	rotation.rotate(temp_file,output_file,1)
	img = cv2.imread(output_file,cv2.IMREAD_GRAYSCALE)
	cv2.imwrite(temp1_file,img)
	rows,cols = img.shape
	'''
	#os.system("tesseract "+output_file+" out1 hocr")
	#os.rename('out.hocr','out.xml')
	'''
	f = open('out1.hocr','r')
	data=f.read()
	soup = BeautifulSoup(data)
	
	i = soup.find('span',{'class':'ocr_line'})
	h= i.get('title').split(' ')
	k= h[1:5]
	k[-1]=k[-1][:-1]
	print k
	
	min = 1000000000
	
	for i in soup.find_all('span',{'class':'ocr_line'}) :
		h= i.get('title').split(' ')
		k= h[1:5]
		k[-1]=k[-1][:-1]
		print k
		if int(k[3])<min :
			min = int(k[3])
	'''
	os.system("tesseract "+output_file+" out3 hocr")
	f = open('out3.hocr','r')
	data=f.read()
	soup = BeautifulSoup(data)
	for i in soup.find_all('span',{'class':'ocrx_word'}) :
		flag = 0
		#print 'dnsk'
		
		for char in i.text :
			#print char
			#print type(char)
			#print char
			h= i.get('title').split(' ')
			k= h[1:5]
			k[-1]=k[-1][:-1]
			if char.isalpha() :
				flag = 1
				break	
		if flag == 0 :
			output_array.append(i.text)
			xpos.append((int(k[0]),int(k[2])))

	


if __name__ == '__main__':
	array = []
	extract_x_scale('pic1.png',523,'test2.png',array)
	print len(array)
	for i in array :
		print i,


