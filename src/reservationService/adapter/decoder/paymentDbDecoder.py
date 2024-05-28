
from reservationService.decoders.decoder import Decoder
from reservationService.data.datamodel import ShowDetails,Theatre,Movie,Price,BookingDetails

class PaymentDbDecoder(Decoder):
    def __init__(self, content) -> None:
        super().__init__(content)
        # self.movie=Movie
        # self.theatre=Theatre
        # self.available_slots=ShowDetails
        # self.price=Price
        self.response=[]

    def decode(self,db_response):
        theatre=[]
        dbcontent=self.get_dbcontent()
        req_content=dbcontent.get_content()
        booking_amount=req_content.get('Booking_Amount',None)
        NumberOfSeats=req_content.get('NumberOfSeats',None)
        booking_id,status=db_response[0],db_response[1]
        price=Price(booking_amount,'INR')
        showdetails=ShowDetails(db_response[-5],db_response[-2],db_response[-1],NumberOfSeats)
        # theatre.append(Theatre(db_response[-3],db_response[2],db_response[3],db_response[4],showdetails,price))
        # movie=Movie(db_response[7],db_response[5],theatre)
        Bookingdetails=BookingDetails(status,booking_id,db_response[2],db_response[3],db_response[4],db_response[5],showdetails,price)
        self.response.append(Bookingdetails)
        # self.response.extend([booking_id,status])   
        dbcontent.set_res_content(self.response)
