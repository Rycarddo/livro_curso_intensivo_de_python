name = input('Digite seu nome:')

while not name.isalpha():
    print('Você não digitou um nome válido, tente novamente.')
    name = input('Digite seu nome:')

print(f'Seu nome todo minúsculo é: {name.lower()}')
print()
print(f'Seu nome todo maiúsculo é: {name.upper()}')
print()
print(f'Seu nome com a primeira letra maiúscula é: {name.title()}')
