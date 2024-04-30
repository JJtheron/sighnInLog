import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def create_form():
    window = tk.Tk()
    window.title("User Information")

    # Create a dictionary to store user input
    user_info = {}
    get_user_info = {"Name": tk.StringVar(), "Company Name": tk.StringVar(), "Person Visiting": tk.StringVar(), "Phone Number": tk.StringVar()}
    # Create labels and entry fields
    labels = list(get_user_info.keys())
    for i in range(len(labels)):
        tk.Label(window, text=labels[i]).grid(row=i)
        user_info[labels[i]] = tk.Entry(window,textvariable=get_user_info[labels[i]],width=17)
        user_info[labels[i]].grid(row=i, column=1)
    # Function to handle 'Submit' button click
    def submit():
        for key in user_info:
            user_info[key] = user_info[key].get()
        messagebox.showinfo("Saved", "User information saved.")
        window.destroy()

    # Function to handle 'Cancel' button click
    def cancel():
        window.destroy()

    # Create 'Submit' and 'Cancel' buttons
    submit_button = tk.Button(window, text="Submit", state="disabled", command=submit)
    submit_button.grid(row=4, column=0)
    tk.Button(window, text="Cancel", command=cancel).grid(row=4, column=1)

    # Function to enable 'Submit' button
    def enable_submit(*args):
        if get_user_info["Name"].get():
            submit_button.config(state="normal")
        else:
            submit_button.config(state="disabled")

    # Monitor the 'Name' field
    get_user_info["Name"].trace_add("write", enable_submit)

    window.mainloop()

    return user_info

# Call the function
#print(create_form())

def create_table():
    window = tk.Tk()
    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            window.destroy()
    window.title("User Information")
    window.protocol("WM_DELETE_WINDOW", on_closing)
    # Create a treeview with scrollbars
    tree = ttk.Treeview(window, columns=("Name", "Time In", "Time Out", "Company Name", "Visiting Who?", "Phone Number"), show="headings")
    vsb = ttk.Scrollbar(window, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(window, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    # Create column headings
    for col in ("Name", "Time In", "Time Out", "Company Name", "Visiting Who?", "Phone Number"):
        tree.heading(col, text=col)
    
    tree.insert(
    "",
    tk.END,
    text="UniquiID2",
    values=("JJ","now","later","wy","All my peeps", "18:30")
    )
    tree.insert(
    "",
    tk.END,
    text="UniquiID",
    values=("JjJ","now","later","wy","All my peeps", "18:30")
    )

    # Function to handle 'Check In' button click
    def check_in():
        print("Check In button clicked.")

    # Function to handle row click
    def on_click(event):
        item = tree.identify('item', event.x, event.y)
        print("You clicked on", tree.item(item, "values"), tree.item(item, "text"))

    # Bind the click event to the handler
    tree.bind("<Double-1>", on_click)

    # Create 'Check In' button
    tk.Button(window, text="Check In", command=check_in).grid(column=0, row=2)

    window.mainloop()


# Call the function
create_table()