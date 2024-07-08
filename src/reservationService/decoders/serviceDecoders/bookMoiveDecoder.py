
from logging import exception
from reservationService.decoders.decoder import Decoder
from reservationService.decoders.serviceDecoders.requestTokenDecoder import RequesTokenDecoder

class BookMovieDecoder(Decoder):

    def __init__(self, content) -> None:
        super().__init__(content)

    def decode(self, request):
        rtd=RequesTokenDecoder(self.get_content())
        rtd.decode(request)
        req_json_obj=request.get_json()
        number_of_seats=req_json_obj.get('NumberOfSeats',None)
        booking_amount=req_json_obj.get('Booking_Amount',None)
        show_id=req_json_obj.get('showid',None)
        service_content=self.get_content().get_content()
        service_content.update({'NumberOfSeats':number_of_seats,'Booking_Amount':booking_amount,'showid':show_id})
        self.get_content().set_content(service_content)
