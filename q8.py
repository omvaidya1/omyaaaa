# Class to represent an Employee
class Employee:

    # Constructor
    def __init__(self, emp_id, name, department, salary):
        self.emp_id = emp_id
        self.name = name
        self.details = (department, salary)   # Tuple

    # Method to display employee details
    def show_details(self):
        print("Employee ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.details[0])
        print("Salary:", self.details[1])
        print()


# Dictionary to store Employee objects
employees = {}

# Input details for 3 employees
for i in range(3):
    print(f"\nEnter details for Employee {i + 1}")

    emp_id = input("Employee ID: ")
    name = input("Name: ")
    department = input("Department: ")

    try:
        salary = float(input("Salary: "))
    except ValueError:
        print("Invalid salary! Salary set to 0.")
        salary = 0

    # Create object and store in dictionary
    employees[emp_id] = Employee(emp_id, name, department, salary)

# Display all employees
print("\n----- Employee Details -----")
for emp in employees.values():
    emp.show_details()