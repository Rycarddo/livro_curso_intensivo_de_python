pet_1 = {'type': 'cat', 'owner': 'Joseph'}
pet_2 = {'type': 'dog', 'owner': 'Elizabeth'}
pet_3 = {'type': 'lion', 'owner': 'Newton'}
pet_4 = {'type': 't-rex', 'owner': 'Einstein'}
pet_5 = {'type': 'turtle', 'owner': 'Toni'}


pets = [pet_1, pet_2, pet_3, pet_4, pet_5]

for pet in pets:
    print(f'Type of the animal:{pet["type"].title()}\nName of the owner:{pet["owner"].title()}\n')
