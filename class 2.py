
#class for artist who creates artworks
class Artist:
    #in def for Initializing an Artist object with a name and nationality.
    def __init__(self, name: str, nationality: str):
        self.name= name
        self.nationality= nationality
        self.artworks= []

#getter functions
    def get_name(self) -> str:
        return self.name
    def get_nationality(self) -> str:
        return self.nationality

#setter functions
    def set_name(self, name: str) :
        self.name = name
    def set_nationality(self, nationality: str):
        self.nationality = nationality




