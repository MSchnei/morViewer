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
strPathData = '/Users/Marian/gdrive/testIma.nii.gz'

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

        # image item needs to be embedded in a view box, which in turn is
        # embedded in a graphics window in oder to be able to add it to layout
        self.win = pg.GraphicsWindow(size=(self.data.shape[0],
                                           self.data.shape[2]))
        self.viewbox = self.win.addViewBox()
        self.image = pg.ImageItem()
        self.viewbox.addItem(self.image)
        # add window (with viewbox, with image) to layout
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
#        self.win.fitInView(QtCore.QRectF, QtCore.Qt.KeepAspectRatio)

#        self.scene.sceneRect()

    def sliderMoved(self, val):
        print("Slider moved to:"), print(val)
        try:
            self.image.setImage(data[:, val, :])
        except IndexError:
            print("Error: No image at index"), print(val)

#    def resizeEvent(self, event):
#        # if the window is resized
#        super(Widget, self).resizeEvent(event)
#        # scale view object that embeds image to full screen
#        self.viewbox.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)

# %% render
app = QtGui.QApplication([])
w = Widget()
w.show()
w.raise_()
app.exec_()
