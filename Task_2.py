"""Create a Python function called requisitions_total. Call the function  staff_info from Task 1 and then ask the staff to input his requisition items (i.e., each item name with a price). This function should return the computed total value for all the requisition items."""
# Importing Staff_info function from Task_1
from Task_1 import staff_info 

"""
    Programming Principle - Separation of Concerns
    It collects requisition items (name and price) from user input for a staff member and computes the total value of all the requisition items.
"""

# Creating function named requisitions_total and also takes staff_data as input
def requisitions_total(staff_data): 
    # Setting variable total to 0
    total = 0
    # Setting a while so that i keeps looping until the user ends it
    while True:
        # Asking for input of item name and storing it in item variable
        item = input("Enter item name (leave blank to finish): ")
        # Setting the if else condition so if the user enters empty input the loop stops with break 
        if item == "":
            break
        # Setting a while loop so it keeps asking for price until entered a valid price
        while True:
            try:
                # Asking price input and storing it in the from of integer
                price = int(input(f"Enter price of {item}: "))
            # We used try except so if the user inputs any other thing then integer value it will show a value error
            except ValueError:
                print("Invalid input")
            # If the price is valid it will exit the while loop and try except
            else:
                break
        # Adds and stores the price in a variable named total   
        total += price
    # Prints the total of all items in the form "Total requisition value: variable"
    print(f"\nTotal requisition value: {total}")
    # Returning the total value 
    return total