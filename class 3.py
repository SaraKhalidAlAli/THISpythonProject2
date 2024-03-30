#class 3 for Ticket

class Ticket:
    def __init__(self, ticket_num, event: str, price: float, is_group: bool):
        self.ticket_num=ticket_num
        self.event = event
        self.price = price
        self.is_group = is_group


    #g