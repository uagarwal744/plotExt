from PyQt4 import QtCore, QtGui
import sys, time
import os
import layout_gene
import qdarkstyle
import pdf_to_img
from multiprocessing import Pool
from PyQt4.QtCore import *
import graphextract_returnArray
import image_class
#import image_class

import cv2


class Example(QtGui.QMainWindow, layout_gene.Ui_MainWindow):
    def __init__(self):
        super(Example, self).__init__()
        self.setupUi(self)
        self.axes=[['', ''], ['', ''], ['',''], ['','']]
        self.axes_values=['','','','']
        self.plots=[]
        self.listOfFiles = []
        self.deletedItems=[]         # stores the deleted graphlistWidget items
        self.graph_per_page=[]
        self.plot_dic={}


        self.pdfSelectBtn.clicked.connect(self.openfile)
        self.pdfSelectBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.pdflistWidget.itemClicked.connect(self.pdfItem_click)
        self.graphlistWidget.itemClicked.connect(self.graphItem_click)
        self.btn_x1.clicked.connect(self.Coordinate)
        self.btn_x2.clicked.connect(self.Coordinate)
        self.btn_y1.clicked.connect(self.Coordinate)
        self.btn_y2.clicked.connect(self.Coordinate)
        self.proceed_btn.clicked.connect(self.fix_axes)
        self.delete_btn.clicked.connect(self.delete_item)
        self.selectAreaBtn.clicked.connect(self.enableDrag)
        self.undo_btn.clicked.connect(self.undo)
        """disabling buttons before a pdf is chosen"""
        self.runBtn.setEnabled(False)
        self.btn_x1.setEnabled(False)
        self.btn_x2.setEnabled(False)
        self.btn_y1.setEnabled(False)
        self.btn_y2.setEnabled(False)
        self.proceed_btn.setEnabled(False)
        self.display_item.btnReleased.connect(self.manualAddGraph)
        self.runBtn.clicked.connect(self.getGraphs)
        self.display_item.resizeEvent = self.onResize
        self.pushButton_5.clicked.connect(self.getTables)


    def getTables(self):
        for plots in self.plots:
            for plot in plots:
                plot.run()
                print(plot.table)
                return

    def onResize(self, event):
        items=self.pdflistWidget.selectedItems()
        print items
        self.pdfItem_click(items[0])
    def removePlot(self,filename):
        print(self.plot_dic)
        print(self.plots)
        for plots in self.plots:
            plot = (self.plot_dic[str(filename)])
            if plot in plots:
                plots.remove(self.plot_dic[str(filename)])
        print(self.plots)

    '''def changeEvent(self, event):
        QtGui.QMainWindow.changeEvent(self, event)
        if event.type() == QtCore.QEvent.WindowStateChange:
        #print QtCore.Qt.WindowFullScreen
            if self.windowState() & QtCore.Qt.WindowMaximized:
                print 'a'

                items=self.pdflistWidget.selectedItems()
                print items
                self.pdfItem_click(items[0])
            elif event.oldState() & QtCore.Qt.WindowMaximized:
                items=self.pdflistWidget.selectedItems()
                print items, 'b'
                self.pdfItem_click(items[0])'''

    def getGraphs(self):
        images,files = graphextract_returnArray.PlotExtractor(self.listOfFiles).graphextract()
        print files
        for i in range(len(images)):
            new_list=[]
            for j in range(len(images[i])):
                new_list.append(image_class.Graph(images[i][j],files[i][j]))
                self.addGraphItem(new_list[-1])
                self.plot_dic[new_list[-1].outer_image_file]=new_list[-1]
            self.plots.append(new_list)

        print self.plots



    def undo(self):
        if len(self.deletedItems)!=0:
            self.graphlistWidget.addItem(self.deletedItems.pop())

    def addGraphItem(self, plot):
        item=QtGui.QListWidgetItem(QtGui.QIcon(plot.outer_image_file), QString(plot.outer_image_file))
        self.graphlistWidget.addItem(item)

    def manualAddGraph(self):
        self.selectAreaBtn.setChecked(False)
        self.display_item.isEnabled=False
        rect=self.display_item.currentQRect
        pdf_item=self.pdflistWidget.selectedItems()
        pg_no=pdf_item[0].text()   #x stores the page no of pdf file currently selected
        self.graph_per_page[int(pg_no)-1]+=1
        img = cv2.imread(str(self.x)+str(int(pg_no)-1)+'.png')
        height, width = img.shape[:2]     # dimensions of original image
        #size of pixmap
        h=self.display_item.pixmap().height()
        w=self.display_item.pixmap().width()        
        #multiplying ratio to convert pixels of pixmap to original image
        y_ratio=float(height)/h            
        x_ratio=float(width)/w

        top_left=QtCore.QPoint(rect.topLeft())
        bottom_right=QtCore.QPoint(rect.bottomRight())
        xstart=int(top_left.x()*x_ratio)
        ystart=int(top_left.y()*y_ratio)
        xend=int(bottom_right.x()*x_ratio)
        yend=int(bottom_right.y()*y_ratio)
        graph = img[int(ystart):int(yend),int(xstart):int(xend)]  
        cv2.imwrite('graph'+str(pg_no)+str(self.graph_per_page[int(pg_no)-1])+'.png', graph)
        item=QtGui.QListWidgetItem(QtGui.QIcon('cd'+str(pg_no)+'.png'),QtCore.QString('graph'+str(pg_no)+str(self.graph_per_page[int(pg_no)-1])+'.png'))
        self.graphlistWidget.addItem(item)
        self.plots[int(pg_no)-1].append(image_class.Graph(graph,'graph'+str(pg_no)+str(self.graph_per_page[int(pg_no)-1])+'.png'))



    def enableDrag(self):
        self.display_item.isEnabled=True
        

    def fix_axes(self):
        #self.x1.setReadOnly(True)mg=cv2.imread("test.pdf0.jpg")
        
        #self.x2.setReadOnly(True)
        #self.y1.setReadOnly(True)
        #self.y2.setReadOnly(True)
        self.axes_values[0]=self.x1.text()
        self.axes_values[1]=self.x2.text()
        self.axes_values[2]=self.y1.text()
        self.axes_values[3]=self.y2.text()

    def delete_item(self):
        items=self.graphlistWidget.selectedItems()
        for item in items:
            self.graphlistWidget.takeItem(self.graphlistWidget.row(item))
            self.deletedItems.append(item)
            self.removePlot(item.text())
        '''to change the display of custom Qlabel after delleting an item'''
        items=self.graphlistWidget.selectedItems()
        item=items[0]

        self.display_item.setPixmap(QtGui.QPixmap(item.text()).scaled(self.display_item.size(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation))
        
    
    def Coordinate(self):
        def getPos(event):
            x = event.pos().x()
            y = event.pos().y()
            
            
            sender.setChecked(False)
            if sender.text()=='X1':
                self.axes[0][0]=x
                self.axes[0][1]=y
                print 'X1',self.axes[0]
            elif sender.text()=='X2':
                self.axes[1][0]=x
                self.axes[1][1]=y
                print 'X2',self.axes[1]
            elif sender.text()=='Y1':
                self.axes[2][0]=x
                self.axes[2][1]=y
                print 'Y1',self.axes[2]
            else:
                self.axes[3][0]=x
                self.axes[3][1]=y
                print 'Y2',self.axes[3]

            self.display_item.setCursor(QtCore.Qt.ArrowCursor)
            self.display_item.mousePressEvent=self.mousePressEvent
        sender=self.sender()
        if sender.isChecked():
            self.display_item.setCursor(QtCore.Qt.CrossCursor)
            self.display_item.mousePressEvent=getPos



    def graphItem_click(self, item):
        self.display_item.setPixmap(QtGui.QPixmap(item.text()).scaled(self.display_item.size(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation))
    def pdfItem_click(self, item):
        loc=self.x+str(int(item.text())-1)+"new.png"
        self.display_item.setPixmap(QtGui.QPixmap(loc).scaled(self.display_item.size(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation))

    def openfile(self):
        
        self.x = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile', filter='*pdf')
        #self.x stores the address of the chosen pdf
        print self.x
        if self.x=="":      # No file is Chosen
            return


        z=QtCore.QFileInfo(self.x)     #z stores only the file name
        
        #y stores the number of pages in the pdf 
        y=pdf_to_img.pdf_to_img1(self.x,"300")
        for i in range(y):
            self.graph_per_page.append(0)
        self.pdflistWidget.clear()

        
        for i in range(y):
            w=self.x+str(i)+"new.png"
            
            self.item=QtGui.QListWidgetItem(QtGui.QIcon(w),QtCore.QString(str(i+1)))
            self.pdflistWidget.addItem(self.item)

        for i in range(y):
            w=self.x+str(i)+".png"
            self.listOfFiles.append(str(w))
        self.pdflistWidget.setItemSelected(self.pdflistWidget.item(0), True)
        self.display_item.setPixmap(QtGui.QPixmap(self.x+"0new.png").scaled(self.display_item.size(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation))
        self.runBtn.setEnabled(True)
        self.btn_x1.setEnabled(True)
        self.btn_x2.setEnabled(True)
        self.btn_y1.setEnabled(True)
        self.btn_y2.setEnabled(True)
        self.proceed_btn.setEnabled(True)

class MySplashScreen(QtGui.QSplashScreen):
    def __init__(self, animation, flags=None):
        # run event dispatching in another thread
        QtGui.QSplashScreen.__init__(self, QtGui.QPixmap())
        self.movie = QtGui.QMovie(animation)
        #self.connect(self.movie, QtCore.SIGNAL('frameChanged(int)'), QtCore.SLOT('onNextFrame()'))
        self.movie.frameChanged.connect(self.onNextFrame)
        self.movie.start()

    #@pyqtSlot()
    def onNextFrame(self):
        pixmap = self.movie.currentPixmap()
        self.setPixmap(pixmap)
        self.setMask(pixmap.mask())

def longInitialization(arg):
    time.sleep(arg)
    return 0

def main():
    app=QtGui.QApplication(sys.argv)
    splash=MySplashScreen('splash.gif')
    splash.show()
    app.processEvents()
    for count in range(1, 100):
        splash.showMessage(splash.tr('Processing %1...').arg(count),
                           QtCore.Qt.AlignBottom+20, QtCore.Qt.black)
        QtGui.QApplication.processEvents()
        QtCore.QThread.msleep(15)
    app.setStyleSheet(qdarkstyle.load_stylesheet(pyside=False))
    # this event loop is needed for dispatching of Qt events
    '''Note, that you need to run your initialization code in a separate
     thread, since the main thread should dispatch Qt events.'''
    initLoop = QtCore.QEventLoop()
    pool = Pool(processes=1)
    pool.apply_async(longInitialization, [2], callback=lambda exitCode: initLoop.exit(exitCode))
    initLoop.exec_()

    ex=Example()
    ex.show()
    splash.finish(ex)
    app.exec_()
    
if __name__=='__main__':
    main()