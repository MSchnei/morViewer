#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 19:49:03 2018

@author: marian
"""

import os
from nibabel import load, save, Nifti1Image
from PyQt4 import QtCore, QtGui
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

# %% define widget

class Widget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.resize(640, 480)
        self.layout = QtGui.QVBoxLayout(self)

        self.scene = QtGui.QGraphicsScene(self)
        self.view = QtGui.QGraphicsView(self.scene)
        self.layout.addWidget(self.view)

        self.image = pg.ImageItem()
        self.scene.addItem(self.image)
        self.view.centerOn(self.image)
        self.data = data

        self.slider = QtGui.QSlider(self)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setMinimum(0)
        # max is the last index of the image list
        self.slider.setMaximum(self.data.shape[1]-1)
        self.layout.addWidget(self.slider)

        # set it to the first image, if you want.
        self.sliderMoved(0)

        self.slider.sliderMoved.connect(self.sliderMoved)

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
