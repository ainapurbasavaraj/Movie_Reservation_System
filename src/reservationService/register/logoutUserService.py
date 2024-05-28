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
        # print(f'self.decoder.decode(request) --> {request}')
        self.decoder.decode(request)
        
        self.pre_execute(self.serviceContent, self.usecaseContent)

        usecase = LogoutUsecase(self.usecaseContent)

        # self.post_execute(self.usecaseContent, self.serviceContent)

        if usecase.run():
            return "logout successful"
        else:
            return "logout failed"
        # print(f'self.serviceContent.get_response() --> {self.serviceContent.get_response()}')
        # return self.serviceContent.get_response()
        #return "PASS"

    
    def pre_execute(self,serviceContent, usecaseContent):
        #print(f'inside pre-execute --> {serviceContent.get_request()}')
        usecaseContent.set_content(serviceContent.get_content())
        #print(f'usecaseContent.get_content() --> {usecaseContent.get_content()}')


    # def post_execute(self,usecaseContent, serviceContent):
    #     #print(f'inside the post_execute --> {usecaseContent.get_res_theatre_list()}')
    #     print(f'usecaseContent.get_res_content() --> {usecaseContent.get_res_content()}')
    #     serviceContent.set_response(usecaseContent.get_res_content())