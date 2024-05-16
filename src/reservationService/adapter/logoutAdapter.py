#from sre_constants import SUCCESS
from reservationService.adapter.dbAdapter import DbAdapter
from reservationService.adapter.tokenAuthAdapter import TokenAuth
from reservationService.adapter.content.logoutDbContent import LogoutUserDbContent
from reservationService.adapter.encoder.logoutDbEncoder import LogoutDbEncoder
from reservationService.adapter.decoder.logoutDbDecoder import LogoutDbDecoder
from reservationService.dbinterface.sqlbuilder import SqlBuilder
from reservationService.dbinterface.sqlbuildmaker import BuildMaker
from reservationService.dbinterface.db_client import DbClient
from datetime import datetime, timedelta
from secrets import token_urlsafe

class AuthenticateToken(TokenAuth):
    def __init__(self, usecase_content):
        super().__init__(usecase_content)


    # def __init__(self,usecase_content):
        
    #     self.db_content = LogoutUserDbContent()
    #     self.db_encoder = LogoutDbEncoder(self.db_content)
    #     self.db_decoder = LogoutDbDecoder(self.db_content)
    #     super().__init__(usecase_content, self.db_content, self.db_encoder, self.db_decoder)

    # def pre_execute(self, usecase_content, db_content ):
    #     db_content.set_content(usecase_content.get_content())

    
    # def execute(self):
    #     db_content=self.get_adapter_content()
    #     self.pre_execute(self.get_usecase_content(), db_content)
    #     #fetch the userid and password from db 
   
    #     token,userid = self.encoder.encode()
    #     sql_builder=SqlBuilder()
    #     build_maker=BuildMaker(sql_builder)
    #     sql_statement=build_maker.fetchToken(userid)
    #     #print(sql_statement)
    #     dbc=DbClient()
    #     dbc.execute(sql_statement)
    #     try:
    #         token_from_db=dbc.get_result()[0][0]
    #     except IndexError:
    #         token_from_db=None
    #     #print(f'token_from_db --> {token_from_db}')
    #     token_delete_status=None
    #     if token_from_db==token:
    #         print('token match successful')
    #         sql_builder.result=''
    #         build_maker=BuildMaker(sql_builder)
    #         sql_statement=build_maker.deleteToken(userid)
    #         print(sql_statement)
    #         dbc.result=None
    #         dbc.execute(sql_statement)
    #         try:
    #             token_delete_status=dbc.get_result()
    #         except IndexError:
    #             pass

    #     print(f'token_delete_status --> {token_delete_status}')
    #     return token_delete_status
    
    # def post_execute(self, db_content, usecase_content):
    #     pass
    #     # usecase_content.set_res_movie_list(db_content.get_db_response())

class DeleteToken(DbAdapter):
    def __init__(self,usecase_content):
        
        self.db_content = LogoutUserDbContent()
        self.db_encoder = LogoutDbEncoder(self.db_content)
        self.db_decoder = LogoutDbDecoder(self.db_content)
        super().__init__(usecase_content, self.db_content, self.db_encoder, self.db_decoder)

    def pre_execute(self, usecase_content, db_content ):
        db_content.set_content(usecase_content.get_content())

    
    def execute(self):
        db_content=self.get_adapter_content()
        self.pre_execute(self.get_usecase_content(), db_content)
        #fetch the userid and password from db 
   
        token,userid = self.encoder.encode()
        sql_builder=SqlBuilder()
        dbc=DbClient()
        build_maker=BuildMaker(sql_builder)
        sql_statement=build_maker.deleteToken(userid)
        dbc.execute(sql_statement)
        try:
            token_delete_status=dbc.get_result()
        except IndexError:
            pass
        return token_delete_status
    
    def post_execute(self, db_content, usecase_content):
        pass
        # usecase_content.set_res_movie_list(db_content.get_db_response())



