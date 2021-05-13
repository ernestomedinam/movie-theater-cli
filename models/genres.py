import enum


class Genres(enum.Enum):
    ACTION = (1, "Action")
    COMEDY = (2, "Comedy")
    DRAMA = (3, "Drama")

    @classmethod
    def list_values(cls):
        """ returns a list with human readable values """
        value_list = []
        for name in Genres.__members__:
            value_list.append(
                Genres[name].value[1]
            )
        return value_list

    @classmethod
    def print_genres_menu(cls):
        print("Please choose one or more genres for this movie: \n")
        for name in Genres.__members__:
            print(f"{Genres[name].value[0]}- {Genres[name].value[1]}")
        genre_ids = input("(separate your values with a comma)\n")
        return genre_ids

    @classmethod
    def parse_genre(cls, chosen_id):
        """ returns enum member name matching chosen_id """
        for name in Genres.__members__:
            print(f"CHUCK: {Genres[name].value[0]} {chosen_id}")
            if Genres[name].value[0] == int(chosen_id):
                return name
