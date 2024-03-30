# class 5; Employee
'''This class represents an employee with attributes for name and role, along with getter and setter methods for accessing and modifying these attributes.
'''
class Employee:

#useing __init__ method that initializes an Employee object with the provided name and role.
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

#Getter functions for name and role
    def get_name(self) ->str:
        return self.name
    # Return the name of the employee
    def get_role(self) ->str:
        return self.role
    # Return the role of the employee

#Setter functions for name and role
    def set_name(self, name: str) -> None:
        self.name = name
     # Update the name of the employee with the provided value
    def set_role(self, role: str):
        self.role = role
    # Update the role of the employee with the provided value


