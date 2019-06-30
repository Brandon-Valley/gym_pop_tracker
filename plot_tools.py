
import plotly.graph_objs as go
import plotly

import datetime


# creating the hour range 
hours = []
for i in range (0, 24):
    hours.append(datetime.datetime(2000, 1, 1, hour=i, minute=0, second=0))


    
    
def set_time_l_to_date(time_l):
    datetime_l = []
    for time in time_l:
        datetime_l.append(datetime.datetime(2000, 1, 1, time.hour, time.minute, time.second))
    return datetime_l

def set_date_l_to_same_year(date_l):
    datetime_l = []
    for date in date_l:
        datetime_l.append(datetime.datetime(2000, date.month, date.day))
    return datetime_l
    
    
def time_axis(axis_title):
    return {    'title': axis_title,
                'type': 'date',
                'tickformat': '%I:%M',# %p',  
                'nticks': 30, 
                'tick0': hours[0],
                'range': [hours[0], hours[len(hours)-1]],
                'autorange': False}
    

def plot_num_ppl__vs__time(time_l, num_ppl_l, title, filename, x_axis_title, y_axis_title):
    trace = go.Scatter( x = set_time_l_to_date(time_l),
                        y = num_ppl_l,
                        mode = 'markers')
    
    earliest_time = min(time_l)
    latest_time = max(time_l)
    print(earliest_time)
    
    layout = go.Layout( title=title,

                        xaxis=time_axis(x_axis_title),

                       yaxis={'title': y_axis_title})
    
    plotly.offline.plot({"data": [trace], "layout": layout}, filename=filename, auto_open=True)



        
def plot_num_ppl__vs__time__vs__date(time_l, num_ppl_l, date_l, title, filename, x_axis_title, y_axis_title, z_axis_title):

    trace = go.Scatter3d(   x = set_date_l_to_same_year(date_l),
                            y = set_time_l_to_date(time_l),
                            z = num_ppl_l,
                            mode = 'markers',
                            marker=dict(
                                        size=12,
    #                                     color=z,                # set color to an array/list of desired values
                                        colorscale='Viridis',   # choose a colorscale
                                        opacity=0.8))
    
    earliest_time = min(time_l)
    latest_time = max(time_l)
    print(earliest_time)
    
    layout = go.Layout( title=title,
                         scene = dict(   #xaxis={    'title': x_axis_title,
#                                                     'type': 'date',
#                                                     'tickformat': '%I:%M',# %p',  
#                                                     'nticks': 30, 
#                                                     'tick0': hours[0],
#                                                     'range': [hours[0], hours[len(hours)-1]],
#                                                     'autorange': False},
                                        xaxis={'title': x_axis_title},
                                        zaxis={'title': z_axis_title},

                                        yaxis=time_axis(y_axis_title))
                                    )
#                         yaxis=time_axis('TITLES ARE NOT SHOWN ON 3d GRAPHS'),)
#                         yaxis={'title': y_axis_title})
#                         zaxis=time_axis('TITLES ARE NOT SHOWN ON 3d GRAPHS'))
    
    plotly.offline.plot({"data": [trace], "layout": layout}, filename=filename, auto_open=True)     
        
        
        
        
# def plot_single_trace(title, filename, trace, x_axis_title, y_axis_title, z_axis_title=None):    
#     
#     if z_axis_title == None:
#         layout = go.Layout(  title=title,
#                              xaxis={'title': x_axis_title},
#                              yaxis={'title': y_axis_title})
#     else:
#         layout = go.Layout(  title=title,
#                      xaxis={'title': x_axis_title},
#                      yaxis={'title': y_axis_title},
#                      zaxis={'title': z_axis_title})
#     
#     plotly.offline.plot({"data": [trace], "layout": layout}, filename=filename, auto_open=True)
#     
    
    
    
if __name__ == '__main__':
    import main
    main.main()
    
    