
from reservationService.encoders.encoder import Encoder
from reservationService.dbinterface.sqlbuilder import SqlBuilder
from reservationService.dbinterface.sqlbuildmaker import BuildMaker
from reservationService.dbinterface.db_client import DbClient

class SearchByMovieDbEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)

    def encode(self):
        locationid=self.get_content().get_req_locationid()
        # locationid="1"
        sql_builder=SqlBuilder()
        build_maker=BuildMaker(sql_builder)
        sql_statement=build_maker.BuildSqlSearchByMovie(locationid)
        dbc=DbClient()
        dbc.execute(sql_statement)
        return dbc.get_result()

# if __name__=="__main__":
#     s=SearchByMovieDbEncoder(Encoder)
#     print(s.encode())