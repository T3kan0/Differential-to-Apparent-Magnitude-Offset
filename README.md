# Differential-to-Apparent-Magnitude-Offset
Tekano Mbonani

## System Docs 📃
A **Python** code for converting the differential magnitudes of astrophysical sources into apparent magntudes, using the apparent magnitudes of standard stars in the field-of-view of the image frames. Additionally, the code performs corrections on the apparent magnitudes from the Sloan (PanSTARR u'g'r') to the Johnson (BVRI) filters, using second order, colour dependent correction coeffients, i.e.,

$V - r = D_{0} + D_{1} \times \left( g - r \right) + D_{2} \times \left( g - r \right)^{2}$,

where $D_{i}$ are the correction coefficients, $V$ the Johnson target apparent magnitude, $r$ and $g$ are the Sloan target apparent magnitudes and, therefore, $(g - r)$ are the Sloan colour of the targets.
## Software Requirements 🔌
You will need to install the following software on your system in order to run/edit the Python script.
* Mac OS/ Ubuntu 18.04 OS
* Python 3.7
* Textedit/ IDE - spyder or jupyter-notebook
* Python libraries
  * Numpy
  * Matplotlib
  * Scipy
<p align="center">
  <img align="center" width="700" height="600" src="[](https://github.com/T3kan0/Differential-to-Apparent-Magnitude-Offset/blob/main/off_set_apparent.png)https://github.com/T3kan0/Differential-to-Apparent-Magnitude-Offset/blob/main/off_set_apparent.png">
</p>
