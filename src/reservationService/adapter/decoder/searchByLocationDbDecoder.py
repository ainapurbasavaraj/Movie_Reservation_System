
from logging import exception
from reservationService.decoders.decoder import Decoder

class SearchByLocationDbDecoder(Decoder):

    def __init__(self, content) -> None:
        super().__init__(content)

    def decode(self, response):
        self.content.set_location(response)
        
