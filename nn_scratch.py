#!/usr/bin/env python

import numpy as np
#from pybrain.tools.shortcuts import buildNetwork
from pybrain.structure import RecurrentNetwork
from pybrain.structure import FullConnection
from pybrain.structure import LinearLayer, SigmoidLayer
from pybrain.datasets import SupervisedDataSet
from pybrain.supervised.trainers import BackpropTrainer
#from boomslang import Line, Scatter, Plot, PlotLayout

#profile1 = np.genfromtxt("./assets/profile3.txt")
#x = profile1[:, 0]
#surf = profile1[:, 1]

#net = buildNetwork(2, 3, 1)
#n = buildNetwork(2, 3, 1, bias=True)

# from http://en.wikibooks.org/wiki/Artificial_Neural_Networks/Neural_Network_Basics
no_hiddenLayer = 8
learningRate = 0.3
momentum = 0.05
tainingType = 1 #train by minimum error
minimumError = 0.01

n = RecurrentNetwork()

n.addInputModule(LinearLayer(2, name='in'))
n.addModule(SigmoidLayer(3, name='hidden'))
n.addOutputModule(LinearLayer(1, name='out'))
n.addConnection(FullConnection(n['in'], n['hidden'], name='c1'))
n.addConnection(FullConnection(n['hidden'], n['out'], name='c2'))

ds = SupervisedDataSet(2, 1)
ds.addSample((0, 0), (0,))
ds.addSample((0, 1), (1,))
ds.addSample((1, 0), (1,))
ds.addSample((1, 1), (0,))

#trainer = BackpropTrainer(n, ds)
#trainer.trainUntilConvergence()

n.sortModules()

print net.activate([0,1])
