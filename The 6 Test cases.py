#First test case

def test_add_art():
    artist = Artist("Leonardo da Vinci", "Italian") #artist object

#Creating new artworks to test
    artwork1 =Art("Mona Lisa", "Leonardo da Vinci", "An iconic portrait of Lisa Gherardini", "c. 1503")
    artwork2 =Art("The Last Supper", "Leonardo da Vinci", "A mural painting depicting the Last Supper of Jesus", "1495–1498")

  #adding the artworks to the museum here
    artist.add_artwork(artwork1)
    artist.add_artwork(artwork2)

    # Output
    print("<</*Louvre Museum Event*\>> \n")
    print("New artworks added to the museum:")
    for artwork in artist.get_artworks():
        print("- Name:", artwork.get_name())
        print("  Artist:", artwork.get_artist())
        print("  History Significance:", artwork.get_history_significance())
        print("  Date Produced:", artwork.get_date_produced(), "\n")








