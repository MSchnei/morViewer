# Morphology Viewer

[WIP] The aim is to provide an easy way of visualizing basic morphology operations
such as erosion and dilation using the excellent pyqt graph interface.

<img src="morphViewer.png" width=420 align="center" />

## Core dependencies
[**Python 3.5**](https://www.python.org/download/releases/3.5/)

| Package                                   | Tested version |
|-------------------------------------------|----------------|
| [NumPy](http://www.numpy.org/)            | 1.14.1         |
| [Scipy](https://www.scipy.org/)           | 1.0.0          |
| [NiBabel](http://nipy.org/nibabel/)       | 2.2.1          |
| [Pyqtgraph](http://www.pyqtgraph.org/)    | 0.10.0         |
| [scikit-image](http://scikit-image.org)   | 0.13.1         |
| [pyqt](https://en.wikipedia.org/wiki/PyQt)| 4.11.4         |

## Installation & Quick Start

- _(Optional but recommended)_ Create a virtual environment:
```
conda create --name envMorphViewer python=3.5
source activate envMorphViewer
conda install pip
```
- Install dependencies:
```
pip install numpy scipy nibabel
conda install -c anaconda pyqtgraph=0.10.0
conda install -c anaconda scikit-image
conda install pyqt=4
```
- _(Optional)_ Install pyOpenGL:
```
pip install PyOpenGL PyOpenGL_accelerate
```
- Clone MorpView repository:
```
git clone https://github.com/MSchnei/morphViewer.git
```
