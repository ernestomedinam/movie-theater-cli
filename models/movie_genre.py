import os, json
from models.genres import Genres
from models.base import Base

class MovieGenre(Base):

    @classmethod
    def batch_create(cls, movie_id, genre_ids):
        def _parse_as_int(value):
            try:
                int(value)
                return True
            except Exception as error:
                return False
        genre_ids_list = genre_ids.replace(" ", "").split(",")
        clean_list = list(filter(lambda item: _parse_as_int(item), genre_ids_list))
        integers_list = list(map(lambda item: int(item), clean_list))
        ids_set = set(integers_list)
        for id in ids_set:
            cls.items.append(cls.create(
                movie_id=movie_id,
                genre_name=Genres.parse_genre(id)
            ))


    def serialize(self):
        return {
            "id": self.id,
            "movie_id": self.movie_id,
            "genre_name": self.genre_name
        }
    