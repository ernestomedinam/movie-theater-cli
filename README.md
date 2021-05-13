# movie-theater-cli 
Complementary class exercise to practice & get used to python.

## navigate comments
Check all docs in this repo and read comments for all the code.
> note: except for function's docstrings, most comments are in spanish 🙈😅

### recommended file order to read comments:
- `models/base.py`
- `models/movie.py`
- `models/genres.py`
- `models/movie_genre.py`
- `app.py`
- `utils/handlers.py`

## use the app
You can start the app after cloning this repo by running:
```sh
python app.py
```

## class diagram (so far 🙈)
![current class diagram](assets/movie-theater-cli_class-diagram.jpg?raw=true "Class diagram").

## what to do next?
You may use this repo to read and understand python code, consider class diagram to python class code translation, as well as checking differences between functional programming paradigm and object oriented paradigm approaches. 🤓

You may also try to implement the rest of classes adding methods you consider necessary in order to complete missing features, as well as needed json files in order to save data.

If you deploy any feature and would like to push it to this repo, fork it and send your pull request to check it out and merge it! 😎

### missing features:
- schedule movies on screens (expecting to use static time blocks, as 1pm, 4pm, 7pm, 10pm for each screen; schedule is always today's schedule...)
- sell a ticket to a customer to watch a specific movie on a specific time block at a specific screen
- view movie theater movie schedule
- delete a movie (also deletes movie_genres...)
- delete a schedule object (a movie on a screen at a time block)
