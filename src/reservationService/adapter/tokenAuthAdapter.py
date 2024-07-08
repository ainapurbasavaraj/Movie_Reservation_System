from sre_constants import SUCCESS
from reservationService.adapter.dbAdapter import DbAdapter
from reservationService.adapter.content.tokenDbContent import TokenDbContent
from reservationService.adapter.encoder.tokenDbEncoder import TokenDbEncoder
from reservationService.adapter.decoder.tokenDbDecoder import TokenDbDecoder
from reservationService.dbinterface.sqlbuilder import SqlBuilder
from reservationService.dbinterface.sqlbuildmaker import BuildMaker
from reservationService.dbinterface.db_client import DbClient
# from reservationService.data.reservationLogger import ReservationLogger
from reservationService.Log import log
class TokenAuth(DbAdapter):
    def __init__(self,usecase_content):
        
        self.db_content = TokenDbContent()
        self.db_encoder = TokenDbEncoder(self.db_content)
        self.db_decoder = TokenDbDecoder(self.db_content)
        # log=ReservationLogger.get_logger()
        super().__init__(usecase_content, self.db_content, self.db_encoder, self.db_decoder)

    def pre_execute(self, usecase_content, db_content ):
        db_content.set_content(usecase_content.get_content())

    
    def execute(self):
        log.info("TokenAuth validation started ")
        db_content=self.get_adapter_content()
        self.pre_execute(self.get_usecase_content(), db_content)
        #fetch the userid and password from db 
   
        token,userid = self.encoder.encode()
        log.info(f"The token and userid decoded values are : {token}, {userid}")
        sql_builder=SqlBuilder()
        build_maker=BuildMaker(sql_builder)
        sql_statement=build_maker.fetchToken(userid)
        log.info(f'The sql statement to be executed is: {sql_statement}')
        dbc=DbClient()
        dbc.execute(sql_statement)
        try:
            token_from_db=dbc.get_result()[0][0]
        except IndexError:
            log.error(f'db execution failed with return value = {token_from_db}')
            token_from_db=None
        token_auth_status=None
        if token_from_db==token:
            token_auth_status='SUCCESS'
            log.info(f'token authentication is successfull as token from db {token_from_db} == token recieved in request {token}')
        log.info("TokenAuth validation completed ")
        return token_auth_status
    
    def post_execute(self, db_content, usecase_content):
        pass



