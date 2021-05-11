# data model
import os


class Movie:

    def __init__(self, title, description, rate, duration):
        self.id = os.urandom(8).hex()
        self.title = title
        self.description = description
        self.duration = duration
        self.rate = rate

    def __str__(self):
        return self.title

    def __repr__(self):
        return f"<Movie {self.id}-{self.title}>"

    def update(self, data):
        pass

    @classmethod
    def create(cls, title, description, rate, duration):
        """ create and returns an instance for this class """ 
        return cls(title, description, rate, duration)

    def serialize(self):
        """ return a dictionary representing an object """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "duration": self.duration
        }

new_movie = Movie("terminator", "ai", "PG-13", 90)
new_movie_2 = Movie.create("terminator II", "ai", "PG-13", 90)


print(new_movie)
print(new_movie.serialize())
print(new_movie.title)

print(new_movie_2)
print(new_movie_2.title)
