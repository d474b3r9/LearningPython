# La serialisation est une méthode pour transmettre des data ou des binaires d'un language à un autre
# Les fonctions qui ne prennent pas en charge la sérialisation antive via DUMP nécessitent un encode / decode

from json import dump
from io import StringIO

data = {'records': [{'nom': 'Xavier', 'prénom': 'Xavier',
                     'langages': [{'nom': 'C++', 'age': 40},
                                  {'nom': 'Python', 'age': 20}]}]}

buffer = StringIO()
res = dump(data, buffer)
seq = buffer.getvalue()
print(seq)


from json import dump, JSONEncoder
from io import StringIO


class A:
    def __init__(self, att):
        self.att = att


class MyEncoder(JSONEncoder):
    def default(self, o):
        return {'classname': o.__class__.__name__, 'data': o.__dict__}


data = A('e')
buffer = StringIO()
res = dump(data, buffer, cls=MyEncoder)
res = buffer.getvalue()
print(res)