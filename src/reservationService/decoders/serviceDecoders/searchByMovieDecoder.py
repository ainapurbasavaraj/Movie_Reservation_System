
from reservationService.decoders.decoder import Decoder

class SearchByMovieDecoder(Decoder):
    def __init__(self, content) -> None:
        super().__init__(content)
        self.content=content

    def decode(self,data):
        #set the request object with locationID
        self.content.set_request(data)
        
 