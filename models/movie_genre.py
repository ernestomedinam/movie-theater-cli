import os, json
from models.genres import Genres
from models.base import Base

class MovieGenre(Base):

    # este método se usa para crear todos los objetos
    # género de una película relacionados con una 
    # película a través del movie_id, todo a partir 
    # de un string con números (idealmente) separados 
    # por comas (ej.:'5, 12 , A, ., jksa, 4')
    @classmethod
    def batch_create(cls, movie_id, genre_ids):
        def _parse_as_int(value):
            try:
                int(value)
                return True
            except Exception as error:
                return False
        # creamos una lista a partir del string separando
        # por las comas con el método split; previamente 
        # hemos reemplazado los espacios en blanco por
        # strings vacíos, equivalente a eliminarlos
        genre_ids_list = genre_ids.replace(" ", "").split(",")
        # filtramos la lista para dejar fuera todo lo que
        # no sea convertible a entero
        clean_list = list(filter(lambda item: _parse_as_int(item), genre_ids_list))
        # convertimos cada string de la lista en un entero
        integers_list = list(map(lambda item: int(item), clean_list))
        # creamos un set con estos datos para eliminar duplicados
        ids_set = set(integers_list)
        # ahora tenemos los ids que corresponden
        # a los géneros que el usuario seleccionó;
        # hacemos un ciclo y para cada elemento vamos
        # a crear un objeto MovieGenre y agregarlo a 
        # la propiedad items de esta clase: MovieGenre.items
        for id in ids_set:
            cls.items.append(cls.create(
                movie_id=movie_id,
                genre_name=Genres.parse_genre(id)
            ))

    # este método devuelve un diccionario python que representa 
    # al objeto self
    def serialize(self):
        return {
            "id": self.id,
            "movie_id": self.movie_id,
            "genre_name": self.genre_name
        }
