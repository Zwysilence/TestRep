"""This is a python3 GUI test"""
# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

N = 50
X = np.random.ranf(N)
Y = np.random.ranf(N)
COLOR = np.random.ranf(N)
AREA = np.pi * (15 * np.random.ranf(N))**2
plt.scatter(X, Y, s=AREA, c=COLOR, alpha=0.5)
plt.show()
