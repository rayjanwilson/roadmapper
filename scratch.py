#!/usr/bin/env python

import numpy as np
import scipy
import scipy.fftpack
from boomslang import Line, Scatter, Plot, PlotLayout

profile1 = np.genfromtxt("./assets/profile1.txt")
x = profile1[:,0]
surf = profile1[:,1]
surfGradient = np.gradient(surf)

FFT = abs(scipy.fft(surf))
freqs = scipy.fftpack.fftfreq(surf.size, x[1]-x[0])

### Plotting
scatter = Scatter()
scatter.xValues = x
scatter.yValues = surf
scatter.markerSize = 1

scatterPlot = Plot()
scatterPlot.add(scatter)
scatterPlot.xLabel = "X Data"
scatterPlot.yLabel = "Height"
scatterPlot.title = "Profile 1"

layout = PlotLayout()
layout.addPlot(scatterPlot)
#layout.plot()
layout.save("profile1.png")

# now plot the gradient
scatter.yValues = surfGradient
scatterPlot.yLabel = "dHeight/dX"
scatterPlot.title = "Profile 1 - Gradient"

layout = PlotLayout()
layout.addPlot(scatterPlot)
#layout.plot()
layout.save("profile1_gradient.png")

#now plot the fft of the surface
line = Line()
line.xValues = freqs
line.yValues = FFT

linePlot = Plot()
linePlot.add(line)
linePlot.xLimits = (0, .5)
linePlot.xLabel = "freqs"
linePlot.yLabel = "Amplitude"
linePlot.title = "Profile 1 - FFT"

layout = PlotLayout()
layout.addPlot(linePlot)
layout.plot()
layout.save("profile1_fft.png")
#pylab.subplot(212)
#pylab.plot(freqs,20*scipy.log10(FFT),'x')
#pylab.show()