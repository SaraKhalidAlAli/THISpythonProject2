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

#getter fucntions for the attributes in the uml class
    def get_title(self) -> str:
        return self.title

    def get_artist(self) -> str:
        return self.artist

    def get_history_significance(self) -> str:
        return self.history_significance

    def get_dateproduced(self) -> str:
        return self.dateproduced

#setter fucntions for the attributes in the uml class
    def set_title(self):
        self.title= title

    def set_artist(self):
        self.artist= artist

    def set_history_significance(self):
        self.history_significance= history_significance

    def set_dateproduced(self):
        self.dateproduced= dateproduced
