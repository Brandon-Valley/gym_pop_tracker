import datetime

import month_weekday_lists



class Log_Event:
    def __init__(self, row_d):
        self.datetime = self.get_datetime(row_d['date_time'])
        
        self.num_ppl  = int(row_d['num_ppl'])
        self.year     = self.datetime.year
        self.month    = month_weekday_lists.MONTHS[self.datetime.month]
        self.weekday  = month_weekday_lists.WEEKDAYS[self.datetime.weekday()]
        self.time     = self.datetime.time()
        self.date     = self.datetime.date()
        
        
        
        
    def get_datetime(self, date_time):
        date_str, time_str = date_time.split(' ')
        month_str, day_str, year_str = date_str.split('-')
        hour_str, min_str, sec_str = time_str.split(':')
        return datetime.datetime(int(year_str), int(month_str), int(day_str), int(hour_str), int(min_str), int(sec_str))
        
    def print_me(self):
        print('{{')
        print('  num_ppl:  ', self.num_ppl)
        print('  datetime: ', self.datetime)
        print('}}')
        
        
        
        
        
        
        
        
        
        
        
if __name__ == '__main__':
    import main
    main.main()