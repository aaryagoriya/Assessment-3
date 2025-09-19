"""Task 1: Create a Python function called staff_info. Use Python input methods to collect information about a staff member submitting a requisition (i.e., Date, Staff ID, Staff Name, and requisition ID). A unique ID should be generated using a counter plus 10000 and assigned as the requisition ID, as shown in the sample below. This function should return all inputs and the requisition ID."""

counter = 0  # Global counter for unique requisition IDs

"""
    Programming Principle - KISS (Keep It Simple, Stupid)
    This function is kept simple. It asks for staff details and makes a new requisition ID using a counter. It avoids extra steps and only does what is needed.
"""

def staff_info():
    
    global counter  # Global state counter variable
    counter += 1  # Increment counter for each new requisition ID
    req_id = str(counter + 10000)  # Create unique requisition ID starting at 10001

    date = input("Enter Date: ")
    staff_id = input("Enter Staff ID: ")
    staff_name = input("Enter Name: ")

    print("Printing Staff Information:")
    print(f"Date: {date}")
    print(f"Staff ID: {staff_id}")
    print(f"Staff Name: {staff_name}")
    print(f"Requisition ID: {req_id}")

    return {
        "Date": date,
        "Staff ID": staff_id,
        "Staff Name": staff_name,
        "Requisition ID": req_id
    }
