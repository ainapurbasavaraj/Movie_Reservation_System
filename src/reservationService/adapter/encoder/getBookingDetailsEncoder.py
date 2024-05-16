from reservationService.encoders.encoder import Encoder
from reservationService.dbinterface.sqlbuilder import SqlBuilder
from reservationService.dbinterface.sqlbuildmaker import BuildMaker
from reservationService.dbinterface.db_client import DbClient

class GetBookingDetailsDbEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)
        self.required_content=dict()

    def encode(self):
        return self.get_content().get_content()