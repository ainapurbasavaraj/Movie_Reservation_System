
from reservationService.decoders.decoder import Decoder

class SearchByLocationDecoder(Decoder):

    def __init__(self, content) -> None:
        super().__init__(content)

    def decode(self, request):
        pass
