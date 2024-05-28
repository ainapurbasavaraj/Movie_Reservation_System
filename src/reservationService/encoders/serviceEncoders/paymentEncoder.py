from json import load
from reservationService.encoders.encoder import Encoder

class PaymentEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)
        self.response=dict()

    def encode(self):
        res_content_from_db=self.get_content().get_response()

        return "SUCCESS"

