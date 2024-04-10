from reservationService.adapter.dbAdapter import DbAdapter
from reservationService.adapter.content.searchDbContent import SearchByLocationDbContent
from reservationService.adapter.encoder.searchByLocationDbEncoder import SearchByLocationDbEncoder
from reservationService.adapter.decoder.searchByLocationDbDecoder import SearchByLocationDbDecoder

class GetLocationAdapter(DbAdapter):
    def __init__(self,usecase_content):
        
        db_content = SearchByLocationDbContent()
        db_encoder = SearchByLocationDbEncoder(db_content)
        db_decoder = SearchByLocationDbDecoder(db_content)
        #self.set_encoder(SearchByLocationDbEncoder(self.get_adapter_content()))
        #self.set_decoder(SearchByLocationDbDecoder(self.get_adapter_content()))
        super().__init__(usecase_content, db_content, db_encoder, db_decoder)

    def pre_execute(self, usecase_content, db_content ):
        pass

    
    def post_execute(self, db_content, usecase_content):
        usecase_content.set_locations(db_content.get_locations())

