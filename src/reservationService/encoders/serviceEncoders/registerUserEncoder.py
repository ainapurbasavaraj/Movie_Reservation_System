from json import load
from reservationService.encoders.encoder import Encoder

class RegisterUserEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)
        self.response=dict()
        self.location_list=list()

    def encode(self):
        pass
