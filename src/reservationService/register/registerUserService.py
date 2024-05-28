from reservationService.register.userCoontent import RegisterUserContent
from reservationService.encoders.serviceEncoders.registerUserEncoder import RegisterUserEncoder
from reservationService.decoders.serviceDecoders.registerUserDecoder import RegisterUserDecoder
from reservationService.usecases.usecaseContent.RegisterUserUsecaseContent import RegisterUserUsecaseContent
from reservationService.usecases.registerUserUsecase import RegisterUserUsecase


class RegisterUserService:
    def __init__(self) -> None:
        self.serviceContent=RegisterUserContent()
        self.encoder=RegisterUserEncoder(self.serviceContent)
        self.decoder=RegisterUserDecoder(self.serviceContent)
        self.usecaseContent=RegisterUserUsecaseContent()

    def execute(self, request):
        # print(f'self.decoder.decode(request) --> {request}')
        self.decoder.decode(request)
        
        self.pre_execute(self.serviceContent, self.usecaseContent)

        # usecase = SearchByTheatreUsecase(self.usecaseContent)
        # usecase.run()

        usecase=RegisterUserUsecase(self.usecaseContent)
        # usecase.run()

        # self.post_execute(self.usecaseContent, self.serviceContent)

        # retur
        # n self.encoder.encode()
        if usecase.run():
            return 'user registration is successful'
        return 'user registration failed'

    
    def pre_execute(self,serviceContent, usecaseContent):
        #print(f'inside pre-execute --> {serviceContent.get_request()}')
        usecaseContent.set_request_usecase_content(serviceContent.get_request())


    def post_execute(self,usecaseContent, serviceContent):
        #print(f'inside the post_execute --> {usecaseContent.get_res_theatre_list()}')
        serviceContent.set_response(usecaseContent.get_res_theatre_list())