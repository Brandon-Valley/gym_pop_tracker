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


class Plot_Tab(Tab.Tab):
    def __init__(self, master, tab_control):
        self.tab_control = tab_control
        Tab.Tab.__init__(self, master)

        

        self.weekdays_____widget_setup()


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

            

        

        
    def grid_widgets(self):
#         self.master.grid_columnconfigure(3, weight=1)

        self.weekdays_lf            .grid(column=1, row=1, sticky='NSWE', ipadx=5, ipady=5, padx=5, pady=5)
        self.select_all_weekdays_btn.grid(column=1, row=1)

        
if __name__ == '__main__':
    GUI.main()