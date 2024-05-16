from reservationService.book.getBookingDetailContent import GetBookingDetailsContent
from reservationService.encoders.serviceEncoders.getBookingDetailsEncoder import GetBookingDetailsEncoder
from reservationService.decoders.serviceDecoders.getBookingDetailsDecoder import GetBookingDetailsDecoder
from reservationService.usecases.usecaseContent.getBookingDetailsContent import GetBookingDetailsUsecaseContent
from reservationService.usecases.getBookingDetailsUsecase import GetBookingDetailsUsecase


class GetBookingDetailService:
    def __init__(self) -> None:
        self.serviceContent=GetBookingDetailsContent()
        self.encoder=GetBookingDetailsEncoder(self.serviceContent)
        self.decoder=GetBookingDetailsDecoder(self.serviceContent)
        self.usecaseContent=GetBookingDetailsUsecaseContent()

    def execute(self, request):
        # print(f'self.decoder.decode(request) --> {request}')
        self.decoder.decode(request)
        
        self.pre_execute(self.serviceContent, self.usecaseContent)
        usecase=GetBookingDetailsUsecase(self.usecaseContent)
        usecase.run()
        
        
        if usecase.run():
            self.post_execute(self.usecaseContent,self.serviceContent)
            return self.encoder.encode()
        else:
            return "ERROR: Get Booking Details Failed" 

    
    def pre_execute(self,serviceContent, usecaseContent):
        usecaseContent.set_content(serviceContent.get_content())


    def post_execute(self,usecaseContent, serviceContent):
        serviceContent.set_res_content(usecaseContent.get_res_content())