import cv2
def h_scale(img,haxis_y,haxis_right,haxis_left):
	"""
	returns the horizontal unit scale
	takes the grayscaled image, the y-position of the horizontal axis
	and the left and right extremes of the horizontal axis as parameters


	"""
	cv2.imshow("as",img)
	
	crop_img=img[haxis_y-20:haxis_y+20,haxis_left-20:haxis_right+20]		#crops the image to some area around the horizontal axis
	#cv2.imshow("Crop",crop_img)
	th2 = cv2.adaptiveThreshold(crop_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)  #using adaptive thresholding
	l=[]
	f1=0
	k=[]
	caxis_y=20
	caxis_left=20
	caxis_right=haxis_right-haxis_left+20
	y_trav=caxis_y-2
	#cv2.rectangle(crop_img,(22,20),(690,30),(0,255,0),2)
	#cv2.imshow("Crop",crop_img)
	for x in range(caxis_left-2,caxis_right+2):
		print (str(th2[y_trav,x]))
		if(th2[y_trav,x]==0 and f1==0):
			f1=1
		 	lx=x
		if(th2[y_trav,x]==255 and f1==1):
			l.append((x+lx)/2)
			f1=0
	cv2.imshow("th2",th2)
	print l
	for i in range(len(l)-1,0,-1):
		k.append(l[i]-l[i-1])
	print "Successive distances are",
	k.sort()
	print k
	if(len(k)%2==0):
		final=(k[len(k)/2-1]+k[len(k)/2])/2
	else:
		final=k[len(k)/2]
	
	return final


if __name__ == '__main__':
	img=cv2.imread('axistest.png',cv2.IMREAD_GRAYSCALE)
	haxis_y=360
	haxis_left=60
	haxis_right=720
	h_unit=h_scale(img,haxis_y,haxis_right,haxis_left)															#scale function call
	print "Unit scale is  "+str(h_unit)
	cv2.waitKey(0)
