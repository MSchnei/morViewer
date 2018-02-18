# -*- coding: utf-8 -*-

import os
import pyqtgraph as pg
from PyQt4 import QtCore, QtGui
from nibabel import load, save, Nifti1Image
from scipy.ndimage import morphology

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

        # set initial window size
        self.resize(800, 800)
        # set initial slider value
        self.val = 0

        # define the data
        self.data = data
        self.datatype = self.data.dtype

        # define a layout
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        # define a graphics window, to which a viewbox and image are added
        self.graphicsView = pg.GraphicsWindow()
        self.viewbox = self.graphicsView.addViewBox(lockAspect=1)  # aspect rat
        self.image = pg.ImageItem()
        self.image.setImage(self.data[:, self.val, :])
        self.viewbox.addItem(self.image)
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 4, 2)

        # define all the buttons
        self.Erode = QtGui.QPushButton("Erode")
        self.gridLayout.addWidget(self.Erode, 0, 2, 1, 1)

        self.Dilate = QtGui.QPushButton("Dilate")
        self.gridLayout.addWidget(self.Dilate, 1, 2, 1, 1)

        self.Save = QtGui.QPushButton("Save")
        self.gridLayout.addWidget(self.Save, 2, 2, 1, 1)

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
        # make buttons reactive
        self.Erode.clicked.connect(self.updateEro)
        self.Dilate.clicked.connect(self.updateDil)
        self.Save.clicked.connect(self.updateSave)

    def sliderMoved(self, val):
        self.val = val
        try:
            self.image.setImage(self.data[:, self.val, :])
        except IndexError:
            print("Error: No image at index", self.val)

    def updateEro(self):
        # perform erode
        self.data = morphology.binary_erosion(self.data, iterations=1)
        # convert to original data type
        self.data = self.data.astype(self.datatype)
        # update image of nii data
        self.image.setImage(self.data[:, self.val, :])

    def updateDil(self):
        # perform dilate
        self.data = morphology.binary_dilation(self.data, iterations=1)
        # convert to original data type
        self.data = self.data.astype(self.datatype)
        # update image of nii data
        self.image.setImage(self.data[:, self.val, :])

    def updateSave(self):
        # save as nifti
        out = Nifti1Image(self.data, header=nii.header, affine=nii.affine)
        save(out, basename + "_morph.nii.gz")
        print("data saved as: " + basename + "_morph.nii.gz")

# %% render
app = QtGui.QApplication([])
mV = morphViewer()
mV.show()
mV.raise_()
app.exec_()
