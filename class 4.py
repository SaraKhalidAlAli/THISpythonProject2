#class 4 for Customer

class Customer:
    def __init__(self, id:str, email: str, age: int):

        self.id= id
        self.email = email
        self.age= age

    def get_id(self) -> str:
        return self.id

    def get_email(self) -> str:
        return self.email

    def get_age(self) -> int:
        return self.age