import custom_Qlabel
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout_outline.ui'
#
# Created: Tue Mar 15 17:55:38 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1061, 817)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.graphlistWidget = QtGui.QListWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphlistWidget.sizePolicy().hasHeightForWidth())
        self.graphlistWidget.setSizePolicy(sizePolicy)
        self.graphlistWidget.setMaximumSize(QtCore.QSize(16777215, 130))
        self.graphlistWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphlistWidget.setIconSize(QtCore.QSize(110, 60))
        self.graphlistWidget.setFlow(QtGui.QListView.TopToBottom)
        self.graphlistWidget.setResizeMode(QtGui.QListView.Adjust)
        self.graphlistWidget.setViewMode(QtGui.QListView.IconMode)
        self.graphlistWidget.setObjectName(_fromUtf8("graphlistWidget"))
        self.horizontalLayout_5.addWidget(self.graphlistWidget)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_5)
        self.verticalLayout_6 = QtGui.QVBoxLayout()
        self.verticalLayout_6.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.delete_btn = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_btn.sizePolicy().hasHeightForWidth())
        self.delete_btn.setSizePolicy(sizePolicy)
        self.delete_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.delete_btn.setObjectName(_fromUtf8("delete_btn"))
        self.verticalLayout_6.addWidget(self.delete_btn)
        self.undo_btn = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.undo_btn.sizePolicy().hasHeightForWidth())
        self.undo_btn.setSizePolicy(sizePolicy)
        self.undo_btn.setMaximumSize(QtCore.QSize(30, 16777215))
        self.undo_btn.setObjectName(_fromUtf8("undo_btn"))
        self.verticalLayout_6.addWidget(self.undo_btn)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.horizontalLayout_14.setObjectName(_fromUtf8("horizontalLayout_14"))
        self.display_item = custom_Qlabel.customLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display_item.sizePolicy().hasHeightForWidth())
        self.display_item.setSizePolicy(sizePolicy)
        self.display_item.setMinimumSize(QtCore.QSize(300, 0))
        self.display_item.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.display_item.setObjectName(_fromUtf8("display_item"))
        self.horizontalLayout_14.addWidget(self.display_item)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_14)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.gif = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gif.sizePolicy().hasHeightForWidth())
        self.gif.setSizePolicy(sizePolicy)
        self.gif.setText(_fromUtf8(""))
        self.gif.setAlignment(QtCore.Qt.AlignCenter)
        self.gif.setObjectName(_fromUtf8("gif"))
        self.verticalLayout_4.addWidget(self.gif)
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setMinimumSize(QtCore.QSize(300, 0))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_4.addWidget(self.tableWidget)
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout_5.addWidget(self.label_2)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_16.setObjectName(_fromUtf8("horizontalLayout_16"))
        self.horizontalLayout_18 = QtGui.QHBoxLayout()
        self.horizontalLayout_18.setObjectName(_fromUtf8("horizontalLayout_18"))
        self.btn_x1 = QtGui.QPushButton(self.centralwidget)
        self.btn_x1.setCheckable(True)
        self.btn_x1.setObjectName(_fromUtf8("btn_x1"))
        self.horizontalLayout_18.addWidget(self.btn_x1)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_18)
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout_16.addWidget(self.lineEdit)
        self.horizontalLayout_17 = QtGui.QHBoxLayout()
        self.horizontalLayout_17.setObjectName(_fromUtf8("horizontalLayout_17"))
        self.btn_x2 = QtGui.QPushButton(self.centralwidget)
        self.btn_x2.setCheckable(True)
        self.btn_x2.setObjectName(_fromUtf8("btn_x2"))
        self.horizontalLayout_17.addWidget(self.btn_x2)
        self.lineEdit_2 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_17.addWidget(self.lineEdit_2)
        self.horizontalLayout_16.addLayout(self.horizontalLayout_17)
        self.verticalLayout_5.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_13 = QtGui.QHBoxLayout()
        self.horizontalLayout_13.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_13.setObjectName(_fromUtf8("horizontalLayout_13"))
        self.horizontalLayout_20 = QtGui.QHBoxLayout()
        self.horizontalLayout_20.setObjectName(_fromUtf8("horizontalLayout_20"))
        self.btn_y1 = QtGui.QPushButton(self.centralwidget)
        self.btn_y1.setCheckable(True)
        self.btn_y1.setObjectName(_fromUtf8("btn_y1"))
        self.horizontalLayout_20.addWidget(self.btn_y1)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_20)
        self.lineEdit_3 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.horizontalLayout_13.addWidget(self.lineEdit_3)
        self.horizontalLayout_19 = QtGui.QHBoxLayout()
        self.horizontalLayout_19.setObjectName(_fromUtf8("horizontalLayout_19"))
        self.btn_y2 = QtGui.QPushButton(self.centralwidget)
        self.btn_y2.setCheckable(True)
        self.btn_y2.setObjectName(_fromUtf8("btn_y2"))
        self.horizontalLayout_19.addWidget(self.btn_y2)
        self.lineEdit_4 = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.horizontalLayout_19.addWidget(self.lineEdit_4)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_19)
        self.verticalLayout_5.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.verticalLayout_4.addLayout(self.verticalLayout_5)
        self.horizontalLayout_21 = QtGui.QHBoxLayout()
        self.horizontalLayout_21.setObjectName(_fromUtf8("horizontalLayout_21"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem)
        self.proceed_btn = QtGui.QPushButton(self.centralwidget)
        self.proceed_btn.setObjectName(_fromUtf8("proceed_btn"))
        self.horizontalLayout_21.addWidget(self.proceed_btn)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_21)
        self.verticalLayout_3.addLayout(self.verticalLayout_4)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setContentsMargins(7, -1, 7, -1)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.savetable = QtGui.QPushButton(self.centralwidget)
        self.savetable.setObjectName(_fromUtf8("savetable"))
        self.horizontalLayout_4.addWidget(self.savetable)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.plotShowBtn = QtGui.QPushButton(self.centralwidget)
        self.plotShowBtn.setObjectName(_fromUtf8("plotShowBtn"))
        self.horizontalLayout_4.addWidget(self.plotShowBtn)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_15 = QtGui.QHBoxLayout()
        self.horizontalLayout_15.setSizeConstraint(QtGui.QLayout.SetMinimumSize)
        self.horizontalLayout_15.setObjectName(_fromUtf8("horizontalLayout_15"))
        self.pdfSelectBtn = QtGui.QPushButton(self.centralwidget)
        self.pdfSelectBtn.setObjectName(_fromUtf8("pdfSelectBtn"))
        self.horizontalLayout_15.addWidget(self.pdfSelectBtn)
        self.runBtn = QtGui.QPushButton(self.centralwidget)
        self.runBtn.setObjectName(_fromUtf8("runBtn"))
        self.horizontalLayout_15.addWidget(self.runBtn)
        self.contin = QtGui.QPushButton(self.centralwidget)
        self.contin.setObjectName(_fromUtf8("contin"))
        self.horizontalLayout_15.addWidget(self.contin)
        self.manual = QtGui.QPushButton(self.centralwidget)
        self.manual.setObjectName(_fromUtf8("manual"))
        self.horizontalLayout_15.addWidget(self.manual)
        self.selectAreaBtn = QtGui.QPushButton(self.centralwidget)
        self.selectAreaBtn.setObjectName(_fromUtf8("selectAreaBtn"))
        self.horizontalLayout_15.addWidget(self.selectAreaBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_15)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1061, 25))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_2 = QtGui.QDockWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_2.sizePolicy().hasHeightForWidth())
        self.dockWidget_2.setSizePolicy(sizePolicy)
        self.dockWidget_2.setMinimumSize(QtCore.QSize(185, 157))
        self.dockWidget_2.setMaximumSize(QtCore.QSize(185, 524287))
        self.dockWidget_2.setObjectName(_fromUtf8("dockWidget_2"))
        self.dockWidgetContents_2 = QtGui.QWidget()
        self.dockWidgetContents_2.setObjectName(_fromUtf8("dockWidgetContents_2"))
        self.verticalLayout = QtGui.QVBoxLayout(self.dockWidgetContents_2)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.pdflistWidget = QtGui.QListWidget(self.dockWidgetContents_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pdflistWidget.sizePolicy().hasHeightForWidth())
        self.pdflistWidget.setSizePolicy(sizePolicy)
        self.pdflistWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.pdflistWidget.setIconSize(QtCore.QSize(150, 200))
        self.pdflistWidget.setResizeMode(QtGui.QListView.Adjust)
        self.pdflistWidget.setViewMode(QtGui.QListView.IconMode)
        self.pdflistWidget.setObjectName(_fromUtf8("pdflistWidget"))
        self.verticalLayout.addWidget(self.pdflistWidget)
        self.progressBar = QtGui.QProgressBar(self.dockWidgetContents_2)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.verticalLayout.addWidget(self.progressBar)
        self.dockWidget_2.setWidget(self.dockWidgetContents_2)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_2)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.delete_btn.setText(_translate("MainWindow", "X", None))
        self.undo_btn.setText(_translate("MainWindow", "U", None))
        self.display_item.setText(_translate("MainWindow", "TextLabel", None))
        self.label_2.setText(_translate("MainWindow", "Align Axes:", None))
        self.btn_x1.setText(_translate("MainWindow", "X1", None))
        self.btn_x2.setText(_translate("MainWindow", "X2", None))
        self.btn_y1.setText(_translate("MainWindow", "Y1", None))
        self.btn_y2.setText(_translate("MainWindow", "Y2", None))
        self.proceed_btn.setText(_translate("MainWindow", "Proceed", None))
        self.savetable.setText(_translate("MainWindow", "Save Table", None))
        self.plotShowBtn.setText(_translate("MainWindow", "Plot from Data", None))
        self.pdfSelectBtn.setText(_translate("MainWindow", "Select PDF", None))
        self.runBtn.setText(_translate("MainWindow", "Run", None))
        self.contin.setText(_translate("MainWindow", "Automatic", None))
        self.manual.setText(_translate("MainWindow", "Manual", None))
        self.selectAreaBtn.setText(_translate("MainWindow", "Select Area", None))

