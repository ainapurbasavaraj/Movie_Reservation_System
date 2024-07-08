from reservationService.encoders.encoder import Encoder
from reservationService.dbinterface.sqlbuilder import SqlBuilder
from reservationService.dbinterface.sqlbuildmaker import BuildMaker
from reservationService.dbinterface.db_client import DbClient

class RegisterUserDbEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)

    def encode(self):
        reg_info=self.get_content().get_register_info()
        sql_builder=SqlBuilder()
        build_maker=BuildMaker(sql_builder)
        sql_statement=build_maker.RegisterUser(reg_info)
        print(f'sql_statement --> {sql_statement}')
        dbc=DbClient()
        dbc.execute(sql_statement)
        return dbc.get_result()