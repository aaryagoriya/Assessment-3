
# Assessment-3

## Introduction
This program lets staff making requisition for items. In Task 1, it asks the staff for their details like date, staff ID, and name, and then gives them a special requisition ID. In Task 2, it lets the staff enter the items they want and their prices, then adds up the total cost. In Task 3, the program checks the total cost. If it is less than $500, the request is approved with a reference number. If it is $500 or more, the request stays pending. In Task 4, the program shows all the information clearly, including the staff details, requisition ID, total amount, and approval status. It also allows the user to make more than one requisition if needed.
## Analysis

### Task 1 – staff_info
In this task, the program collects the basic information of the staff member who is making the requisition. It asks the user to enter the date, their staff ID, and their name. At the same time, the program creates a unique requisition ID by using a counter. The counter starts from 10000, and each time a new requisition is made, it increases by one. This way, the first requisition gets ID 10001, the second gets 10002, and so on. Finally, the program prints and returns all the staff details along with the generated requisition ID.

### Task 2 – requisitions_total
In this task, the program asks the staff member to enter the items they want to request along with the price of each item. The user can type the name of an item and then its price. This continues until the user leaves the item name blank, which tells the program they have finished entering items. While entering prices, the program makes sure that only numbers are accepted, so if the user types something invalid, it will ask again. The program then adds up the prices of all the items to calculate the total value of the requisition and prints this total.

### Task 3 – requisition_approval
In this task, the program decides whether the requisition should be approved or left pending. By default, all requisitions are considered “Pending.” If the total cost of the requisition is less than $500, the program changes the status to “Approved” and also creates an approval reference number. This reference number is made by combining the staff ID with the last three digits of the requisition ID. If the total cost is $500 or more, the requisition stays as “Pending” without any reference number. The program then prints out the total, the status, and the reference number if there is one.

### Task 4 – display_requisitions
This is the main task that brings everything together. It starts by calling the function from Task 1 to collect staff information. Then, it calls the function from Task 2 to gather items and calculate the total cost. After that, it calls the function from Task 3 to check if the requisition is approved or pending. Once all the information is ready, the program prints out the complete requisition details, including the date, staff ID, staff name, requisition ID, total cost, status, and approval reference number if approved. At the end, it asks the user if they want to enter another requisition. If the user says yes, the process starts again; if not, the program ends.

## Software Design Principles Used in the Code

This are Software Design Principles used in every Task:

- **KISS (Keep It Simple, Stupid):**
    The staff_info function applies the KISS principle by keeping the logic straightforward. It only collects the required staff details and generates a requisition ID using a simple counter. No unnecessary complexity is added, which makes the function easy to understand and maintain.
- **Separation of Concerns:** The requisitions_total function demonstrates Separation of Concerns by handling only the collection of requisition items and the calculation of their total value. It does not manage staff details or approval logic, keeping these responsibilities separate. This makes the code modular and easier to extend in the future.
- **Single Responsibility Principle (SRP):**
    The requisition_approval function follows the SRP because its sole responsibility is to decide whether a requisition is “Approved” or remains “Pending.” It does not collect data or compute totals but instead focuses only on approval logic. This clear separation improves clarity and maintainability.
- **Open/Closed Principle:** The display_requisitions function reflects the Open/Closed Principle by being open for extension but closed for modification. It relies on other functions (staff_info, requisitions_total, and requisition_approval) to perform specific tasks. If new rules or features are needed, they can be added by updating those supporting functions without altering the display logic.

## Software Design Principles Not Used in the Code

- **D.R.Y (Don’t Repeat Yourself):** The current code doesn’t have much repetition to eliminate. Each function has a unique role, and there aren’t recurring blocks of logic that would need refactoring into shared helpers. Since duplication wasn’t a problem in these tasks, DRY was not explicitly applied.

- **Composition Over Inheritance:** The program does not use classes or inheritance. It is procedural in nature, using functions and data dictionaries. Because no class hierarchy was required, the principle of preferring composition to inheritance does not apply here.

- **Y.A.G.N.I (You Aren’t Gonna Need It):** This principle is about avoiding adding unnecessary features before they are required. The tasks only asked for specific functionality (collect staff info, compute totals, approve requisitions, display results). No extra features were built, so there was no risk of “overengineering.” Hence, YAGNI was not explicitly relevant.

- **Refactor, Refactor, Refactor:** The code is small, simple, and written directly for the exercise, so it hasn’t yet reached the scale where continuous refactoring is necessary. While refactoring is always good practice in larger, evolving projects, the given codebase is straightforward enough not to need major restructuring.

- **Clean Code > Clever Code:** The functions already aim to be simple and easy to read (especially with the use of KISS). However, since the tasks were small and did not present opportunities for “clever” but confusing shortcuts, this principle didn’t explicitly come into play.

- **Avoid Premature Optimisation:** The program deals with simple inputs and small datasets (staff info and requisition items). Performance bottlenecks are unlikely, so optimisation wasn’t necessary at this stage. The focus was correctness and clarity, not efficiency. Therefore, this principle was not applicable.
