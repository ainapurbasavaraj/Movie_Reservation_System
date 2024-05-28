
from reservationService.content import Content

class SearchByLocationDbContent(Content):

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


class SearchByMovieDbContent(Content):

    def __init__(self) -> None:
        self.locationid = None
        self.db_response = None

    def set_req_locationid(self, locationid):
        self.locationid = locationid

    def get_req_locationid(self):
        return self.locationid

    def set_db_response(self,db_response):
        self.db_response=db_response

    def get_db_response(self):
        return self.db_response



class SearchByTheatreDbContent(Content):

    def __init__(self) -> None:
        self.request = None
        self.response = None

    def set_request(self, request):
        self.request = request

    def set_response(self, response):
        self.response = response