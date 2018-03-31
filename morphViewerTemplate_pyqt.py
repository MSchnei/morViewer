# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'morphViewerTemplate.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(920, 791)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 901, 771))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Manual = QtGui.QCheckBox(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Manual.sizePolicy().hasHeightForWidth())
        self.Manual.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setItalic(True)
        self.Manual.setFont(font)
        self.Manual.setObjectName(_fromUtf8("Manual"))
        self.gridLayout.addWidget(self.Manual, 14, 2, 1, 1)
        self.horizontalLayout_cluster = QtGui.QHBoxLayout()
        self.horizontalLayout_cluster.setObjectName(_fromUtf8("horizontalLayout_cluster"))
        self.c_thresh = QtGui.QSpinBox(self.layoutWidget)
        self.c_thresh.setObjectName(_fromUtf8("c_thresh"))
        self.horizontalLayout_cluster.addWidget(self.c_thresh)
        self.c_size = QtGui.QSpinBox(self.layoutWidget)
        self.c_size.setObjectName(_fromUtf8("c_size"))
        self.horizontalLayout_cluster.addWidget(self.c_size)
        self.Cluster = QtGui.QPushButton(self.layoutWidget)
        self.Cluster.setObjectName(_fromUtf8("Cluster"))
        self.horizontalLayout_cluster.addWidget(self.Cluster)
        self.gridLayout.addLayout(self.horizontalLayout_cluster, 5, 2, 1, 1)
        self.horizontalLayout_browser = QtGui.QHBoxLayout()
        self.horizontalLayout_browser.setObjectName(_fromUtf8("horizontalLayout_browser"))
        self.cursorBrowserX = QtGui.QSpinBox(self.layoutWidget)
        self.cursorBrowserX.setObjectName(_fromUtf8("cursorBrowserX"))
        self.horizontalLayout_browser.addWidget(self.cursorBrowserX)
        self.cursorBrowserY = QtGui.QSpinBox(self.layoutWidget)
        self.cursorBrowserY.setObjectName(_fromUtf8("cursorBrowserY"))
        self.horizontalLayout_browser.addWidget(self.cursorBrowserY)
        self.cursorBrowserZ = QtGui.QSpinBox(self.layoutWidget)
        self.cursorBrowserZ.setObjectName(_fromUtf8("cursorBrowserZ"))
        self.horizontalLayout_browser.addWidget(self.cursorBrowserZ)
        self.gridLayout.addLayout(self.horizontalLayout_browser, 16, 2, 1, 1)
        self.Cycle = QtGui.QPushButton(self.layoutWidget)
        self.Cycle.setObjectName(_fromUtf8("Cycle"))
        self.gridLayout.addWidget(self.Cycle, 16, 0, 1, 1)
        self.Black_tophat = QtGui.QPushButton(self.layoutWidget)
        self.Black_tophat.setObjectName(_fromUtf8("Black_tophat"))
        self.gridLayout.addWidget(self.Black_tophat, 3, 2, 1, 1)
        self.Rotate = QtGui.QPushButton(self.layoutWidget)
        self.Rotate.setObjectName(_fromUtf8("Rotate"))
        self.gridLayout.addWidget(self.Rotate, 16, 1, 1, 1)
        self.Erode = QtGui.QPushButton(self.layoutWidget)
        self.Erode.setObjectName(_fromUtf8("Erode"))
        self.gridLayout.addWidget(self.Erode, 0, 2, 1, 1)
        self.graphicsView = GraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 14, 2)
        self.Dilate = QtGui.QPushButton(self.layoutWidget)
        self.Dilate.setObjectName(_fromUtf8("Dilate"))
        self.gridLayout.addWidget(self.Dilate, 1, 2, 1, 1)
        self.horizontalSlider = QtGui.QSlider(self.layoutWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.gridLayout.addWidget(self.horizontalSlider, 14, 0, 1, 2)
        self.White_tophat = QtGui.QPushButton(self.layoutWidget)
        self.White_tophat.setObjectName(_fromUtf8("White_tophat"))
        self.gridLayout.addWidget(self.White_tophat, 2, 2, 1, 1)
        self.Save = QtGui.QPushButton(self.layoutWidget)
        self.Save.setObjectName(_fromUtf8("Save"))
        self.gridLayout.addWidget(self.Save, 19, 2, 1, 1)
        self.horizontalLayout_grow = QtGui.QHBoxLayout()
        self.horizontalLayout_grow.setObjectName(_fromUtf8("horizontalLayout_grow"))
        self.Seed = QtGui.QLabel(self.layoutWidget)
        self.Seed.setAlignment(QtCore.Qt.AlignCenter)
        self.Seed.setObjectName(_fromUtf8("Seed"))
        self.horizontalLayout_grow.addWidget(self.Seed)
        self.Coordns = QtGui.QLabel(self.layoutWidget)
        self.Coordns.setAlignment(QtCore.Qt.AlignCenter)
        self.Coordns.setObjectName(_fromUtf8("Coordns"))
        self.horizontalLayout_grow.addWidget(self.Coordns)
        self.Grow = QtGui.QPushButton(self.layoutWidget)
        self.Grow.setObjectName(_fromUtf8("Grow"))
        self.horizontalLayout_grow.addWidget(self.Grow)
        self.gridLayout.addLayout(self.horizontalLayout_grow, 4, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 6, 2, 8, 1)
        self.Open = QtGui.QPushButton(self.layoutWidget)
        self.Open.setObjectName(_fromUtf8("Open"))
        self.gridLayout.addWidget(self.Open, 18, 2, 1, 1)
        self.File_names = QtGui.QListWidget(self.layoutWidget)
        self.File_names.setObjectName(_fromUtf8("File_names"))
        self.gridLayout.addWidget(self.File_names, 17, 0, 3, 2)
        self.Reset = QtGui.QPushButton(self.layoutWidget)
        self.Reset.setObjectName(_fromUtf8("Reset"))
        self.gridLayout.addWidget(self.Reset, 17, 2, 1, 1)
        self.layoutWidget.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.Manual.setText(_translate("Form", "Manual segmentation", None))
        self.Cluster.setText(_translate("Form", "Cluster", None))
        self.Cycle.setText(_translate("Form", "Cycle", None))
        self.Black_tophat.setText(_translate("Form", "Black tophat", None))
        self.Rotate.setText(_translate("Form", "Rotate", None))
        self.Erode.setText(_translate("Form", "Erode", None))
        self.Dilate.setText(_translate("Form", "Dilate", None))
        self.White_tophat.setText(_translate("Form", "White tophat", None))
        self.Save.setText(_translate("Form", "Save", None))
        self.Seed.setText(_translate("Form", "Seed:", None))
        self.Coordns.setText(_translate("Form", "X,Y,Z", None))
        self.Grow.setText(_translate("Form", "Grow", None))
        self.Open.setText(_translate("Form", "Open", None))
        self.Reset.setText(_translate("Form", "Reset", None))

from ..widgets.GraphicsView import GraphicsView
