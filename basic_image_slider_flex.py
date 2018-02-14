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

# %% define widget

class Widget(QtGui.QWidget):

    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.resize(800, 800)
        self.layout = QtGui.QGridLayout(self)

        # define the data
        self.data = data

        self.win = pg.GraphicsWindow(title="Basic plotting examples")
        self.view = self.win.addViewBox()

        # image item needs to be embedded in a view, which in turn is embedded
        # in a scene in oder to be able to add it to layout
        self.image = pg.ImageItem()

        self.view.addItem(self.image)

        # add view (with scene, with image) to layout
        self.layout.addWidget(self.win, 0, 0)

        # add slider
        self.slider = QtGui.QSlider(self)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setMinimum(0)
        # max is the last index of the image list
        self.slider.setMaximum(self.data.shape[1]-1)
        self.layout.addWidget(self.slider, 1, 0)

        # set it to the center image, if you want.
        self.sliderMoved(int((self.data.shape[1]-1)/2.))
        self.slider.sliderMoved.connect(self.sliderMoved)

        # scale view object that embeds image to full screen
#        self.view.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)

    def sliderMoved(self, val):
        print "Slider moved to:", val
        try:
            self.image.setImage(data[:, val, :])
        except IndexError:
            print "Error: No image at index", val

    def resizeEvent(self, event):
        # if the window is resized
        super(Widget, self).resizeEvent(event)
        # scale view object that embeds image to full screen
        self.view.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)

# %% render
app = QtGui.QApplication([])
w = Widget()
w.show()
w.raise_()
app.exec_()
