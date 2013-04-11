#!/usr/bin/env python

import numpy as np
import scipy
import scipy.fftpack
from boomslang import Line, Scatter, Plot, PlotLayout

profile1 = np.genfromtxt("./assets/profile3.txt")
x = profile1[:, 0]
surf = profile1[:, 1]
surfGradient = np.gradient(surf)

FFT = scipy.fft(surf)
freqs = scipy.fftpack.fftfreq(surf.size, x[1]-x[0])

lowPassFilter = FFT[:]
for i in range(len(lowPassFilter)):
    if i >= 4:
        lowPassFilter[i] = 0

surfFilteredComplex = scipy.ifft(lowPassFilter)
surfFiltered = map(lambda x: abs(x), surfFilteredComplex)
surfFilteredGradient = np.gradient(surfFiltered)
surfSeconOrderGradient = np.gradient(surfFilteredGradient)

# find where gradient crosses zero
zero_crossings = np.where(np.diff(np.sign(surfFilteredGradient)))[0]
print zero_crossings
roadFeatures = np.zeros((len(zero_crossings), 2))
j = 0
for i in zero_crossings:
    xval = x[i]
    yval = surf[i]
    roadFeatures[j, 0] = xval
    roadFeatures[j, 1] = yval
    j = j + 1




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
scatter1.label = "Filtered Surface"
scatter1.color = "black"

scatter2 = Scatter()
scatter2.xValues = x
scatter2.yValues = surfFilteredGradient
scatter2.label = "1st Derivative"
scatter2.markerSize = 1
scatter2.color = "green"

scatter3 = Scatter()
scatter3.xValues = x
scatter3.yValues = surf
scatter3.label = "Original Surface"
scatter3.markerSize = 1
scatter3.color = "blue"

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

# plot the filtered surface with the original surface
scatter1 = Scatter()
scatter1.xValues = x
scatter1.yValues = surfFiltered
scatter1.markerSize = 1
scatter1.label = "Filtered Surface"
scatter1.color = "black"

scatter2 = Scatter()
scatter2.xValues = x
scatter2.yValues = surf
scatter2.label = "Original Surf"
scatter2.markerSize = 1
scatter2.color = "blue"


scatterPlot = Plot()
scatterPlot.add(scatter1)
scatterPlot.add(scatter2)

scatterPlot.xLabel = "Distance Along Cross Section"
scatterPlot.yLabel = "Surface Height"
scatterPlot.title = "Compare Surface"
scatterPlot.hasLegend()

layout = PlotLayout()
layout.addPlot(scatterPlot)
#layout.plot()
layout.save("profile1_compare.png")
# now plot the second order gradient of filtered surface
#scatter.yValues = surfSeconOrderGradient
#scatterPlot.yLabel = "dHeight^2/dX^2"
#scatterPlot.title = "Surface - 2nd Gradient (filtered)"

#layout = PlotLayout()
#layout.addPlot(scatterPlot)
#layout.plot()
#layout.save("profile1_so_gradient_filtered.png")

# plot the original surface with the predicted road surface features
scatter1 = Scatter()
scatter1.xValues = x
scatter1.yValues = surf
scatter1.markerSize = 1
scatter1.label = "Surface"
scatter1.color = "black"

scatter2 = Scatter()
scatter2.xValues = roadFeatures[:, 0]
scatter2.yValues = roadFeatures[:, 1]
scatter2.label = "Road Features"
scatter2.marker = "D"
scatter2.markerSize = 65
scatter2.color = "red"


scatterPlot = Plot()
scatterPlot.add(scatter1)
scatterPlot.add(scatter2)

scatterPlot.xLabel = "Distance Along Cross Section"
scatterPlot.yLabel = "Surface Height"
scatterPlot.title = "Road Features"
scatterPlot.hasLegend()

layout = PlotLayout()
layout.addPlot(scatterPlot)
layout.plot()
layout.save("profile1_detected_road_features.png")