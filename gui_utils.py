#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 22:43:38 2018

@author: Marian
"""

import os
import numpy as np
import pyqtgraph as pg
from PyQt4 import QtCore, QtGui
from nibabel import save, Nifti1Image, Nifti1Header
from scipy.ndimage import morphology
from skimage.measure import label

class morphViewer(QtGui.QWidget):

    def __init__(self, inIma, basename="morphIma", header=None, affine=None,
                 parent=None, name="morphViewer"):
        super(morphViewer, self).__init__(parent)

        # define the data
        self.data = inIma 
        # make a copy for reset
        self.orig_data = np.copy(self.data)
        # define data type
        self.datatype = self.data.dtype
        # set initial window size
        self.resize(800, 800)
        # set initial slider value
        self.val = int((self.data.shape[-1]-1)/2.)
        # set initial checkbpx value
        self.checkb_val = False
        # set initial connectivity value
        self.cnntvty_val = 2
        # set cluster size value
        self.c_size_val = 26
        # set intial browser indices
        self.browser_ind = np.array([0, 0, 0])
        # set initial tranpose counter
        self.trnspCount = np.array([0, 1, 2])
        # set initial flip counter
        self.flpCount = np.array([1, 1, 1])
        # set affine
        if affine is None:
            self.affine = np.identity(4)
        else:
            self.affine = affine
        # set header
        if header is None:
            self.header = Nifti1Header()
        else:
            self.header = header
        # set basename
        self.basename = basename

        # define a grid layout
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")

        # define a horizontal layout for cluster
        self.horizontalLayout_cluster = QtGui.QHBoxLayout()
        self.gridLayout.addLayout(self.horizontalLayout_cluster, 5, 2, 1, 1)

        # define a horizontal layout for region growing
        self.horizontalLayout_grow = QtGui.QHBoxLayout()
        self.gridLayout.addLayout(self.horizontalLayout_grow, 4, 2, 1, 1)

        # define a horizontal layout for browser
        self.horizontalLayout_browser = QtGui.QHBoxLayout()
        self.gridLayout.addLayout(self.horizontalLayout_browser, 16, 2, 1, 1)

        # define a graphics window, to which a viewbox and image are added
        self.graphicsView = pg.GraphicsWindow()
        self.viewbox = self.graphicsView.addViewBox(lockAspect=1)  # aspect rat
        self.image = pg.ImageItem(border=(205, 92, 92))
        self.image.setImage(self.data[..., self.val])
        self.viewbox.addItem(self.image)
        self.viewbox.setMenuEnabled(False)
        self.gridLayout.addWidget(self.graphicsView, 0, 0, 14, 2)

        # define all the buttons
        self.Erode = QtGui.QPushButton("Erode")
        self.gridLayout.addWidget(self.Erode, 0, 2, 1, 1)

        self.Dilate = QtGui.QPushButton("Dilate")
        self.gridLayout.addWidget(self.Dilate, 1, 2, 1, 1)

        self.Black_tophat = QtGui.QPushButton("Black tophat")
        self.gridLayout.addWidget(self.Black_tophat, 3, 2, 1, 1)
        
        self.White_tophat = QtGui.QPushButton("White tophat")
        self.gridLayout.addWidget(self.White_tophat, 2, 2, 1, 1)
        
        self.Cycle = QtGui.QPushButton("Cycle")
        self.gridLayout.addWidget(self.Cycle, 16, 0, 1, 1)

        self.Rotate = QtGui.QPushButton("Rotate")
        self.gridLayout.addWidget(self.Rotate, 16, 1, 1, 1)

        self.Reset = QtGui.QPushButton("Reset")
        self.gridLayout.addWidget(self.Reset, 17, 2, 1, 1)

        self.Open = QtGui.QPushButton("Open")
        self.gridLayout.addWidget(self.Open, 18, 2, 1, 1)

        self.Save = QtGui.QPushButton("Save")
        self.gridLayout.addWidget(self.Save, 19, 2, 1, 1)

        # define check box fo manual segmentation
        self.Manual = QtGui.QCheckBox("Manual segmentation")
        self.gridLayout.addWidget(self.Manual, 14, 2, 1, 1)

        # define a horizontal slider
        self.horizontalSlider = QtGui.QSlider(self)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.setObjectName("horizontalSlider")
        
        # set minimum, maximum and starting value of slider
        self.horizontalSlider.setMinimum(0)
        self.horizontalSlider.setValue(self.val)
        self.horizontalSlider.setMaximum(self.data.shape[-1]-1)
        self.horizontalSlider.setTickPosition(QtGui.QSlider.TicksBelow)
        self.horizontalSlider.setTickInterval(5)
        self.gridLayout.addWidget(self.horizontalSlider, 14, 0, 1, 2)

        # define list widget for listing nii files
        self.File_names = QtGui.QListWidget(self)
        self.File_names.addItem(self.basename)
        self.gridLayout.addWidget(self.File_names, 17, 0, 3, 2)

        # define a vertical spacer
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum,
                                       QtGui.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem, 6, 2, 8, 1)

        # define spin boxes and push button for cluster
        self.cnntvty = QtGui.QSpinBox(self)
        self.cnntvty.setMinimum(1)
        self.cnntvty.setValue(self.cnntvty_val)
        self.cnntvty.setMaximum(len(self.data.shape))
        self.horizontalLayout_cluster.addWidget(self.cnntvty)
        
        self.c_size = QtGui.QSpinBox(self)
        self.c_size.setMinimum(1)
        self.c_size.setValue(self.c_size_val)
        self.c_size.setMaximum(100)
        self.horizontalLayout_cluster.addWidget(self.c_size)
        
        self.Cluster = QtGui.QPushButton("Cluster")
        self.horizontalLayout_cluster.addWidget(self.Cluster)

        # define labels and buttons for region growing
        self.Seed = QtGui.QLabel("Seed:")
        self.Seed.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_grow.addWidget(self.Seed)

        self.Coordns = QtGui.QLabel("X, Y, Z")
        self.Coordns.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_grow.addWidget(self.Coordns)

        self.Grow = QtGui.QPushButton("Grow")
        self.horizontalLayout_grow.addWidget(self.Grow)

        # define spin boxes for browser
        self.cursorBrowserX = QtGui.QSpinBox(self)
        self.cursorBrowserX.setMinimum(0)
        self.cursorBrowserX.setValue(self.browser_ind[0])
        self.cursorBrowserX.setMaximum(self.data.shape[0]-1)
        self.horizontalLayout_browser.addWidget(self.cursorBrowserX)
        
        self.cursorBrowserY = QtGui.QSpinBox(self)
        self.cursorBrowserY.setMinimum(0)
        self.cursorBrowserY.setValue(self.browser_ind[1])
        self.cursorBrowserY.setMaximum(self.data.shape[1]-1)
        self.horizontalLayout_browser.addWidget(self.cursorBrowserY)
        
        self.cursorBrowserZ = QtGui.QSpinBox(self)
        self.cursorBrowserZ.setMinimum(0)
        self.cursorBrowserZ.setValue(self.browser_ind[2])
        self.cursorBrowserZ.setMaximum(self.data.shape[2]-1)
        self.horizontalLayout_browser.addWidget(self.cursorBrowserZ)

        # make the slider reactive to changes
        self.horizontalSlider.sliderMoved.connect(self.sliderMoved)

        # make the spin boxes reactive to changes
        self.cursorBrowserX.valueChanged.connect(self.updateBrowserX)
        self.cursorBrowserY.valueChanged.connect(self.updateBrowserY)
        self.cursorBrowserZ.valueChanged.connect(self.updateBrowserZ)
        self.cnntvty.valueChanged.connect(self.updateCnntvty)
        self.c_size.valueChanged.connect(self.updateCsize)

        # make checkbox resposive to change
        self.Manual.stateChanged.connect(self.updateManual)

        # make buttons reactive
        self.Erode.clicked.connect(self.updateEro)
        self.Dilate.clicked.connect(self.updateDil)
        self.Black_tophat.clicked.connect(self.updateBlack_tophat)
        self.White_tophat.clicked.connect(self.updateWhite_tophat)
        self.Grow.clicked.connect(self.updateGrow)
        self.Cluster.clicked.connect(self.updateCluster)
        self.Cycle.clicked.connect(self.updateCycle)
        self.Rotate.clicked.connect(self.updateRotate)
        self.Open.clicked.connect(self.updateOpen)
        self.Reset.clicked.connect(self.updateReset)
        self.Save.clicked.connect(self.updateSave)

    def updatePanels(self, update_ima=True, update_slider=False):
        """Update viewer panels."""
        if update_slider:
            # updates slider
            self.horizontalSlider.setMinimum(0)
            self.horizontalSlider.setMaximum(self.data.shape[-1]-1)
            self.val = int((self.val/self.data.shape[0]) * self.data.shape[-1])
            self.horizontalSlider.setValue(self.val)
        if update_ima:
            # update image data
            self.image.setImage(self.data[..., self.val])

    def mouseClicked(self, evt):
        """Defines actions when mouse button is clicked."""
        evt = evt[0]
        pos = evt.scenePos()
        if self.viewbox.sceneBoundingRect().contains(pos):
            mousePoint = self.viewbox.mapSceneToView(pos)
            if self.checkb_val:
            # manual segmentation mode
                if evt.button() == 1:
                    # add pixel
                    self.data[int(mousePoint.x()), int(mousePoint.y()),
                              self.val] = 1
                    self.viewbox.setOpacity(0.9)
                elif evt.button() == 2:
                    # delete pixel
                    self.data[int(mousePoint.x()), int(mousePoint.y()),
                              self.val] = 0
                    self.viewbox.setOpacity(0.1)
            else:
            # browser mode
                # update browser values
                self.browser_ind[0] = int(mousePoint.x())
                self.browser_ind[1] = int(mousePoint.y())
                self.browser_ind[2] = self.val
                # update spin
                self.cursorBrowserX.setValue(self.browser_ind[0])
                self.cursorBrowserY.setValue(self.browser_ind[1])
                self.cursorBrowserZ.setValue(self.browser_ind[2])
            # update the panels
            self.updatePanels(update_ima=True, update_slider=False)

    def sliderMoved(self, val):
        """Defines actions when slider is moved."""
        self.val = val
        try:
            self.updatePanels(update_ima=True, update_slider=False)
        except IndexError:
            print("Error: No image at index", self.val)

    def updateEro(self):
        """Defines actions when Erode button is pressed."""
        # perform erode
        self.data = morphology.binary_erosion(self.data, iterations=1)
        # convert to original data type
        self.data = self.data.astype(self.datatype)
        # update image of nii data
        self.updatePanels(update_ima=True, update_slider=False)

    def updateDil(self):
        """Defines actions when Dilate button is pressed."""
        # perform dilate
        self.data = morphology.binary_dilation(self.data, iterations=1)
        # convert to original data type
        self.data = self.data.astype(self.datatype)
        # update image of nii data
        self.updatePanels(update_ima=True, update_slider=False)

    def updateBlack_tophat(self):
        """Defines actions when Black_tophat button is pressed."""
        print("Not implemented yet")

    def updateWhite_tophat(self):
        """Defines actions when White_tophat button is pressed."""
        print("Not implemented yet")

    def updateCluster(self):
        """Defines actions when Cluster button is pressed."""
        # perform cluster thresholding
        self.data = label(self.data, connectivity=self.cnntvty_val)
        labels, counts = np.unique(self.data, return_counts=True)
        print(str(labels.size) + ' clusters are found.')
        print('Applying connected clusters threshold with \n cluster size ' +
              str(self.c_size_val) + ' and \n connectivity ' +
              str(self.cnntvty_val))
        for i, (i_label, i_count) in enumerate(zip(labels[1:], counts[1:])):
            if i_count < self.c_size_val:
                self.data[self.data == i_label] = 0
        self.data[self.data != 0] = 1
        # return with old data type
        self.data = self.data.astype(self.data.dtype)
        # update image of nii data
        self.updatePanels(update_ima=True, update_slider=False)
        # print finish message
        print('Cluster thresholding done.')

    def updateGrow(self):
        """Defines actions when Grow button is pressed."""
        print("Not implemented yet")

    def updateOpen(self):
        """Defines actions when Open button is pressed."""
        newfile = QtGui.QFileDialog.getOpenFileName()
        self.File_names.addItem(newfile)

    def updateReset(self, inIma):
        """Defines actions when Reset button is pressed."""
        # reset the data
        self.data = self.orig_data
        # reset data type
        self.datatype = self.data.dtype
        # reset initial checkbpx value
        self.checkb_val = False
        self.Manual.setChecked(self.checkb_val)
        # reset initial connectivity value
        self.cnntvty_val = 2
        self.cnntvty.setMinimum(1)
        self.cnntvty.setValue(self.cnntvty_val)
        self.cnntvty.setMaximum(len(self.data.shape))
        # reset cluster size value
        self.c_size_val = 26
        self.c_size.setMinimum(1)
        self.c_size.setValue(self.c_size_val)
        self.c_size.setMaximum(100)
        # reset browser indices
        self.browser_ind = np.array([0, 0, 0])
        # reset initial transpose counter
        self.trnspCount = np.array([0, 1, 2])
        # reset initial flip counter
        self.flpCount = np.array([1, 1, 1])
        # reset nr of exports
        self.nrExports = 0
        # reset the image
        self.updatePanels(update_ima=True, update_slider=True)

    def updateRotate(self):
        """Defines actions when Rotate button is pressed."""
        # rotate the data by 90 degrees
        self.data = np.transpose(self.data, (1, 0, 2))
        self.data = self.data[::-1, ::1, ::1]
        # indicate that axes 0 and 1 were transposed
        self.trnspCount = self.trnspCount[[1, 0, 2]]
        self.flpCount = self.flpCount[[1, 0, 2]]
        # indicate that axis was flipped
        self.flpCount = self.flpCount * np.array([-1, 1, 1])
        # update the panels
        self.updatePanels(update_ima=True, update_slider=False)

    def updateCycle(self):
        """Cycle through different image views."""
        # transpose data
        self.data = np.transpose(self.data, (2, 0, 1))
        # indicate that axes 0 and 1 were transposed
        self.trnspCount = self.trnspCount[[2, 0, 1]]
        self.flpCount = self.flpCount[[2, 0, 1]]
        # update image of nii data
        self.updatePanels(update_ima=True, update_slider=True)

    def updateManual(self):
        """Defines actions when Manual check box is changed."""
        self.checkb_val = self.Manual.isChecked()

    def updateCnntvty(self):
        """Defines actions when cnntvty scroll bar is changed."""
        self.cnntvty_val = self.cnntvty.value()

    def updateCsize(self):
        """Defines actions when cluster size scroll bar is changed."""
        self.c_size_val = self.c_size.value()

    def updateBrowserX(self):
        """Defines actions when BrowserX scroll bar is changed."""
        self.browser_ind[0] = self.cursorBrowserX.value()

    def updateBrowserY(self):
        """Defines actions when BrowserY scroll bar is changed."""
        self.browser_ind[1] = self.cursorBrowserY.value()

    def updateBrowserZ(self):
        """Defines actions when BrowserZ scroll bar is changed."""
        self.browser_ind[2] = self.cursorBrowserZ.value()

    def updateSave(self):
        """Defines actions when Save button is pressed."""
        # create copy for export, which can be transposed back
        outData = np.copy(self.data)
        # re-flip data
        outData = outData[::self.flpCount[0], ::self.flpCount[1],
                          ::self.flpCount[2]]
        # re-tranpose data
        outData = np.transpose(outData, np.argsort(self.trnspCount))
        # prepare saving as nifti
        out = Nifti1Image(outData, header=self.header, affine=self.affine)
        # get new flex file name and check for overwriting
        self.nrExports = 0
        self.flexfilename = '_morph_' + str(self.nrExports) + '.nii.gz'
        while os.path.isfile(self.basename + self.flexfilename):
            self.nrExports += 1
            self.flexfilename = '_morph_' + str(self.nrExports) + '.nii.gz'
        save(out, self.basename + self.flexfilename)
        # save as nii
        print("successfully exported morph image as: \n" +
              self.basename + self.flexfilename)
