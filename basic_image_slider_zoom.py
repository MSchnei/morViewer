#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 19:49:03 2018

@author: marian
"""

import os
from nibabel import load, save, Nifti1Image
from PyQt4 import QtGui, QtCore
import sys
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


class ViewData(pg.GraphicsLayoutWidget):
    def __init__(self, parent=None):
        super(ViewData, self).__init__(parent)

#        layout = QtGui.QGridLayout()
#        w.setLayout(layout)
        
        # get the data
        self.data = data

        # add the image
        self.view = self.addViewBox()
        # lock the aspect ratio so pixels are always square
        self.view.setAspectLocked(True)
        # Create image item
        self.img = pg.ImageItem()
        self.view.addItem(self.img)

        # add slider
        self.slider = QtGui.QSlider(self)
        self.slider.setOrientation(QtCore.Qt.Horizontal)
        self.slider.setMinimum(0)
        self.slider.setMaximum(self.data.shape[1]-1)

        # set it to the center image, if you want.
        self.sliderMoved(int((self.data.shape[1]-1)/2.))
        self.slider.sliderMoved.connect(self.sliderMoved)

    def sliderMoved(self, val):
        try:
            self.img.setImage(data[:, val, :])
        except IndexError:
            print "Error: No image at index", val

#    def resizeEvent(self, event):
#        # if the window is resized
#        super(Widget, self).resizeEvent(event)
#        # scale view object that embeds image to full screen
#        self.view.fitInView(self.scene.sceneRect(), QtCore.Qt.KeepAspectRatio)

# %% render
app = QtGui.QApplication(sys.argv)
vd = ViewData()
vd.show()
app.exec_()
