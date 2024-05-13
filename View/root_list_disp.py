import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from View.edit_create_form import entry_window
from View.create_tagged_user import entry_window_tagged
from View.edit_entry import Edit_entry

class main_window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User Information")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)
        # Create a treeview with scrollbars
        self.tree = ttk.Treeview(self, columns=("Name", "Time In", "Time Out", "Company Name", "Visiting Who?", "Phone Number"), show="headings")
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self. hsb = ttk.Scrollbar(self, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=self.vsb.set, xscrollcommand=self.hsb.set)
        self.tree.grid(column=0, row=0, sticky='nsew')
        self.vsb.grid(column=1, row=0, sticky='ns')
        self.hsb.grid(column=0, row=1, sticky='ew')
        self.run()
        
    def insert_new_entry(self,tree,**kwargs):
        tree.insert(
        "",
        tk.END,
        text=kwargs["ID"],
        values=(kwargs["Name"],kwargs["Time In"],kwargs["Time Out"],kwargs["Company Name"],kwargs["Visiting Who?"], kwargs["Phone Number"])
        )    
        
    
    def edit_entry(self,uniqueID):
        return True
 
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.destroy()

    # Function to handle 'Check In' button click
    def check_in(self):
        child = tk.Toplevel(self)
        child.transient(self)
        entry_window(child)

    # enter a newtag assiciated with person
    def check_in_tag(self):
        child = tk.Toplevel(self)
        child.transient(self)
        entry_window_tagged(child)

    # Function to handle row click
    def on_click(self,event):
        item = self.tree.identify('item', event.x, event.y)
        child = tk.Toplevel(self)
        child.transient(self)
        Edit_entry(child)
        print("You clicked on", self.tree.item(item, "values"), self.tree.item(item, "text"))

    def run(self):

        # Create column headings
        for col in ("Name", "Time In", "Time Out", "Company Name", "Visiting Who?", "Phone Number"):
            self.tree.heading(col, text=col)

        # Bind the click event to the handler
        self.tree.bind("<Double-1>", self.on_click)

        # Create 'Check In' button
        tk.Button(self, text="Check In", command=self.check_in).grid(column=0, row=2)
        tk.Button(self, text="Add Tag", command=self.check_in_tag).grid(column=1, row=2)