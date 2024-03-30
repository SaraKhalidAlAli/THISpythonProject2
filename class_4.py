#class 4 for Customer

class Customer:
    def __init__(self, id:str, email: str, age: int):

        self.id= id
        self.email = email
        self.age= age

#Getter functions
#to allow external code to retrieve the values of private or protected attributes of an object without directly accessing them.
    def get_id(self) -> str:
        return self.id
        # Return the customer ID
    def get_email(self) -> str:
        return self.email
        # Return the customer email
    def get_age(self) -> int:
        return self.age
        # Return the customer age
#Setter function
    def set_id(self, id: str):
        self.id = id
    #setting customer ID to the provided value
    def set_email(self, email: str):
        self.email = email
    #setting ID to the provided value
    def set_age(self, age: int):
        self.age = age
    #setting age to the provided value

