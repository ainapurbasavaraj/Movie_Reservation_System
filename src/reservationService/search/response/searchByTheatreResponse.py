

class searchByTheatreResponse:

    def __init__(self) -> None:
        self.theatre = list()

    def set_theatre(self, theatre):
        self.theatres.append(theatre)

    def get_theatres(self):
        return self.theatres

    def get_theatre(self, theatreId):
        theatre = [theatre for theatre in self.theatres
                if theatre.theatreId == theatreId]

        if theatre:
            return theatre[0]
