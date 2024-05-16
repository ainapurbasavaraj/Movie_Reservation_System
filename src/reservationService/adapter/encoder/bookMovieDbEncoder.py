from reservationService.encoders.encoder import Encoder
from reservationService.dbinterface.sqlbuilder import SqlBuilder
from reservationService.dbinterface.sqlbuildmaker import BuildMaker
from reservationService.dbinterface.db_client import DbClient
from datetime import datetime, timedelta
from secrets import token_urlsafe

class CheckSeatAvailability(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)
        self.required_content=dict()

    def encode(self):
        req_content=self.get_content().get_content()
        showid=req_content.get('showid',None)
        NumberOfSeats=req_content.get('NumberOfSeats',None)
        self.required_content.update({'showid':showid,'NumberOfSeats':NumberOfSeats})
        return self.required_content
        # login_info=self.get_content().get_content()
        # sql_builder=SqlBuilder()
        # build_maker=BuildMaker(sql_builder)
        # sql_statement=build_maker.loginUser(login_info)
        # #print(f'sql_statement --> {sql_statement}')
        # dbc=DbClient()
        # dbc.execute(sql_statement)
        # return dbc.get_result()


class GenerateBookingIdEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)

    def encode(self):
        return self.get_content().get_content()

    def encode_bookingId(self):
        return self.get_content().get_booking_id()

class GenerateBookingResponseEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)

    def encode(self):
        req_content= self.get_content().get_content()
        return req_content.get('showid',None)