from json import load
from reservationService.encoders.encoder import Encoder

class GetBookingDetailsEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)
        self.bookingDetail=list()
        self.response=dict()

    def encode(self):
        bookingDetail=dict()
        showdetails=[]
        res_content_from_db=self.get_content().get_res_content()
        for each_bookingDetail in res_content_from_db:
            sd=each_bookingDetail.showDetails
            showDate=str(sd.showDate)
            showtime=str(sd.showTime)
            seatNumbers=sd.seatNumbers
            showdetails=[showDate,showtime,seatNumbers]
            booking_price=each_bookingDetail.bookingAmount
            bookingDetail.update({
                'status':each_bookingDetail.status,
                'bookingid':each_bookingDetail.bookingId,
                'theatreName':each_bookingDetail.theatreName,
                'theatretype':each_bookingDetail.theatreType,
                'address':each_bookingDetail.address,
                'MovieName':each_bookingDetail.movieName,
                'showDetails':showdetails,
                'bookingAmount':[booking_price.amount,booking_price.currency]
            })
            self.bookingDetail.append(bookingDetail)
        self.response.update({
            "booking_details":self.bookingDetail
        })
        print(self.response)
        return self.response

