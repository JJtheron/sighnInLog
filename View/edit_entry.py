import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from View.date_time_pick import date_time

class Edit_entry(tk.Frame):
    def __init__(self,parent):
        super().__init__(parent)
        parent.title("User Information")
        self.grid(row=0, column=0, padx=10, pady=10)
        # Create a dictionary to store user input
        self.time_in={"year":0,"month":0,"day":0,"hour":0,"min":0,"sec":0}
        self.time_out={"year":0,"month":0,"day":0,"hour":0,"min":0,"sec":0}
        
        self.user_info = {}
        self.labels = []
        self.time_in_or_out = ""
        self.get_user_info = {"Name": tk.StringVar(), "Company Name": tk.StringVar(), "Person Visiting": tk.StringVar(), "Phone Number": tk.StringVar(), "TimeIn":tk.StringVar(), "TimeOut":tk.StringVar()}
        # Create labels and entry fields
        labels = list(self.get_user_info.keys())
        for i in range(len(labels)):
            self.labels.append(tk.Label(self, text=labels[i]).grid(row=i))
            self.user_info[labels[i]] = tk.Entry(self,textvariable=self.get_user_info[labels[i]],width=17)
            self.user_info[labels[i]].grid(row=i, column=1)
        # Function to handle 'Submit' button click
        def pick_time_in():
            child = tk.Toplevel(self)
            child.transient(self)
            self.time_in_or_out = "TimeIn"
            child.uncle = self
            date_time(child)
            

        
        def pick_time_out():
            child = tk.Toplevel(self)
            child.transient(self)
            self.time_in_or_out = "TimeOut"
            child.uncle = self
            date_time(child)


        def submit():
            for key in self.user_info:
                self.user_info[key] = self.user_info[key].get()
            messagebox.showinfo("Saved", "User information saved.")
            self.destroy()
            parent.destroy()

        # Function to handle 'Cancel' button click
        def cancel():
            self.destroy()
            parent.destroy()

        time_in_button = tk.Button(self,text="Pick",command=pick_time_in)
        time_in_button.grid(row=4,column=2)
        time_out_button = tk.Button(self,text="Pick",command=pick_time_out)
        time_out_button.grid(row=5,column=2)
        # Create 'Submit' and 'Cancel' buttons
        submit_button = tk.Button(self, text="Submit", state="disabled", command=submit)
        submit_button.grid(row=6, column=0)
        tk.Button(self, text="Cancel", command=cancel).grid(row=6, column=1)

        # Function to enable 'Submit' button
        def enable_submit(*args):
            if self.get_user_info["Name"].get():
                submit_button.config(state="normal")
            else:
                submit_button.config(state="disabled")

        # Monitor the 'Name' field
        self.get_user_info["Name"].trace_add("write", enable_submit)
