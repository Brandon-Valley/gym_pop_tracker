
import plotly.graph_objs as go
import plotly

import datetime


    
    
    
    
# creating the hour range 
hours = []
for i in range (0, 24):
    hours.append(datetime.datetime(2000, 1, 1, hour=i, minute=0, second=0))
#     hours.append(datetime.datetime(hour=i, minute=0, second=0))

# # declaring the Layout with the 'range' attribute, and Figure
# layout = dict(title='Times On', xaxis=dict(type='date'), yaxis={'type': 'date', 'tickformat': '%H:%M', 
#                                                                 'nticks': 30, 'tick0': hours[0],
#                                                                 'range': [hours[0], hours[len(hours)-1]],
#                                                                 'autorange': False})
    
    


# def make_num_ppl__vs__time_trace(time_l, num_ppl_l):
#     trace = go.Scatter( x = time_l,
#                         y = num_ppl_l,
#                         mode = 'markers')
#     return trace


def get_time_range(datetime_l):
    def _to_unix_time(dt):
        epoch =  datetime.datetime.utcfromtimestamp(0)
        return (dt - epoch).total_seconds() * 1000
    
#     return [_to_unix_time(min(datetime_l)), _to_unix_time(max(datetime_l))]
    return [(min(datetime_l)), (max(datetime_l))]
    
    
def set_time_l_to_date(time_l):
    datetime_l = []
    for time in time_l:
        datetime_l.append(datetime.datetime(2000, 1, 1, time.hour, time.minute, time.second))
    return datetime_l
    

def plot_num_ppl__vs__time(time_l, num_ppl_l, title, filename, x_axis_title, y_axis_title):
    trace = go.Scatter( x = set_time_l_to_date(time_l),
                        y = num_ppl_l,
                        mode = 'markers')
    
    earliest_time = min(time_l)
    latest_time = max(time_l)
    print(earliest_time)
    
    layout = go.Layout(title=title,
#                        xaxis={'type': 'date',
#                               'title': x_axis_title,
# #                               'autorange':True,
#                             'range': [hours[0], hours[len(hours)-1]]
#                               },
                       
                        xaxis={'type': 'date', 'tickformat': '%H:%M', 
                                                                'nticks': 30, 'tick0': hours[0],
                                                                'range': [hours[0], hours[len(hours)-1]],
                                                                'autorange': False},
                       
                       
                       yaxis={'title': y_axis_title})
    
    plotly.offline.plot({"data": [trace], "layout": layout}, filename=filename, auto_open=True)

        
def plot_single_trace(title, filename, trace, x_axis_title, y_axis_title, z_axis_title=None):    
    
    if z_axis_title == None:
        layout = go.Layout(  title=title,
                             xaxis={'title': x_axis_title},
                             yaxis={'title': y_axis_title})
    else:
        layout = go.Layout(  title=title,
                     xaxis={'title': x_axis_title},
                     yaxis={'title': y_axis_title},
                     zaxis={'title': z_axis_title})
    
    plotly.offline.plot({"data": [trace], "layout": layout}, filename=filename, auto_open=True)
    
    
    
    
if __name__ == '__main__':
    import main
    main.main()
    
    