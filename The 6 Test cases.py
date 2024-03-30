#FIRST TEST CASE

from class_1 import Art
from class_2 import Artist
from class_6 import EventWebsite


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
