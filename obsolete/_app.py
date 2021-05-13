# this was functional programming approached used for
# first live session... this is obsolete and not used anymore

# esta fue la aproximación desde paradigma de programación
# funcional que usamos en la primera sesión en vivo... ha quedado
# obsoleto y no esta en uso

main_menu = """\n
    Welcome, just welcome.

    1. Add a movie
    2. List movies
    3. Edit a movie
    4. List screens
    5. List today's schedules
    6. Exit
"""

choice = 0

import json

def load_movies():
    """
        opens file, parses content to 
        python dictionary and returns it. 
    """
    with open("json/movies.json", "r") as movies_file:
        try:
            movies = json.load(movies_file)
        except Exception as error:
            print("file is empty...")
            movies = []
    return movies

def save_movies():
    """ 
        parse movies to json, 
        open/create file, dump 
        data and save 
    """
    with open("json/movies.json", "w+") as movies_file:
        json.dump(movies, movies_file)

movies = load_movies()

# crear una peli
def create_movie():
    """
        gets title and description from user,
        adds an ID to the new movie and returns it
    """
    import os

    title = input("\nWhat's the title for this movie? ")
    description = input("\nGive us a little description about it:\n")
    new_movie_id = os.urandom(8).hex()
    return {
        "id": new_movie_id,
        "title": title,
        "description": description
    }

# agregar una peli
def add_movie():
    """ 
        calls create_movie and adds
        recently created movie to 
        the movies list 
    """
    movies.append(create_movie())
    print("\nYour movie was successfully added!")
    print(f"Movies currently on your database: {len(movies)}")

# listar las pelis
def list_movies():
    """ 
        prints number - movie title for 
        each movie on movies list 
    """
    number = 1
    for movie in movies:
        print(f"{number}- {movie['title']}")
        number += 1 
    print(f"{number}- Back to main menu")

# obtener la elecci'on del usuario en el menu de pelis
def get_movie_menu_choice():
    """ 
        asks user for input and returns 
        selected movie id or None 
    """
    choice = 0
    while choice != len(movies) + 1:
        choice = get_choice("Please choose a movie")
        if choice > 0 and choice <= len(movies):
            return movies[choice - 1]
    return None

def get_choice(text = None):
    """ gets users choice from a numbered list """
    try:
        choice = int(input(text if text else "Choose something...\n"))
        return choice
    except Exception as error:
        print("Please don't be a douche, input a valid number.")
        return 0

def show_movie_detail(movie):
    """ prints movie dictionary """
    print("\nThis is your selected movie:\n")
    for key, value in movie.items():
        print(f"{key}: {value}")
    print("")

while choice != 6:
    print(main_menu)
    choice = get_choice()
    if choice == 1:
        add_movie()
    elif choice == 2:
        list_movies()
        selected_movie = get_movie_menu_choice()
        if selected_movie:
            show_movie_detail(selected_movie)
            input("\nPress any key to continue...")
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    elif choice == 5:
        pass
    elif choice == 6:
        save_movies()
        print("\nThank you for dropping by, take care.")
