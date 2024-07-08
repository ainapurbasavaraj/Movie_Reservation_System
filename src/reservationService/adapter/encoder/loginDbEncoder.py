from reservationService.encoders.encoder import Encoder
from reservationService.dbinterface.sqlbuilder import SqlBuilder
from reservationService.dbinterface.sqlbuildmaker import BuildMaker
from reservationService.dbinterface.db_client import DbClient
from datetime import datetime, timedelta
from secrets import token_urlsafe

class LoginDbEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)

    def encode(self):
        return self.get_content().get_content()


class InsertTokenEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)

    def encode(self):
        return self.get_content().get_content()