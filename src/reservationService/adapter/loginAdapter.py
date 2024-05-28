from sre_constants import SUCCESS
from reservationService.adapter.dbAdapter import DbAdapter
from reservationService.adapter.content.loginDbContent import LoginUserDbContent
from reservationService.adapter.encoder.loginDbEncoder import LoginDbEncoder,InsertTokenEncoder
from reservationService.adapter.decoder.loginDbDecoder import LoginDbDecoder
from reservationService.dbinterface.sqlbuilder import SqlBuilder
from reservationService.dbinterface.sqlbuildmaker import BuildMaker
from reservationService.dbinterface.db_client import DbClient
from datetime import datetime, timedelta
from secrets import token_urlsafe

class ValidateInputParams(DbAdapter):
    def __init__(self,usecase_content):
        
        self.db_content = LoginUserDbContent()
        self.db_encoder = LoginDbEncoder(self.db_content)
        self.db_decoder = LoginDbDecoder(self.db_content)
        #self.set_encoder(SearchByLocationDbEncoder(self.get_adapter_content()))
        #self.set_decoder(SearchByLocationDbDecoder(self.get_adapter_content()))
        super().__init__(usecase_content, self.db_content, self.db_encoder, self.db_decoder)

    def pre_execute(self, usecase_content, db_content ):
        db_content.set_content(usecase_content.get_content())

    
    def execute(self):
        db_content=self.get_adapter_content()
        self.pre_execute(self.get_usecase_content(), db_content)
        #fetch the userid and password from db 
   
        req_creds = self.encoder.encode()
        print(f'req_creds --> {req_creds}')
        sql_builder=SqlBuilder()
        build_maker=BuildMaker(sql_builder)
        sql_statement=build_maker.loginUser(req_creds)
        #print(f'sql_statement --> {sql_statement}')
        dbc=DbClient()
        dbc.execute(sql_statement)
        user_creds_from_db=dbc.get_result()[0]
        print(f'user_creds --> {user_creds_from_db}')
        #authenticate  the userid and password 
        #user_creds=db_content.get_content()
        success='SUCCESS'
        failure='FAILURE'
        if req_creds and len(req_creds)==2:
            if req_creds.get('userid',None)==user_creds_from_db[0] and req_creds.get('password',None)==user_creds_from_db[1]:
                print(f'user is authenticated successfully')
                return success
            else:
                print('user authentication failed')
        else:
            print('fetching the credentials from db failed')
        return failure
    # def execute(self):
    #     db_content=self.get_adapter_content()
    #     self.pre_execute(self.get_usecase_content(), db_content)
    #     #fetch the userid and password from db     
    #     user_creds = self.encoder.encode()[0]
    #     #authenticate  the userid and password 
    #     req_creds=db_content.get_content()
    #     success='SUCCESS'
    #     failure='FAILURE'
    #     if req_creds and len(req_creds)==2:
    #         if req_creds.get('userid',None)==user_creds[0] and req_creds.get('password',None)==user_creds[1]:
    #             print(f'user is authenticated successfully')
    #             return success
    #         else:
    #             print('user authentication failed')
    #     else:
    #         print('fetching the credentials from db failed')
    #     return failure

    
    def post_execute(self, db_content, usecase_content):
        pass
        # usecase_content.set_res_movie_list(db_content.get_db_response())

class GenerateToken(DbAdapter):
    def __init__(self,usecase_content):
        
        db_content = LoginUserDbContent()
        db_encoder = InsertTokenEncoder(db_content)
        db_decoder = LoginDbDecoder(db_content)
        #self.set_encoder(SearchByLocationDbEncoder(self.get_adapter_content()))
        #self.set_decoder(SearchByLocationDbDecoder(self.get_adapter_content()))
        super().__init__(usecase_content, db_content, db_encoder, db_decoder)
        self.token=dict()

    def pre_execute(self, usecase_content, db_content ):
        db_content.set_content(usecase_content.get_content())

    
    def execute(self):
        db_content=self.get_adapter_content()
        self.pre_execute(self.get_usecase_content(), self.get_adapter_content())        
        #send and recv data to db interface
        login_req = self.encoder.encode()
        sql_builder=SqlBuilder()
        build_maker=BuildMaker(sql_builder)
        refresh_timer=self.generateRefreshTimer(10)
        token=self.generateToken()
        sql_statement=build_maker.insertToken(login_req,token,refresh_timer)
        dbc=DbClient()
        dbc.execute(sql_statement)
        db_operation_status=dbc.get_result()
        dbc.close_cursor()
        if db_operation_status=='SUCCESS':
            self.token.update({'token':token})
        elif db_operation_status=="FAILURE":
            sql_builder.result=''
            #dbc.execute("SELECT setval(pg_get_serial_sequence('login_session', 'userid'), (SELECT MAX(userid) FROM login_session) + 1);")
            sql_statement=build_maker.updateToken(login_req,token,refresh_timer)
            print(f'sql_statement --> {sql_statement}')
            dbc1=DbClient()
            dbc1.execute(sql_statement)
            db_operation_status=dbc1.get_result()
            dbc1.close_cursor()
            if db_operation_status=="FAILURE":
                self.token.update({'token':'Token update failed'})
            else:
                self.token.update({'token':token})
        else:
            self.token.update({'token':'user auth failed'})
        
        db_content.set_res_content(self.token)
        
        self.post_execute(db_content,self.get_usecase_content())

        return db_operation_status 

    
    def post_execute(self, db_content, usecase_content):
        usecase_content.set_res_content(db_content.get_res_content())
        
        # usecase_content.set_res_movie_list(db_content.get_db_response())
    def generateRefreshTimer(self,mins):
        now = datetime.now()
        refresh_time=now + timedelta(minutes=mins)
        return refresh_time.strftime("%Y-%m-%d %H:%M:%S")

    def generateToken(self):
        return token_urlsafe(32)

