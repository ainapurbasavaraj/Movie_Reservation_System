
from reservationService.usecases.actions.action import UsecaseAction
from reservationService.content import Content
from reservationService.decoders.decoder import Decoder
from reservationService.encoders.encoder import Encoder
from reservationService.data.datamodel import Location

class DbAdapter(UsecaseAction):

    def __init__(self,usecase_content, db_content, encoder, decoder) -> None:
        super().__init__(usecase_content)
        self.content = db_content
        self.encoder = encoder
        self.decoder = decoder
        

    # # These setters are set by derived classes of DbAdapter
    # def set_adapter_content(self, content):
    #     self.content = content

    def get_adapter_content(self):
        return self.content

    def pre_execute(self, usecase_content, db_content):
        pass

    def execute(self):
        self.pre_execute(self.get_usecase_content(), self.get_adapter_content())        
        #send and recv data to db interface
        data = self.encoder.encode()
        print(f'data --> {data}')

        self.decoder.decode(data) #pass response to decoder
        self.post_execute(self.get_adapter_content(), self.get_usecase_content())
        return "SUCCESS"

    def post_execute(self, db_content, usecase_content):
        pass
