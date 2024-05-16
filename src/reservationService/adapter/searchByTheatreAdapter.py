from reservationService.adapter.dbAdapter import DbAdapter
from reservationService.adapter.content.searchDbContent import SearchByTheatreDbContent
from reservationService.adapter.encoder.searchByTheatreDbEncoder import SearchByTheatreDbEncoder
from reservationService.adapter.decoder.searchByTheatreDbDecoder import SearchByTheatreDbDecoder

class SearchByTheatreAdapter(DbAdapter):
    def __init__(self,usecase_content):
        
        db_content = SearchByTheatreDbContent()
        db_encoder = SearchByTheatreDbEncoder(db_content)
        db_decoder = SearchByTheatreDbDecoder(db_content)
        #self.set_encoder(SearchByLocationDbEncoder(self.get_adapter_content()))
        #self.set_decoder(SearchByLocationDbDecoder(self.get_adapter_content()))
        super().__init__(usecase_content, db_content, db_encoder, db_decoder)

    def pre_execute(self, usecase_content, db_content ):
        db_content.set_req_locationid(usecase_content.get_req_locationid())

    
    # def execute(self):
    #     self.pre_execute(self.get_usecase_content(), self.get_adapter_content())        
    #     #send and recv data to db interface
    #     list_of_movies = self.encoder.encode()
    #     print(f'list_of_movies --> {list_of_movies}')


    #     #location.id,location.name=1,'Bengaluru'
    #     #db_content=self.get_adapter_content()
    #     #db_content.set_location(location)

    #     decoded_movie_list_from_db=self.decoder.decode(list_of_movies) #pass response to decoder
    #     print(f'decoded_movie_list_from_db --> {decoded_movie_list_from_db}')
    #     self.get_adapter_content().set_db_response(decoded_movie_list_from_db)
    #     self.post_execute(self.get_adapter_content(), self.get_usecase_content())
    #     return "SUCCESS" 

    
    def post_execute(self, db_content, usecase_content):
        usecase_content.set_res_theatre_list(db_content.get_db_response())

