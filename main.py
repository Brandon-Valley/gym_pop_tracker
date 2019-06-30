import plotly.graph_objs as go
import plotly


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





import dl_data

import logger
import Log_Event
import month_weekday_lists

def build_log_event_l(input_csv_path):
    row_dl = logger.readCSV(input_csv_path)
    print(row_dl)#``````````````````````````````````````````````````````````````````````````````````````
    
    log_event_l = []
    for row_d in row_dl:
        log_event_l.append(Log_Event.Log_Event(row_d))
        
    return log_event_l


def make_graph(log_event_l, weekdays_l, months_l, graph_type):
    def _graph_name():
        graph_name = graph_type + '_'
        
        if len(weekdays_l) == 7:
            graph_name += 'All_Weekdays_'
        else:
            graph_name += str(weekdays_l) + '_'
            
        if len(months_l) == 12:
            graph_name += 'All_Months_'
        else:
            graph_name += str(months_l) + '_'
        return graph_name + '.html'
    
    def _make_trace():
        def __get_data_lists():
            num_ppl_l = []
            time_l    = []
            date_l    = []
            
            for log_event in log_event_l:
                if log_event.weekday in weekdays_l and \
                   log_event.month   in months_l:
                        num_ppl_l.append(log_event.num_ppl)
                        time_l   .append(log_event.time)
                        date_l   .append(log_event.date)
                        
#             print(num_ppl_l)
#             print(time_l)
#             print(date_l)
            return num_ppl_l, time_l, date_l
#                     if graph_type == 'num_ppl__vs__time__vs__date':
#                         date
    
        num_ppl_l, time_l, date_l = __get_data_lists()
        print(num_ppl_l)
        print(time_l)
        print(date_l)
        
        if graph_type == 'num_ppl__vs__time':
            trace = go.Scatter( x = time_l,
                                y = num_ppl_l,
                                mode = 'markers')
        elif graph_type == 'num_ppl__vs__time__vs__date':
            print('NEED TO make trace for other graph type')#```````````````````````````````````````````````````````````
        return trace

        

        
    
    print(_graph_name())
    trace = _make_trace()
    plotly.offline.plot([trace], filename=_graph_name())
        
        
        
           

def main():
    shareable_link = "https://drive.google.com/open?id=1o3qlhQPgk_VM2i48y2DPBhsI6fGFeCtsXyTmU31RWAs"
    local_csv_save_path = 'gym_pop.csv'
    weekdays_l = month_weekday_lists.WEEKDAYS#['Monday', 'Friday']
    months_l = month_weekday_lists.MONTHS
    graph_type = 'num_ppl__vs__time'
    dl_data.download_google_sheet_as_csv(shareable_link, local_csv_save_path)
    log_event_l = build_log_event_l(local_csv_save_path)
#     print(log_event_l)

    for log_event in log_event_l:
        print(vars(log_event))
#         log_event.print_me()

#     trimmed_log_event_l = trim_log_event_l(log_event_l, weekdays_l, months_l)
    make_graph(log_event_l, weekdays_l, months_l, graph_type)


if __name__ == '__main__':
    main()