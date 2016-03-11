from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.units import inch,cm
import numpy as np

x='new.pdf'
c=canvas.Canvas(x,pagesize=A4)
width, height=A4
ar=np.zeros((40,4))
c.translate(0,height)
title=['X Value']
for i in xrange(len(ar[0])-1):
	title.append('Y ' + str(i+1) + " Value")
for i in xrange(len(ar[0])):
	c.drawString((i+1.1)*inch,-1.5*cm,title[i])
xlist=[]
for i in xrange(len(ar[0])+1):
	xlist.append((i+1)*inch)
ylist=[]
for i in xrange(len(ar)):
	ylist.append(-(i+1)*cm)
c.grid(xlist, ylist)


c.showPage()
c.save()