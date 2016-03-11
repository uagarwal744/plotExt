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
c.drawString(width/3,-inch,"Input Page")
c.setFont("Times-Roman", 10)

#Image Print
im=ImageReader('b.jpg')
w=im.getSize()[0]
h=im.getSize()[1]
c.drawImage(im,(width-.75*w)/2,-(height+.75*h)/2,.75*w,.75*h)

#Save Page
c.showPage()

#New Page

#Array to be printed
ar=np.zeros((50,3))

c.translate(0,height)

#Title of the Graph
c.drawString(2*inch,-.4*cm,"Title of the Plot")

#Title of X and Y axes
title=['X Value']
for i in xrange(len(ar[0])-1):
	title.append('Y ' + str(i+1) + " Value")
for i in xrange(len(ar[0])):
	c.drawString((i+1.1)*inch,-cm,title[i])

#Size of the Grid
xlist=[]
for i in xrange(len(ar[0])+1):
	xlist.append((i+1)*inch)
ylist=[]
for i in xrange(len(ar)+2):
	ylist.append(-(i+1)*0.6*cm)
#Creating the Grid
c.grid(xlist, ylist)

#Printing the Output Array
for i in xrange(len(ar)):
	for j in xrange(len(ar[0])):
		c.drawString((j+1.1)*inch,-cm*(1.6+0.6*i),str(ar[i][j]))

c.showPage()


#Save PDF
c.save()
