class Employee:
    # Static variable for the company name
    company_name = "ABC Corp"

    # Static variable to store the total number of employees
    total_employees = 0

    def __init__(self, employee_id, employee_name, employee_role):
        # Initialize instance variables
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_role = employee_role

        # Increment the total number of employees
        Employee.total_employees += 1

    @classmethod
    def get_total_employees(cls):
        # Class method to retrieve the total number of employees
        return cls.total_employees

    def display_details(self):
        # Method to display employee details
        print("Employee ID:", self.employee_id)
        print("Employee Name:", self.employee_name)
        print("Employee Role:", self.employee_role)
        print("Company Name:", self.company_name)
        print()

# Creating employee instances
employee1 = Employee(1, "John Doe", "Manager")
employee2 = Employee(2, "Alice Smith", "Engineer")
employee3 = Employee(3, "Bob Johnson", "Designer")

# Calling the class method to retrieve the total number of employees
total_employees = Employee.get_total_employees()
print("Total Employees in", Employee.company_name + ":", total_employees)

# Displaying employee details
print("Employee 1 Details:")
employee1.display_details()

print("Employee 2 Details:")
employee2.display_details()

print("Employee 3 Details:")
employee3.display_details()
