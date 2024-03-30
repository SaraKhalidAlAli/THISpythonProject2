# class 5; Employee
'''This class represents an employee with attributes for name and role, along with getter and setter methods for accessing and modifying these attributes.
'''
class Employee:

#useing __init__ method that initializes an Employee object with the provided name and role.
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

