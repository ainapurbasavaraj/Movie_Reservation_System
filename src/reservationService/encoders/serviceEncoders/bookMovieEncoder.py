from json import load
from reservationService.encoders.encoder import Encoder

class BookMovieEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)
        self.response=dict()
        self.location_list=list()

    def encode(self):
        res_content_from_db=self.get_content().get_response()
        # movie,booking_id,status=res_content_from_db[0],res_content_from_db[1],res_content_from_db[2]
        bookingDetails=res_content_from_db[0]
        print(f'bookingDetails --> {bookingDetails}')
        #print(f'res_content_from_db --> {res_content_from_db}')
        booking_detail=dict()
        showdetails=dict()
        show_details=bookingDetails.showDetails
        showDate=show_details.showDate
        showTime=show_details.showTime
        seatNumbers=show_details.seatNumbers
        showdetails.update({
            'showDate':str(showDate),
            'showTime':str(showTime),
            'seatNumbers':str(seatNumbers)
        })
        price=bookingDetails.bookingAmount


        # print(f'theatre.theatreName --> {theatre.theatreName}, theatre.availableSlots --> {theatre.availableSlots}')
        booking_detail.update({
            "status":bookingDetails.status,
            "bookingid":bookingDetails.bookingId,
            "theatreName":bookingDetails.theatreName,
            "theatretype":bookingDetails.theatreType,
            "Address":bookingDetails.address,
            "moviename":bookingDetails.movieName,
            "showdetails":showdetails,
            "bookingAmount":[price.amount,price.currency]
        })
        return booking_detail

        # return "SUCCESS"

