

class searchByMovieResponse:

    def __init__(self) -> None:
        self.movies = list()

    def set_movie(self, movie):
        self.movies.append(movie)

    def get_movies(self):
        return self.movies

    def get_movie(self, movieId):
        movie = [movie for movie in self.movies
                if movie.movieId == movieId]

        if movie:
            return movie[0]
