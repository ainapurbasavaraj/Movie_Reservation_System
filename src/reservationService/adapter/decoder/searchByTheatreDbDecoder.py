from reservationService.decoders.decoder import Decoder

class SearchByTheatreDbDecoder(Decoder):
    def __init__(self, content) -> None:
        super().__init__(content)

    def decoder(self, request):
        
        pass