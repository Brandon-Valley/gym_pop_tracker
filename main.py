
import dl_data

import logger
import Log_Event

def build_log_event_l(input_csv_path):
    row_dl = logger.readCSV(input_csv_path)
    print(row_dl)#``````````````````````````````````````````````````````````````````````````````````````
    
    log_event_l = []
    for row_d in row_dl:
        log_event_l.append(Log_Event.Log_Event(row_d))
        
    return log_event_l




def main():
    shareable_link = "https://drive.google.com/open?id=1o3qlhQPgk_VM2i48y2DPBhsI6fGFeCtsXyTmU31RWAs"
    local_csv_save_path = 'gym_pop.csv'
    
#     dl_data.download_google_sheet_as_csv(shareable_link, local_csv_save_path)
    log_event_l = build_log_event_l(local_csv_save_path)
#     print(log_event_l)

    for log_event in log_event_l:
        print(vars(log_event))
#         log_event.print_me()

if __name__ == '__main__':
    main()