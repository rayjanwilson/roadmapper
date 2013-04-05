#!/usr/bin/env python

import numpy as np
import scipy
import scipy.fftpack
from boomslang import Line, Scatter, Plot, PlotLayout

profile1 = np.genfromtxt("./assets/profile1.txt")
x = profile1[:,0]
surf = profile1[:,1]
surfGradient = np.gradient(surf)

FFT = scipy.fft(surf)
freqs = scipy.fftpack.fftfreq(surf.size, x[1]-x[0])

lowPassFilter = FFT[:]
for i in range(len(lowPassFilter)):
    if i>=25:lowPassFilter[i]=0

surfFiltered = scipy.ifft(lowPassFilter)
surfFilteredGradient = np.gradient(surfFiltered)
surfSeconOrderGradient = np.gradient(surfFilteredGradient)

### Plotting
scatter = Scatter()
scatter.xValues = x
scatter.yValues = surf
scatter.markerSize = 1

scatterPlot = Plot()
scatterPlot.add(scatter)
scatterPlot.xLabel = "X Data"
scatterPlot.yLabel = "Height"
scatterPlot.title = "Surface (raw)"

layout = PlotLayout()
layout.addPlot(scatterPlot)
#layout.plot()
layout.save("profile1.png")

# now plot the gradient
scatter.yValues = surfGradient
scatterPlot.yLabel = "dHeight/dX"
scatterPlot.title = "Surface - Gradient"

layout = PlotLayout()
layout.addPlot(scatterPlot)
#layout.plot()
layout.save("profile1_gradient.png")

#now plot the fft of the surface
line = Line()
line.xValues = freqs
line.yValues = abs(FFT)

linePlot = Plot()
linePlot.add(line)
linePlot.xLimits = (0, .5)
linePlot.xLabel = "Freqs [Hz]"
linePlot.yLabel = "Amplitude"
linePlot.title = "Surface - FFT (zoomed)"

layout = PlotLayout()
layout.addPlot(linePlot)
#layout.plot()
layout.save("profile1_fft.png")
#pylab.subplot(212)
#pylab.plot(freqs,20*scipy.log10(FFT),'x')
#pylab.show()

# plot the filtered surface with the gradient
scatter1 = Scatter()
scatter1.xValues = x
scatter1.yValues = surfFiltered
scatter1.markerSize = 1
scatter1.label = "Surface"
scatter1.color = "black"

scatter2 = Scatter()
scatter2.xValues = x
scatter2.yValues = surfFilteredGradient
scatter2.label = "1st Derivative"
scatter2.markerSize = 1
scatter2.color = "green"

scatterPlot = Plot()
scatterPlot.add(scatter1)
scatterPlot.add(scatter2)

scatterPlot.xLabel = "Distance Along Cross Section"
scatterPlot.yLabel = "Surface Height"
scatterPlot.setTwinX("1st Derivative", 1)
scatterPlot.title = "Surface (filtered)"
scatterPlot.hasLegend()

layout = PlotLayout()
layout.addPlot(scatterPlot)
layout.plot()
layout.save("profile1_filtered.png")


# now plot the second order gradient of filtered surface
#scatter.yValues = surfSeconOrderGradient
#scatterPlot.yLabel = "dHeight^2/dX^2"
#scatterPlot.title = "Surface - 2nd Gradient (filtered)"

#layout = PlotLayout()
#layout.addPlot(scatterPlot)
#layout.plot()
#layout.save("profile1_so_gradient_filtered.png")