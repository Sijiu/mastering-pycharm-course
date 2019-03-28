#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: mxh @time:2019/3/28 14:28
"""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


fig = plt.figure(figsize=(6, 3))
ax = Axes3D(fig)

X = np.arange(-5, 5, 0.25)
Y = np.arange(-5, 5, 0.25)
X, Y = np.meshgrid(X, Y)
Z = -(X ** 2 + Y ** 2)

surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm, linewidth=0, antialiased=True)

fig.show()
