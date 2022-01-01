name = input('Digite seu nome:')

while not name.isalpha():
    print('Você não digitou um nome.')
    name = input('Digite seu nome:')

print(f'Alô {name.title()}, você gostaria de aprender um pouco de Python hoje?')
