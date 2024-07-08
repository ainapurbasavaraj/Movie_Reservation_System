from reservationService.decoders.decoder import Decoder

class SearchByTheatreDecoder(Decoder):
    def __init__(self, content) -> None:
        super().__init__(content)

    def decode(self, request):
        print(f'request --> {request}')
        self.content.set_request(request)