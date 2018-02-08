#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 16:47:00 2018

@author: marian
"""

import numpy as np
from nibabel import save, Nifti1Image
from scipy.ndimage import morphology, generate_binary_structure

# %% define functions for updating

def updateOpen():
    global data, imv1
    # morphology structure
    struct = generate_binary_structure(3, 1)
    # perform opening
    data = morphology.binary_erosion(data, structure=struct, iterations=1)
    data = morphology.binary_dilation(data, structure=struct, iterations=1)
    # update image of nii data
    imv1.setImage(data)


def updateClose():
    global data, imv1
    # morphology structure
    struct = generate_binary_structure(3, 1)
    # perform closing
    data = morphology.binary_dilation(data, structure=struct, iterations=1)
    data = morphology.binary_erosion(data, structure=struct, iterations=1)
    # update image of nii data
    imv1.setImage(data)


def updateSave():
    # save as nifti
    out = Nifti1Image(data, header=nii.header, affine=nii.affine)
    save(out, basename + "_morph.nii.gz")
    print "data saved as: " + basename + "_morph.nii.gz"


def setEverySecVoxel():
    global data, imv1
    # identify voxels greater than 0
    boolMask = np.greater(data, 0)
    # set every second voxel to 50 and every other to 100
    process = data[boolMask]
    process[::2] = 100
    process[1::2] = 50
    data[boolMask] = process
    # update image of nii data
    imv1.setImage(data)


def undoEverySecVoxel():
    global data, imv1
    # identify voxels greater than 0
    boolMask = np.greater(data, 0)
    # set every voxel greater than 0 to 1
    data[boolMask] = 1
    # update image of nii data
    imv1.setImage(data)