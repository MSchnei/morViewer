# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/marian/Documents/Git/morphView/morphViewerTemplate3.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt4 import QtCore, QtGui
from nibabel import load, save, Nifti1Image
import pyqtgraph as pg

# %% set parameters

# provide string to nii data
strPathData = '/home/marian/Documents/Testing/testMorphViewer/testIma.nii.gz'

# %% import data

# load data
nii = load(strPathData)
basename = nii.get_filename().split(os.extsep, 1)[0]
dirname = os.path.dirname(nii.get_filename())

data = nii.get_data()

# %%
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class Widget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.resize(800, 800)

        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))

        self.Dilate = QtGui.QPushButton(_fromUtf8("Dilate"))
        self.gridLayout.addWidget(self.Dilate, 1, 2, 1, 1)

        self.data = data

        self.graphicsView = pg.GraphicsWindow(size=(self.data.shape[0],
                                                    self.data.shape[2]))
        self.viewbox = self.graphicsView.addViewBox()
        self.image = pg.ImageItem()
        self.viewbox.addItem(self.image)
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 4, 2)

        self.Reset = QtGui.QPushButton(_fromUtf8("Reset"))
        self.gridLayout.addWidget(self.Reset, 4, 2, 1, 1)

        self.Cluster = QtGui.QPushButton(_fromUtf8("Cluster"))
        self.gridLayout.addWidget(self.Cluster, 2, 2, 1, 1)

        self.Rotate = QtGui.QPushButton(_fromUtf8("Rotate"))
        self.gridLayout.addWidget(self.Rotate, 5, 1, 1, 1)

        self.Erode = QtGui.QPushButton(_fromUtf8("Erode"))
        self.gridLayout.addWidget(self.Erode, 0, 2, 1, 1)

        self.Save = QtGui.QPushButton(_fromUtf8("Save"))
        self.gridLayout.addWidget(self.Save, 5, 2, 1, 1)

        self.Cycle = QtGui.QPushButton(_fromUtf8("Cycle"))
        self.gridLayout.addWidget(self.Cycle, 5, 0, 1, 1)

        self.horizontalSlider = QtGui.QSlider(self)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(self.data.shape[1]-1)
        self.gridLayout.addWidget(self.horizontalSlider, 4, 0, 1, 2)

        # set it to the center image, if you want.
        self.sliderMoved(int((self.data.shape[1]-1)/2.))
        self.horizontalSlider.sliderMoved.connect(self.sliderMoved)

    def sliderMoved(self, val):
        print "Slider moved to:", val
        try:
            self.image.setImage(data[:, val, :])
        except IndexError:
            print "Error: No image at index", val

# %% render
app = QtGui.QApplication([])
w = Widget()
w.show()
w.raise_()
app.exec_()
