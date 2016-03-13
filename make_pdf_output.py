import write_to_pdf
a=[[5,2,3,4,5,7,8],[0,2,3,4,1,7,8]]
img='a.jpg'
c=write_to_pdf.createpdf('newpdf.pdf')
write_to_pdf.pdfoutput(c,img,a)
