from reservationService.content import Content

class BookMovieUsecaseContent(Content):

    def __init__(self) -> None:
        super().__init__()
        self.booking_id=None
        
    def set_booking_id(self,booking_id):
        self.booking_id=booking_id

    def get_booking_id(self):
        return self.booking_id