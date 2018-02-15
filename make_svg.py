#! /usr/bin/env python2.7
import matplotlib.pyplot as plt
import numpy as np
import scipy.misc
import tifffile

DOWNSAMPLE = 20  # determines the smoothing in pixels
METERS_PER_FOOT = .3048  # for conversion from feet to meters
ELEVATIONS = [-2000., -200., 0., 200., 2000.]  # elevations (in feet) that will become layers

im = tifffile.imread('./dem-item-147398/ngdc1_n38x75_w124x00_mhw_2010v1.tif')
im = np.flipud(im)
im = scipy.misc.imresize(im, 1./DOWNSAMPLE, interp='bilinear', mode='F')

thresholds = METERS_PER_FOOT * np.array(ELEVATIONS)

fig = plt.figure(figsize=(13, 9.75))
ax = fig.add_subplot(1, 1, 1)
conts = ax.contour(im, thresholds, origin='lower', cmap='winter', vmin=-100, vmax=100)

ax.axis('equal')
ax.set_ylim((0, 310))
ax.set_xlim((0, 370))
ax.set_xticks([])
ax.set_yticks([])
fig.savefig('map.svg', facecolor='none')