###/ This programs keeps track of the customer details and the number of item they have hired \###
"""
Assessment Summary Details:
- Customer Full Name
- Item
- Item Hired
- Receipt Number
- Multi-Dimensional List
- GUI (Base)
- Button Widgets
- Looping

"""

from tkinter import *  # This imports all the functions from tkinter module

# This will quit the subroutine
def quit():
    main_window.destroy()

# Prints the customer details after appending it
def print_customer_details():
    # Global variables that are used
    global total_entries, name_count
    name_count = 0
    Label(main_window, text="Row", font='bold').grid(column=3, row=1, columnspan=1)
    Label(main_window, text="Customer Name", font='bold').grid(column=4, row=1, columnspan=1)
    Label(main_window, text="Item Hired", font='bold').grid(column=5, row=1, columnspan=1)
    Label(main_window, text="Number of Item Hired", font='bold').grid(column=6, row=1, columnspan=1)
    Label(main_window, text="Receipt Number", font='bold').grid(column=7, row=1, columnspan=1)

    # Multi-Dimensional List
    while name_count < total_entries:
        Label(main_window, text=name_count).grid(column=3, row=name_count + 2, columnspan=1)
        Label(main_window, text=(customer_details[name_count][0])).grid(column=4, row=name_count + 2, columnspan=1)
        Label(main_window, text=(customer_details[name_count][1])).grid(column=5, row=name_count + 2, columnspan=1)
        Label(main_window, text=(customer_details[name_count][2])).grid(column=6, row=name_count + 2, columnspan=1)
        Label(main_window, text=(customer_details[name_count][3])).grid(column=7, row=name_count + 2, columnspan=1)
        name_count += 1

# This function will append all the details inputted in the entries and checks them
def append_inputs():
    # Global variables that are used
    global customer_details, customer_name, item_hired, number_of_item_hired, customer_receipt, total_entries
    # Checks if the user has inputted the name of the customer
    if len(customer_name.get()) != 0:
        # Appends every detail into one list
        customer_details.append([customer_name.get(), item_hired.get(), number_of_item_hired.get(), customer_receipt.get()])
        customer_name.delete(0, 'end')
        item_hired.delete(0, 'end')
        number_of_item_hired.delete(0, 'end')
        customer_receipt.delete(0, 'end')
        total_entries += 1

def delete_row():
    pass


# Set up for buttons, a function
def setup_buttons():
    # These global variables are used to define variables that are used
    global customer_details, customer_name, item_hired, number_of_item_hired, customer_receipt, total_entries, delete_item

    # Title
    Label(main_window, text="Julie's Tracker", font=25).grid(columnspan=5, row=0, sticky=N)

    # Creates an empty entry and labels along with a dropdown menu
    Label(main_window, text="Customer Name").grid(column=0, row=1, sticky=E)
    customer_name = Entry(main_window)
    customer_name.grid(column=1, row=1)
    Label(main_window, text="Item Hired").grid(column=0, row=2, sticky=E)
    item_hired = Entry(main_window)
    item_hired.grid(column=1, row=2)
    Label(main_window, text="Number of Item Hired").grid(column=0, row=3, sticky=E)
    number_of_item_hired = Entry(main_window)
    number_of_item_hired.grid(column=1, row=3)
    Label(main_window, text="Receipt Number").grid(column=0, row=4, sticky=E)
    customer_receipt = Entry(main_window)
    customer_receipt.grid(column=1, row=4)
    Label(main_window, text="Row #").grid(column=3, row=3, sticky=E)
    delete_item = Entry(main_window)
    delete_item.grid(column=4, row=3)

    # Button Widgets
    Button(main_window, text="Append Details", command=append_inputs).grid(column=3, row=2)
    Button(main_window, text="Print Details", command=print_customer_details, width=10).grid(column=4, row=2, sticky=E)
    Button(main_window, text="Quit", command=quit, width=10).grid(column=4, row=1, sticky=E)
    Button(main_window, text="Delete Row", command=delete_row, width=10).grid(column=4, row=4, sticky=E)
    Label(main_window, text="               ").grid(column=2, row=1)

def main():
    # These global variables are used to define variables that are used
    global main_window
    global customer_details, customer_name, item_hired, number_of_item_hired, customer_receipt, total_entries
    customer_details = []  # Creating an empty list
    total_entries = 0
    # Creating the GUI and setup
    main_window = Tk()
    main_window.title("App")
    setup_buttons()
    main_window.mainloop()

# After defining the function for main set up, the function is then called to start up the GUI
main()
