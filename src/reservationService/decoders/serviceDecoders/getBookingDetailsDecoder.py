
from logging import exception
from reservationService.decoders.decoder import Decoder
from reservationService.decoders.serviceDecoders.requestTokenDecoder import RequesTokenDecoder

class GetBookingDetailsDecoder(Decoder):

    def __init__(self, content) -> None:
        super().__init__(content)
        self.request_params=dict()

    def decode(self, request):
        service_content=self.get_content()
        raw_token=request.get('token',None)
        token=raw_token.split()[1]
        userid=request.get('userid',None)
        self.request_params.update({
            "userid":userid,
            "token":token
        })

        service_content.set_content(self.request_params)