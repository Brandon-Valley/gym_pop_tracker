import plotly.plotly as py
import plotly.graph_objs as go

# Create random data with numpy
import numpy as np



import plotly
import plotly.graph_objs as go
import datetime as dt

from plotly import tools
import plotly.plotly as py
from plotly.presentation_objs.presentation_objs import PRES_THEMES







N = 1000
random_x = [1,2,3]
random_y = [1,2,3]
# print('rand x: ', random_x, len(random_x). type(random_x))
# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)

data = [trace]

# Plot and embed in ipython notebook!
# py.iplot(data, filename='basic-scatter')
plotly.offline.plot(data, filename='basic-line')




