# -*- coding: utf-8 -*-

import os
import pyqtgraph as pg
from nibabel import load
from PyQt4 import QtGui
from gui_utils import morphViewer

# %% set parameters

# provide string to nii data
strPathData = '/Users/Marian/gdrive/testIma.nii.gz'

# %% import data

nii = load(strPathData)
basename = nii.get_filename().split(os.extsep, 1)[0]
dirname = os.path.dirname(nii.get_filename())
data = nii.get_data().astype('int8')

# %% render

app = QtGui.QApplication([])
mV = morphViewer(data, basename=basename, affine=nii.affine, header=nii.header)
mV.show()

# make programm response to mouse clicks
proxy = pg.SignalProxy(mV.viewbox.scene().sigMouseClicked, rateLimit=60,
                       slot=mV.mouseClicked)
#mV.viewbox.scene().sigMouseClicked.connect(mV.mouseClicked)

mV.raise_()
app.exec_()
