#FIRST TEST CASE

from class_1 import Art
from class_2 import Artist
from class_6 import EventWebsite
from class_4 import Customer
from Class_5 import Employee
from class_3 import Ticket



def test_add_art():
    artist = Artist("Leonardo da Vinci", "Italian") #artist object

#Creating new artworks to test
    artwork1 =Art("Mona Lisa", "Leonardo da Vinci", "An iconic portrait of Lisa Gherardini", "c. 1503")
    artwork2 =Art("The Last Supper", "Leonardo da Vinci", "A mural painting depicting the Last Supper of Jesus", "1495–1498")

  #adding the artworks to the museum here
    artist.add_artworks(artwork1)
    artist.add_artworks(artwork2)

    # Output
    print("\n<</*Louvre Museum Event*\>> \n")
    print("New artworks added to the museum:")
    for artwork in artist.set_artworks():
        print("- Name:", artwork.get_title())
        print("  Artist:", artwork.get_artist())
        print("  History Significance:", artwork.get_history_significance())
        print("  Date Produced:", artwork.get_dateproduced(), "\n")

# Run the test case
test_add_art()

print("---------------------------------------------------------------------------\n")

#SECOND TEST CASE

#having an opening of a new exhibition or event at the museum "Concert, Le Trio Joubran" with information like ulr and
def open_new_exhibition():
    #creating the object of event website information to print
    event_website = EventWebsite("Concert, Le Trio Joubran", "Tradition of Arabic oud music and also celebrate the culture of their home country, Palestine, by setting the words of renowned poet Mahmoud Darwish to music.", "https://www.louvreabudhabi.ae/en/programmes/performing-arts/performing-arts-2", "Louvre Abu Dhabi")

#Outputs for info
    print("Announcement!!! New exhibition opened at the museum: \n")
    print("- Event Name:",event_website.get_event_name())
    print("- Event Description:",event_website.get_event_description())
    print("- Location:",event_website.get_location())
    print("- URL:",event_website.get_url())

#running the test case
open_new_exhibition()
print("\n---------------------------------------------------------------------------\n")



# THIRD TEST CASE
# WITH 4 EXAMPLES

#here I mixed the test cases of The purchase of tickets by an individual or tour group for an event-
#-and with "display of payment receipts for purchasing (one or more) tickets. The final bill should be presented to the customer upon completion of the purchase."
# where we have test cases 3, 4, 5, 6; I just wanted the output to look nice :)

def purchase_tickets():
    adult_customer = Customer("123", "adult@example.com", 30)
    child_customer = Customer("456", "child@example.com", 10)
    senior_customer = Customer("789", "senior@example.com", 70)
    group_customer = Customer("101", "group@example.com", 25)

    #definig the event details
    event_name = "Concert, Le Trio Joubran"

    #putting into place the ticket prices for diffrenet instances
    adult_ticket_price = 63.0
    child_ticket_price = 0.0  # Free for children
    senior_ticket_price = 0.0  # Free for seniors
    group_ticket_price = 63.0 * 0.5  # 50% discount for groups


    #creating the ticket objects for each customer for the test case to look at the different recipes people get
    adult_ticket = Ticket(1, event_name, adult_ticket_price, False)
    child_ticket = Ticket(2, event_name, child_ticket_price, False)
    senior_ticket = Ticket(3, event_name, senior_ticket_price, False)
    group_ticket = Ticket(4, event_name, group_ticket_price, True)

    #provideing output so we can see the purchase of tickets by an individual or tour group for an event andddd recipes
    print("Tickets purchased:")
    print("Adult Ticket:")
    print("- Customer ID:", adult_customer.get_id())
    print("- Event:", adult_ticket.get_event())
    print("- Price:", adult_ticket.get_price())
    print("- Group Ticket:", "Yes" if adult_ticket.is_group else "No")
    print("-----------------")
    # Output for Child Ticket
    print("Child Ticket:")
    print("- Customer ID:", child_customer.get_id())
    print("- Event:", child_ticket.get_event())
    print("- Price:", child_ticket.get_price())
    print("- Group Ticket:", "Yes" if child_ticket.is_group else "No")
    print("-----------------")
    # Output for Senior Ticket
    print("Senior Ticket:")
    print("- Customer ID:", senior_customer.get_id())
    print("- Event:", senior_ticket.get_event())
    print("- Price:", senior_ticket.get_price())
    print("- Group Ticket:", "Yes" if senior_ticket.is_group else "No")
    print("-----------------")
    # Output for Group Ticket
    print("Group Ticket:")
    print("- Customer ID:", group_customer.get_id())
    print("- Event:", group_ticket.get_event())
    print("- Price:", group_ticket.get_price())
    print("- Group Ticket:", "Yes" if group_ticket.is_group else "No")

# Run the test case
purchase_tickets()