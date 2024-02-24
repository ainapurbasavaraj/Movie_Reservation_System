
class SearchByLocationResponse:

    def __init__(self) -> None:
        self.locations = list()

    def set_location(self, location):
        self.locations.append(location)

    def get_locations(self):
        self.locations

    def get_location(self, locationId):
        locationobj = [location for location in self.locations
                    if location.id == locationId]

        if locationobj:
            return locationobj[0]

