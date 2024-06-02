import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Controler.C_create_tagged_user import c_entry_window_tag

class entry_window_tagged(tk.Frame):
    def __init__(self,parent,tag):
        super().__init__(parent)
        parent.title("User Information+Tag")
        self.grid(row=0, column=0, padx=10, pady=10)
        # Create a dictionary to store user input
        self.user_info = {}
        self.parent = parent
        self.labels = []
        self.controller = c_entry_window_tag(self)
        get_user_info = {"Name": tk.StringVar(), "Company Name": tk.StringVar(), "Phone Number": tk.StringVar(), "Tag#": tk.StringVar()}
        get_user_info["Tag#"].set(tag)
        # Create labels and entry fields
        labels = list(get_user_info.keys())

        for i in range(len(labels)):
            self.labels.append(tk.Label(self, text=labels[i]).grid(row=i))
            self.user_info[labels[i]] = tk.Entry(self,textvariable=get_user_info[labels[i]],width=17)
            self.user_info[labels[i]].grid(row=i, column=1)
        # Function to handle 'Submit' button click
        def submit():
            for key in self.user_info:
                self.user_info[key] = self.user_info[key].get()
            self.controller.submit_info()
            self.destroy()
            parent.destroy()

        # Function to handle 'Cancel' button click
        def cancel():
            self.destroy()
            parent.destroy()

        # Create 'Submit' and 'Cancel' buttons
        submit_button = tk.Button(self, text="Submit", state="disabled", command=submit)
        submit_button.grid(row=5, column=0)
        tk.Button(self, text="Cancel", command=cancel).grid(row=5, column=1)

        # Function to enable 'Submit' button
        def enable_submit(*args):
            if get_user_info["Name"].get():
                submit_button.config(state="normal")
            else:
                submit_button.config(state="disabled")

        # Monitor the 'Name' field
        get_user_info["Name"].trace_add("write", enable_submit)