# -*- coding: utf-8 -*-

import os
import pyqtgraph as pg
from PyQt4 import QtCore, QtGui
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

    def __init__(self, inIma, parent=None, name="morphViewer"):
        super(morphViewer, self).__init__(parent)

        # define the data
        self.data = inIma
        # define data type
        self.datatype = self.data.dtype
        # set initial window size
        self.resize(800, 800)
        # set initial slider value
        self.val = int((self.data.shape[-1]-1)/2.)
        # set initial cycle view value
        self.cycleCount = 0

        # define a layout
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        # define a graphics window, to which a viewbox and image are added
        self.graphicsView = pg.GraphicsWindow()
        self.viewbox = self.graphicsView.addViewBox(lockAspect=1)  # aspect rat
        self.image = pg.ImageItem()
        self.image.setImage(self.data[..., self.val])
        self.viewbox.addItem(self.image)
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 4, 2)

        # define all the buttons
        self.Erode = QtGui.QPushButton("Erode")
        self.gridLayout.addWidget(self.Erode, 0, 2, 1, 1)

        self.Dilate = QtGui.QPushButton("Dilate")
        self.gridLayout.addWidget(self.Dilate, 1, 2, 1, 1)

        self.Cluster = QtGui.QPushButton("Cluster")
        self.gridLayout.addWidget(self.Cluster, 2, 2, 1, 1)

        self.Cycle = QtGui.QPushButton("Cycle")
        self.gridLayout.addWidget(self.Cycle, 5, 0, 1, 1)

        self.Rotate = QtGui.QPushButton("Rotate")
        self.gridLayout.addWidget(self.Rotate, 5, 1, 1, 1)

        self.Reset = QtGui.QPushButton("Reset")
        self.gridLayout.addWidget(self.Reset, 4, 2, 1, 1)

        self.Save = QtGui.QPushButton("Save")
        self.gridLayout.addWidget(self.Save, 5, 2, 1, 1)

        # define a slider
        self.horizontalSlider = QtGui.QSlider(self)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.setObjectName("horizontalSlider")
        # set minimum, maximum and starting value of slider
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(self.data.shape[-1]-1)
        self.horizontalSlider.setValue(self.val)
        self.horizontalSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(5)
        self.gridLayout.addWidget(self.horizontalSlider, 4, 0, 1, 2)

        # make the slider reactive to changes
        self.horizontalSlider.sliderMoved.connect(self.sliderMoved)
        # make buttons reactive
        self.Erode.clicked.connect(self.updateEro)
        self.Dilate.clicked.connect(self.updateDil)
        self.Cluster.clicked.connect(self.updateCluster)
        self.Cycle.clicked.connect(self.updateCycle)
        self.Rotate.clicked.connect(self.updateRotate)
        self.Reset.clicked.connect(self.updateReset)
        self.Save.clicked.connect(self.updateSave)

    def sliderMoved(self, val):
        self.val = val
        try:
            self.image.setImage(self.data[..., self.val])
        except IndexError:
            print("Error: No image at index", self.val)

    def updateEro(self):
        # perform erode
        self.data = morphology.binary_erosion(self.data, iterations=1)
        # convert to original data type
        self.data = self.data.astype(self.datatype)
        # update image of nii data
        self.image.setImage(self.data[..., self.val])

    def updateDil(self):
        # perform dilate
        self.data = morphology.binary_dilation(self.data, iterations=1)
        # convert to original data type
        self.data = self.data.astype(self.datatype)
        # update image of nii data
        self.image.setImage(self.data[..., self.val])

    def updateSave(self):
        # put the permuted indices back to their original format
        cycBackPerm = (self.cycleCount, (self.cycleCount+1) % 3,
                       (self.cycleCount+2) % 3)
        # create copy for export, which can be transposed back
        outData = np.copy(self.data)
        outData = np.transpose(outData, cycBackPerm)
        # prepare saving as nifti
        out = Nifti1Image(outData, header=nii.header, affine=nii.affine)
        # get new flex file name and check for overwriting
        self.nrExports = 0
        self.flexfilename = '_morph_' + str(self.nrExports) + '.nii.gz'
        while os.path.isfile(basename + self.flexfilename):
            self.nrExports += 1
            self.flexfilename = '_labels_' + str(self.nrExports) + '.nii.gz'
        save(out, basename + self.flexfilename)
        # save as nii
        print("successfully exported morph image as: \n" +
              basename + self.flexfilename)

    def updateCluster(self):
        # perform cluster thresholding
        print("Not implemented")

    def updateReset(self):
        # reset layout to initial state
        print("Not implemented")

    def updateCycle(self):
        # cycle through different image views
        """Cycle through views."""
        # take count of the cycles
        self.cycleCount = (self.cycleCount + 1) % 3
        # transpose data
        self.data = np.transpose(self.data, (2, 0, 1))
        # transpose ima2volHistMap
        self.image.setImage(self.data[..., self.val])
        # updates slider
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setMaximum(self.data.shape[-1]-1)

    def updateRotate(self):
        # rotate the image view
        print("Not implemented")

# %% render
app = QtGui.QApplication([])
mV = morphViewer(data)
mV.show()
mV.raise_()
app.exec_()
