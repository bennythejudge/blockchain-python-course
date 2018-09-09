from typing import List

import names
import random
import uuid; uuid.uuid4().hex.upper()[0:6]


persons = []
person = {
    'name': '',
    'age': 0,
    'hobbies': []
}

for i in range(0,random.randint(1,5)):
    hobbies = []
    hobbies = [uuid.uuid4().hex.lower() for i in range(0,6)]
    print(hobbies)
    person = {
        'name': names.get_first_name(),
        'age': random.randint(1, 90),
        'hobbies': hobbies
    }
    persons.append(person)


print("persons: {}".format(persons))

names = [el['name'] for el in persons]

print("names: {} len(persons): {}".format(names, len(persons)))

ages = [el['age'] > 20 for el in persons]

print("ages: {}".format(ages))

print("are they all over 20? {}".format(all(ages)))

edit_persons = persons[:]

edit_persons[0]['name'] = "Pippo"

print("0 edit_persons: {} --- 0 persons: {}".format(edit_persons[0]['name'],persons[0]['name']))