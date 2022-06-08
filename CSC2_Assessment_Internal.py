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

# Set up for buttons, a function
def setup_buttons():
    # These global variables are used to define variables that are used
    global customer_details, customer_name, item_hired, number_of_item_hired, customer_receipt, total_entries, delete_item

    # Creates an empty entry and labels along with a dropdown menu
    Label(main_window, text="Customer Name").grid(column=0, row=0, sticky=E)
    customer_name = Entry(main_window)
    Label(main_window, text="Item Hired").grid(column=0, row=1, sticky=E)
    item_hired = Entry(main_window)
    Label(main_window, text="Number of Item Hired").grid(column=0, row=2, sticky=E)
    number_of_item_hired = Entry(main_window)
    Label(main_window, text="Receipt Number")

def main():
    # These global variables are used to define variables that are used
    global main_window
    global customer_details, customer_name, item_hired, number_of_item_hired, customer_receipt, total_entries
    customer_details = []  # Creating an empty list
    total_entries = 0
    # Creating the GUI and setup
    main_window = Tk()
    #setup_buttons()
    main_window.mainloop()

# After defining the function for main set up, the function is then called to start up the GUI
main()
