import enum


class Genres(enum.Enum):
    ACTION = (1, "Action")
    COMEDY = (2, "Comedy")
    DRAMA = (3, "Drama")

    # este método devuelve una lista de valores
    # legibles correspondientes a los miembros de
    # esta enumeración
    @classmethod
    def list_values(cls):
        """ returns a list with human readable values """
        value_list = []
        # la propiedad __members__ devuelve un diccionario
        # con los miembros de la enumeración donde las 
        # llaves son los nombres de los miembros
        for name in Genres.__members__:
            value_list.append(
                Genres[name].value[1]
            )
        return value_list

    # este método imprime un menú con los géneros en
    # la forma de lista numerada a partir del id de
    # miembro, siendo este el primer valor de la tupla
    @classmethod
    def print_genres_menu(cls):
        print("Please choose one or more genres for this movie: \n")
        for name in Genres.__members__:
            print(f"{Genres[name].value[0]}- {Genres[name].value[1]}")
        genre_ids = input("(separate your values with a comma)\n")
        return genre_ids

    # este método devuelve el valor legible de un 
    # miembro de esta enumeración a partir de su id,
    # siendo este el primer valor de la tupla
    @classmethod
    def parse_genre(cls, chosen_id):
        """ returns enum member name matching chosen_id """
        for name in Genres.__members__:
            if Genres[name].value[0] == int(chosen_id):
                return name
