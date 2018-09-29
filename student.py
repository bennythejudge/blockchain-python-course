# Create a list of person dictionaries with a name, age and a list hobbies for each person.
persons_list = [
    {'name': 'Randy', 'age': 59, 'hobbies': ['Hiking', 'Biking', 'Golf']},
    {'name': 'Milo', 'age': 43, 'hobbies': ["Wine", "Food", "Napping"]},
    {'name': 'Kathy', 'age': 58, 'hobbies': ["Sewing", "Music", "Reading"]},
]

# Use a list comprehension to convert this list of persons into a list of names.
persons = [txt['name'] for txt in [nm for nm in persons_list]]
print(persons)

# Use a list comprehension to check to see if all persons are age over 20.
elderly = all([txt['age'] > 20 for txt in [nm for nm in persons_list]])
print(elderly)

# Copy the person list such that you can safely edit the name of the first person (without changing the original list)
persons2 = persons[:]
print(persons2)
persons2[0] = 'Randall'
print(persons2)
print(persons)

# Unpack the persons of the original list into different variables and output these variables
first, second, third = [txt['name'] for txt in [nm for nm in persons_list]]
print(first)
print(second)
print(third)