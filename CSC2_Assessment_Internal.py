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
    Label(main_window, text="Row", font=('bold', 12, 'underline')).grid(column=0, row=8, columnspan=1)
    Label(main_window, text="Customer Name", font=('bold', 12, 'underline')).grid(column=1, row=8, columnspan=1)
    Label(main_window, text="Item Hired", font=('bold', 12, 'underline')).grid(column=2, row=8, columnspan=1)
    Label(main_window, text="Number of Item Hired", font=('bold', 12, 'underline')).grid(column=3, row=8, columnspan=1)
    Label(main_window, text="Receipt Number", font=('bold', 12, 'underline')).grid(column=4, row=8, columnspan=1)

    # Multi-Dimensional List
    while name_count < total_entries:
        Label(main_window, text=name_count).grid(column=0, row=name_count + 9, columnspan=1)
        Label(main_window, text=(customer_details[name_count][0])).grid(column=1, row=name_count + 9, columnspan=1)
        Label(main_window, text=(customer_details[name_count][1])).grid(column=2, row=name_count + 9, columnspan=1)
        Label(main_window, text=(customer_details[name_count][2])).grid(column=3, row=name_count + 9, columnspan=1)
        Label(main_window, text=(customer_details[name_count][3])).grid(column=4, row=name_count + 9, columnspan=1)
        name_count += 1


# Validity Checker
def checking_inputs():
    # Global variables that are used
    global customer_details, customer_name, item_hired, number_of_item_hired, customer_receipt, total_entries
    input_check = 0
    Label(main_window, text="               ").grid(column=2, row=1)
    Label(main_window, text="               ").grid(column=2, row=2)
    Label(main_window, text="               ").grid(column=2, row=3)
    Label(main_window, text="               ").grid(column=2, row=4)
    # Checks if the customer name is not blank, if it is, print error text
    if len(customer_name.get()) == 0:
        Label(main_window, text="Required", fg='red').grid(column=2, row=1)
        input_check = 1
    # Checks if the item hired is not blank, if it is, print error text
    if len(item_hired.get()) == 0:
        Label(main_window, text="Required", fg='red').grid(column=2, row=2)
        input_check = 1
    # Checks how many of the item is hired with an amount between 1 and 500,
    # if it is not entered or not within range, print error text
    if number_of_item_hired.get().isdigit():
        if int(number_of_item_hired.get()) < 1 or int(number_of_item_hired.get()) > 500:
            Label(main_window, text="1-500 only", fg='red').grid(column=2, row=3)
            input_check = 1
    else:
        Label(main_window, text="1-500 only", fg='red').grid(column=2, row=3)
        input_check = 1
    # Checks if the customer receipt is not blank and an integer only, if it is, print error text
    if item_hired.get().isdigit():
        if len(item_hired.get()) == 0:
            Label(main_window, text="Required, Integer only", fg='red').grid(column=2, row=2)
            input_check = 1
    # Appends the details if ll entries are inputted properly
    if input_check == 0:
        append_details()
        pass


# This function will append all the details inputted in the entries and checks them
def append_details():
    # Global variables that are used
    global customer_details, customer_name, item_hired, number_of_item_hired, customer_receipt, total_entries
    # Appends every detail into one list
    customer_details.append([customer_name.get(), item_hired.get(), number_of_item_hired.get(), customer_receipt.get()])
    # Deletes all the values inputted in the entry boxes once appended
    customer_name.delete(0, 'end')
    item_hired.delete(0, 'end')
    number_of_item_hired.delete(0, 'end')
    customer_receipt.delete(0, 'end')
    total_entries += 1


# Deletes a row from the list
def delete_row():
    # Global variables that are used
    global customer_details, delete_item, total_entries, name_count

    # Finding which row that is going to be deleted and removed it from the list
    del customer_details[int(delete_item.get())]
    total_entries -= 1
    delete_item.delete(0, 'end')
    # clear the last item on the displayed GUI
    Label(main_window, text="       ").grid(column=0, row=name_count + 8)
    Label(main_window, text="       ").grid(column=1, row=name_count + 8)
    Label(main_window, text="       ").grid(column=2, row=name_count + 8)
    Label(main_window, text="       ").grid(column=3, row=name_count + 8)
    Label(main_window, text="       ").grid(column=4, row=name_count + 8)
    # Print all other items in the list after that
    print_customer_details()


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
    Button(main_window, text="Append Details", command=checking_inputs).grid(column=3, row=2)
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
