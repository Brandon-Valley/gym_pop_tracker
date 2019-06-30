import plotly.plotly as py
import plotly.graph_objs as go

import numpy as np


import plotly
import plotly.graph_objs as go
import datetime as dt

from plotly import tools
import plotly.plotly as py
from plotly.presentation_objs.presentation_objs import PRES_THEMES








x, y, z = np.random.multivariate_normal(np.array([0,0,0]), np.eye(3), 400).transpose()

trace1 = go.Scatter3d(
    x=x,
    y=y,
    z=z,
    mode='markers',
    marker=dict(
        size=12,
        color=z,                # set color to an array/list of desired values
        colorscale='Viridis',   # choose a colorscale
        opacity=0.8
    )
)

data = [trace1]
layout = go.Layout(
    margin=dict(
        l=0,
        r=0,
        b=0,
        t=0
    )
)
fig = go.Figure(data=data, layout=layout)
plotly.offline.plot(fig, filename='3d-scatter-colorscale')