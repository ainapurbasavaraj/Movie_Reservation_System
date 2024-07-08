from reservationService.encoders.encoder import Encoder
from reservationService.dbinterface.sqlbuilder import SqlBuilder
from reservationService.dbinterface.sqlbuildmaker import BuildMaker
from reservationService.dbinterface.db_client import DbClient

class SearchByTheatreDbEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)


    def encode(self):
        locationid=self.get_content().get_req_locationid()
        print(f'locationid ---> {locationid}')
        sql_builder=SqlBuilder()
        build_maker=BuildMaker(sql_builder)
        sql_statement=build_maker.BuildSqlSearchByTheatre(locationid)
        dbc=DbClient()
        dbc.execute(sql_statement)
        return dbc.get_result()