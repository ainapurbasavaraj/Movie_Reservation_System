from reservationService.decoders.decoder import Decoder
from reservationService.data.datamodel import ShowDetails,Theatre,Movie,Price

class SearchByTheatreDbDecoder(Decoder):
    def __init__(self, content) -> None:
        super().__init__(content)
        self.response=[]

    def decode(self,request):
        response=[]
        for theatre_obj in request:

            price=Price(theatre_obj[-2],theatre_obj[-1])
            available_slots=ShowDetails(theatre_obj[6],theatre_obj[7],theatre_obj[8],theatre_obj[9])
            theatre=Theatre(theatre_obj[0],theatre_obj[1],theatre_obj[2],theatre_obj[3],available_slots,price)
            movie=Movie(theatre_obj[5],theatre_obj[4],[])
            
            response.append([
                theatre,
                movie,
                available_slots,
                price
            ])
        self.response.extend(response)

        dbcontent=self.get_dbcontent()
        dbcontent.set_db_response(self.response)