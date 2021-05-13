# movie-theater-cli 
Ejercicio complementario a las clases para practicar y familiarizarse con python.

## revisa los comentarios
Revisa todos los documentos en este repo y lee los comentarios que explican el código.
> nota: la mayoría de los comentarios están en español, pero los docstrings de las funciones están en inglés 🙈😅

### orden recomendado para revisar los archivos:
- `models/base.py`
- `models/movie.py`
- `models/genres.py`
- `models/movie_genre.py`
- `app.py`
- `utils/handlers.py`

## usar la app
Puedes arrancar la aplicación, después de clonar el repo, usando el comando:
```sh
python app.py
```

## diagrama de clases (hasta ahora 🙈)
![diagrama de clases actual](assets/movie-theater-cli_class-diagram.jpg?raw=true "Diagrama de clases")

## ¿qué viene a continuación?
Puedes usar este repo para leer y entender el código, considerar la traducción del diagrama de clases a código python, así como para revisar la diferencia entre aproximarse a una solución desde el paradigma de programación funcional respecto al paradigma orientado a objetos. 🤓

También puedes intentar implementar el resto de las clases, agregando los métodos que consideres necesarios y los archivos correspondientes (para las clases y el almacenamiento en formato `json`).

Si implementas alguna funcionalidad que te gustaría subir a este repo, hazlo desde un fork y envía el pull request para revisarlo e incorporarlo! 😎

### funcionalidades por completar:
- asignar película a sala en un horario (se espera usar bloques de tiempo estáticos, como 1pm, 4pm, 7pm, 10pm para cada screen; la cartelera siempre es la del día)
- vender a un cliente un ticker para una película específica en una sala específica a una hora específica
- ver la cartelera del cine
- borrar una película (también borra sus objetos movie_genre...)
- borrar un objeto schedule (una película en una sala a una hora)
