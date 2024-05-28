
from logging import exception
from reservationService.decoders.decoder import Decoder
from reservationService.decoders.serviceDecoders.requestTokenDecoder import RequesTokenDecoder

class PaymentDecoder(Decoder):

    def __init__(self, content) -> None:
        super().__init__(content)
        self.payment_request=dict()

    def decode(self, request):
        service_content=self.get_content()
        RequesTokenDecoder(service_content).decode(request)
        #service_content.set_request(request)
        payment_request=request.get_json()
        booking_id=payment_request.get("bookingId",None)
        bookingAmount=payment_request.get("bookingAmount",None)
        status=payment_request.get("PaymentDetails",None)
        payment_status=""
        if "success" in status:
            payment_status="SUCCESS"
        else:
            payment_status="FAILURE"

        self.payment_request.update({
            "bookingId":booking_id,
            "bookingAmount":bookingAmount,
            "PaymentDetails":payment_status

        })
        headers=service_content.get_content()
        self.payment_request.update(headers)
        service_content.set_content(self.payment_request)