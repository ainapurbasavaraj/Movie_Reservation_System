
from reservationService.decoders.decoder import Decoder
from reservationService.data.datamodel import ShowDetails,Theatre,Movie,Price,BookingDetails

class GetBookingDetailsDbDecoder(Decoder):
    def __init__(self, content) -> None:
        super().__init__(content)
        # self.movie=Movie
        # self.theatre=Theatre
        # self.available_slots=ShowDetails
        # self.price=Price
        self.response=[]

    def decode(self,db_response):
        dbcontent=self.get_dbcontent()
        # req_content=dbcontent.get_content()
        for each_record in db_response:
            print(f'each_record --> {each_record}')
            booking_id,status=each_record[0],each_record[1]
            theatreName=each_record[5]
            theatreType=each_record[6]
            address=each_record[7]
            movieName=each_record[8]
            showdetails=ShowDetails(each_record[2],each_record[10],each_record[11],each_record[-1])
            price=Price(each_record[-2],each_record[-1])
            bd=BookingDetails(
                status,
                booking_id,
                theatreName,
                theatreType,
                address,
                movieName,
                showdetails,
                price
            )
            self.response.append(bd)
        dbcontent.set_res_content(self.response)


