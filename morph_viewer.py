#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 21 11:48:19 2017

@author: Marian
"""

import os
import numpy as np
from nibabel import load, save, Nifti1Image
from pyqtgraph.Qt import QtGui
from button_functions_functions import (updateOpen, updateClose, updateSave,
                                        setEverySecVoxel, undoEverySecVoxel)
import pyqtgraph as pg


# %% set parameters

# provide string to nii data
strPathData = '/home/marian/Documents/Testing/testMorphViewer/testIma.nii.gz'


# %% create window with two ImageView widgets

# Always start by initializing Qt (only once per application)
app = QtGui.QApplication([])

# define main windows
win = QtGui.QMainWindow()
win.resize(800, 800)  # set main window size
win.setWindowTitle('Morph Viewer')  # set main window title

# Define a top-level widget to hold everything
cw = QtGui.QWidget()
win.setCentralWidget(cw)

# Create a grid layout to manage the widgets size and position
l = QtGui.QGridLayout()
cw.setLayout(l)


# %% import data

# load data
nii = load(strPathData)
basename = nii.get_filename().split(os.extsep, 1)[0]
dirname = os.path.dirname(nii.get_filename())

data = nii.get_data()
# show smallest axis first
data = np.transpose(data, np.argsort(data.shape))

# %% arrange graph

# define image of the nii data with pyqtgraph
imv1 = pg.image(data)
# add the image widget to the layout in its proper positions
l.addWidget(imv1, 0, 0)

# create a push button widget
btn1 = QtGui.QPushButton('Open')
btn2 = QtGui.QPushButton('Close')
btn3 = QtGui.QPushButton('DiverseVoxels')
btn4 = QtGui.QPushButton('BinarizeVoxels')
btn5 = QtGui.QPushButton('Save')

# Add button widgets to the layout in their proper positions
l.addWidget(btn1, 1, 0)
l.addWidget(btn2, 2, 0)
l.addWidget(btn3, 3, 0)
l.addWidget(btn4, 4, 0)
l.addWidget(btn5, 5, 0)

# define what the buttons should do when clicked
# check for more options:
# https://www.tutorialspoint.com/pyqt/pyqt_qpushbutton_widget.htm
btn1.clicked.connect(updateOpen)
btn2.clicked.connect(updateClose)
btn3.clicked.connect(setEverySecVoxel)
btn4.clicked.connect(undoEverySecVoxel)
btn5.clicked.connect(updateSave)


# %%
# Display the widget as a new window
win.show()

# Start the Qt event loop
app.exec_()
