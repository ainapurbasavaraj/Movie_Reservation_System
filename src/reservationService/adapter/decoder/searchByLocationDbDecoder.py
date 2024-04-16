
from logging import exception
from reservationService.decoders.decoder import Decoder
from reservationService.data.datamodel import Location

class SearchByLocationDbDecoder(Decoder):

    def __init__(self, content) -> None:
        super().__init__(content)

    def decode(self, response):
        for location in response:
            self.content.set_location(Location(location[0],location[1]))
        
