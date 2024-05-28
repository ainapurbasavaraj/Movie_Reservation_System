
from reservationService.content import Content
#from reservationService.data.datamodel import Location

class SearchByLocationUsecaseContent(Content):

    def __init__(self) -> None:
        super().__init__()
        self.locations= []

    def set_locations(self, locations):
        self.locations.extend(locations)

    def set_location(self, location):
        self.locations.append(location)

    def get_locations(self):
        return self.locations

    def get_location(self, location_id):
        location = [location for location in self.locations if location.id == location_id]
        return location[0] if location else None
           