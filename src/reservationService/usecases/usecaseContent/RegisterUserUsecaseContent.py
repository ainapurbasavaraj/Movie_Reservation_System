from reservationService.content import Content

class RegisterUserUsecaseContent:
    def __init__(self) -> None:
        self.content=None

    def set_request_usecase_content(self,content):
        self.content=content

    def get_request_usecase_content(self):
        return self.content

