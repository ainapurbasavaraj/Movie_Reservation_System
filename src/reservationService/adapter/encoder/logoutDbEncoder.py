from reservationService.encoders.encoder import Encoder
from reservationService.dbinterface.sqlbuilder import SqlBuilder
from reservationService.dbinterface.sqlbuildmaker import BuildMaker
from reservationService.dbinterface.db_client import DbClient
from datetime import datetime, timedelta
from secrets import token_urlsafe

class LogoutDbEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)

    def encode(self):
        request_data=self.get_content().get_content()
        token=request_data.get('token',None)
        print(f'token inside encoder --> {token}')
        userid=request_data.get('userid',None)
        return token,userid


class InsertTokenEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)

    def encode(self):
        return self.get_content().get_content()