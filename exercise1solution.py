from typing import List

import names
import random
import uuid; uuid.uuid4().hex.upper()[0:6]
persons = [
    {
        'name': 'max',
        'age': 29,
        'hobbies': ['sports','cooking']
    },
    {
        'name': 'rita',
        'age': 28,
        'hobbies': ['reading', 'movies']
    },
    {
        'name': 'angelo',
        'age': 13,
        'hobbies': ['sleeping', 'computers']
    },
]



person_names = [person['name'] for person in persons]

print("persons: {}".format(persons))

print("person_names: {}".format(person_names))


are_older = [person['age'] > 20 for person in persons]
print("are_older: {}".format(are_older))
print("are all > 20? {}".format(all(are_older)))

# shallow copy - not a deep clone
copied_persons = persons[:]
copied_persons[0]['name'] = 'giorgio'

print("persons: {}".format(persons))
print("copied_persons: {}".format(copied_persons))


# deep clone of a list of dictionaries
deep_cloned_persons = [person.copy() for person in persons]
deep_cloned_persons[0]['name'] = 'marco'

print("persons: {}".format(persons))
print("deep_cloned_persons: {}".format(deep_cloned_persons))

# unpack
p1,p2,p3 = persons

print(p1,p2,p3)