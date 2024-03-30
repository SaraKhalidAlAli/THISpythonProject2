#class 4 for Customer

class Customer:
    def __init__(self, id:str, email: str, age: int):

        self.id= id
        self.email = email
        self.age= age

#Getter functions
    def get_id(self) -> str:
        return self.id
        # Return the customer ID
    def get_email(self) -> str:
        return self.email
        # Return the customer email
    def get_age(self) -> int:
        return self.age
        # Return the customer age
