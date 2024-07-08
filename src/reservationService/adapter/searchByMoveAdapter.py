from reservationService.adapter.dbAdapter import DbAdapter
from reservationService.adapter.content.searchDbContent import SearchByMovieDbContent
from reservationService.adapter.encoder.searchByMovieDbEncoder import SearchByMovieDbEncoder
from reservationService.adapter.decoder.searchByMovieDbDecoder import SearchByMovieDbDecoder

class SearchByMovieAdapter(DbAdapter):
    def __init__(self,usecase_content):
        
        db_content = SearchByMovieDbContent()
        db_encoder = SearchByMovieDbEncoder(db_content)
        db_decoder = SearchByMovieDbDecoder(db_content)
        super().__init__(usecase_content, db_content, db_encoder, db_decoder)

    def pre_execute(self, usecase_content, db_content ):
        db_content.set_req_locationid(usecase_content.get_req_locationid())
    
    def post_execute(self, db_content, usecase_content):
        usecase_content.set_res_movie_list(db_content.get_db_response())

