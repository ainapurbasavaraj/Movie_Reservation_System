
from reservationService.usecases.usecase import usecase
from reservationService.search.searchContent import SearchByLocationContent
from reservationService.decoders.serviceDecoders.searchByLocationDecoder import SearchByLocationDecoder
from reservationService.encoders.serviceEncoders.searchByLocationEncoder import SearchByLocationEncoder
from reservationService.usecases.usecaseContent.searchByLocationUsecaseContent import SearchByLocationUsecaseContent
from reservationService.usecases.searchUsecase import searchUsecase
from reservationService.usecases.searchByLocationUsecase import SearchByLocationUsecase

class SearchByLocationService:
    def __init__(self) -> None:
        self.serviceContent = SearchByLocationContent()
        self.decoder = SearchByLocationDecoder(self.serviceContent)
        self.encoder = SearchByLocationEncoder(self.serviceContent)
        self.usecaseContent = SearchByLocationUsecaseContent()


    def execute(self, request):
        self.decoder.decode(request)
        self.pre_execute(self.serviceContent, self.usecaseContent)
        usecase = SearchByLocationUsecase(self.usecaseContent)
        usecase.run()
        self.post_execute(self.usecaseContent, self.serviceContent)
        return self.encoder.encode()

    
    def pre_execute(self,serviceContent, usecaseContent):
        pass


    def post_execute(self,usecaseContent, serviceContent):
        serviceContent.set_response(usecaseContent.get_locations())