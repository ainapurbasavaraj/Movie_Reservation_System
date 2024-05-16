from reservationService.book.paymentContent import PaymentContent
from reservationService.encoders.serviceEncoders.paymentEncoder import PaymentEncoder
from reservationService.decoders.serviceDecoders.paymentDecoder import PaymentDecoder
from reservationService.usecases.usecaseContent.paymentUsecaseContent import PaymentUsecaseContent
from reservationService.usecases.paymentUsecase import PaymentUsecase


class paymentService:
    def __init__(self) -> None:
        self.serviceContent=PaymentContent()
        self.encoder=PaymentEncoder(self.serviceContent)
        self.decoder=PaymentDecoder(self.serviceContent)
        self.usecaseContent=PaymentUsecaseContent()

    def execute(self, request):
        # print(f'self.decoder.decode(request) --> {request}')
        self.decoder.decode(request)
        
        self.pre_execute(self.serviceContent, self.usecaseContent)
        usecase=PaymentUsecase(self.usecaseContent)
        if usecase.run():
            return "Payment updated successfully"
        else:
            return "Payment update failed"

    
    def pre_execute(self,serviceContent, usecaseContent):
        usecaseContent.set_content(serviceContent.get_content())


    # def post_execute(self,usecaseContent, serviceContent):
    #     #print(f'inside the post_execute --> {usecaseContent.get_res_theatre_list()}')
    #     serviceContent.set_response(usecaseContent.get_res_content())