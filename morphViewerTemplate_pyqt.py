# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'morphViewerTemplate_update.ui'
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
        Form.resize(918, 791)
        self.layoutWidget = QtGui.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 901, 771))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.Save = QtGui.QPushButton(self.layoutWidget)
        self.Save.setObjectName(_fromUtf8("Save"))
        self.gridLayout.addWidget(self.Save, 6, 2, 1, 1)
        self.Cycle = QtGui.QPushButton(self.layoutWidget)
        self.Cycle.setObjectName(_fromUtf8("Cycle"))
        self.gridLayout.addWidget(self.Cycle, 6, 0, 1, 1)
        self.Rotate = QtGui.QPushButton(self.layoutWidget)
        self.Rotate.setObjectName(_fromUtf8("Rotate"))
        self.gridLayout.addWidget(self.Rotate, 6, 1, 1, 1)
        self.Erode = QtGui.QPushButton(self.layoutWidget)
        self.Erode.setObjectName(_fromUtf8("Erode"))
        self.gridLayout.addWidget(self.Erode, 0, 2, 1, 1)
        self.Reset = QtGui.QPushButton(self.layoutWidget)
        self.Reset.setObjectName(_fromUtf8("Reset"))
        self.gridLayout.addWidget(self.Reset, 5, 2, 1, 1)
        self.graphicsView = GraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 5, 2)
        self.Dilate = QtGui.QPushButton(self.layoutWidget)
        self.Dilate.setObjectName(_fromUtf8("Dilate"))
        self.gridLayout.addWidget(self.Dilate, 1, 2, 1, 1)
        self.horizontalSlider = QtGui.QSlider(self.layoutWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.gridLayout.addWidget(self.horizontalSlider, 5, 0, 1, 2)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 3, 2, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.c_thresh = QtGui.QSpinBox(self.layoutWidget)
        self.c_thresh.setObjectName(_fromUtf8("c_thresh"))
        self.horizontalLayout_2.addWidget(self.c_thresh)
        self.c_size = QtGui.QSpinBox(self.layoutWidget)
        self.c_size.setObjectName(_fromUtf8("c_size"))
        self.horizontalLayout_2.addWidget(self.c_size)
        self.Cluster = QtGui.QPushButton(self.layoutWidget)
        self.Cluster.setObjectName(_fromUtf8("Cluster"))
        self.horizontalLayout_2.addWidget(self.Cluster)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 2, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.Save.setText(_translate("Form", "Save", None))
        self.Cycle.setText(_translate("Form", "Cycle", None))
        self.Rotate.setText(_translate("Form", "Rotate", None))
        self.Erode.setText(_translate("Form", "Erode", None))
        self.Reset.setText(_translate("Form", "Reset", None))
        self.Dilate.setText(_translate("Form", "Dilate", None))
        self.Cluster.setText(_translate("Form", "Cluster", None))

from ..widgets.GraphicsView import GraphicsView
