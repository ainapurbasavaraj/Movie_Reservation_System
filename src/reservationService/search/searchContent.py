
from reservationService.content import Content

class SearchByLocationContent(Content):

    def __init__(self) -> None:
        self.request = None
        self.response = None

    def set_request(self, request):
        self.request = request

    def set_response(self, response):
        self.response = response

    def get_response(self):
        return self.response

class SearchByMovieContent(Content):

    def __init__(self) -> None:
        self.request = None
        self.response = None

    def set_request(self, request):
        self.request = request

    def set_response(self, response):
        self.response = response


class SearchByTheatreContent(Content):

    def __init__(self) -> None:
        self.request = None
        self.response = None

    def set_request(self, request):
        self.request = request

    def set_response(self, response):
        self.response = response