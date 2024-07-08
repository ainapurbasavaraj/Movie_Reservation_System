from reservationService.register.userCoontent import LoginContent
from reservationService.encoders.serviceEncoders.loginEncoder import LoginEncoder
from reservationService.decoders.serviceDecoders.loginUserDecoder import LoginDecoder
from reservationService.usecases.usecaseContent.loginUseContent import LoginUsecaseContent
from reservationService.usecases.loginUsecase import LoginUsecase


class LoginService:
    def __init__(self) -> None:
        self.serviceContent=LoginContent()
        self.encoder=LoginEncoder(self.serviceContent)
        self.decoder=LoginDecoder(self.serviceContent)
        self.usecaseContent=LoginUsecaseContent()

    def execute(self, request):
        self.decoder.decode(request)
        self.pre_execute(self.serviceContent, self.usecaseContent)
        usecase = LoginUsecase(self.usecaseContent)
        usecase.run()
        self.post_execute(self.usecaseContent, self.serviceContent)
        print(f'self.serviceContent.get_response() --> {self.serviceContent.get_response()}')
        return self.serviceContent.get_response()

    
    def pre_execute(self,serviceContent, usecaseContent):
        usecaseContent.set_content(serviceContent.get_request())


    def post_execute(self,usecaseContent, serviceContent):
        print(f'usecaseContent.get_res_content() --> {usecaseContent.get_res_content()}')
        serviceContent.set_response(usecaseContent.get_res_content())