from tkinter import *
from tkcalendar import *
import tkinter as tk
from datetime import datetime

class date_time(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        now = datetime.now()
        parent.title("Select Date")
        self.grid(row=0, column=0, padx=10, pady=10)
        self.hour_string=StringVar(value=now.strftime("%H"))
        self.min_string=StringVar(value=now.strftime("%M"))
        self.sec_string= StringVar(value=now.strftime("%S"))       
        self.f = ('Times', 20)
        self.parent=parent
        self.cal = Calendar(
            self, 
            selectmode="day", 
            year=int(now.strftime("%Y")), 
            month=int(now.strftime("%m")),
            day=int(now.strftime("%d"))
            )
        self.cal.grid(row=0, column=1)
        self.time_select_frame = tk.Frame(self)
        self.time_select_frame.grid(row=1, column=1,padx=4, pady=3)
        self.min = Spinbox(
            self.time_select_frame,
            from_=0,
            to=59,
            wrap=True,
            textvariable=self.min_string,
            width=2,
            font=self.f,
            justify=CENTER
            )
        
        self.sec = Spinbox(
            self.time_select_frame,
            from_=0,
            to=59,
            wrap=True,
            textvariable=self.sec_string,
            font=self.f,
            width=2,
            justify=CENTER
            )

        self.hour = Spinbox(
            self.time_select_frame,
            from_=0,
            to=23,
            wrap=True,
            textvariable=self.hour_string,
            width=2,
            font=self.f,
            justify=CENTER
            )
        self.hour.grid(row=0, column=0)
        self.min.grid(row=0, column=1)
        self.sec.grid(row=0, column=2)
        self.actionBtn =Button(
            self.time_select_frame,
            text="Submit",
            padx=10,
            pady=10,
            command=self.submit_time
        )
        self.actionBtn.grid(row=1,column=1)

    def submit_time(self):
        date = self.cal.get_date()
        m = self.min_string.get()
        h = self.hour_string.get()
        s = self.sec_string.get()
        self.parent.uncle.get_user_info[self.parent.uncle.time_in_or_out].set(f"{date} , {h}:{m}:{s}")
        self.destroy()
        self.parent.destroy()
        


    def run(self):
        if last_value == "59" and self.min_string.get() == "0":
            self.hour_string.set(int(self.hour_string.get())+1 if self.hour_string.get() !="23" else 0)   
            last_value = self.min_string.get()

        if last_value_sec == "59" and self.sec_hour.get() == "0":
            self.min_string.set(int(self.min_string.get())+1 if self.min_string.get() !="59" else 0)
        if last_value == "59":
            self.hour_string.set(int(self.hour_string.get())+1 if self.hour_string.get() !="23" else 0)            
            last_value_sec = self.sec_hour.get()
