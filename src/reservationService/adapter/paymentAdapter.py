from sre_constants import SUCCESS
from reservationService.adapter.dbAdapter import DbAdapter
from reservationService.adapter.content.paymentDbContent import PaymentDbContent,GenerateTicketDbContent
from reservationService.adapter.encoder.paymentDbEncoder import PaymentDbEncoder
from reservationService.adapter.decoder.paymentDbDecoder import PaymentDbDecoder
from reservationService.dbinterface.sqlbuilder import SqlBuilder
from reservationService.dbinterface.sqlbuildmaker import BuildMaker
from reservationService.dbinterface.db_client import DbClient
from reservationService.data.datamodel import ShowDetails,Theatre,Movie,Price
import uuid

class updatePayment(DbAdapter):
    def __init__(self,usecase_content):
        
        self.db_content = PaymentDbContent()
        self.db_encoder = PaymentDbEncoder(self.db_content)
        self.db_decoder = PaymentDbDecoder(self.db_content)
        super().__init__(usecase_content, self.db_content, self.db_encoder, self.db_decoder)

    def pre_execute(self, usecase_content, db_content ):
        db_content.set_content(usecase_content.get_content())

    
    def execute(self):
        db_content=self.get_adapter_content()
        self.pre_execute(self.get_usecase_content(), db_content)
        #fetch the userid and password from db 
   
        payment_request = self.encoder.encode()
        booking_id=payment_request.get('bookingId',None)
        payment_status=payment_request.get("PaymentDetails",None)
        sql_builder=SqlBuilder()
        build_maker=BuildMaker(sql_builder)
        sql_statement=build_maker.payment(booking_id,payment_status)
        dbc=DbClient()
        dbc.execute(sql_statement)
        payment_update_status=dbc.get_result()
        if payment_update_status == "SUCCESS":
            return payment_status
        return payment_update_status

    
    def post_execute(self, db_content, usecase_content):
        pass
        # usecase_content.set_res_movie_list(db_content.get_db_response())

class GenerateTicketingID(DbAdapter):
    def __init__(self,usecase_content):
        
        db_content = GenerateTicketDbContent()
        db_encoder = PaymentDbEncoder(db_content)
        db_decoder = PaymentDbDecoder(db_content)
        super().__init__(usecase_content, db_content, db_encoder, db_decoder)
        self.ticket=dict()

    def pre_execute(self, usecase_content, db_content ):
        db_content.set_content(usecase_content.get_content())

    
    def execute(self):
        db_content=self.get_adapter_content()
        self.pre_execute(self.get_usecase_content(), self.get_adapter_content())        
        #send and recv data to db interface
        booking_id = self.encoder.encode_bookingId()
        ticket_id=self.generateTicket()
        ticket_url=self.generate_ticket_url()
        sql_builder=SqlBuilder()
        build_maker=BuildMaker(sql_builder)
        self.ticket.update({
            "booking_id":booking_id,
            "ticket_id":ticket_id,
            "ticket_url":ticket_url
        })
        sql_statement=build_maker.BookTicket(self.ticket)
        print(f'sql_statement for BookTicket --> {sql_statement}')
        dbc=DbClient()
        dbc.execute(sql_statement)
        db_operation_status=dbc.get_result()
        dbc.close_cursor()
        if db_operation_status=='SUCCESS':
            return "SUCCESS"
        else:
            print('DB ERROR : Generating movie bookingid failed')
            return "FAILURE"
            
    def generateTicket(self):
        return str(uuid.uuid4())

    def generate_ticket_url(self):
        endpoint=str(uuid.uuid4())
        baseUrl='https:/MovieReservationService/tickets/'+endpoint.split('-')[0]
        return baseUrl

