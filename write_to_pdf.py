#mine
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch,cm
from reportlab.lib.utils import ImageReader
import numpy as np

#Name of Output PDF
x='new.pdf'

#Size of Canvas
c=canvas.Canvas(x,pagesize=A4)
width, height=A4


#New Page...
c.translate(0,height)

c.setFont("Times-Roman", 30)
c.drawString(width/3,-.5*inch,"Input Page")

#Image Print
im=ImageReader('b.jpg')
w=im.getSize()[0]
h=im.getSize()[1]
c.drawImage(im,(width-.75*w)/2,-(height+.75*h)/2,.75*w,.75*h)

#Save Page
c.showPage()

#New Page
c.translate(0,height)
c.setFont("Times-Roman", 30)
c.drawString(width/3,-.3*inch,"Output Page")
c.setFont("Times-Roman",14)
#Array to be printed
ar=np.zeros((50,8))
ar[2][4]=2985.5258
W = width/(len(ar[0])+2)
H = (height-inch)/(len(ar)+2)

#Title of the Graph
c.drawString(width/3,-.9*inch,"Title of the Plot")


c.setFont("Times-Roman", 16-.1*len(ar))

#Title of X and Y axes
title=['X Value']
for i in xrange(len(ar[0])-1):
	title.append('Y ' + str(i+1) + " Value")
for i in xrange(len(ar[0])):
	c.drawString((i+1.1)*W,-inch-.7*H,title[i])

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
		c.drawString((j+1.1)*W,-H*(1.7+i)-inch,str(ar[i][j]))

c.showPage()


#Save PDF
c.save()
