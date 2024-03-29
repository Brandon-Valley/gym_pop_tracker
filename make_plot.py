
import dl_data
import logger
import Log_Event
import month_weekday_lists
import plot_tools


NUM_PPL_AXIS_NAME = "Number of People"
TIME_AXIS_NAME = 'Time'
DATE_AXIS_NAME = 'Date'

GOOGLE_SHEETS_SHAREABLE_LINK = "https://drive.google.com/open?id=1o3qlhQPgk_VM2i48y2DPBhsI6fGFeCtsXyTmU31RWAs"
LOCAL_CSV_SAVE_PATH = 'gym_pop.csv'

def build_log_event_l(input_csv_path):
    row_dl = logger.readCSV(input_csv_path)
    
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
    
    
    def _get_data_lists():
        num_ppl_l = []
        time_l    = []
        date_l    = []
        
        for log_event in log_event_l:
            if log_event.weekday in weekdays_l and \
               log_event.month   in months_l:
                    num_ppl_l.append(log_event.num_ppl)
                    time_l   .append(log_event.time)
                    date_l   .append(log_event.date)
                    
        return num_ppl_l, time_l, date_l

    def _plot_data_lists(num_ppl_l, time_l, date_l):
        if graph_type == 'num_ppl__vs__time':            
            plot_tools.plot_num_ppl__vs__time(time_l, num_ppl_l, _graph_name(), _graph_name(), TIME_AXIS_NAME, NUM_PPL_AXIS_NAME)
            
        elif graph_type == 'num_ppl__vs__time__vs__date':
            plot_tools.plot_num_ppl__vs__time__vs__date(time_l, num_ppl_l, date_l, _graph_name(), _graph_name(), DATE_AXIS_NAME, TIME_AXIS_NAME, NUM_PPL_AXIS_NAME)

    
    num_ppl_l, time_l, date_l = _get_data_lists()
#     print(num_ppl_l)
#     print(time_l)
#     print(date_l)
    
    _plot_data_lists(num_ppl_l, time_l, date_l)
    
        
        
def make_plot(weekdays_l, months_l, graph_type):
    print('making plot...')
    dl_data.download_google_sheet_as_csv(GOOGLE_SHEETS_SHAREABLE_LINK, LOCAL_CSV_SAVE_PATH)
    log_event_l = build_log_event_l(LOCAL_CSV_SAVE_PATH)
    make_graph(log_event_l, weekdays_l, months_l, graph_type)
    print('done!')


def main():
    shareable_link = "https://drive.google.com/open?id=1o3qlhQPgk_VM2i48y2DPBhsI6fGFeCtsXyTmU31RWAs"
    local_csv_save_path = 'gym_pop.csv'
    weekdays_l = month_weekday_lists.WEEKDAYS#['Monday', 'Friday']
    months_l = month_weekday_lists.MONTHS
    graph_type = 'num_ppl__vs__time__vs__date'#'num_ppl__vs__time'
     
    dl_data.download_google_sheet_as_csv(shareable_link, local_csv_save_path)
    log_event_l = build_log_event_l(local_csv_save_path)
 
#     for log_event in log_event_l:
#         print(vars(log_event))
 
    make_graph(log_event_l, weekdays_l, months_l, graph_type)


# if __name__ == '__main__':
#     from gui import GUI
#     GUI.main()