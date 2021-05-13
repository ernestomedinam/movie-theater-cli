from models.movie import Movie
from models.movie_genre import MovieGenre
from models.genres import Genres
from utils.handlers import get_choice

# estructura del menú principal
main_menu = """\n
    Welcome, choose an option:

    1. Add a movie
    2. List movies
    3. Search for movie
    4. Exit
\n"""

# se ejecutan los métodos load de las clases de la app
# que inicializan la clase y cargan desde los archivos json
# correspondientes los objetos de su tipo
Movie.load("movies")
MovieGenre.load("movie_genres")

# valor inicial de la elección del usuario
choice = 0

# mientras choice no sea 4, la aplicación se mantiene en el ciclo
while choice != 4:
    print(main_menu)
    choice = get_choice()
    if choice == 1:
        # add movie
        # se crea la película nueva con base en el método
        # user_create de la clase Movie
        new_movie = Movie.user_create()
        # se usa el método print_genres_menu para que el
        # usuario escoja los géneros de la película nueva
        chosen_genres = Genres.print_genres_menu()
        # se usa el método batch_create para crear todos
        # los objetos de la clase MovieGenre que se asocian
        # con esta nueva película
        MovieGenre.batch_create(new_movie.id, chosen_genres)
    elif choice == 2:
        # list movies
        # se usa el método list_items de la clase Movie para
        # mostrar todas las películas
        Movie.list_items()
        # se usa el método get_move_menu_choice para que el 
        # usuario pueda escoger una película para ver en detalle
        chosen_movie = Movie.get_movie_menu_choice()
        # si escogió una se muestra el detalle y luego volvemos
        # al menú, si no, volvemos al menú sin mostrar detalle
        if chosen_movie:
            chosen_movie.show_detail()
            input("Press any key to continue...")
    elif choice == 3:
        # search for movie
        pass
    elif choice == 4:
        # antes de salir, salvamos todos los items de todas las
        # clases de la app
        Movie.save("movies")
        MovieGenre.save("movie_genres")
        print("\nGoodbye.\n")
