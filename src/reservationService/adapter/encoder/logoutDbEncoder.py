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

        # login_info=self.get_content().get_content()
        # sql_builder=SqlBuilder()
        # build_maker=BuildMaker(sql_builder)
        # sql_statement=build_maker.loginUser(login_info)
        # #print(f'sql_statement --> {sql_statement}')
        # dbc=DbClient()
        # dbc.execute(sql_statement)
        # return dbc.get_result()


class InsertTokenEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)

    def encode(self):
        return self.get_content().get_content()
        # print(f'login_info --> {login_info}')
        # sql_builder=SqlBuilder()
        # build_maker=BuildMaker(sql_builder)
        # refresh_timer=self.generateRefreshTimer(10)
        # token=self.generateToken()
        # sql_statement=build_maker.insertToken(login_info,token,refresh_timer)
        # print(f'sql_statement --> {sql_statement}')
        # dbc=DbClient()
        # dbc.execute(sql_statement)
        # return dbc.get_result()
        # return "SUCCESS"

    # def generateRefreshTimer(self,mins):
    #     now = datetime.now()
    #     refresh_time=now + timedelta(minutes=mins)
    #     return refresh_time.strftime("%Y-%m-%d %H:%M:%S")

    # def generateToken(self):
    #     return token_urlsafe(32)