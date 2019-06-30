from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
from plotly.graph_objs import *
from datetime import datetime, time

init_notebook_mode(connected=True)

# in the example i am using fabricated data. declaring the data:
time_data = [datetime(2017, 7, 28, 21, 37, 19), datetime(2017, 7, 29, 17, 11, 56), datetime(2017,8, 1, 11, 15, 45), datetime(2017, 8, 2, 13, 54, 3)]
x_data = []
y_data = []

# creating the x-row data with dates only, and the y-row data with the time only
for row in time_data:
    x_data.append(row.date())
    y_data.append(str(datetime.combine(datetime(2017, 1, 1).date(), row.time())))

#declaring the data for the graph
data = [Scatter(x=x_data, y=y_data, name='Times On', mode='markers')]

# creating the hour range 
hours = []
for i in range (0, 24):
    hours.append(datetime(2017, 1, 1, i, 0, 0))

# declaring the Layout with the 'range' attribute, and Figure
layout = dict(title='Times On', xaxis=dict(type='date'), yaxis={'type': 'date', 'tickformat': '%H:%M', 
                                                                'nticks': 30, 'tick0': hours[0],
                                                                'range': [hours[0], hours[len(hours)-1]],
                                                                'autorange': False})
fig = Figure(data=data, layout=layout)


import plotly.graph_objs as go
import plotly


# plotting
plotly.offline.plot(figure_or_data=fig, auto_open=True)