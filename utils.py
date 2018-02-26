#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 22:21:42 2018

@author: Marian
"""


import os
from nibabel import load
import numpy as np


strPathData1 = '/Users/Marian/gdrive/testIma.nii.gz'
nii1 = load(strPathData1)
basename = nii1.get_filename().split(os.extsep, 1)[0]
dirname = os.path.dirname(nii1.get_filename())
ima1 = nii1.get_data().astype('int8')

strPathData2 = '/Users/Marian/gdrive/testIma_morph_0.nii.gz'

nii2 = load(strPathData2)
basename = nii2.get_filename().split(os.extsep, 1)[0]
dirname = os.path.dirname(nii2.get_filename())
ima2 = nii2.get_data().astype('int8')


def rtnDiffVox(ima1, ima2, lstInd):
    """Calculate indices of voxels that were added or subtracted."""
    # get bool for values that are now included
    now_incl = np.logical_and(ima1==0, ima2==1).astype('int8')
    # get bool for values that are now excluded
    now_excl = np.logical_and(ima1==1, ima2==0).astype('int8')
    # get non-zero indices for now included voxels
    ind_now_incl = np.flatnonzero(now_incl)
    # get non-zero indices for now excluded voxels    
    ind_now_excl = np.flatnonzero(now_excl)
    
    lstInd[0].append(ind_now_incl)
    lstInd[1].append(ind_now_excl)
    
    return lstInd    
    