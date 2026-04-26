# Base class: Person
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print(f"Name: {self.name}, Age: {self.age}")


# Derived class: Employee (inherits from Person)
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        super().__init__(name, age)   # Call Person constructor
        self.employee_id = employee_id
        self.salary = salary

    def display_employee(self):
        print(f"Employee ID: {self.employee_id}, Salary: ₹{self.salary}")


# Manager class (Multiple Inheritance)
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display_manager(self):
        print(f"Department: {self.department}")


# Create object of Manager
mgr = Manager("Vaibhavi", 20, "EMP101", 50000, "IT")

# Access all methods
print("Manager Details:\n")
mgr.display_person()     # from Person
mgr.display_employee()   # from Employee
mgr.display_manager()    # from Manager