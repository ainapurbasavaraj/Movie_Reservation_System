from reservationService.register.userCoontent import LogoutContent
from reservationService.encoders.serviceEncoders.logoutEncoder import LogoutEncoder
from reservationService.decoders.serviceDecoders.logoutUserDecoder import LogoutDecoder
from reservationService.usecases.usecaseContent.logoutUsecaseContent import LogoutUsecaseContent
from reservationService.usecases.logoutUsecase import LogoutUsecase


class LogoutService:
    def __init__(self) -> None:
        self.serviceContent=LogoutContent()
        self.encoder=LogoutEncoder(self.serviceContent)
        self.decoder=LogoutDecoder(self.serviceContent)
        self.usecaseContent=LogoutUsecaseContent()

    def execute(self, request):
        self.decoder.decode(request)
        
        self.pre_execute(self.serviceContent, self.usecaseContent)

        usecase = LogoutUsecase(self.usecaseContent)

        if usecase.run():
            return "logout successful"
        else:
            return "logout failed"

    
    def pre_execute(self,serviceContent, usecaseContent):
        usecaseContent.set_content(serviceContent.get_content())