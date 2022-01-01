person_1 = {'name': 'Joshua', 'age': '17', 'height': '165cm'}
person_2 = {'name': 'Elizabeth', 'age': '23', 'height': '166cm'}
person_3 = {'name': 'Heisenberg', 'age': '43', 'height': '170cm'}

people = [person_1, person_2, person_3]

for person in people:
    print(f'{person["name"]}\n{person["age"]} years\n{person["height"]}\n')
