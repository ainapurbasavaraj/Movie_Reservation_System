from reservationService.encoders.encoder import Encoder

class SearchByTheatreEncoder(Encoder):
    def __init__(self, content) -> None:
        super().__init__(content)
        self.response=dict()

    def encode(self):
        data=self.get_content().get_response()
        Theatre=[]

        for each_theatre_obj in data:
            movies_list=[]
            price=[]
            available_slots=[]
            movie_dict=dict()
            theatre=dict()
            movie_data=each_theatre_obj[1]
            theatre_data=each_theatre_obj[0]
            available_slots_data=each_theatre_obj[2]
            price_data=each_theatre_obj[3]
            theatre_id_found=False
            theatre.update({
                'theatreid':theatre_data.theatreId,
                'theatrename':theatre_data.theatreName,
                'theatretype':theatre_data.theatreType,
                'address':theatre_data.address
            })

            price=[price_data.amount,price_data.currency]
            available_slots.extend([available_slots_data.showid,available_slots_data.showDate,available_slots_data.showTime,available_slots_data.seatNumbers,price])
            movie_dict.update({
                "movieId":movie_data.movieId,
                "moviename":movie_data.movieName,
                'available_slots':available_slots
            })
            movies_list.append(movie_dict)
            for i in range(len(Theatre)):
                try:
                    if Theatre[i]['Movies']:
                        existing_theatre_id=Theatre[i]['theatreid']
                        if theatre_data.theatreId == existing_theatre_id:
                            Theatre[i]['Movies'].append(movie_dict)
                            theatre_id_found=True
                except KeyError as e:
                    print(f'KeyError = {e}')
                    pass

            if not theatre_id_found:
                theatre.update({
                    "Movies":movies_list
                })
                Theatre.append(theatre)

        self.response.update({
            "theatres":Theatre
        })
    
        return self.response