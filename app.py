from models.movie import Movie
from models.movie_genre import MovieGenre
from models.genres import Genres

main_menu = """\n
    Welcome, choose an option:

    1. Add a movie
    2. List movies
    3. Search for movie
    4. Exit
\n"""

Movie.load("movies")
MovieGenre.load("movie_genres")

choice = 0

def get_choice(text = None):
    """ gets users choice from a numbered list """
    try:
        choice = int(input(text if text else "Choose something...\n"))
        return choice
    except Exception as error:
        print("Please don't be a douche, input a valid number.")
        return 0

while choice != 4:
    print(main_menu)
    choice = get_choice()
    if choice == 1:
        # add movie
        new_movie = Movie.user_create()
        chosen_genres = Genres.print_genres_menu()
        MovieGenre.batch_create(new_movie.id, chosen_genres)
    elif choice == 2:
        # list movies
        Movie.list_items()
        chosen_movie = Movie.get_movie_menu_choice()
        if chosen_movie:
            chosen_movie.show_detail()
            input("\nPress any key to continue...")
    elif choice == 3:
        # search for movie
        pass
    elif choice == 4:
        Movie.save("movies")
        MovieGenre.save("movie_genres")
        print("\nGoodbye.\n")
