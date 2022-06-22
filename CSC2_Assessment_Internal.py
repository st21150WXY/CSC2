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
# CONTINUE ON DELETING SYSTEM, WHEN REMOVE FROM TAB 1 and DELETE from TAB 2, it breaks
"""

from tkinter import *  # This imports all the functions from tkinter module
from tkinter import ttk
from random import randint  # This imports randint (random integer) from random module

# This will quit the subroutine
def quit():
    main_window.destroy()

def close_viewer():
    global new_window
    new_window.destroy()

def delete_receipt(receipt_click):
    # Global variables that are used
    global new_window, frame, frame2
    global customer_details, delete_item, total_entries, name_count, save_details, Check_Receipts, customer_name

    # Finds the customer name of the receipt and removes it
    receipt_selected = 0
    for num_receipt in range(len(save_details)):
        if save_details[num_receipt][0] == receipt_click:
            receipt_selected = num_receipt
            break

    # Finding which customer receipt will be removed from the 'save_details' list
    # Each 'try and except' will test if that item in the list is still there, if not it will except as a pass -
    # instead of an error
    try:
        del save_details[receipt_selected]
    except:
        pass
    try:
        del customer_details[receipt_selected]
        customer_details = save_details
    except:
        pass
    try:
        del Check_Receipts[receipt_selected]
        Check_Receipts.append(list(customer_details[receipt_selected][3]))
        for remove_tags in range(len(Check_Receipts)):
            Check_Receipts[remove_tags][remove_tags].remove('#')
    except:
        pass
    total_entries -= 1
    customer_name.delete(0, 'end')

    # Makes a for loop for changing variable to be 'widget' and inside the frame.customer_info()...
    # This will run and destroy the widget in frame.customer_info
    for widget in frame.winfo_children():
        widget.destroy()
    frame.pack_forget()  # This basically removed the frame completely once destroyed
    # Same concept but for the Tab 2 display (viewing customer details)
    for widget2 in frame2.winfo_children():
        widget2.destroy()
    frame2.pack_forget()

    # Closes the window after deleting the item from the list
    new_window.destroy()

    # Print all other items in the list after that
    print_view_customer_details()
    if len(customer_details) != 0:
        print_customer_details()

def print_view_customer_details():
    # Global variables that are used
    global frame2, name_count2, details_button, \
        customer_view_details, specified_buttons, save_details, item_list, item_number_list, name_checker
    name_count2 = 0
    global customer_details, customer_name, item_hired, number_of_item_hired, customer_receipt, total_entries, Check_Receipts

    total_entries = 0
    for how_many_in_list in range(len(customer_details)):
        total_entries += 1

    increment_value = 0
    while name_count2 < total_entries:
        print()
        print(customer_details)
        print(save_details)
        print(Check_Receipts)
        try:
            if save_details[increment_value][0] == customer_details[increment_value][0]:
                Label(frame2, text=f"{customer_details[name_count2][0]}", font=('bold', 12)).grid(column=1,
                                                                                                  row=3 + name_count2)
                customer_view_details.append("Button" + str(name_count2 + 1))

                for details in range(len(customer_view_details)):
                    specified_buttons.append(
                        Button(frame2, text="View Details",
                               command=lambda counter=name_count2: view_details(save_details[counter][0]))
                        .grid(column=2, row=3 + name_count2))
                increment_value += 1
                name_count2 += 1
        except:
            if len(customer_details) == 0:
                if len(save_details) == 0:
                    break
    try:
        customer_view_details.pop(0)
    except:
        pass


def clear_name():
    global customer_name
    customer_name.delete(0, 'end')


# Prints the customer details after appending it
def print_customer_details():
    # Global variables that are used
    global frame, frame2, tab2
    global save_details, name_count, total_entries
    name_count = 0

    Button(tab2, text="Quit", command=quit, width=10).grid(column=3, row=0, sticky=E)
    Label(tab2, text="Customer Receipt Details", font=('bold', 16, 'underline')).grid(columnspan=7, row=0, sticky=N)
    Label(frame2, text="Customer Name", font=('bold', 12, 'underline')).grid(column=1, row=1, columnspan=1, padx=105)
    Label(frame2, text="Details", font=('bold', 12, 'underline')).grid(column=2, row=1, columnspan=1, padx=225)
    frame2.grid(column=0, row=1, columnspan=1, rowspan=10, sticky=N)

    Label(frame, text="Row", font=('bold', 12, 'underline')).grid(column=0, row=8, columnspan=1)
    Label(frame, text="Customer Name", font=('bold', 12, 'underline')).grid(column=1, row=8, columnspan=1)
    Label(frame, text="Item Hired", font=('bold', 12, 'underline')).grid(column=2, row=8, columnspan=1)
    Label(frame, text="Number of Item Hired", font=('bold', 12, 'underline')).grid(column=3, row=8, columnspan=1)
    Label(frame, text="Receipt Number", font=('bold', 12, 'underline')).grid(column=4, row=8, columnspan=1)
    frame.grid(column=5, row=1, columnspan=1, rowspan=10, sticky=N)
    print("---------------------")
    print(total_entries)

    # Multi-Dimensional List
    while name_count < total_entries:
        Label(frame, text=f"#{name_count}").grid(column=0, row=name_count + 9, columnspan=1)
        try:
            Label(frame, text=(customer_details[name_count][0])).grid(column=1, row=name_count + 9, columnspan=1)
        except:
            Label(frame, text=(customer_details[name_count - 1][0])).grid(column=1, row=name_count + 9, columnspan=1)
        try:
            Label(frame, text=(customer_details[name_count][1][len(customer_details[name_count][1]) - 1]))\
                .grid(column=2, row=name_count + 9, columnspan=1)
            Label(frame, text=(customer_details[name_count][2][len(customer_details[name_count][2]) - 1]))\
                .grid(column=3, row=name_count + 9, columnspan=1)
        except:
            Label(frame, text=(customer_details[name_count][1])).grid(column=2, row=name_count + 9, columnspan=1)
            Label(frame, text=(customer_details[name_count][2])).grid(column=3, row=name_count + 9, columnspan=1)
        Label(frame, text=(customer_details[name_count][3])).grid(column=4, row=name_count + 9, columnspan=1)
        name_count += 1


# View Details for the specific customer
def view_details(name_clicked):
    # These are the global variables that will be used
    global new_window, menu
    global customer_details, customer_name, item_hired, number_of_item_hired, customer_receipt, Check_Receipts, \
        save_details

    # Creating new window
    new_window = Toplevel()
    new_window.title(f"{name_clicked} Receipt")
    new_window.geometry("360x550")

    # Adding an option menu to the new window
    a_menu = Menu(new_window)
    new_window.config(menu=a_menu)
    option_menu = Menu(a_menu, tearoff=False, bg="light gray")
    a_menu.add_cascade(label="Options", menu=option_menu)
    # Option for Menu Dropdown
    option_menu.add_command(label="Delete Receipt", command=lambda: delete_receipt(name_clicked))
    option_menu.add_separator()
    option_menu.add_command(label="Close", command=close_viewer)

    for check_for_customer_details in range(len(save_details)):
        if save_details[check_for_customer_details][0] == name_clicked:
            Label(new_window, text=f"Receipt Number: {save_details[check_for_customer_details][3]}").grid(column=0, row=1, sticky=NW)
            Label(new_window, text=f"{name_clicked}", font=('bold', 15, 'underline')).grid(column=1, row=2, sticky=N)
            Label(new_window, text="Items:", font=('bold', 13, 'underline')).grid(column=0, row=3, sticky=W)
            for print_items in range(len(save_details[check_for_customer_details][1])):
                Label(new_window, text=f"{save_details[check_for_customer_details][1][print_items]} "
                                       f"x{save_details[check_for_customer_details][2][print_items]}")\
                    .grid(column=0, row=4 + print_items, sticky=W)


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
    global frame2, name_count2, details_button, \
        customer_view_details, specified_buttons, save_details, item_list, item_number_list, name_checker
    name_count2 = 0
    global customer_details, customer_name, item_hired, number_of_item_hired, customer_receipt, total_entries
    # Appends every detail into one list
    customer_details.append([customer_name.get(), [item_hired.get()], [number_of_item_hired.get()], customer_receipt.get()])

    # Removes and changes the list if the customer name is the same
    same_name = 0
    for check_customer_list in range(len(customer_details)):
        if customer_details[check_customer_list][0] == customer_name.get():
            same_name += 1
            if same_name >= 2:
                customer_details.pop()
                for check_customer_list2 in range(len(customer_details)):
                    if customer_details[check_customer_list2][0] == customer_name.get():
                        customer_details[check_customer_list2][1].append(item_hired.get())
                        customer_details[check_customer_list2][2].append(number_of_item_hired.get())

    # This is the starting list, which is empty
    if len(save_details) == 0:  # This checks for whether the list is empty or not, this will only work once
        # If the list is empty append details
        save_details.append([customer_name.get(), [], [], customer_receipt.get()])
        name_checker = 0

    # This checks if the name entered is in the customer_details list, if it is not then it will append customer details
    for check_name in range(len(save_details)):
        print(customer_details)
        if save_details[check_name][0] != customer_name.get():
            name_checker += 1
            if name_checker >= len(save_details):
                save_details.append([customer_name.get(), [], [], customer_receipt.get()])
                # This will pop/remove any additional or extra list of the same name
                for check_name2 in range(len(save_details)):
                    # This will count for every of 'x' in 'save_details' list
                    duplicate_name = sum(x.count(customer_name.get()) for x in save_details)
                    # A condition to check if there is 2 of 'x' 
                    # if so removes the last item from the 'save_details' list
                    if duplicate_name >= 2:
                        save_details.pop()
                name_checker = 0
                break

    # This checks if the name entered is the same, if so it will override the random generated receipt number -
    # with the original one
    for receipt_check in range(len(customer_details)):
        #print(save_details[receipt_check][3])
        if save_details[receipt_check][0] == customer_name.get():
            save_details[receipt_check][3] = customer_details[receipt_check][3]
            #print(customer_details)

    # A 'nested for loop', first one for loop is checking how many customer details there are within item range
    # second for loop inside the first is for checking if the customer name already exists and appends to the same name
    # It checks if the name entered is the same, if so it will add the item to the matching name in a list
    for item_check in range(len(customer_details)):
        #print(customer_details)
        #print(save_details[item_check][item_check])
        if save_details[item_check][0] == customer_name.get():
            save_details[item_check][1].append(item_hired.get())
            save_details[item_check][2].append(number_of_item_hired.get())
            #print(save_details)
            break
        # This checks for whether if the name entered is already in the 'save_details' list, if so append by index
        num = 0  # Set an imaginary number to a variable as 0, used for
        for item_check2 in range(len(customer_details)):
            if save_details[item_check2][0] == customer_name.get():
                if num > 1:
                    save_details[item_check2][1].append(item_hired.get())
                    save_details[item_check2][2].append(number_of_item_hired.get())
                    #print("Not Recognised")
                    #print(save_details)
                    num += 1
        if num - 1 == len(customer_details):
            break
    # Deletes all the values inputted in the entry boxes once appended
    #customer_name.delete(0, 'end')
    item_hired.delete(0, 'end')
    number_of_item_hired.delete(0, 'end')
    customer_receipt.delete(0, 'end')

    # If there are no duplicates of the same nme then create a new label and view button
    if same_name < 2:
        total_entries += 1

        # Creating the Button for Tab 2 and Appending the customer details in them
        increment_value = 0
        while name_count2 < total_entries:
            if save_details[increment_value][0] == customer_details[increment_value][0]:
                Label(frame2, text=f"{customer_details[name_count2][0]}", font=('bold', 12)).grid(column=1, row=3 + name_count2)
                customer_view_details.append("Button" + str(name_count2 + 1))

                for details in range(len(customer_view_details)):
                    specified_buttons.append(
                        Button(frame2, text="View Details",
                               command=lambda counter=name_count2: view_details(save_details[counter][0]))
                        .grid(column=2, row=3 + name_count2))
            name_count2 += 1
        customer_view_details.pop(0)


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

    # Print all other items in the list after that
    print_customer_details()


# Set up for buttons, a function
def setup_buttons():
    # These global variables are used to define variables that are used
    global tab1, tab2, frame2, list_num
    global customer_details, customer_name, item_hired, number_of_item_hired, customer_receipt, total_entries, delete_item

    # Title
    Label(tab1, text="Julie's Tracker", font=('bold', 18, 'underline')).grid(columnspan=7, row=0, sticky=N)
    # Title for Second Tab
    Label(tab2, text="Customer Receipt Details", font=('bold', 16, 'underline')).grid(columnspan=7, row=0, sticky=N)

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

    # Tab 2 Details
    Label(frame2, text="Customer Name", font=('bold', 12, 'underline')).grid(column=1, row=1, columnspan=1, padx=105)
    Label(frame2, text="Details", font=('bold', 12, 'underline')).grid(column=2, row=1, columnspan=1, padx=225)
    frame2.grid(column=0, row=1, columnspan=1, rowspan=10, sticky=N)

    # Button Widgets
    Button(tab1, text="Quit", command=quit, width=10).grid(column=6, row=0, sticky=E)  # Make quit button for Tab1
    Button(tab2, text="Quit", command=quit, width=10).grid(column=3, row=0, sticky=E)  # Make quit button for Tab2
    for spacing in range(5):  # a 'for loop' for making a gap, 5 is the number of times it will loop [range being 5]
        Button(tab1, text="Clear Name", command=clear_name).grid(column=0, row=7, sticky=E)
        Button(tab1, text="Append Details", command=checking_inputs).grid(column=1, row=7)
        Button(tab1, text="Print Details", command=print_customer_details, width=10).grid(column=2, row=7, sticky=E)
        if spacing != 2:
            Label(tab1, text="               ").grid(column=2, row=6 + spacing)
    Button(tab1, text="Generate", command=generate_receipt_number, width=10).grid(column=2, row=5, sticky=E)
    Button(tab1, text="Delete Row", command=delete_row, width=10).grid(column=2, row=10, sticky=E)
    Label(tab1, text="               ").grid(column=2, row=2)


def main():
    # These global variables are used to define variables that are used
    global main_window, frame, frame2, tab1, tab2
    global customer_details, customer_name, item_hired, number_of_item_hired, \
        customer_receipt, total_entries, Check_Receipts, customer_view_details, specified_buttons, save_details, item_list, item_number_list
    customer_details = []  # Creating an empty list
    customer_view_details = []  # This is to store all the Button Number/ID
    specified_buttons = []  # This is to store all the Buttons specified with functions
    save_details = []  # This is to save the customer details when appended, it is used in 'view customer details
    item_list = []  # This is the amount of items ordered with the same customer name
    item_number_list = []  # This is the amount of number of items hired with the same customer name

    total_entries = 0
    Check_Receipts = []
    # Creating the GUI and setup
    main_window = Tk()

    Tabs = ttk.Notebook(main_window)
    tab1 = Frame(Tabs)
    frame = Frame(tab1)
    tab2 = Frame(Tabs)
    frame2 = Frame(tab2)
    Tabs.add(tab1, text="Customer Receipts")
    Tabs.add(tab2, text="View Customer Receipts")
    Tabs.pack(expand=True, fill="both")

    main_window.title("App")
    main_window.geometry("920x500")
    setup_buttons()
    main_window.mainloop()

# After defining the function for main set up, the function is then called to start up the GUI
main()
