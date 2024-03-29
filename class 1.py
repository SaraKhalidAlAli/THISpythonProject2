#first class from uml; Art
class Art:
    #constructor method for initializing :
    def __init__(self, title, artist, history_significance, dateproduced):
        self.title= title #initializing title attribute with "title" paremeter
        self.artist= artist
        self.history_significance= history_significance
        self.dateproduced= dateproduced

    def __str__(self):
        return f"Title: {self.title}, Artist: {self.artist}, History significance: {self.history_significance}, Date Created: {self.dateproduced}" #return statement for attributes "

    #gettter
    def

