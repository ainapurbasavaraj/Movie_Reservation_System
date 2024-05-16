from reservationService.adapter.dbAdapter import DbAdapter
from reservationService.adapter.content.registerDbContent import RegisterUserDbContent
from reservationService.adapter.encoder.registerUserDbEncoder import RegisterUserDbEncoder
from reservationService.adapter.decoder.RegisterUserDbDecoder import RegisterUserDbDecoder

class ValidateInputParams(DbAdapter):
    def __init__(self,usecase_content):
        
        self.db_content = RegisterUserDbContent()
        self.db_encoder = RegisterUserDbEncoder(self.db_content)
        self.db_decoder = RegisterUserDbDecoder(self.db_content)
        #self.set_encoder(SearchByLocationDbEncoder(self.get_adapter_content()))
        #self.set_decoder(SearchByLocationDbDecoder(self.get_adapter_content()))
        super().__init__(usecase_content, self.db_content, self.db_encoder, self.db_decoder)

    def pre_execute(self, usecase_content, db_content ):
        db_content.set_register_info(usecase_content.get_request_usecase_content())

    
    def execute(self):
        db_content=self.get_adapter_content()
        self.pre_execute(self.get_usecase_content(), db_content)        
        request_params=db_content.get_register_info()
        success='SUCCESS'
        failure='FAILURE'
        #validate if the userid is not null and its a string
        for key,val in request_params.items():
            if not isinstance(val,str):
                return failure

            if key == "emailid":
                if not len(val.split('@'))==2:
                    return failure

            if key=='phoneNumber':
                if ((len(val)!=13) or ('+' not in val)):
                    return failure
            # if not isinstance(request_params.get('userid'),str):
            #     return failure
        return success

    
    def post_execute(self, db_content, usecase_content):
        pass
        # usecase_content.set_res_movie_list(db_content.get_db_response())

class CheckIfUserIDIsUnique(DbAdapter):
    def __init__(self,usecase_content):
        
        db_content = RegisterUserDbContent()
        db_encoder = RegisterUserDbEncoder(db_content)
        db_decoder = RegisterUserDbDecoder(db_content)
        #self.set_encoder(SearchByLocationDbEncoder(self.get_adapter_content()))
        #self.set_decoder(SearchByLocationDbDecoder(self.get_adapter_content()))
        super().__init__(usecase_content, db_content, db_encoder, db_decoder)

    def pre_execute(self, usecase_content, db_content ):
        db_content.set_register_info(usecase_content.get_request_usecase_content())
        pass

    
    def execute(self):
        self.pre_execute(self.get_usecase_content(), self.get_adapter_content())        
        #send and recv data to db interface
        registration_status = self.encoder.encode()
        print(f'registration_status --> {registration_status}')
    #     print(f'list_of_movies --> {list_of_movies}')


    #     #location.id,location.name=1,'Bengaluru'
    #     #db_content=self.get_adapter_content()
    #     #db_content.set_location(location)

    #     decoded_movie_list_from_db=self.decoder.decode(list_of_movies) #pass response to decoder
    #     print(f'decoded_movie_list_from_db --> {decoded_movie_list_from_db}')
    #     self.get_adapter_content().set_db_response(decoded_movie_list_from_db)
    #     self.post_execute(self.get_adapter_content(), self.get_usecase_content())
        return "SUCCESS" 

    
    def post_execute(self, db_content, usecase_content):
        pass
        # usecase_content.set_res_movie_list(db_content.get_db_response())

class RegisterUserAdapter(DbAdapter):
    def __init__(self,usecase_content):
        
        db_content = RegisterUserDbContent()
        db_encoder = RegisterUserDbEncoder(db_content)
        db_decoder = RegisterUserDbDecoder(db_content)
        #self.set_encoder(SearchByLocationDbEncoder(self.get_adapter_content()))
        #self.set_decoder(SearchByLocationDbDecoder(self.get_adapter_content()))
        super().__init__(usecase_content, db_content, db_encoder, db_decoder)

    def pre_execute(self, usecase_content, db_content ):
        db_content.set_register_info(usecase_content.get_request_usecase_content())
        pass

    
    def execute(self):
        self.pre_execute(self.get_usecase_content(), self.get_adapter_content())        
        #send and recv data to db interface
        registration_status = self.encoder.encode()
        #print(f'registration_status --> {registration_status}')
        self.post_execute(self.get_adapter_content(), self.get_usecase_content())
        return registration_status 

    
    def post_execute(self, db_content, usecase_content):
        pass
        # usecase_content.set_res_movie_list(db_content.get_db_response())