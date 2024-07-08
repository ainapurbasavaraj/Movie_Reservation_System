from reservationService.book.bookMovieContent import BookMovieContent
from reservationService.encoders.serviceEncoders.bookMovieEncoder import BookMovieEncoder
from reservationService.decoders.serviceDecoders.bookMoiveDecoder import BookMovieDecoder
from reservationService.usecases.usecaseContent.bookMovieUsecaseContent import BookMovieUsecaseContent
from reservationService.usecases.bookMovieUsecase import BookMovieUsecase
#from reservationService.data.reservationLogger import ReservationLogger
from reservationService.Log import log


class BookTicketService:
    def __init__(self) -> None:
        self.serviceContent=BookMovieContent()
        self.encoder=BookMovieEncoder(self.serviceContent)
        self.decoder=BookMovieDecoder(self.serviceContent)
        self.usecaseContent=BookMovieUsecaseContent()
        #log=ReservationLogger.get_logger()

    def execute(self, request):
        log.info("decode request has started")
        self.decoder.decode(request)
        log.info("decode request finished")
        self.pre_execute(self.serviceContent, self.usecaseContent)
        log.info("pre execution finished successfuly")

        usecase=BookMovieUsecase(self.usecaseContent)
        if usecase.run():
            self.post_execute(self.usecaseContent, self.serviceContent)
            return self.encoder.encode()
        return "FAILED"

    
    def pre_execute(self,serviceContent, usecaseContent):
        log.info("pre execution started")
        usecaseContent.set_content(serviceContent.get_content())


    def post_execute(self,usecaseContent, serviceContent):
        serviceContent.set_response(usecaseContent.get_res_content())