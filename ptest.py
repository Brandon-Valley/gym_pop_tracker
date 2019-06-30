import plotly.graph_objs as go
import pandas as pd
from datetime import datetime
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)

d = pd.Series(['1.10.28','1.09.97','1.09.44','1.10.05',
           '1.11.21','1.09.63','1.09.90','1.10.28',
           '1.10.09','1.09.68','1.09.96','1.10.28',
           '1.10.75','1.11.43'])
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
y = pd.to_datetime(d, format='%M.%S.%f').dt.to_pydatetime()
trace1 = go.Scatter(x=x,y=y)
layout = go.Layout(yaxis={'type': 'time','tickformat': '%M.%S.%f'})
fig = go.Figure(data = [trace1], layout=layout)
iplot(fig)