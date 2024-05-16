
from reservationService.content import Content

class RegisterUserDbContent(Content):

    def __init__(self) -> None:
        super().__init__()
        self.register=dict()

    def set_register_info(self, register):
        self.register=register

    def get_register_info(self):
        return self.register

