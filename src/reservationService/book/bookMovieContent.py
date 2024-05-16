from reservationService.content import Content

class BookMovieContent(Content):

    def __init__(self) -> None:
        super().__init__()
        self.request = None
        self.response = None

    def set_request(self, request):
        self.request = request

    def set_response(self, response):
        self.response = response

    def get_response(self):
        return self.response

    def get_request(self):
        return self.request