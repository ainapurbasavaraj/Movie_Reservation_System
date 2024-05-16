from reservationService.book.bookMovieContent import BookMovieContent
from reservationService.encoders.serviceEncoders.bookMovieEncoder import BookMovieEncoder
from reservationService.decoders.serviceDecoders.bookMoiveDecoder import BookMovieDecoder
from reservationService.usecases.usecaseContent.bookMovieUsecaseContent import BookMovieUsecaseContent
from reservationService.usecases.bookMovieUsecase import BookMovieUsecase


class BookTicketService:
    def __init__(self) -> None:
        self.serviceContent=BookMovieContent()
        self.encoder=BookMovieEncoder(self.serviceContent)
        self.decoder=BookMovieDecoder(self.serviceContent)
        self.usecaseContent=BookMovieUsecaseContent()

    def execute(self, request):
        # print(f'self.decoder.decode(request) --> {request}')
        self.decoder.decode(request)
        
        self.pre_execute(self.serviceContent, self.usecaseContent)

        usecase=BookMovieUsecase(self.usecaseContent)
        if usecase.run():
            self.post_execute(self.usecaseContent, self.serviceContent)
            return self.encoder.encode()

        

        # # retur
        # # n 
        # if usecase.run():
        #     return 'user registration is successful'
        # return 'user registration failed'
        return "FAILED"

    
    def pre_execute(self,serviceContent, usecaseContent):
        #print(f'inside pre-execute --> {serviceContent.get_request()}')
        usecaseContent.set_content(serviceContent.get_content())


    def post_execute(self,usecaseContent, serviceContent):
        #print(f'inside the post_execute --> {usecaseContent.get_res_theatre_list()}')
        serviceContent.set_response(usecaseContent.get_res_content())