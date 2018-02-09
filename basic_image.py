# -*- coding: utf-8 -*-
"""
Demonstrates basic use of ImageItem to display image data inside a ViewBox.
"""

import os
from pyqtgraph.Qt import QtCore, QtGui
import numpy as np
import pyqtgraph as pg
from nibabel import load, save, Nifti1Image

# %% set parameters

# provide string to nii data
strPathData = '/home/marian/Documents/Testing/testMorphViewer/testIma.nii.gz'


# %% create window

# Always start by initializing Qt (only once per application)
app = QtGui.QApplication([])

# Create window with GraphicsView widget
win = pg.GraphicsLayoutWidget()
# add title
win.setWindowTitle('pyqtgraph example: ImageItem')

# define view
view = win.addViewBox()
# lock the aspect ratio so pixels are always square
view.setAspectLocked(True)


# Create image item
img = pg.ImageItem()

view.addItem(img)

# Set initial view bounds
view.setRange(QtCore.QRectF(0, 0, 600, 600))

# %% import data

# load data
nii = load(strPathData)
basename = nii.get_filename().split(os.extsep, 1)[0]
dirname = os.path.dirname(nii.get_filename())

data = nii.get_data()


# %%
i = 100
img.setImage(data[:, i, :])


# %%
# Display the widget as a new window
win.show()

# Start the Qt event loop
app.exec_()
