#FIRST TEST CASE

from class_2 import Artist
from class_1 import Art
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

print("------------------------------------------------------------------\n")

#SECOND TEST CASE

#having an opening of a new exhibition or event at the museum "Concert, Le Trio Joubran" with information like ulr and
def open_new_exhibition():


