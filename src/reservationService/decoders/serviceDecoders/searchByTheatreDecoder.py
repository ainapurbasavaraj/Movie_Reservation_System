from reservationService.decoders.decoder import Decoder

class SearchByTheatreDecoder(Decoder):
    def __init__(self, content) -> None:
        super().__init__(content)

    def decode(self, request):
        # location_id=request.split('=')[1]
        # print('decoded location_id --> {location_id}')
        print(f'request --> {request}')
        self.content.set_request(request)