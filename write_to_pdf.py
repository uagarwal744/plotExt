from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch,cm
from reportlab.lib.utils import ImageReader
import numpy as np

width, height=A4

def createpdf(x):
	#Size of Canvas
	c=canvas.Canvas(x,pagesize=A4)
	return c

def pdfoutput(c,img,ar):
	#Name of Output PDF
	global z
	global x
	global width
	global height
	
	#New Page...
	c.translate(0,height)

	c.setFont("Times-Roman", 30)
	c.drawCentredString(width/2,-.5*inch,"Input Page "+ str(z+1))

	#Image Print
	im=ImageReader(img)
	w=im.getSize()[0]
	h=im.getSize()[1]
	r=(width-2*cm)/w
	w= width-2*cm
	c.drawImage(im,(width-w)/2,-(height+h*r)/2,w,r*h)


	#Save Page
	c.showPage()

	#New Page
	c.translate(0,height)
	c.setFont("Times-Roman", 30)
	c.drawCentredString(width/2,-.3*inch,"Output Page "+ str(z+1))
	c.setFont("Times-Roman",14)
	#Array to be printed
	W = width/(len(ar[0])+2)
	H = (height-inch)/(len(ar)+2)
	if H>inch:
		H=inch

	#Title of the Graph
	#c.drawString(width/3,-.9*inch,"Title of the Plot")
	c.drawCentredString(width/2, -.9*inch, "Title of the Plot")

	c.setFont("Times-Roman", 16-.1*len(ar))

	#Title of X and Y axes
	title=['X Value']
	for i in xrange(len(ar[0])-1):
		title.append('Y ' + str(i+1) + " Value")
	for i in xrange(len(ar[0])):
		c.drawCentredString((i+1.5)*W,-inch-.7*H,title[i])

	#Size of the Grid
	xlist=[]
	for i in xrange(len(ar[0])+1):
		xlist.append(W*(i+1))
	ylist=[]
	for i in xrange(len(ar)+2):
		ylist.append(-i*H-inch)
	#Creating the Grid
	c.grid(xlist, ylist)

	#Printing the Output Array
	for i in xrange(len(ar)):
		for j in xrange(len(ar[0])):
			c.drawCentredString((j+1.5)*W,-H*(1.7+i)-inch,str(ar[i][j]))

	c.showPage()


	#Save PDF
	c.save()
	z=z+1

img = 'b.jpg'
ar=np.zeros((100,8))
ar[2][4]=2985.5258
z=0
