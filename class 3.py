#class 3 for Ticket

class Ticket:
    #initializing the ticket object with the attributes
    def __init__(self, ticket_num, event: str, price: float, is_group: bool):
        self.ticket_num=ticket_num
        self.event = event
        self.price = price
        self.is_group = is_group #looks at if the ticket is for a group or individual


#getter functions for retrieving attributes values

    def get_ticket_num(self) ->int:
        return self.ticket_num
    #returning the ticket number
    def get_event(self) -> str:
        return self.event
    #returning the event time
    def get_price(self) -> float:
        return self.price
    #retuning the the ticket price

# Setter methods with parameters to update attributes

    def set_ticket_num(self, ticket_num: int) -> None:
        self.ticket_num = ticket_num
    #setting the ticket number to the provided value
    def set_event(self, event: str) -> None:
        self.event = event
    # setting the event name to the provided value
    def set_price(self, price: float) -> None:
        self.price = price
    #seeting the price to the provided value
    def set_is_group(self, is_group: bool) -> None:
        self.is_group = is_group
    #setting this attribute to indicate if the ticket is for a group

