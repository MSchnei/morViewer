# -*- coding: utf-8 -*-
"""Test QT  designer design connected with some simpe pyqtgraph widgets."""

import sys
import numpy as np
import pyqtgraph as pg
from design import Ui_MainWindow
from pyqtgraph.Qt import QtCore, QtGui
from nibabel import load

APP = QtGui.QApplication(sys.argv)
WIN = QtGui.QMainWindow()
UI = Ui_MainWindow()
UI.setupUi(WIN)
WIN.show()
# sys.exit(APP.exec_())

# Get MRI DATA
NII = load('/home/faruk/gdrive/Segmentator/data/amaia/T1w.nii.gz')
DATA = NII.get_data()

# Interface related
ROI = pg.LineSegmentROI([[10, 64], [120, 64]], pen='r')  # slicer line
IMV_1 = pg.ImageView()  # upper image pane
IMV_2 = pg.ImageView()  # lower image pane


def window_with_2_images():
    """Create window with two ImageView widgets procedure."""
    global APP, WIN, ROI, IMV_1, IMV_2, DATA

    # Window design
    layout = UI.imgGridLayout
    layout.addWidget(IMV_1, 0, 0)
    layout.addWidget(IMV_2, 0, 1)
    IMV_1.addItem(ROI)

    # Set the DATA images
    IMV_1.setImage(DATA)
    tr_min, tr_max = np.percentile(DATA, [2, 98])  # truncation points
    IMV_1.setHistogramRange(tr_min, tr_max)
    IMV_1.setLevels(tr_min, tr_max)

    WIN.show()


def update():
    """Image update procedure."""
    global DATA, IMV_1, IMV_2
    data_2 = ROI.getArrayRegion(DATA, IMV_1.imageItem, axes=(1, 2))
    IMV_2.setImage(data_2)


# update when the user interacts with slicer line
ROI.sigRegionChanged.connect(update)

# Display the DATA
window_with_2_images()
update()

# Start Qt event loop unless running in interactive mode.
if __name__ == '__main__':
    import sys
    if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()
