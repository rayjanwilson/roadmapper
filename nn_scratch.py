#!/usr/bin/env python

import numpy as np
from pybrain.tools.shortcuts import buildNetwork
#from boomslang import Line, Scatter, Plot, PlotLayout

profile1 = np.genfromtxt("./assets/profile3.txt")
x = profile1[:, 0]
surf = profile1[:, 1]

net = buildNetwork(2, 3, 1)
net.activate([2, 1])
