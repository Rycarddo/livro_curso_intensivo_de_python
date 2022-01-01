pizzas = ['Pizza_A', 'Pizza_B', 'Pizza_C']

for pizza in pizzas:
    print(f'Gosto da {pizza}')
print('Eu realmente gosto de pizza.')

for i in range(1, 1):
    print(i)

pizzas_amigos = pizzas[:]

pizzas.append('Pizza_D')
pizzas_amigos.append('Pizza_E')

for pizza in pizzas:
    print(pizza)

print()

for pizza_amigo in pizzas_amigos:
    print(pizza_amigo)

