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
    def get_name(self) -> str:
        return self.name

    def get_artist(self) -> str:
        return self.artist

    def get_history_significance(self) -> str:
        return self.history_significance

    def get_date_produced(self) -> str:
        return self.date_produced


#setter fucntions for the attributes in the uml class
    def set_name(self):
        self.name= name

    def set_artist(self):
        self.artist= artist

    def set_history_significance(self):
        self.history_significance= history_significance

    def set_date_produced(self):
        self.date_produced= date_produced
