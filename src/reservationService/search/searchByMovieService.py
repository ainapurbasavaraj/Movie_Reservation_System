from reservationService.usecases.usecase import usecase
from reservationService.search.searchContent import SearchByMovieContent
from reservationService.decoders.serviceDecoders.searchByMovieDecoder import SearchByMovieDecoder
from reservationService.encoders.serviceEncoders.searchByMovieEncoder import SearchByMovieEncoder
from reservationService.usecases.usecaseContent.searchByMovieUsecaseContent import SearchByMovieUsecaseContent
from reservationService.usecases.searchByMovieUsecase import SearchByMovieUsecase


class SearchByMovieService:
    def __init__(self) -> None:
        self.serviceContent = SearchByMovieContent()
        self.decoder = SearchByMovieDecoder(self.serviceContent)
        self.encoder = SearchByMovieEncoder(self.serviceContent)
        self.usecaseContent = SearchByMovieUsecaseContent()


    def execute(self, request):
        self.decoder.decode(request)
        self.pre_execute(self.serviceContent, self.usecaseContent)

        usecase = SearchByMovieUsecase(self.usecaseContent)
        usecase.run()

        self.post_execute(self.usecaseContent, self.serviceContent)
        return self.encoder.encode()

    
    def pre_execute(self,serviceContent, usecaseContent):
        usecaseContent.set_req_locationid(serviceContent.get_request())


    def post_execute(self,usecaseContent, serviceContent):
        print(f'inside the post_execute --> {usecaseContent.get_res_movie_list()}')
        serviceContent.set_response(usecaseContent.get_res_movie_list())