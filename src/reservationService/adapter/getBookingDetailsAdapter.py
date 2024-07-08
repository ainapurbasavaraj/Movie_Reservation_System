from sre_constants import SUCCESS
from reservationService.adapter.dbAdapter import DbAdapter
from reservationService.adapter.content.getBookingDetailsDbContent import GetBookingDetailsDbContent
from reservationService.adapter.encoder.getBookingDetailsEncoder import GetBookingDetailsDbEncoder
from reservationService.adapter.decoder.getBookingDetailsDbDecoder import GetBookingDetailsDbDecoder
from reservationService.dbinterface.sqlbuilder import SqlBuilder
from reservationService.dbinterface.sqlbuildmaker import BuildMaker
from reservationService.dbinterface.db_client import DbClient
from reservationService.data.datamodel import ShowDetails,Theatre,Movie,Price
import uuid

class GetBookingDetailsAdapter(DbAdapter):
    def __init__(self,usecase_content):
        
        self.db_content = GetBookingDetailsDbContent()
        self.db_encoder = GetBookingDetailsDbEncoder(self.db_content)
        self.db_decoder = GetBookingDetailsDbDecoder(self.db_content)
        super().__init__(usecase_content, self.db_content, self.db_encoder, self.db_decoder)

    def pre_execute(self, usecase_content, db_content ):
        db_content.set_content(usecase_content.get_content())

    
    def execute(self):
        db_content=self.get_adapter_content()
        self.pre_execute(self.get_usecase_content(), db_content)
        #fetch the userid and password from db 
   
        payment_request = self.encoder.encode()
        userid=payment_request.get('userid',None)
        sql_builder=SqlBuilder()
        build_maker=BuildMaker(sql_builder)
        sql_statement=build_maker.getBookingDetails(userid)
        # print(f'sql_statement --> {sql_statement}')
        
        dbc=DbClient()
        dbc.execute(sql_statement)
        getBooking_Details=dbc.get_result()
        self.decoder.decode(getBooking_Details)
        self.post_execute(db_content,self.get_usecase_content())
        # return payment_update_status
        return "SUCCESS"

    
    def post_execute(self, db_content, usecase_content):
        usecase_content.set_res_content(db_content.get_res_content())

