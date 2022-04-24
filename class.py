
class Car:
    def __init__(self, name: str, immat:str) -> None:
        self.name = name
        self.__immat = immat
        self.frozen_desc = self.name + self.immat
        # set during instanciation, won't be update is self.name is changed

    def hello(self):
        return f'hello, i am {self.name}'

    def desc(self):
        return self.name + self.immat
    #use for attribute it's suger for defining getter/setter and deleter + helpful forprivacy by name mangling
    @property
    def immat(self):
        return self.__immat
    @immat.setter
    def immat(self, value):
        self.__immat = value
    @immat.deleter
    def immat(self):
        del self.__immat

    #utiliser pour une méthode il permet de mimick un attribut et de le rendre actuablisable en fonction des autres attributs.
    @property
    def desc(self):
        return f'{self.name} - {self.immat}'
    # method but behave like an attribute, will be update is self.name is changed

class Bus:
    def __init__(self, name: str) -> None:
        self.name = name
    def hello(self):
        return f'hello, i am {self.name}'

class Stealth:
    def __init__(self) -> None:
        pass
    def hello(self):
        return f'hello, i am {self.name}'

# En fait python s'en bat les couilles  de la classe de l'instance tant que les bons attributs sont présents.
car = Car('voiture', '104-tz-94')
bus = Bus('bus')
stealth_bus = Stealth()

print(f'1 -- {car.hello()}')
print(f'2 -- {bus.hello()}')
print(f'3 -- {Car.hello(car)}')
print(f'4 -- {Bus.hello(bus)}')
print(f'5 -- {Car.hello(bus)}')
#print(f'6 -- {Car.hello(stealth_bus)}')

class A():
    count = 0
    def __init__(self) -> None:
        count += 1
    def exclaim(self):
        print('I am an A')
    @classmethod
    def kids(cls):
        return cls.count


class Book:
    TYPES = ['hardcover', 'paperback']
    def __init__(self, name: str, book_type: str, weight:int|float):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f'<Book {self.name}>'

    def cut_in_half(self):
        print(self.weight/2)

class Magazine(Book):
    def __init__(self, name: str, book_type: str, weight: int | float, cover_id: int):
        super().__init__(name, book_type, weight)
        self.cover_id = cover_id

# Aggregation
class Tires():
	def __init__(self, diameter: int|float):
	    self.diameter = diameter

class Engine():
    def __init__(self, cylinder: int) -> None:
        self.cylinder = cylinder

class Voiture():
    def __init__(self, model: str, tires: Tires, engine: Engine) -> None:
        self.model = model
        self.tires = tires
        self.engine = engine

    def __repr__(self) -> str:
        return f'Car model : {self.model}\nEngine Cylinder: {self.engine.cylinder}\nTire Diameter: {self.tires.diameter}'

from pprint import pprint

quotes = dict([
('Moe', 'A wise guy, huh?'),
('Larry', 'Ow!'),
('Curly', 'Nyuk nyuk!'),
('Curlyz', 'Nyuk nyuk!'),
('Curlyr', 'Neuk nyuk!'),
('Curlyz', 'Nyuk nyuk!'),
('Curlya', 'Nyuk nyuk!'),
])
print(quotes)
print('***')
pprint(quotes)

import typing, inspect
Card = typing.NamedTuple('Card',[('rank', str),('suit',str)])
card = Card('2', 'diamond')
print(typing.get_type_hints(Card))
print(inspect.get_annotations(Card))

def append_to(element, to=[]):
    to.append(element)
    return to
my_list = append_to(12)
print(my_list)

my_other_list = append_to(42)
print(my_other_list)

breakpoint
print('end')
