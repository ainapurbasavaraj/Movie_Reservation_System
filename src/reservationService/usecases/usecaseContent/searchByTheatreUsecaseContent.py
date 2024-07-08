from reservationService.content import Content

class SearchByTheatreUsecaseContent(Content):

    def __init__(self) -> None:
        super().__init__()
        self.locationid=str
        self.res_movielist=list()
        
    def set_req_locationid(self,locationid):
        self.locationid=locationid

    def get_req_locationid(self):
        return self.locationid

    def set_res_theatre_list(self,movie):
        self.res_movielist.extend(movie)

    def get_res_theatre_list(self):
        return self.res_movielist