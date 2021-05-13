import os, json

# Esta clase será nuestra propia clase base, a partir
# de la cual heredarán las clases que vamos a crear.
class Base:
    items = []

    # toda clase que hereda de Base tiene definido
    # un método __init__ que agrega un id aleatorio
    # si el diccionario de keyword arguments (kwargs)
    # no incluye una propiedad "id"
    def __init__(self, **kwargs):
        # establece id aleatorio salvo que kwargs["id"] exista
        self.id = os.urandom(8).hex() if "id" not in kwargs else kwargs["id"]
        # este ciclo recorre todos los items() del diccionario
        # kwargs, donde cada item es un tupla con un par
        # (llave, valor), que es lo que recibimos destructurado
        # en las variables key, value
        for key, value in kwargs.items():
            # setattr es una función predeterminada de python
            # que permite agregar un atributo a un objeto;
            # existen también hasattr y getattr, entre otras
            setattr(self, key, value)
        # al finalizar el ciclo el objeto creado (self)
        # tiene todas las propiedades del diccionario kwargs
        # como atributos: self.attribute

    # las clases heredan también un método de clase llamado
    # create, que en principio devuelve la instancia creada
    # por el constructor
    @classmethod
    def create(cls, **kwargs):
        return cls(**kwargs)
    
    # las clases heredan un método load que consiste en abrir
    # el archivo .json que corresponde al valor de la variable
    # filename (por ejemplo, si filename es "movies", se trata
    # del archivo movies.json); de este archivo se cargan los
    # diccionarios json que representan objetos de esta clase
    # y se convierten en objetos. La colección de objetos que
    # resulta se guarda en una propiedad de la clase llamada
    # items: cls.items
    @classmethod
    def load(cls, filename):
        # abre el archivo
        with open(f"json/{filename}.json", "r") as items_file:
            try:
                # carga en esta variable los diccionarios json
                # convertidos en diccionarios python
                items_as_dictionaries = json.load(items_file)
            except Exception as error:
                # si el archivo está vacío, asignamos una lista
                # vacía a la variable items_as_dictionaries
                print("file is empty...")
                items_as_dictionaries = []
        # en esta variable iremos agregando cada objeto generado
        # a partir de un diccionario python
        items = []
        for item_dictionary in items_as_dictionaries:
            # en cada iteración agregamos a la lista items la
            # instancia que devuelve el método create cuando le
            # pasamos el contenido del diccionario python como
            # keyword arguments (por eso el **)
            items.append(cls.create(**item_dictionary))
        # creamos una propiedad para la clase llamada items y
        # ahora tiene como valor la colección de objetos de 
        # esta clase: cls.items
        setattr(cls, "items", items)
        # creamos una propiedad para la clase llamada name con 
        # el valor del nombre de la clase, a partir del nombre
        # del archivo: cls.name
        setattr(cls, "name", f"{filename[:-1].capitalize()}")

    # las clases heredan un método save, análogo a load, que
    # consiste en abri el archivo .json que corresponde, convertir
    # en diccionarios python cada objeto de la colección de
    # objetos de la clase y finalmente guardar estos diccionarios
    # como diccionarios json en el archivo.
    @classmethod
    def save(cls, filename):
        # este map devuelve el resultado de la función
        # serialize para cada objeto de la colección
        # cls.items
        items_as_dictionaries = list(map(
            lambda i: i.serialize(),
            cls.items
        ))
        with open(f"json/{filename}.json", "w+") as items_file:
            # se guarda el contenido de la lista de diccionarios
            # python como diccionarios json en el archivo
            json.dump(items_as_dictionaries, items_file)
        # imprime un aviso para el usuario
        print(f"{len(cls.items)} {filename} stored.")

    # también heredan las clases un método get que busca
    # y devuelve, con base en el id, un objeto específico 
    # dentro de la colección de objetos de la clase
    @classmethod
    def get(cls, id):
        # filtra cls.items con base en el valor del id
        filtered_items = list(filter(
            lambda i: i.id == id,
            cls.items
        ))
        # si encuentra al menos uno, lo devuelve
        if len(filtered_items) > 0:
            return filtered_items[0]
        # si no encuentra objeto con id = id, devuelve None
        return None

    # también heredan el método find, que filtra los cls.items 
    # con base en una serie de keyword arguments y devuelve los
    # resultados que cumplen con esos "filtros"
    @classmethod
    def find(cls, **kwargs):
        # creamos la variable filtered_items con los elementos
        # que forman parte de cls.items
        filtered_items = [*cls.items]
        # para cada par (llave, valor) del diccionario de kwargs:
        for attr, value in kwargs.items():
            # ejecutamos el método filter para dejar fuera de
            # la lista aquellos items (i) cuyo atributo (attr)
            # no tiene el valor buscado (value)
            filtered_items = list(filter(
                lambda i: getattr(i, attr, None) == value,
                filtered_items
            ))
        # devuelve la lista de items resultante
        return filtered_items

    # heredan también el método list_items, que consiste en 
    # imprimir los cls.items como una lista numerada de opciones,
    # agregando al final la opción de volver al menú anterior
    @classmethod
    def list_items(cls):
        count = 1
        print("")
        for item in cls.items:
            print(f"{count}- {item}")
            count += 1
        print(f"{count}- Back to previous menu\n")

    # heredan también este método __repr__ modificado
    # para mostrar clase y id cuando un objeto sea
    # impreso directamente en pantalla
    def __repr__(self): 
        return f"<{self.__class__} id:{self.id}>"
    