from reservationService.usecases.usecase import usecase
from reservationService.search.searchContent import SearchByTheatreContent
from reservationService.decoders.serviceDecoders.searchByTheatreDecoder import SearchByTheatreDecoder
from reservationService.encoders.serviceEncoders.searchByTheatreEncoder import SearchByTheatreEncoder
from reservationService.usecases.usecaseContent.searchByTheatreUsecaseContent import SearchByTheatreUsecaseContent
from reservationService.usecases.searchByTheatreUsecase import SearchByTheatreUsecase


class SearchByTheatreService:
    def __init__(self) -> None:
        self.serviceContent = SearchByTheatreContent()
        self.decoder = SearchByTheatreDecoder(self.serviceContent)
        self.encoder = SearchByTheatreEncoder(self.serviceContent)
        self.usecaseContent = SearchByTheatreUsecaseContent()


    def execute(self, request):
        # print(f'self.decoder.decode(request) --> {request}')
        self.decoder.decode(request)
        self.pre_execute(self.serviceContent, self.usecaseContent)

        usecase = SearchByTheatreUsecase(self.usecaseContent)
        usecase.run()

        self.post_execute(self.usecaseContent, self.serviceContent)
        return self.encoder.encode()

    
    def pre_execute(self,serviceContent, usecaseContent):
        #print(f'inside pre-execute --> {serviceContent.get_request()}')
        usecaseContent.set_req_locationid(serviceContent.get_request())


    def post_execute(self,usecaseContent, serviceContent):
        #print(f'inside the post_execute --> {usecaseContent.get_res_theatre_list()}')
        serviceContent.set_response(usecaseContent.get_res_theatre_list())