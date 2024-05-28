from reservationService.decoders.decoder import Decoder
from reservationService.data.datamodel import ShowDetails,Theatre,Movie,Price

class LoginDbDecoder(Decoder):
    def __init__(self, content) -> None:
        super().__init__(content)
        self.response=[]

    def decode(self,request):
        pass
        # response=[]
        # for movie_obj in request:

        #     price=Price(movie_obj[-2],movie_obj[-1])
        #     available_slots=ShowDetails(movie_obj[6],movie_obj[7],movie_obj[8],movie_obj[9])
        #     theatre=Theatre(movie_obj[2],movie_obj[3],movie_obj[4],movie_obj[5],available_slots,price)
        #     movie=Movie(movie_obj[0],movie_obj[1],theatre)
            
        #     response.append([
        #         movie,
        #         theatre,
        #         available_slots,
        #         price
        #     ])
        # self.response.extend(response)

        # dbcontent=self.get_dbcontent()
        # dbcontent.set_db_response(self.response)