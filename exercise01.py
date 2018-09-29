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

# for i in range(0,random.randint(1,5)):
for i in range(0, 3):
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

print()
print("list comprehensions")
names = [el['name'] for el in persons]

print("names: {} len(persons): {}".format(names, len(persons)))

print()
print("are they all > 20yrs old?")

ages = [el['age'] > 20 for el in persons]

print("ages: {}".format(ages))

print("are they all over 20? {}".format(all(ages)))

print()
print("real edit - deep clone")

edit_persons = [person.copy() for person in persons]

edit_persons[0]['name'] = "Pippo"

print("persons: {}".format(persons))
print("edit_persons: {}".format(edit_persons))

# unpacking
print()
print("Unpacking")
f1, f2, f3 = persons

print(f1)
print(f2)
print(f3)