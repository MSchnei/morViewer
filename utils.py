#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 22:21:42 2018

@author: Marian
"""


import os
from nibabel import load
import numpy as np


#strPathData1 = '/Users/Marian/gdrive/testIma.nii.gz'
#nii1 = load(strPathData1)
#basename = nii1.get_filename().split(os.extsep, 1)[0]
#dirname = os.path.dirname(nii1.get_filename())
#ima1 = nii1.get_data().astype('int8')
#
#strPathData2 = '/Users/Marian/gdrive/testIma_morph_0.nii.gz'
#
#nii2 = load(strPathData2)
#basename = nii2.get_filename().split(os.extsep, 1)[0]
#dirname = os.path.dirname(nii2.get_filename())
#ima2 = nii2.get_data().astype('int8')

def rtn_diff_vox(ima1, ima2, lstInd):
    """Calculate indices of voxels that were added or subtracted."""
    # get bool for values that are now included    
    now_incl = np.logical_and(ima1==0, ima2==1)
    # get bool for values that are now excluded
    now_excl = np.logical_and(ima1==1, ima2==0)
    # get non-zero indices for now included voxels
    ind_now_incl = np.flatnonzero(now_incl)
    # get non-zero indices for now excluded voxels    
    ind_now_excl = np.flatnonzero(now_excl)

    lstInd[0].append(ind_now_incl)
    lstInd[1].append(ind_now_excl)
    
    return lstInd    

def get_nbhd(pnt, checked, dims):
    """Get 6 voxel neighborhood."""
    nbhd = []

    if (pnt[0] > 0) and not checked[pnt[0]-1, pnt[1], pnt[2]]:
        nbhd.append((pnt[0]-1, pnt[1], pnt[2]))
    if (pnt[1] > 0) and not checked[pnt[0], pnt[1]-1, pnt[2]]:
        nbhd.append((pnt[0], pnt[1]-1, pnt[2]))
    if (pnt[2] > 0) and not checked[pnt[0], pnt[1], pnt[2]-1]:
        nbhd.append((pnt[0], pnt[1], pnt[2]-1))

    if (pnt[0] < dims[0]-1) and not checked[pnt[0]+1, pnt[1], pnt[2]]:
        nbhd.append((pnt[0]+1, pnt[1], pnt[2]))
    if (pnt[1] < dims[1]-1) and not checked[pnt[0], pnt[1]+1, pnt[2]]:
        nbhd.append((pnt[0], pnt[1]+1, pnt[2]))
    if (pnt[2] < dims[2]-1) and not checked[pnt[0], pnt[1], pnt[2]+1]:
        nbhd.append((pnt[0], pnt[1], pnt[2]+1))

    return nbhd

def grow_reg(data, seed):
    """
    data: ndarray, ndim=3
        3D volumetric data.
    
    seed: tuple, len=3
        Region growing starts from this point.
    -----
    source: http://notmatthancock.github.io/
    """
    reg = np.zeros(data.shape, dtype=np.int8)
    checked = np.zeros(data.shape, dtype=np.bool)
    
    # set region image to True for seed point
    reg[seed] = 1
    # set seed point checked
    checked[seed] = True
    # set neighborhood of seed point on list to be checked
    needs_check = get_nbhd(seed, checked, data.shape)

    while len(needs_check) > 0:
        pnt = needs_check.pop()

        # Its possible that the point was already checked and was
        # put in the needs_check stack multiple times.
        if checked[pnt]:
            continue
        if data[pnt] == 1:
            # set region image to True for point
            reg[pnt] = 1
            # set point checked
            checked[pnt] = True
            # set neighborhood of point on list to be checked
            needs_check += get_nbhd(pnt, checked, data.shape)

    return reg.astype('int8')