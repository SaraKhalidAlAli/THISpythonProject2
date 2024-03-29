
#class for artist who creates artworks
class Artist:
    #in def for Initializing an Artist object with a name and nationality.
    def __init__(self, name: str, nationality: str):
        self.name= name
        self.nationality= nationality
        self.artworks= []

    def get_name(self) -> str:
        return self.name
    def get_nationality(self) -> str:
        return self.nationality






