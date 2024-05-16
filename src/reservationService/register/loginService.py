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
        # print(f'self.decoder.decode(request) --> {request}')
        self.decoder.decode(request)
        
        self.pre_execute(self.serviceContent, self.usecaseContent)

        usecase = LoginUsecase(self.usecaseContent)
        usecase.run()

        self.post_execute(self.usecaseContent, self.serviceContent)

        # if usecase.run():
        #     return "login successful"
        # else:
        #     return "login failed"
        print(f'self.serviceContent.get_response() --> {self.serviceContent.get_response()}')
        return self.serviceContent.get_response()

    
    def pre_execute(self,serviceContent, usecaseContent):
        #print(f'inside pre-execute --> {serviceContent.get_request()}')
        usecaseContent.set_content(serviceContent.get_request())
        #print(f'usecaseContent.get_content() --> {usecaseContent.get_content()}')


    def post_execute(self,usecaseContent, serviceContent):
        #print(f'inside the post_execute --> {usecaseContent.get_res_theatre_list()}')
        print(f'usecaseContent.get_res_content() --> {usecaseContent.get_res_content()}')
        serviceContent.set_response(usecaseContent.get_res_content())