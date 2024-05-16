
from logging import exception
from reservationService.decoders.decoder import Decoder
from reservationService.register.request.registerRequest import RegisterRequest

class RegisterUserDecoder(Decoder):

    def __init__(self, content) -> None:
        super().__init__(content)
        self.request=dict()
        self.register_request=RegisterRequest()

    def decode(self, request):
        self.register_request.set_request(request.get_json())
        self.content.set_request(self.register_request.get_request())




