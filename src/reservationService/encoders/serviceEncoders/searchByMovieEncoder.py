
from reservationService.data.datamodel import Movie
from reservationService.encoders.encoder import Encoder

class SearchByMovieEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)
        self.response=dict()

    def encode(self):
        data=self.get_content().get_response()
        movie=[]

        for each_movie_obj in data:
            theatre_list=[]
            price=[]
            available_slots=[]
            movie_dict=dict()
            theatre=dict()
            movie_data=each_movie_obj[0]
            theatre_data=each_movie_obj[1]
            available_slots_data=each_movie_obj[2]
            price_data=each_movie_obj[3]
            #print(f'movie_data.movieName --> {movie_data.movieName}')
            movie_dict.update({
                "movieId":movie_data.movieId,
                "moviename":movie_data.movieName
            })
            price=[price_data.amount,price_data.currency]
            available_slots.extend([available_slots_data.showid,available_slots_data.showDate,available_slots_data.showTime,available_slots_data.seatNumbers,price])
            theatre.update({
                'theatreid':theatre_data.theatreId,
                'theatrename':theatre_data.theatreName,
                'theatretype':theatre_data.theatreType,
                'address':theatre_data.address,
                'available_slots':available_slots
            })
            theatre_list.append(theatre)
            movie_id_found=False
            if len(movie) >= 1:
                for i in range(len(movie)):
                    if movie[i]['movieId'] == movie_data.movieId:
                        movie[i]['theatres'].append(theatre)
                        movie_id_found=True

            if not movie_id_found:
                movie_dict.update({
                    "theatres":theatre_list
                })
                movie.append(movie_dict)

        # self.response.update({
        #     "movies":movie
        # })
    
        # return self.response
        return movie