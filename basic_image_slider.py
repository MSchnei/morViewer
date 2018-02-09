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

        # image item needs to be embedded in a view, which in turn is embedded
        # in a scene in oder to be able to add it to layout
        self.image = pg.ImageItem()
        self.scene = QtGui.QGraphicsScene(self)
        # add image item to scene
        self.scene.addItem(self.image)
        # add scene to view
        self.view = QtGui.QGraphicsView(self.scene)

        # add view to layout
        self.layout.addWidget(self.view, 0, 0)

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
        widthScale = np.floor(self.width() / self.scene.sceneRect().width())
        heightScale = np.floor(self.height() / self.scene.sceneRect().height())
        self.view.scale(widthScale, heightScale)

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
