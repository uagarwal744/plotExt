from PyQt4 import QtCore, QtGui
import sys, time
import os
import layout_gene
import qdarkstyle
import pdf_to_img
import write_to_pdf
from pdf_to_img import ImageThread, ResultObj
from multiprocessing import Pool
from PyQt4.QtCore import *
from graphextract_returnArray1 import GraphThread, ReturnObj
import image_class
import write_to_pdf
import numpy as np
#import image_class

import cv2

class plotThread(QtCore.QThread):

    table_completed = QtCore.pyqtSignal()
    def __init__(self, plot, index):
        QtCore.QThread.__init__(self)
        self.plot=plot
        self.index=index

    def run(self):
        self.plot.run()
        table=self.plot.table
        print '^^^^^^^^^^$$$$$$######^^^^^^^^^'
        print table
        self.table_completed.emit()

class popup(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.label=QtGui.QLabel()


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

        #self.tables=[]
        self.pdfSelectBtn.clicked.connect(self.openfile)
        self.pdfSelectBtn.setCursor(QtCore.Qt.PointingHandCursor)
        self.btn_x1.clicked.connect(self.Coordinate)
        self.btn_x2.clicked.connect(self.Coordinate)
        self.btn_y1.clicked.connect(self.Coordinate)
        self.btn_y2.clicked.connect(self.Coordinate)
        self.proceed_btn.clicked.connect(self.fix_axes)
        self.delete_btn.clicked.connect(self.delete_item)
        self.selectAreaBtn.clicked.connect(self.enableDrag)
        self.undo_btn.clicked.connect(self.undo)
        self.pdflistWidget.itemClicked.connect(self.pdfItem_click)
        self.graphlistWidget.itemClicked.connect(self.graphItem_click)
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
        self.manual.clicked.connect(self.manual_fun)
        self.contin.clicked.connect(self.getTables)
        self.progressBar.hide()
        self.graphlistWidget.itemSelectionChanged.connect(self.change_selected_item)
        self.pdflistWidget.itemSelectionChanged.connect(self.change_selected_pdf_item)
        self.savetable.clicked.connect(self.download_table)

        self.manual.hide()
        self.contin.hide()
        self.selectAreaBtn.hide()
        self.proceed_btn.hide()
        self.btn_x1.hide()
        self.btn_y2.hide()
        self.btn_y1.hide()
        self.btn_x2.hide()
        self.lineEdit.hide()
        self.lineEdit_2.hide()
        self.lineEdit_3.hide()
        self.lineEdit_4.hide()
        self.plotShowBtn.clicked.connect(self.show_plot)
        self.gif.hide()

    def show_plot(self):
        img=cv2.imread('plot_from_data.png')
        cv2.imshow('plot',img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def download_table(self):
        '''still to add
        name of the plot
        names from legend in an array of strings
        call this function in a loop for all the generated graphs

        '''
        export_dialog = QtGui.QFileDialog()
        export_dialog.setWindowTitle('Save PDF')
        export_dialog.setAcceptMode(QtGui.QFileDialog.AcceptSave)
        export_dialog.setNameFilter('PDF files (*.pdf)')
        export_dialog.setDefaultSuffix('pdf')
        export_dialog.show()
        #z=export_dialog.selectedFiles()
        if export_dialog.exec_() == QtGui.QFileDialog.Accepted:
            location=export_dialog.selectedFiles()[0]
            print location
            c=write_to_pdf.createpdf(str(location))
            write_to_pdf.pdfoutput(c,self.plots[0].table,self.plots[0].outer_image_file)
            # print(export_dialog.selectedFiles()[0])
            #self.x = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile', filter='*pdf')
        # c=write_to_pdf.createpdf(xz)
        #write_to_pdf.pdfoutput(c,self.table)
        # write_to_pdf.pdfoutput(c,self.plots[0].table,self.plots[0].outer_image_file)


    def change_selected_pdf_item(self):
        items=self.pdflistWidget.selectedItems()
        item=items[0]
        self.pdfItem_click(item)
    def change_selected_item(self):
        items=self.graphlistWidget.selectedItems()
        item=items[0]
        self.graphItem_click(item)
    def getTables(self):
        #self.tables = [0 for plot in self.plots ]
        #self.gif.show()
        #self.tableWidget.hide()
        #movie=QtGui.QMovie("loading.gif")
        #self.gif.setMovie(movie)
        #movie.start()
        self.thread_per_plot=[]
        for plot in self.plots:
            temp_thread=plotThread(plot,self.plots.index(plot))
            temp_thread.table_completed.connect(self.on_table_completion)
            self.thread_per_plot.append(temp_thread)
            temp_thread.start()



        '''for plots in self.plots:
            for plot in plots:
                print plot
                print '##########################################'
                self.tThread=image_class.TableThread(plot,self.table_progress)
                self.tThread.start()

                return'''

    def on_table_completion(self):
        #self.tables[index]=table
        print '())()()())()^^^^^^()()()()()'
        self.gif.hide()
        self.tableWidget.show()
        items=self.graphlistWidget.selectedItems()
        self.graphItem_click(items[0])
        #print self.tables

        '''def table_progress(self, result):
        print '$$$$$$$'
        print result.table
        self.tableWidget.setColumnCount(len(result.table)) #rows and columns of table
        self.tableWidget.setRowCount(len(result.table[0]))
        for row in range(len(result.table[0])): # add items from array to QTableWidget
            for column in range(len(result.table)):
                #item = self.array[0] # each item is a QTableWidgetItem
                # add the QTableWidgetItem to QTableWidget, but exception thrown
                self.tableWidget.setItem(row, column, QtGui.QTableWidgetItem(result.table[column][row])) '''
                        
                

    def manual_fun(self):
        self.btn_x1.show()
        self.btn_x2.show()
        self.btn_y1.show()
        self.btn_y2.show()
        self.contin.hide()
        self.lineEdit.show()
        self.lineEdit_2.show()
        self.lineEdit_3.show()
        self.lineEdit_4.show()
        self.label_2.show()
        self.proceed_btn.show()
        self.selectAreaBtn.show()
        #self.tableWidget.hide()
    def onResize(self, event):
        items=self.pdflistWidget.selectedItems()
        if len(items)==0:
            return
        self.pdfItem_click(items[0])
    def removePlot(self,filename):
        print(self.plot_dic)
        print(self.plots)
        plot = (self.plot_dic[str(filename)])
        self.plots.remove(plot)
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

    
    #def loadingFinished(self):

    def progress_of_extract(self, result):
        images=result.list1
        files=result.list2
        # images.append(result.list1)
        # files.append(result.list2)
        print result.page_no
        print result.list2
        print "**************"
        new_list=[]
        for j in range(len(images)):
            plot = image_class.Graph(images[j],files[j])
            #new_list.append(image_class.Graph(images[j],files[j]))
            #print new_list
            self.addGraphItem(plot)
            self.plot_dic[plot.outer_image_file]=plot
            self.plots.append(plot)
        self.progressBar.setValue(self.progressBar.value()+1)
        self.statusbar.showMessage('Extracting Graphs from '+str(result.page_no+2)+' page ...')

        print self.plots
    def finished_extracting(self, result):
        self.statusbar.clearMessage()
        self.progressBar.hide()
        self.runBtn.hide()
        self.manual.show()
        self.contin.show()

    def getGraphs(self):
        self.graphlistWidget.clear()

        self.gthread = GraphThread(self.listOfFiles, self.progress_of_extract, self.finished_extracting)
        self.gthread.start()
        self.progressBar.show()
        self.progressBar.setValue(0)
        self.statusbar.showMessage('Extracting Graphs from 1 page ...')

        '''images,files = graphextract_returnArray1.PlotExtractor(self.listOfFiles).graphextract()
        for i in range(len(images)):
            new_list=[]
            print i,images[i]
            for j in range(len(images[i])):
                new_list.append(image_class.Graph(images[i][j],files[i][j]))
                self.addGraphItem(new_list[-1])
                self.plot_dic[new_list[-1].outer_image_file]=new_list[-1]
            self.plots.append(new_list)

        print self.plots'''



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
        p='graph'+str(pg_no)+str(self.graph_per_page[int(pg_no)-1])+'.png'  
        cv2.imwrite(p, graph)
        item=QtGui.QListWidgetItem(QtGui.QIcon(p),QtCore.QString(p))
        self.graphlistWidget.addItem(item)
        plot = image_class.Graph(graph,p)
        self.plots.append(plot)
        self.plot_dic[p]=plot
        #print self.plots



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
        ind=self.graphlistWidget.row(item)
        print ind
        print (self.plots)
        if(not hasattr( self.plots[ind],'table')):
            return

        self.tableWidget.setColumnCount(len(self.plots[ind].table)) #rows and columns of table
        self.tableWidget.setRowCount(len(self.plots[ind].table[0]))
        for column in range(len(self.plots[ind].table)): # add items from array to QTableWidget
            for row in range(len(self.plots[ind].table[0])):
                #item = self.array[0] # each item is a QTableWidgetItem
                # add the QTableWidgetItem to QTableWidget, but exception thrown
                self.tableWidget.setItem(row, column, QtGui.QTableWidgetItem(self.plots[ind].table[column][row]))
            
    def pdfItem_click(self, item):
        loc=self.x+str(int(item.text())-1)+"new.png"
        self.display_item.setPixmap(QtGui.QPixmap(loc).scaled(self.display_item.size(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation))

    def loadingFinished(self, result):
        '''self.numpages = result.val
        y = self.numpages
        #y=pdf_to_img.pdf_to_img1(self.x, "300")
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
        '''
        self.statusbar.clearMessage()
        self.runBtn.setEnabled(True)
        self.btn_x1.setEnabled(True)
        self.btn_x2.setEnabled(True)
        self.btn_y1.setEnabled(True)
        self.btn_y2.setEnabled(True)
        self.proceed_btn.setEnabled(True)
        self.pdfSelectBtn.setEnabled(True)
        self.progressBar.hide()
        #self.tables=[[]]*(result.numPages)
        #print self.tables
        #print result.val

    def progress_handle(self, result):
        
        self.statusbar.showMessage(QString(' Loading '+str(result.val+2)+' page ....'))
        w=self.x+str(result.val)+"new.png"
            
        self.item=QtGui.QListWidgetItem(QtGui.QIcon(w),QtCore.QString(str(result.val+1)))
        self.pdflistWidget.addItem(self.item)

        self.graph_per_page.append(0)

        w=self.x+str(result.val)+".png"
        self.listOfFiles.append(str(w))

        if result.val==0:
            self.progressBar.setMaximum(result.numPages)
            self.progressBar.setValue(1)
            self.pdflistWidget.setItemSelected(self.pdflistWidget.item(0), True)
            self.display_item.setPixmap(QtGui.QPixmap(self.x+"0new.png").scaled(self.display_item.size(), QtCore.Qt.KeepAspectRatio,QtCore.Qt.SmoothTransformation))
        else:
            self.progressBar.setValue(self.progressBar.value()+1)


    def openfile(self):
        
        self.x = QtGui.QFileDialog.getOpenFileName(self, 'OpenFile', filter='*pdf')
        #self.x stores the address of the chosen pdf
        print self.x
        if self.x=="":      # No file is Chosen
            return
        z=QtCore.QFileInfo(self.x)     #z stores only the file name
        self.pdfSelectBtn.setEnabled(False)
        self.progressBar.show()
        self.statusbar.showMessage(QString(' Loading '+'1'+' page ....'))
        # self.statusbar.insertWidget(3,progress_bar)
        # self.statusbar.progress_bar.setMaximum(6)
        # self.statusbar.progress_bar.setValue(1)
        self.ithread = ImageThread(self.x,"300", self.loadingFinished, self.progress_handle)
        self.ithread.start()

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
    # for count in range(1, 100):
    #     splash.showMessage(splash.tr('Processing %1...').arg(count),
    #                        QtCore.Qt.AlignBottom+20, QtCore.Qt.black)
    #     QtGui.QApplication.processEvents()
    #     QtCore.QThread.msleep(15)
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
