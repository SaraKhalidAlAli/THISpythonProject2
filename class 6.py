#class 6; EventWebsite

class EventWebsite:
    def __init__(self, event_name:str, event_description:str, url:str, location:str):
        self.event_name = event_name  #storing the name of the event
        self.event_description = event_description  #storing the description of the event
        self.url = url  #storing the URL of the event
        self.location = location  #storing the location of the event

#Getter functions for all the attributes
    def get_event_name(self) ->str:
        return self.event_name
    #returning name of event
    def get_event_description(self) -> str:
        return self.event_description
    #returning description of the event
    def get_url(self) -> str:
        return self.url
    #returning the URL of the event
    def get_location(self) -> str:
        return self.location
    #returning the location of the event


#Setter functions for all the attributes
    def set_event_name(self, event_name: str) -> None:
        # Update the name of the event with the provided value
        self.event_name = event_name

    def set_event_description(self, event_description: str) -> None:
        self.event_description = event_description

    def set_url(self, url: str) -> None:
        self.url = url

    def set_location(self, location: str) -> None:
        self.location = location
