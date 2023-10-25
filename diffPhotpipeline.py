#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  6 15:48:26 2019

@author: tekano
"""

import numpy as np
from matplotlib import pyplot as plt

comp_stars = '3C279_apparent.csv'##Standards
optical_phot = 'V_20310.phot'##Watcher


phot = np.loadtxt(optical_phot,
                  delimiter=',',
                  dtype=float)##Optical_data
apparent_comp_mag = np.loadtxt(comp_stars,
                     delimiter=',',
                     dtype=float)##Standards



offset = phot[:,3::2] - apparent_comp_mag[1:,3]

offset_avg = np.average(offset, axis = 1)

check = offset - offset_avg[:,None]

#
#
#


phot[:,1::2] = phot[:,1::2] - offset_avg[:, np.newaxis]

### R_filter calculations
Dr0_err = 0.0
Dr1_err = 0.002
Dr2_err = 0.002

### B_filter calculations
Db0_err = 0.001
Db1_err = 0.004
Db2_err = 0.003

### V_filter calculations
Dv0_err = 0.001
Dv1_err = 0.002
Dv2_err = 0.002

### I_filter calculations
#Di0_err = 0.0
#Di1_err = 0.002
#Di2_err = 0.002

phot[:,2::2] = np.sqrt((phot[:,2::2])**2 +
                     apparent_comp_mag[:,2]**2 + 
                     apparent_comp_mag[:,4]**2 +
                     apparent_comp_mag[:,6]**2 +
                     Dv0_err**2 +
                     Dv1_err**2 +
                     Dv2_err**2)


x,y = phot[:,1::].shape
#np.savetxt('3C279_V_offset.txt', 
#           phot, 
#           fmt = "%.5f ")


plt.errorbar(phot[:,0], phot[:,1], phot[:,2], label = "Target", fmt = ".", c = 'black')
plt.errorbar(phot[:,0], phot[:,3], phot[:,4], label = "Comp Star 1", fmt = ".", c = 'grey')
plt.errorbar(phot[:,0], phot[:,5], phot[:,6], label = "Comp Star 2", fmt = ".", c = 'red')
plt.errorbar(phot[:,0], phot[:,7], phot[:,8], label = "Comp Star 3", fmt = ".", c = 'yellow')
plt.errorbar(phot[:,0], phot[:,9], phot[:,10], label = "Comp Star 4", fmt = ".", c = 'purple')
plt.errorbar(phot[:,0], phot[:,11], phot[:,12], label = "Comp Star 5", fmt = ".", c = 'orange')
plt.errorbar(phot[:,0], phot[:,13], phot[:,14], label = "Comp Star 6", fmt = ".", c = 'pink')
plt.errorbar(phot[:,0], phot[:,15], phot[:,16], label = "Comp Star 7", fmt = ".", c = 'green' )
plt.title("target: Off-set magnitudes")
plt.xlabel("MJD")
plt.ylabel("Off-set intrumental \n Magnitudes")
plt.legend(loc=3)
plt.gca().invert_yaxis()
#plt.set_ylim(12, 25)
plt.show()

flx = np.power(10, (phot[:,1]/ - 2.5))
flx_err = (flx * np.power(10, phot[:,2] / 2.5) - flx)
print(flx, flx_err)
plt.errorbar(phot[:,0], flx, flx_err, label = 'Target', c = 'black', fmt = '.')
plt.title('target: Flux')
plt.xlabel('mjd')
plt.ylabel('Flux')
plt.legend(loc=1)
plt.ticklabel_format(style = 'sci', axis = 'y', scilimits = (0,0))
plt.show()



