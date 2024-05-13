from tkinter import *
from tkcalendar import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

class date_time(tk.Frame):
    def __init__(self,parent,date_a_time):
        super().__init__(parent)
        now = datetime.now()
        parent.title("Select Date")
        self.grid(row=0, column=0, padx=10, pady=10)
        self.hour_string=StringVar(value=now.strftime("%H"))
        self.min_string=StringVar(value=now.strftime("%M"))
        self.sec_string= StringVar(value=now.strftime("%S"))       
        self.f = ('Times', 20)
        self.dnt = date_a_time
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
        date_split = date.split("/")
        self.dnt.DATE_TIME = {"year":int(date_split[0]),"month":int(date_split[1]),"day":int(date_split[2]),"hour":int(h),"min":int(m),"sec":int(s)}

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
        """
        fone = Frame(ws)
        ftwo = Frame(ws)

        fone.pack(pady=10)
        ftwo.pack(pady=10)
        """
        """
        min_sb = Spinbox(
            ftwo,
            from_=0,
            to=23,
            wrap=True,
            textvariable=hour_string,
            width=2,
            state="readonly",
            font=f,
            justify=CENTER
            )
        sec_hour = Spinbox(
            ftwo,
            from_=0,
            to=59,
            wrap=True,
            textvariable=min_string,
            font=f,
            width=2,
            justify=CENTER
            )

        sec = Spinbox(
            ftwo,
            from_=0,
            to=59,
            wrap=True,
            textvariable=sec_hour,
            width=2,
            font=f,
            justify=CENTER
            )

        min_sb.pack(side=LEFT, fill=X, expand=True)
        sec_hour.pack(side=LEFT, fill=X, expand=True)
        sec.pack(side=LEFT, fill=X, expand=True)

        msg = Label(
            ws, 
            text="Hour  Minute  Seconds",
            font=("Times", 12),
            bg="#cd950c"
            )
        msg.pack(side=TOP)

        actionBtn =Button(
            ws,
            text="Submit",
            padx=10,
            pady=10,
            command=display_msg
        )
        actionBtn.pack(pady=10)

        msg_display = Label(
            ws,
            text="",
            bg="#cd950c"
        )
        msg_display.pack(pady=10)
        """

