import os, json

class Base:

    def __init__(self, **kwargs):
        self.id = os.urandom(8).hex() if id not in kwargs else kwargs["id"]
        for key, value in kwargs.items():
            setattr(self, key, value)

    @classmethod
    def create(cls, **kwargs):
        return cls(**kwargs)

    @classmethod
    def save(cls, filename):
        items_as_dictionaries = list(map(
            lambda i: i.serialize(),
            cls.items
        ))
        with open(f"json/{filename}.json", "w+") as items_file:
            json.dump(items_as_dictionaries, items_file)
        print(f"{len(cls.items)} {filename} stored.")

    @classmethod
    def load(cls, filename):
        with open(f"json/{filename}.json", "r") as items_file:
            try:
                items_as_dictionaries = json.load(items_file)
            except Exception as error:
                print("file is empty...")
                items_as_dictionaries = []
        items = []
        for item_dictionary in items_as_dictionaries:
            items.append(cls.create(**item_dictionary))
        setattr(cls, "items", items)
        setattr(cls, "name", f"{filename[:-1].capitalize()}")

    @classmethod
    def get(cls, id):
        filtered_items = list(filter(
            lambda i: i.id == id,
            cls.items
        ))
        if len(filtered_items) > 0:
            return filtered_items[0]
        return None

    @classmethod
    def find(cls, **kwargs):
        filtered_items = [*cls.items]
        for attr, value in kwargs.items():
            filtered_items = list(filter(
                lambda i: getattr(i, attr, None) == value,
                filtered_items
            ))
        return filtered_items

    @classmethod
    def list_items(cls):
        count = 1
        for item in cls.items:
            print(f"{count}- {item}")
            count += 1
        print(f"{count}- Back to main menu\n")

    def __repr__(self): 
        return f"<{self.__class__} id:{self.id}>"
    