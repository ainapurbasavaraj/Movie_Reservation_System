from reservationService.decoders.decoder import Decoder
from reservationService.data.datamodel import ShowDetails,Theatre,Movie,Price

class RegisterUserDbDecoder(Decoder):
    def __init__(self, content) -> None:
        super().__init__(content)
        self.response=[]

    def decode(self,request):
        pass