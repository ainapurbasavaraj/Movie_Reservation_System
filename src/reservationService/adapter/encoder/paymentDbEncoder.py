from reservationService.encoders.encoder import Encoder
from reservationService.dbinterface.sqlbuilder import SqlBuilder
from reservationService.dbinterface.sqlbuildmaker import BuildMaker
from reservationService.dbinterface.db_client import DbClient
from datetime import datetime, timedelta
from secrets import token_urlsafe

class PaymentDbEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)
        self.required_content=dict()

    def encode(self):
        return self.get_content().get_content()

    def encode_bookingId(self):
        request=self.get_content().get_content()
        booking_id=request.get('bookingId',None)
        return booking_id