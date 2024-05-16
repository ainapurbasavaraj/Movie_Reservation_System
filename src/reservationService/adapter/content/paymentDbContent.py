
from reservationService.content import Content

class PaymentDbContent(Content):

    def __init__(self) -> None:
        super().__init__()

class GenerateTicketDbContent(Content):

    def __init__(self) -> None:
        super().__init__()

    def set_booking_id(self,data):
        self.booking_id=data

    def get_booking_id(self):
        return self.booking_id
