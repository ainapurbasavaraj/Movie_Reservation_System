from json import load
from reservationService.encoders.encoder import Encoder

class SearchByLocationDbEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)

    def encode(self):
        # locations={
        #         '1':'Bengaluru','2':'Mumbai','3':'Chennai'
        #         }

        # data=locations
        # return data
        pass
