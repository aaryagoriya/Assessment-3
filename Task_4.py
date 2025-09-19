"""Create a Python function called display_requisitons. The function should display the staff's basic information and the total of his requisition."""

# Importing Staff_info function from Task_1
from Task_1 import staff_info
# Importing requisitions_total function from Task_2
from Task_2 import requisitions_total
# Importing requisition_approval function from Task_3
from Task_3 import requisition_approval

"""
    Programming Principle - Open/Closed Principle
    This function is open for extension but closed for modification. New features like extra approval rules or different display formats can be added by updating the called functions, without changing display_requisitions itself.
"""

# Creating a function named display_requisitions
def display_requisitions():
    # Setting while loop so that the looping until the user wants to stop
    while True:
        # Storing all the returned data of staff_info in staff_data variable
        staff_data = staff_info()
        # Calling the requistion_total function to get the total of all items 
        total = requisitions_total(staff_data)
        # if the requisition is approved or pending, and also get the approval reference number if approved
        status, reference_number = requisition_approval(staff_data, total)

        # Printing all the data
        print("\nPrinting Requisitions:")
        print(f"Date: {staff_data['Date']}")
        print(f"Requisition ID: {staff_data['Requisition ID']}")
        print(f"Staff ID: {staff_data['Staff ID']}")
        print(f"Staff Name: {staff_data['Staff Name']}")
        print(f"Total: ${total}")
        print(f"Status: {status}")
        # Settting if condition to print the reference number
        if reference_number:
            print(f"Approval Reference Number: {reference_number}")

        # Taking input and storing it in variable named final_input and also using lower() to convert the entered text in lower case
        final_input = input("\nDo you want to process another requisition? (y/n): ").lower()
        # Setting if condition to check if the user will enter any other input then y, it will end the loop
        if final_input != 'y':
            print("End")
            break

# Calling function or running it
display_requisitions()