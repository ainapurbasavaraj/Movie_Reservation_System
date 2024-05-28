from reservationService.content import Content

class RegisterUserContent(Content):

    def __init__(self) -> None:
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

class LoginContent(Content):

    def __init__(self) -> None:
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

class LogoutContent(Content):

    def __init__(self) -> None:
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