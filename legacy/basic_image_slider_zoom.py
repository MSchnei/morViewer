#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 19:49:03 2018

@author: marian
"""

import os
from PyQt4 import QtCore, QtGui
import pyqtgraph as pg
from nibabel import load, save, Nifti1Image
from scipy.ndimage import morphology
import numpy as np

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


class morphViewer(QtGui.QWidget):

    def __init__(self, parent=None, name="morphViewer"):
        super(morphViewer, self).__init__(parent)
        self.resize(800, 800)
        self.val = 0

        # define the data
        self.data = data

        # define a layout
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        # define a graphics window, to which a viewbox and image are added
        self.graphicsView = pg.GraphicsWindow()
        self.viewbox = self.graphicsView.addViewBox(lockAspect=1)  # aspect rat
        self.image = pg.ImageItem()
        self.image.setImage(data[:, 0, :])
        self.viewbox.addItem(self.image)
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 4, 2)

        # define a slider
        self.horizontalSlider = QtGui.QSlider(self)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.setObjectName("horizontalSlider")
        # set minimum and maximum of slider
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(self.data.shape[1]-1)
        self.gridLayout.addWidget(self.horizontalSlider, 4, 0, 1, 2)

        # make the slider reactive to changes
        self.horizontalSlider.sliderMoved.connect(self.sliderMoved)

    def sliderMoved(self, val):
        self.val = val
        try:
            self.image.setImage(self.data[:, self.val, :])
        except IndexError:
            print "Error: No image at index", self.val

# %% render
app = QtGui.QApplication([])
mV = morphViewer()
mV.show()
mV.raise_()
app.exec_()
