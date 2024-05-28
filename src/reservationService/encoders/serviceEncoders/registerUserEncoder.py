from json import load
from reservationService.encoders.encoder import Encoder

class RegisterUserEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)
        self.response=dict()
        self.location_list=list()

    def encode(self):
        pass
        # #location=self.content.get_locations()
        # location_response=self.content.get_response()
        # print(f'location_response --> {location_response}')
        # for location in location_response:
        #     self.location_list.append(  \
        #         {
        #             'locationid':location.id,
        #             'locationname':location.name
        #         }
        #     )
        # self.response.update({'Locations':self.location_list})

        # return self.response
