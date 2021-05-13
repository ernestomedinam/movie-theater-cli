import os, json
from models.base import Base
from models.genres import Genres
from models.movie_genre import MovieGenre
from utils.handlers import get_choice

# la clase Movie hereda de Base todos sus métodos y propiedades
class Movie(Base):

    # Este método se usa para crear una película a partir del
    # insumo del usuario, incluye la captura de inputs, su
    # validación y el uso del método 'create' heredado de Base
    # con estos valores como **kwargs
    @classmethod
    def user_create(cls, **kwargs):
        # se capturan los valores para los atributos de la
        # nueva película
        title = input("\nWhat's the title for this movie? ")
        description = input("\nGive us a little description about it:\n")
        rate = input("\nRate for this movie: ")
        # esta variable se crea para la "validación" de duration
        valid = False
        while valid == False:
            duration = input("\nHow many minutes does this movie last? ")
            try:
                # si duración es válido como entero, salimos del ciclo
                int(duration)
                valid = True
            except Exception as error:
                # si no, continuamos en el ciclo...
                print("\nPlease input a valid number of minutes\n")
        # usamos el método de clase 'create' y recibimos la
        # nueva película
        new_movie = cls.create(
            title=title,
            description=description,
            duration=duration,
            rate=rate
        )
        # agregamos la nueva película a la propiedad items
        # de la clase
        cls.items.append(new_movie)
        return new_movie

    # Este método se usa para obtener la elección del usuario
    # cuando le es presentado el menú de películas disponibles
    # en la app
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

    # Este método tiene como finalidad devolver una lista
    # legible de los géneros de una película; esto es, una lista
    # con los segundos valores de la tupla que corresponde a la
    # propiedad nombre de género (genre_name) en los objetos
    # MovieGenre que están relacionados con esta película
    def get_genres(self):
        genres = []
        # aquí usamos el método find heredado de base para
        # recibir una lista filtrada de los MovieGenre.items 
        # que tengan como valor de la propiedad movie_id el
        # id de este objeto: self.id
        for movie_genre in MovieGenre.find(movie_id=self.id):
            # para cada elemento de esta lista, agregamos el
            # nombre legible del género
            genres.append(Genres[movie_genre.genre_name].value[1])
        return genres

    # este método devuelve un diccionario python que
    # representa al objeto self
    def serialize(self):
        """ return a dictionary representing an object """
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "duration": int(self.duration),
            "rate": self.rate
        }

    # este método devuelve en cónsola una representación del
    # objeto self con un formato 'propiedad: valor'
    def show_detail(self):
        print("\nThis is your selected movie\n")
        for key, value in self.serialize().items():
            print(f"{key}: {value}")
        print(f"genres: {self.get_genres()}\n")

    # sobreescribe el método __str__ para devolver el título 
    # de la película
    def __str__(self):
        return self.title
