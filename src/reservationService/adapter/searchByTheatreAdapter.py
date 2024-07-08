from reservationService.adapter.dbAdapter import DbAdapter
from reservationService.adapter.content.searchDbContent import SearchByTheatreDbContent
from reservationService.adapter.encoder.searchByTheatreDbEncoder import SearchByTheatreDbEncoder
from reservationService.adapter.decoder.searchByTheatreDbDecoder import SearchByTheatreDbDecoder

class SearchByTheatreAdapter(DbAdapter):
    def __init__(self,usecase_content):
        
        db_content = SearchByTheatreDbContent()
        db_encoder = SearchByTheatreDbEncoder(db_content)
        db_decoder = SearchByTheatreDbDecoder(db_content)
        super().__init__(usecase_content, db_content, db_encoder, db_decoder)

    def pre_execute(self, usecase_content, db_content ):
        db_content.set_req_locationid(usecase_content.get_req_locationid())
    
    def post_execute(self, db_content, usecase_content):
        usecase_content.set_res_theatre_list(db_content.get_db_response())

