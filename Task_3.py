"""This function is built on Tasks 1 and 2. Write a Python function called  requisition_approval.  This function is intended to make approval decisions based on the conditions provided in the 'Responding to requests' section below.

This function should use the function  requisitions_total (from Task 2) as input.

Responding to requests:

The default status of all submitted requisitions should be set as “Pending”. Once a requisition is approved, the status should change to “Approved”.
If the Total of a submitted requisition is less than $500, the system should automatically approve the requisition and assign an approval reference number based on the following rule.
Staff ID followed by the last three characters of the Requisition ID.
If the Total of a submitted requisition is $500 or higher, the program should automatically set the status to  “Pending”."""

# Import the requisitions_total function from the file Task_2
from Task_2 import requisitions_total

"""
    Programming Principle - Single Responsibility Principle
    This function makes approval decisions only. It sets requisition status to “Pending” or “Approved” and generates an approval reference number when needed, based on the total amount. 
"""

# Creating a function named requisition_approval that takes staff_data and total as inputs
def requisition_approval(staff_data, total):
    # Created a status variable and storing pending status in it
    status = "Pending"
    # Creating a reference_number variable and storing none datatype in it so i won't generate reference number if the status is pending
    reference_number = None
    # Setting a condition If the total is less than 500 dollars, the program will automatically set approved in status
    if total < 500:
        status = "Approved"
         # Generating the reference number with Staff_ID + Requisition ID
        reference_number = staff_data["Staff ID"] + staff_data["Requisition ID"][-3:]
    # Printing total amount with f function "Total: variable"
    print(f"Total: ${total}")
    # Printing status with f function "Status: variable"
    print(f"Status: {status}")
    # Setting condition if there is an approved requisition print the reference number
    if reference_number:
        print(f"Approval Reference Number: {reference_number}")
    # Returning the status and reference_number
    return status, reference_number