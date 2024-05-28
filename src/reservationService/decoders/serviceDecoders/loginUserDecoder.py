
from logging import exception
from reservationService.decoders.decoder import Decoder

class LoginDecoder(Decoder):

    def __init__(self, content) -> None:
        super().__init__(content)

    def decode(self, request):
        #print(f'request --> {request.get_json()}')
        credentials=request.get_json()
        if isinstance(credentials,dict):
            self.get_content().set_request(credentials)
            # print(f'self.get_content().get_request() --> {self.get_content().get_request()}')
