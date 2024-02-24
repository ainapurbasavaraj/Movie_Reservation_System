
from reservationService.search.searchContent import SearchByLocationContent
from reservationService.decoders.serviceDecoders.searchByLocationDecoder import SearchByLocationDecoder
from reservationService.encoders.serviceEncoders.searchByLocationEncoder import SearchByLocationEncoder
from reservationService.usecases.usecaseContent.searchByLocationUsecaseContent import SearchByLocationUsecaseContent
from reservationService.usecases.searchUsecase import searchUsecase

class SearchByLocationService:
    def __init__(self) -> None:
        self.serviceContent = SearchByLocationContent()
        self.decoder = SearchByLocationDecoder(self.serviceContent)
        self.encoder = SearchByLocationEncoder(self.serviceContent)
        self.usecaseContent = SearchByLocationUsecaseContent()


    def execute(self, request):
        self.decoder.decode(request)
        self.pre_execute(self.serviceContent, self.usecaseContent)

        usecase = searchUsecase(self.usecaseContent)
        usecase.run()

        self.post_execute(self.usecaseContent, self.serviceContent)
        return self.encoder.encode()

    
    def pre_execute(serviceContent, usecaseContent):
        pass

    def post_execute(usecaseContent, serviceContent):
        pass
