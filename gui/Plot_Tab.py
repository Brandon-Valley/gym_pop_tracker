from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import *

from tkinter import *

import GUI
import Tab


# to be able to import from parent dir
import sys
parent_dir_path = ''
for dir in sys.path[0].split('\\')[0:-1]:
    parent_dir_path += dir + '\\'
sys.path.append(parent_dir_path[0:-1])

# from parent dir
import month_weekday_lists

PLOT_TYPES_L = ['num_ppl__vs__time',
                'num_ppl__vs__time__vs__date']


class Plot_Tab(Tab.Tab):
    def __init__(self, master, tab_control):
        self.tab_control = tab_control
        Tab.Tab.__init__(self, master)

        

        self.weekdays_____widget_setup()
        self.months_____widget_setup()
        self.plot_____widget_setup()


        self.grid_widgets()
        
        
    def weekdays_____widget_setup(self):
        self.weekdays_dl = []
        
        self.weekdays_lf = LabelFrame(self.master, text=" Weekdays: ")
        
        # weekday cbtns
        for weekday in month_weekday_lists.WEEKDAYS:
            weekday_cbtn_sel = IntVar(value = 0)
            self.weekdays_dl.append({'sel' : weekday_cbtn_sel,
                                     'cbtn': Checkbutton(self.weekdays_lf, text=weekday, variable=weekday_cbtn_sel)})#, command = trim_cbtn_clk)
        # grid
        start_row = 2
        for weekday_d_num, weekday_d in enumerate(self.weekdays_dl):
            weekday_d['cbtn'].grid(column=1, row=start_row + weekday_d_num, sticky = 'w')
            
        
        # select all weekdays btn
        def select_all_weekdays_btn_clk(event=None):
            for weekday_d in self.weekdays_dl:
                weekday_d['sel'].set(1)
        self.select_all_weekdays_btn = Button(self.weekdays_lf, text="Select All", command = select_all_weekdays_btn_clk) #lambda: GUI_commands.back(self.master, self)

            

    def months_____widget_setup(self):
        self.months_dl = []
        
        self.months_lf = LabelFrame(self.master, text=" Months: ")

        # month cbtns
        for month in month_weekday_lists.MONTHS:
            month_cbtn_sel = IntVar(value = 0)
            self.months_dl.append({'sel' : month_cbtn_sel,
                                     'cbtn': Checkbutton(self.months_lf, text=month, variable=month_cbtn_sel)})#, command = trim_cbtn_clk)
        # grid
        start_row = 2
        for month_d_num, month_d in enumerate(self.months_dl):
            month_d['cbtn'].grid(column=1, row=start_row + month_d_num, sticky = 'w')
            
        
        # select all months btn
        def select_all_months_btn_clk(event=None):
            for month_d in self.months_dl:
                month_d['sel'].set(1)
        self.select_all_months_btn = Button(self.months_lf, text="Select All", command = select_all_months_btn_clk) #lambda: GUI_commands.back(self.master, self)

        


    def plot_____widget_setup(self):
        self.plot_lf = LabelFrame(self.master, text=" Months: ")

        # plot type combobox
        self.plot_type_cbox_lbl = Label(self.plot_lf, text="Plot Type:")
        self.plot_type_cbox = Combobox(self.plot_lf, state = 'readonly')
        self.plot_type_cbox['values'] = PLOT_TYPES_L
        self.plot_type_cbox.current(0) #set the selected item

        
    def grid_widgets(self):
#         self.master.grid_columnconfigure(3, weight=1)

        # weekdays
        self.weekdays_lf            .grid(column=1, row=1, sticky='NSWE', ipadx=5, ipady=5, padx=5, pady=5)
        self.select_all_weekdays_btn.grid(column=1, row=1)
        
        # months
        self.months_lf              .grid(column=2, row=1, sticky='NSWE', ipadx=5, ipady=5, padx=5, pady=5)
        self.select_all_months_btn  .grid(column=1, row=1)
        
        # plot 
        self.plot_lf                .grid(column=3, row=1, sticky='NSWE', ipadx=5, ipady=5, padx=5, pady=5)
        self.plot_type_cbox_lbl     .grid(column=1, row=1)
        self.plot_type_cbox         .grid(column=1, row=2)

        
if __name__ == '__main__':
    GUI.main()