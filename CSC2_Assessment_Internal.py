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
from tkinter import ttk
from random import randint  # This imports randint (random integer) from random module

# This will quit the subroutine
def quit():
    main_window.destroy()


# Prints the customer details after appending it
def print_customer_details():
    # Global variables that are used
    global total_entries, name_count, frame
    name_count = 0
    Label(frame, text="Row", font=('bold', 12, 'underline')).grid(column=0, row=8, columnspan=1)
    Label(frame, text="Customer Name", font=('bold', 12, 'underline')).grid(column=1, row=8, columnspan=1)
    Label(frame, text="Item Hired", font=('bold', 12, 'underline')).grid(column=2, row=8, columnspan=1)
    Label(frame, text="Number of Item Hired", font=('bold', 12, 'underline')).grid(column=3, row=8, columnspan=1)
    Label(frame, text="Receipt Number", font=('bold', 12, 'underline')).grid(column=4, row=8, columnspan=1)
    frame.grid(column=5, row=1, columnspan=1, rowspan=10, sticky=N)

    # Multi-Dimensional List
    while name_count < total_entries:
        Label(frame, text=f"#{name_count}").grid(column=0, row=name_count + 9, columnspan=1)
        Label(frame, text=(customer_details[name_count][0])).grid(column=1, row=name_count + 9, columnspan=1)
        Label(frame, text=(customer_details[name_count][1])).grid(column=2, row=name_count + 9, columnspan=1)
        Label(frame, text=(customer_details[name_count][2])).grid(column=3, row=name_count + 9, columnspan=1)
        Label(frame, text=(customer_details[name_count][3])).grid(column=4, row=name_count + 9, columnspan=1)
        name_count += 1


# Validity Checker
def checking_inputs():
    # Global variables that are used
    global tab1
    global customer_details, customer_name, item_hired, number_of_item_hired, customer_receipt, total_entries, Check_Receipts
    input_check = 0
    only_letters = True
    numbers = []
    start_num_value = 0
    for adding_number in range(10):
        indexing_value = start_num_value + adding_number
        numbers.append(str(indexing_value))

    for label_spacing in range(3):  # Loops 4 times
        Label(tab1, text="                    ").grid(column=2, row=2 + label_spacing)
    # Checks if the customer name is not blank, if it is, print error text
    if len(customer_name.get()) == 0:
        Label(tab1, text="Required", fg='red').grid(column=2, row=2)
        input_check = 1
    else:
        # Checking if there is only letters
        check_customer_name = list(customer_name.get())
        for checking in range(len(check_customer_name)):
            if check_customer_name[checking] in numbers:
                only_letters = False

        if customer_name.get().isdigit() or only_letters is False:
            Label(tab1, text="Letters Only", fg='red').grid(column=2, row=2)
            input_check = 1

    # Checks if the item hired is not blank, if it is, print error text
    if len(item_hired.get()) == 0:
        Label(tab1, text="Required", fg='red').grid(column=2, row=3)
        input_check = 1
    # Checks how many of the item is hired with an amount between 1 and 500,
    # if it is not entered or not within range, print error text
    if number_of_item_hired.get().isdigit():
        if int(number_of_item_hired.get()) < 1 or int(number_of_item_hired.get()) > 500:
            Label(tab1, text="1-500 only", fg='red').grid(column=2, row=4)
            input_check = 1
    else:
        Label(tab1, text="1-500 only", fg='red').grid(column=2, row=4)
        input_check = 1
    # Checks if the customer receipt is not blank and an integer only, if it is, print error text
    if item_hired.get().isdigit():
        if len(item_hired.get()) == 0:
            Label(tab1, text="Required, Integer only", fg='red').grid(column=2, row=3)
            input_check = 1

    if not customer_receipt.get():
        convert_sets_to_string = " "

        random_length_number = randint(4, 9)
        Receipt = []
        for i in range(random_length_number):
            Receipt_Number = randint(0, 9)
            Receipt.append(Receipt_Number)

        if Receipt not in Check_Receipts:
            Check_Receipts.append(Receipt)
            convert_sets = Receipt
            for join in range(len(convert_sets)):
                convert_sets_to_string = "".join(str(joined_receipt_num) for joined_receipt_num in convert_sets)

            customer_receipt.delete(0, 'end')
            customer_receipt.insert(0, f"#{convert_sets_to_string}")
        else:
            while Receipt in Check_Receipts:
                for i in range(random_length_number):
                    Receipt_Number = randint(0, 9)
                    Receipt.append(Receipt_Number)
                break

            if Receipt not in Check_Receipts:
                Check_Receipts.append(Receipt)
                convert_sets = Receipt
                for join in range(len(convert_sets)):
                    convert_sets_to_string = "".join(str(joined_receipt_num) for joined_receipt_num in convert_sets)

                customer_receipt.delete(0, 'end')
                customer_receipt.insert(0, f"#{convert_sets_to_string}")

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


