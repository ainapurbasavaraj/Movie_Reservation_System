
from reservationService.usecases.actions.action import UsecaseAction
from reservationService.content import Content
from reservationService.decoders.decoder import Decoder
from reservationService.encoders.encoder import Encoder

class DbAdapter(UsecaseAction):

    def __init__(self) -> None:
        super().__init__()
        self.content = Content()
        self.encoder = Encoder(self.content)
        self.decoder = Decoder(self.content)

    # These setters are set by derived classes of DbAdapter
    def set_adapter_content(self, content):
        self.content = content

    def get_adapter_content(self):
        return self.content

    def set_encoder(self, encoder):
        self.encoder = encoder(self.get_adapter_content())

    def set_decoder(self, decoder):
        self.decoder = decoder(self.get_adapter_content())

    def pre_execute(self, usecase_content, db_content):
        pass

    def execute(self):
        self.pre_execute(self.get_usecase_content(), self.get_adapter_content())
        encoded_data = self.encoder.encode(self.get_adapter_content())
        #send and recv data to db interface
        self.decoder.decode() #pass response to decoder
        self.post_execute(self.get_adapter_content(), self.get_usecase_content())

    def post_execute(self, db_content, usecase_content):
        pass
