
from logging import exception
from reservationService.decoders.serviceDecoders.requestTokenDecoder import RequesTokenDecoder

class LogoutDecoder(RequesTokenDecoder):

    def __init__(self, content) -> None:
        super().__init__(content)


