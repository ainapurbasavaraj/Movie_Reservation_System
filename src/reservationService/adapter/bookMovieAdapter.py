from sre_constants import SUCCESS
from reservationService.adapter.dbAdapter import DbAdapter
from reservationService.adapter.content.bookMovieDbContent import BookMovieDbContent
from reservationService.adapter.encoder.bookMovieDbEncoder import CheckSeatAvailability,GenerateBookingIdEncoder,GenerateBookingResponseEncoder
from reservationService.adapter.decoder.bookMovieDbDecoder import BookMovieDbDecoder
from reservationService.dbinterface.sqlbuilder import SqlBuilder
from reservationService.dbinterface.sqlbuildmaker import BuildMaker
from reservationService.dbinterface.db_client import DbClient
from reservationService.data.datamodel import ShowDetails,Theatre,Movie,Price
import uuid

class checkIfSeatsAvailable(DbAdapter):
    def __init__(self,usecase_content):
        
        self.db_content = BookMovieDbContent()
        self.db_encoder = CheckSeatAvailability(self.db_content)
        self.db_decoder = BookMovieDbDecoder(self.db_content)
        #self.set_encoder(SearchByLocationDbEncoder(self.get_adapter_content()))
        #self.set_decoder(SearchByLocationDbDecoder(self.get_adapter_content()))
        super().__init__(usecase_content, self.db_content, self.db_encoder, self.db_decoder)
        self.available_seats=0

    def pre_execute(self, usecase_content, db_content ):
        db_content.set_content(usecase_content.get_content())

    
    def execute(self):
        db_content=self.get_adapter_content()
        self.pre_execute(self.get_usecase_content(), db_content)
        #fetch the userid and password from db 
   
        req_details = self.encoder.encode()
        print(f'req_details --> {req_details}')
        sql_builder=SqlBuilder()
        build_maker=BuildMaker(sql_builder)
        sql_statement=build_maker.fetchSeatsAvailable(req_details)
        print(f'sql_statement --> {sql_statement}')
        dbc=DbClient()
        dbc.execute(sql_statement)
        available_seats_from_db=dbc.get_result()[0][0]
        print(f'available_seats_from_db --> {available_seats_from_db}')
        #authenticate  the userid and password 
        #user_creds=db_content.get_content()
        success='SUCCESS'
        failure='FAILURE'
        requested_seats=req_details.get('NumberOfSeats',None)
        self.available_seats=available_seats_from_db
        if available_seats_from_db >= requested_seats:
            return success
        else:
            print(f'ERROR The seats available: {available_seats_from_db} is less than the request seats : {requested_seats}')
            return failure

    
    def post_execute(self, db_content, usecase_content):
        pass
        # usecase_content.set_res_movie_list(db_content.get_db_response())

class GenerateBookingID(DbAdapter):
    def __init__(self,usecase_content):
        
        db_content = BookMovieDbContent()
        db_encoder = GenerateBookingIdEncoder(db_content)
        db_decoder = BookMovieDbDecoder(db_content)
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
        book_movie_req = self.encoder.encode()

        #generate the bookingid
        booking_id=self.generateid()
        book_movie_req.update({'booking_id':booking_id})
        sql_builder=SqlBuilder()
        build_maker=BuildMaker(sql_builder)
        sql_statement=build_maker.BookMovie(book_movie_req)
        print(f'sql_statement for bookMovie --> {sql_statement}')
        dbc=DbClient()
        dbc.execute(sql_statement)
        db_operation_status=dbc.get_result()
        dbc.close_cursor()
        if db_operation_status=='SUCCESS':
            # db_content.set_booking_id(booking_id)
            # self.post_execute(db_content,self.get_usecase_content())
            return "SUCCESS"
        else:
            print('DB ERROR : Generating movie bookingid failed')
            return "FAILURE"

    
    # def post_execute(self, db_content, usecase_content):
    #     usecase_content.set_booking_id(db_content.get_booking_id())
        
#         # usecase_content.set_res_movie_list(db_content.get_db_response())
    def generateid(self):
        return str(uuid.uuid4())


class UpdateAvailableSeats(DbAdapter):
    def __init__(self,usecase_content):
        
        db_content = BookMovieDbContent()
        db_encoder = CheckSeatAvailability(db_content)
        db_decoder = BookMovieDbDecoder(db_content)
        #self.set_encoder(SearchByLocationDbEncoder(self.get_adapter_content()))
        #self.set_decoder(SearchByLocationDbDecoder(self.get_adapter_content()))
        super().__init__(usecase_content, db_content, db_encoder, db_decoder)
        self.token=dict()

    def pre_execute(self, usecase_content, db_content ):
        db_content.set_content(usecase_content.get_content())

    
    def execute(self):
        self.pre_execute(self.get_usecase_content(), self.get_adapter_content())        
        aso=checkIfSeatsAvailable(self.get_usecase_content())
        aso.execute()
        available_seats_from_db=aso.available_seats
        req_details = self.encoder.encode()
        requested_seats=req_details.get('NumberOfSeats',None)

        #update the available seats to available_seats_from_db - requested_seats
        update_seats=available_seats_from_db-requested_seats
        sql_builder=SqlBuilder()
        build_maker=BuildMaker(sql_builder)
        sql_statement=build_maker.updateAvailableSeats(req_details,update_seats)
        dbc=DbClient()
        dbc.execute(sql_statement)
        available_seats_update_status=dbc.get_result()[0]
        if available_seats_update_status:
            return "SUCCESS"
        else:
            print('DB ERROR: update available seats failed')
            return "FAILURE"

class GenerateBookingResponse(DbAdapter):
    def __init__(self,usecase_content):
        
        db_content = BookMovieDbContent()
        db_encoder = GenerateBookingResponseEncoder(db_content)
        db_decoder = BookMovieDbDecoder(db_content)
        #self.set_encoder(SearchByLocationDbEncoder(self.get_adapter_content()))
        #self.set_decoder(SearchByLocationDbDecoder(self.get_adapter_content()))
        super().__init__(usecase_content, db_content, db_encoder, db_decoder)

    def pre_execute(self, usecase_content, db_content ):
        db_content.set_content(usecase_content.get_content())

    
    def execute(self):
        self.pre_execute(self.get_usecase_content(), self.get_adapter_content())
        showid = self.encoder.encode()
        sql_builder=SqlBuilder()
        build_maker=BuildMaker(sql_builder)
        sql_statement=build_maker.bookMovieResponse(showid)
        print(f'sql_statement --> {sql_statement}')
        dbc=DbClient()
        dbc.execute(sql_statement)
        db_booking_response=dbc.get_result()[-1]
        print(f'db_booking_response --> {db_booking_response}')

        self.decoder.decode(db_booking_response)
        # print(f'self.get_adapter_content().get_res_content() --> {self.get_adapter_content().get_res_content()}')
        # dbcontent=self.get_adapter_content()
        # encoded_content=dbcontent.get_res_content()[0]
        self.post_execute(self.get_adapter_content(),self.get_usecase_content())
        # print(f'self.get_usecase_content().get_res_content() --> {self.get_usecase_content().get_res_content()}')
        return "SUCCESS"

    def post_execute(self, db_content, usecase_content):
        usecase_content.set_res_content(db_content.get_res_content())
