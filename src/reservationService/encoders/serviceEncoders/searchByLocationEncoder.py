from json import load
from reservationService.encoders.encoder import Encoder

class SearchByLocationEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)

    def encode(self):
        #location=self.content.get_locations()
        location_response=self.content.get_response()
        print(f'location_response --> {location_response}')
        # location=location_response.get_locations()
        # if location:
        #     return location
        return location_response
