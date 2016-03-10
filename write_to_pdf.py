import PyPDF2, numpy as np
from reportlab.pdfgen import canvas

#Name of output pdf
x='ne2.pdf'

c=canvas.Canvas(x)

#Final output array
ar=np.zeros((40,2))

#End Horizontal Lines of the table
c.drawString(203,820,'_'*28)
c.drawString(203,793-len(ar)*16,'_'*28)

#All Vertical Lines of the table
for i in xrange(0,18+len(ar)*16,8):
	c.drawString(200,810-i,'|')
	c.drawString(295,810-i,'|')
	c.drawString(390,810-i,'|')

#Name of the X and Y axis (to be changed accordingly)
c.drawString(230, 800, "X Value")
c.drawString(325, 800, "Y Value")

#Writing the values of array in the table
for i in xrange(len(ar)):
	c.drawString(245,780-i*16,str(ar[i][0]))
	c.drawString(203,780-i*16+14,'_'*28)
	c.drawString(340,780-i*16,str(ar[i][1]))

c.save()