# Generates a random receipt number
def generate_receipt_number():
    # Global variables that are used
    global customer_receipt, Check_Receipts
    convert_sets_to_string = " "

    random_length_number = randint(4, 9)
    Receipt = []
    for i in range(random_length_number):
        Receipt_Number = randint(0, 9)
        Receipt.append(Receipt_Number)

    if Receipt not in Check_Receipts:
        Check_Receipts.append(Receipt)
        convert_sets = Receipt
        for join in range(len(convert_sets)):
            convert_sets_to_string = "".join(str(joined_receipt_num) for joined_receipt_num in convert_sets)

        customer_receipt.delete(0, 'end')
        customer_receipt.insert(0, f"#{convert_sets_to_string}")
    else:
        while Receipt in Check_Receipts:
            for i in range(random_length_number):
                Receipt_Number = randint(0, 9)
                Receipt.append(Receipt_Number)
            break

        if Receipt not in Check_Receipts:
            Check_Receipts.append(Receipt)
            convert_sets = Receipt
            for join in range(len(convert_sets)):
                convert_sets_to_string = "".join(str(joined_receipt_num) for joined_receipt_num in convert_sets)

            customer_receipt.delete(0, 'end')
            customer_receipt.insert(0, f"#{convert_sets_to_string}")


# Deletes a row from the list
def delete_row():
    # Global variables that are used
    global customer_details, delete_item, total_entries, name_count, Check_Receipts

    # Finding which row that is going to be deleted and removed it from the list
    del customer_details[int(delete_item.get())]
    del Check_Receipts[int(delete_item.get())]
    total_entries -= 1
    delete_item.delete(0, 'end')

    # Makes a for loop for changing variable to be 'widget' and inside the frame.customer_info()...
    # This will run and destroy the widget in frame.customer_info
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack_forget()  # This basically removed the frame completely once destroyed

    """# clear the last item on the displayed GUI
    Label(main_window, text="       ").grid(column=0, row=name_count + 8)
    Label(main_window, text="       ").grid(column=1, row=name_count + 8)
    Label(main_window, text="       ").grid(column=2, row=name_count + 8)
    Label(main_window, text="       ").grid(column=3, row=name_count + 8)
    Label(main_window, text="       ").grid(column=4, row=name_count + 8)"""
    # Print all other items in the list after that
    print_customer_details()


# Set up for buttons, a function
def setup_buttons():
    # These global variables are used to define variables that are used
    global tab1, tab2
    global customer_details, customer_name, item_hired, number_of_item_hired, customer_receipt, total_entries, delete_item

    # Title
    Label(tab1, text="Julie's Tracker", font=('bold', 18, 'underline')).grid(columnspan=7, row=0, sticky=N)

    # Creates an empty entry and labels along with a dropdown menu
    Label(tab1, text="Customer Name").grid(column=0, row=2, sticky=E)
    customer_name = Entry(tab1)
    customer_name.grid(column=1, row=2)
    Label(tab1, text="Item Hired").grid(column=0, row=3, sticky=E)
    item_hired = Entry(tab1)
    item_hired.grid(column=1, row=3)
    Label(tab1, text="Number of Item Hired").grid(column=0, row=4, sticky=E)
    number_of_item_hired = Entry(tab1)
    number_of_item_hired.grid(column=1, row=4)
    Label(tab1, text="Receipt Number").grid(column=0, row=5, sticky=E)
    customer_receipt = Entry(tab1)
    customer_receipt.grid(column=1, row=5)
    Label(tab1, text="Row #").grid(column=0, row=10, sticky=E)
    delete_item = Entry(tab1)
    delete_item.grid(column=1, row=10)

    # Button Widgets
    Button(tab1, text="Quit", command=quit, width=10).grid(column=6, row=0, sticky=E)  # Make quit button for Tab1
    Button(tab2, text="Quit", command=quit, width=10).grid(column=6, row=0, sticky=E)  # Make quit button for Tab2
    for spacing in range(5):  # a 'for loop' for making a gap, 5 is the number of times it will loop [range being 5]
        Button(tab1, text="Append Details", command=checking_inputs).grid(column=1, row=7)
        Button(tab1, text="Print Details", command=print_customer_details, width=10).grid(column=2, row=7, sticky=E)
        if spacing != 2:
            Label(tab1, text="               ").grid(column=2, row=6 + spacing)
    Button(tab1, text="Generate", command=generate_receipt_number, width=10).grid(column=2, row=5, sticky=E)
    Button(tab1, text="Delete Row", command=delete_row, width=10).grid(column=2, row=10, sticky=E)
    Label(tab1, text="               ").grid(column=2, row=2)

def main():
    # These global variables are used to define variables that are used
    global main_window, frame, tab1, tab2
    global customer_details, customer_name, item_hired, number_of_item_hired, customer_receipt, total_entries, Check_Receipts
    customer_details = []  # Creating an empty list
    total_entries = 0
    Check_Receipts = []
    # Creating the GUI and setup
    main_window = Tk()

    Tabs = ttk.Notebook(main_window)
    tab1 = Frame(Tabs)
    frame = Frame(tab1)
    tab2 = Frame(Tabs)
    Tabs.add(tab1, text="Customer Receipts")
    Tabs.add(tab2, text="View Customer Receipts")
    Tabs.pack(expand=True, fill="both")

    main_window.title("App")
    main_window.geometry("920x500")
    setup_buttons()
    main_window.mainloop()

# After defining the function for main set up, the function is then called to start up the GUI
main()
