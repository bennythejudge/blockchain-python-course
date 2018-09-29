# 1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person
persons = [
    {'name': 'Phong Hua Dai', 'age': 30,
     'hobbies': ['Football', 'Guitar']},
    {'name': 'Cuong Hua Dai', 'age': 21,
     'hobbies': ['Football', 'Guitar']},
    {'name': 'Thang Hua Dai', 'age': 11,
     'hobbies': ['Football', 'Guitar']}
]

names = []

# 2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
for person in persons:
    names.append(person['name'])

print(names)

# 3) Use a list comprehension to check whether all persons are older than 20.
for person in persons:
    if (person['age'] > 20):
        print(person['name'])

# 4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).

copied_persons = []
for person in persons:
    copied_persons.append(
        {'name': person['name'], 'age': person['age'], 'hobbies': person['hobbies'][:]})

copied_persons[0]['name'] = 'Phong Tran Thanh'
print(copied_persons)
print(persons)

# 5) Unpack the persons of the original list into different variables and output these variables.
person1, person2, person3 = persons
print(person1, person2, person3)