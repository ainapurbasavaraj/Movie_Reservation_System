from json import load
from reservationService.encoders.encoder import Encoder
from reservationService.dbinterface.sqlbuilder import SqlBuilder
from reservationService.dbinterface.sqlbuildmaker import BuildMaker
from reservationService.dbinterface.db_client import DbClient

class SearchByLocationDbEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)

    def encode(self):

        sql_builder=SqlBuilder()
        buil_dmaker=BuildMaker()
        sql_statement=buil_dmaker.Build_sql_searchByLocation(sql_builder)
        dbc=DbClient(sql_statement)
        dbc.execute()
        return dbc.get_result()
