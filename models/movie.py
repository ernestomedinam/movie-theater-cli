import os, json
from models.base import Base
from models.genres import Genres
from models.movie_genre import MovieGenre

class Movie(Base):

    @classmethod
    def user_create(cls, **kwargs):
        title = input("\nWhat's the title for this movie? ")
        description = input("\nGive us a little description about it:\n")
        rate = input("\nRate for this movie: ")
        valid = False
        while valid == False:
            duration = input("\nHow many minutes does this movie last? ")
            try:
                int(duration)
                valid = True
            except Exception as error:
                print("\nPlease input a valid number of minutes\n")
        new_movie = cls.create(
            title=title,
            description=description,
            duration=duration,
            rate=rate
        )
        cls.items.append(new_movie)
        return new_movie


    def update(self, data):
        pass
        
    @classmethod
    def get_movie_menu_choice(cls):
    """ 
        asks user for input and returns 
        selected movie id or None 
    """
    choice = 0
    movies = cls.items
    while choice != len(movies) + 1:
        choice = get_choice("Please choose a movie\n")
        if choice > 0 and choice <= len(movies):
            return movies[choice - 1]
    return None

    def get_genres(self):
        genres = []
        for movie_genre in MovieGenre.find(movie_id=self.id):
            genres.append(Genres[movie_genre.genre_name].value[1])
        return genres

    def serialize(self):
        """ return a dictionary representing an object """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "duration": int(self.duration),
            "rate": self.rate
        }

    def show_detail(self):
        print("\nThis is your selected movie")
        for key, value in self.serialize().items():
            print(f"{key}: {value}")
        print(f"genres: {self.get_genres()}")
        print("\n")

    def __str__(self):
        return self.title